---
description: Coherence check spec<->test<->code on a PR (gate 3)
argument-hint: [FR-XX ...] (optional; otherwise infer from the diff/branch)
---

Run the **coherence check** (gate 3) defined in `governance/coherence-gate.md`.

**Current mode: ADVISORY** — produce the report, do NOT block anything. The outcome is help for the
developer and a data point for governance.

Inputs to compare (the three sides of the triangle):
- **spec**: the `spec/FR-XX-*.md` files of the referenced FRs (from $ARGUMENTS, or inferred from branch/diff);
- **tests**: the tests touched by the PR (linked by the `FR-XX/ACn` naming);
- **code**: the PR diff.

Look for ONLY these four kinds of incoherence, and report **high-confidence findings only**
(3 true beats 30 possible):
1. **Scope creep** — the code does things the spec doesn't call for (use the "Out of scope" section).
2. **Spec drift** — the spec describes things not present in the code.
3. **Test gap** — an AC with no test naming it.
4. **Orphan FR** — the PR isn't attached to any FR → direct to `/reconcile`.

Do NOT assess cross-FR conflicts here (the pre-deploy check covers those). Do NOT block on your own
judgement: for each finding propose the two routes to resolution (align the code / update the spec with
approval), but the decision belongs to the human.

Output: the report in the format of `governance/coherence-gate.md` (max 3 findings highlighted; group if
more). Also list the **coherent** items, so the signal isn't purely negative.
