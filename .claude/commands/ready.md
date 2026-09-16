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
9. **No blocking open point.** Read `governance/open-points.md`: this spec fails criterion 9 if its
   FR/TF appears in the *Blocks* column of a point that is **Critical or High** priority and still
   **Open**. Two exits only — close the point, or narrow the spec (`Out of scope`) so it no longer
   applies. Ignore *programme-level* points (capacity, RACI, signing authority): they block sign-off,
   not G1, and applying this criterion to them deadlocks every spec permanently.

Also flag as **to be confirmed by a human** (you cannot decide these):
5. `depends_on` declared and in state Ready or better.
7. Approvals present: FA-lead + architect (+ client on the functional part).
8. AC coverage adequate to `rigor` (full = happy path + edge; light = happy path).

> **Known contradiction, deliberately left visible.** Criterion 7 makes the client an *approver*, while
> the RACI has the client only *consulted*, and no specification currently carries a client approver.
> The documentation lint detects the disagreement; it cannot resolve it. See finding **E** in
> [`W0-RESULTS.md`](../../W0-RESULTS.md) — this is the honest boundary of mechanization, not an oversight.

Output: a checklist with ✓/✗, and at the bottom a precise list of **what to complete** before moving to
`Ready`/`Approved`. Do not modify code. If everything automatable is ✓, say so and remind that human
items 5/7/8 remain.
