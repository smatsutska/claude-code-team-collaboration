# CLAUDE.md — apps/sgp (app context · Wave 1 focus)

> Scoped context. The root context always applies (`/CLAUDE.md`); here only what is specific to the SGP
> app and the wave in progress. Keep it lean.

## Current wave: W1 — UC-01 · ESL Explore & Standard Insights
We are building the **read side**: ESL area, KPIs, versions catalogue, model navigation, exploration,
search, export. See `docs/waves/wave-1.md` and specs `spec/FR-01..06, FR-08`.

## App conventions (W1)
- **Everything read-only.** In W1 nothing is written: no editing, no draft (that is W2). If a plan
  introduces mutations of ESL data, stop: it is out of wave.
- **Version-scoped.** Every query/view is in the context of *one* version (default: latest officially
  released). Do not mix versions.
- **Official versions only.** The draft does not exist for W1 consultation; the catalogue (FR-03) lists
  released versions only.
- **UI from the design files.** Implement against the mockups referenced in each spec's `screens:`
  (SCR-xx). Do not reinvent layouts.
- **Persistence:** PostgreSQL (see `docs/adr/0001-database-postgresql.md`). Hierarchies via closure
  table/`ltree`; search via full-text/trigram; no access to the draft store from here.

## Outside this wave (do not implement here)
- Editing / draft / workflow -> W2 (FR-09..13)
- External libraries, Mapping Workbench (creating mappings) -> W3
- In W1 mappings are **displayed** only (FR-05), never modified.

## W0 dependencies (must exist)
Auth & RBAC (TF-02), data model + migrated data (TF-03/TF-06), Excel engine for export (TF-04).

## Domain context
Load the `esl-domain` skill for SDC/CDC/TDC and version semantics. FR-05 (Exploration) is the most
complex piece: review its plan carefully, and only after FR-04 is stable.

## Verification (fill in once the stack is wired)
- Test: `<command>`   · Lint: `<command>`   · Types: `<command>`
Do not say "done" without green tests + `/coherence` run on the PR.
