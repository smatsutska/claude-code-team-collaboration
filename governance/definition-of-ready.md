# G1 — Definition of Ready

**Blocking gate.** It says when a spec stops being a draft and can enter build.
It verifies **readiness**, not merit: "is this spec clear and complete enough for a developer + Claude
to build on it without guessing?".

State transition: `Draft` → (checklist ✓ + approvals) → `Ready` → `Approved`.
Only an **Approved** spec enters build. Supporting command: `/ready FR-XX`.

## Checklist (all yes/no)

| # | Criterion | Who verifies |
|---|---|---|
| 1 | Mandatory fields filled: id, title, uc, wave, scope, owner, approvers, rigor | auto |
| 2 | At least one AC, each in Given/When/Then form | auto |
| 3 | Every AC has a **verifiable** outcome (observable, not "works well") | auto |
| 4 | "Out of scope" filled in | auto |
| 5 | `depends_on` declared and in state Ready or better | human |
| 6 | `contract_impact` assessed (none or described) | auto |
| 7 | Approved by: FA-lead + architect (+ **client** on the functional part) | human |
| 8 | AC coverage adequate to `rigor` (full = happy path + edge; light = happy path) | human |

The `auto` items are pre-checked by `/ready` (CI). The `human` items require judgement (approval, coverage).

## Why it blocks from day one
We keep the spec **rigorous from the start**; it is on the *code* that we are team-friendly (see the
advisory coherence gate). A blocking G1 is what makes the advisory coherence gate downstream
sustainable: without a ready spec upstream, the coherence gate would drown in contradictions caused by
vague specs rather than by wrong code.

## The team-friendly nuance
G1 blocks **formal entry into build**, not experimentation. Anyone prototyping and producing code before
the spec is `Approved` comes back in through `/reconcile`: the code becomes input for completing the
spec, which then passes G1. Firm on the principle, not punitive about exploration.
