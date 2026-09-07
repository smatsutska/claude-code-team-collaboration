# CLAUDE.md — root context

> This file is **executable context**, not documentation. Keep it **lean and accurate**:
> more text here = worse agent reasoning. Detail lives in skills (loaded on demand) and in specs.

## What we're building
SGP (Standards Governance Platform): a web application governing the **ESL** standard engineering
data library for EPC engineering. Phase 1 = Standard Domain (UC-01→UC-04). The Project Domain
(UC-05→08) is **out of scope**.

## Golden rule
**The spec is the truth; the code follows it.** A behaviour change requires a spec change *first*
(approved), *then* code. Never the other way round.

## How we work (workflow)
- `/spec FR-XX` — write or update a spec (guided interview). Owner: Functional Analyst.
- `/ready FR-XX` — check the Definition of Ready (G1) before build.
- `/implement FR-XX` — plan → test skeletons from the ACs → build. **Review the plan before writing code.**
- `/coherence` — spec↔test↔code coherence check on a PR (gate 3).
- `/reconcile` — code written without a spec: infer its spec and bring it back into the flow.

## Hard boundaries
- Do not modify `spec/` or `packages/esl-model` without the required approvals (see CODEOWNERS / operating-model).
- Every branch/commit/PR references an **FR-ID** (or TF-ID).
- Every AC (acceptance criterion) must have at least one test naming it: `FR-XX/ACn` (see `docs/testing-convention.md`).
- The contract towards Downstream Studio (`contracts/`) is versioned: if you touch it, the contract tests run.

## Verification (always run before saying "done")
- Test: `<project test command>`   · Lint: `<lint command>`   · Types: `<type-check command>`
  (to be filled in once the stack is defined — see ADR-0001 for the database: PostgreSQL)

## Decisions & boundaries
- Architecture and the "why": `docs/adr/`  · Operating model and AI autonomy: `governance/operating-model.md`
- Domain semantics (SDC/CDC/TDC, versioning): skill `esl-domain` (loads when needed).

## Posture
You are a **thought partner**, not a code generator. Propose, explain trade-offs, ask when the spec is
ambiguous. Simple beats complex: simple control loops, no over-engineering.
