---
description: Check the Definition of Ready (G1) of a spec before build
argument-hint: FR-XX
---

Run the **G1 / Definition of Ready** check on the spec of **$ARGUMENTS** (`governance/definition-of-ready.md`).

You are a verifier of **readiness**, not of merit: don't judge whether the solution is right, but whether
the spec is clear and complete enough for a developer + Claude to build on it without guessing.

Check the **automatable** part and report yes/no for each:
1. Mandatory fields filled: id, title, uc, wave, scope, owner, approvers, rigor.
2. At least one AC, each in Given/When/Then form.
3. Every AC has a **verifiable** outcome (observable; not "works well", "handled correctly").
4. "Out of scope" filled in.
6. `contract_impact` assessed (none, or described).

Also flag as **to be confirmed by a human** (you cannot decide these):
5. `depends_on` declared and in state Ready or better.
7. Approvals present: FA-lead + architect (+ client on the functional part).
8. AC coverage adequate to `rigor` (full = happy path + edge; light = happy path).

Output: a checklist with ✓/✗, and at the bottom a precise list of **what to complete** before moving to
`Ready`/`Approved`. Do not modify code. If everything automatable is ✓, say so and remind that human
items 5/7/8 remain.
