# Quality gates

Controls run at **increasing frequency and decreasing cost** (shift-left). Not one heavy check at deploy.

## The gates

| # | Gate | When | What it verifies | Initial state (friendly) |
|---|---|---|---|---|
| 1 | **Plan review** | pre-code | Is the AI's plan faithful to the spec? | practice (always) |
| 2 | FR-ID convention | every commit | Branch/commits cite an FR-ID | convention |
| 3 | **Coherence gate** | every PR / micro-release | spec ↔ test ↔ code coherent (4 kinds) | **ADVISORY** |
| — | **G1 / Def. of Ready** | pre-build | Is the spec ready | **BLOCKING** |
| 4 | Contract test | pre-deploy | The contract towards Downstream Studio holds (if `contract_impact≠none`) | **BLOCKING** |
| 5 | **Wave sign-off** | end of wave | The wave is accepted (client + governance) | **BLOCKING** |

Standard automated gates in CI on every PR: **test, lint, type-check, security scan** (blocking once the
stack is wired). The coherence gate (gate 3) is defined in `coherence-gate.md`.

## Advisory → blocking progression (data-governed)
A **team-friendly** start: the coherence gate **measures and shows, it does not block**. This:
- collects the **baseline** of current behaviour (contradictions, orphans, spec-first share);
- gets the team used to seeing coherence as a real dimension;
- builds trust, because by the time it starts blocking it will be well calibrated.

The criterion for going **blocking** is a **number, not a date**: when the contradiction curve settles
on a downward trend and the spec-first share passes the agreed threshold, the gate starts blocking —
**critical** FRs first (versioning, workbench, release), then the rest.

**Rule:** the gate and the Definition of Done harden **at the same moment** (see below).

## Definition of Done (DoD)
Evolves together with the coherence gate:

- **DoD v0 (friendly):** acceptance criteria satisfied · every AC has a green `FR-XX/ACn` test ·
  lint/types green · code review approved (CODEOWNERS) · relevant context updated (spec/skill/CLAUDE.md).
- **DoD v1 (when the coherence gate becomes blocking):** v0 **+** no open high-confidence contradiction
  in the coherence report.

## An honest note
The coherence gate is reasoned by Claude: it can produce false positives and negatives. That is why the
outcome is always a **report a human judges**, never a block on the AI's judgement alone — consistent
with human-in-the-lead. AC↔test traceability is guaranteed **by existence** (is there a test naming the
AC?), not by semantic correctness (does that test cover the AC well?): the second remains the job of
human code review.
