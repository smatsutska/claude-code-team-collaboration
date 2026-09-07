# Coherence gate (gate 3) — minimal definition

The control that makes spec↔code coherence an **invariant** rather than an activity. Runs on every
PR/micro-release. Executed by Claude via `/coherence` (locally) and/or in CI.
**Initial phase: ADVISORY** (it does not block; see `quality-gates.md`).

## Shape
One job, one prompt (no multi-agent: simple control loops beat orchestrations).
It compares the **three sides of the triangle**: the **spec** of the referenced FRs, the **tests**
touched, and the code **diff**.

## What it looks for (only these four kinds)
1. **Scope creep** — the code does things not in the spec (uses the *Out of scope* section).
2. **Spec drift** — the spec says things not in the code.
3. **Test gap** — an AC with no test naming it (`FR-XX/ACn`).
4. **Orphan FR** — the PR isn't attached to any FR → `/reconcile`.

*Out of this gate's scope:* **cross-FR** conflicts (the pre-deploy check, gate 4, covers those).

## Confidence
High-confidence findings only: 3 true beats 30 possible. Precision matters more than coverage — in
advisory mode we can afford to show only what the AI is reasonably sure of.
The **structural** part (orphan FR, test gap) is deterministic; the **semantic** part (scope creep,
spec drift) is reasoned.

## Outcome
A **report** (below). For each finding, two routes to resolution: *align the code* / *update the spec
(with approval)*. The decision belongs to the **human**. In advisory mode the PR merges anyway; the
report is visible on the PR and counts as data.

## Report template (v0 — to be calibrated on real operational data)

```
Coherence check · PR #<n> · <FR-.. referenced>
Result: <k> contradictions (advisory — does not block the merge)

#  Kind         What                                   Where               Action
1  Scope creep  <short description>                    <file:line>         remove, or update spec
2  Test gap     <AC not covered>                       <FR-XX · AC#n>      add test
...

Coherent: <FR-XX AC#.. · ...>
```

Max 3 findings highlighted; group them if there are more. Always list the **coherent** items too
(the signal shouldn't be purely negative).

## Note
This gate **augments** human code review, it does not replace it: it hands review a coherence checklist
already filled in. The detailed report and the confidence thresholds get refined **with real operational
data** (first parameter to tune: the *precision* of the findings, not the harshness of the gate).
