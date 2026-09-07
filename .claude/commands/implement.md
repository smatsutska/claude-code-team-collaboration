---
description: Implement an FR from its approved spec (plan -> tests -> code)
argument-hint: FR-XX
---

Implement **$ARGUMENTS**. Role of whoever invokes you: **Developer** (orchestrator + reviewer).

Precondition: the spec must be `Approved`. If it isn't, stop and defer to `/ready $ARGUMENTS`.
If you are working on code already written without a spec, stop and use `/reconcile`.

Proceed in three phases, stopping after the first:

**PHASE 1 — Plan (STOP for review).**
- Load the spec, and the `esl-domain` skill if relevant.
- Propose an implementation plan faithful to the spec: components touched, approach, risks.
- For each AC, generate a **test skeleton** named `FR-XX/ACn`, with the Given/When/Then structure
  mapped onto arrange/act/assert and the assertions still to be completed.
- **Stop here.** Ask the developer to review the plan *for fidelity to the spec* before proceeding.
  This is the cheapest control against drift: do not skip it.

**PHASE 2 — Build (after the plan is approved).**
- Complete the tests, then implement until they pass.
- Branch/commits cite the FR-ID. Respect the ADRs (`docs/adr/`).
- Every AC must have its test green. Do not add behaviour the spec doesn't call for:
  if a gap in the spec emerges, **stop** — the spec must be updated (with approval) before the code.

**PHASE 3 — Pre-PR.**
- Run the verification commands (test, lint, types) declared in CLAUDE.md.
- Run `/coherence` on these changes and resolve the high-confidence findings.
- Summarise what you did, mapped per AC.

Posture: simple beats complex. No over-engineering, no unrequested scope.
