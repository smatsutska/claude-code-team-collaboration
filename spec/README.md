# spec/ — the specifications (the control plane)

This is where the **truth** that drives development, testing and validation lives. Every in-scope FR has
an `FR-XX-<slug>.md` file conforming to `_TEMPLATE.md`.

## States of a spec
`Draft` → (passes **G1 / Definition of Ready**) → `Ready` → (approvals) → `Approved`

Only an **Approved** spec can enter build. See `governance/definition-of-ready.md`.

## Hybrid rigor
One template for everything. What changes is the **depth of the acceptance criteria**, not the structure:
- `rigor: full` → critical FRs (versioning, workbench, release): exhaustive ACs on happy path + edge cases.
- `rigor: light` → the rest: essential ACs on the happy path.

## Rules
- The text in *Description* is **verbatim** from the Functional Annex (keeps naming aligned to the source).
- Every AC is in **Given/When/Then** with a verifiable outcome, and becomes at least one `FR-XX/ACn` test
  (see `docs/testing-convention.md`).
- Spec changes = PR approved by FA-lead + architect (+ client on the functional part).
- Golden rule: **change the spec first, then the code.**

## Index
`traceability.md` maintains the FR ↔ UC ↔ SCR ↔ wave ↔ scope map (from the Functional Annex analysis).
