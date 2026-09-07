# Lifecycle of an FR (end to end)

The unit flowing through the system is the single **FR** (or TF): it is born as a spec, becomes a plan,
then code, passes the gates, gets validated, gets signed off. Every role touches it at a precise stage.

## The flow
```
spec → G1 → plan → build → PR (coherence) → merge → UAT → sign-off
       (blocking)  (review)     (advisory)  (contract test)  (blocking)
```

## The table

| # | Stage | Who | What happens | Gate | Spec state |
|---|---|---|---|---|---|
| 1 | Drafting | FA + Claude (`/spec`) | Guided interview → spec with ACs in GWT | — | Draft |
| 2 | Readiness | FA + architect + client | `/ready` (auto checks) + approvals | **G1** (blocking) | Draft→Approved |
| 3 | Plan | Dev + Claude (`/implement` P1) | Plan + test skeletons (1 per AC); **STOP** for fidelity review | plan review (practice) | Approved |
| 4 | Build | Dev + Claude (`/implement` P2) | Tests → code; branch/commits cite FR-ID | FR-ID convention | Approved |
| 5 | PR | Dev + Claude + CODEOWNERS | `/coherence` posts the report; human code review | **Coherence** (advisory) + review | Approved |
| 6 | Merge→UAT | Dev | Merge; deploy to UAT; contract tests if `contract_impact≠none` | contract test (blocking) | Approved |
| 7 | Verification | Client team | First functional verification on the real domain (first-pass) | UAT | Approved |
| 8 | Sign-off | Client + governance | Wave accepted; metrics consolidated | **wave gate** (blocking) | Approved |

## Recovery flow (vibecoding)
If at step 5 the coherence gate finds an **orphan FR** (code without a spec): `/reconcile` → Claude
infers the spec from the code → back to step 1 → G1 → return to the flow. Vibecoding isn't rejected,
it's **brought back in**.

## The ladder of validations (shift-left)
| Rung | Validates | Owner |
|---|---|---|
| Spec review (G1) | Is the spec right and complete? | FA + client |
| Plan review | Is the plan faithful to the spec? | Developer |
| Automated gates (CI) | Test, lint, types, security, contract | Dev + governance |
| Code review | Does the PR respect the criteria and the ADRs? | Developer (CODEOWNERS) |
| Functional verification | Does it work in the real domain? | Client team |
| Wave sign-off | Is the wave accepted? | Client + governance |
| **Meta-validation** | Do the metrics prove the approach has value? | Governance |

## Operational note
Step 3 (**plan review**) is the cheapest link and the easiest to skip when in a hurry.
That is where drift gets caught before it becomes code. In retrospectives, verify *first* that it is
actually being done — otherwise the whole weight falls on the coherence gate downstream, which is
more expensive.
