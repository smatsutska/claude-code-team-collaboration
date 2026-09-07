# Traceability — index FR ↔ UC ↔ SCR ↔ wave ↔ scope

The index the **coherence gate** measures coverage against. Update it whenever a spec is added, removed
or changes state. Generated from the specs' front-matter plus the Functional Annex analysis.

## Specs on the ground (files present)

| FR/TF | Title | UC | Wave | Scope | Rigor | Status | Spec |
|---|---|---|---|---|---|---|---|
| FR-01 | ESL Dedicated Area | UC-01 | W1 | In Scope | light | Draft | `spec/FR-01-esl-dedicated-area.md` |
| FR-02 | ESL KPI Dashboard | UC-01 | W1 | In Scope | full | Draft | `spec/FR-02-esl-kpi-dashboard.md` |
| FR-03 | ESL Released Versions Catalogue | UC-01 | W1 | In Scope | light | Draft | `spec/FR-03-released-versions-catalogue.md` |
| FR-04 | ESL Data Model Navigation | UC-01 | W1 | In Scope | full | Draft | `spec/FR-04-data-model-navigation.md` |
| FR-05 | ESL Exploration | UC-01 | W1 | In Scope | full | Draft | `spec/FR-05-esl-exploration.md` |
| FR-06 | ESL Search & Filtering | UC-01 | W1 | In Scope | light | Draft | `spec/FR-06-search-filtering.md` |
| FR-08 | ESL Internal Data Export | UC-02 ⚠ | W1 | In Scope | light | Draft | `spec/FR-08-internal-data-export.md` |
| FR-11 | Draft ESL Version | UC-02 | W2 | In Scope | full | Draft | `spec/FR-11-draft-standard-version.md` |
| TF-02 | Authentication & RBAC Framework | — | W0 | In Scope | full | Draft | `spec/TF-02-auth-rbac.md` |

> ⚠ **Inconsistency to fix:** the FR-08 spec has `uc: UC-01`, but FR-08 belongs to **UC-02**
> (ESL Internal Data Management). Align the field to `UC-02`. (It is still delivered in W1 even though
> it is UC-02: waves and use cases are different groupings.)

## Full perimeter by wave (from the Functional Annex analysis)

| Wave | Content | FR / TF |
|---|---|---|
| **W0** | Foundation | TF-01, TF-02, TF-03, TF-04, TF-06 |
| **W1** | UC-01 · Explore & Standard Insights | FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-08 |
| **W2** | UC-02 · Internal Data Management | FR-09, FR-10*, FR-11, FR-12, FR-13 |
| **W3** | UC-03 · External Standards & Mapping | FR-14, FR-15, FR-16, FR-17, FR-18, FR-19, FR-20, FR-21*, FR-22, FR-23, FR-25 |
| **W4** | UC-04 · Release & Communication | FR-26, FR-27, FR-28, FR-29, FR-30, FR-31, FR-32, TF-05 |
| **Out of scope (Phase 1)** | Project Domain + import via UI | FR-07, FR-24, FR-33 → FR-55 |

`*` = partially in scope (FR-10 on editing only; FR-21 aligned to bulk approval).

**Counts:** 28 In Scope · 2 Partial · 25 Out = 55 FR.

## Convention
Every in-scope FR → one `spec/FR-XX-*.md` file. The coherence gate verifies that every PR is attached to
an FR present in this index, and that every AC is covered by an `FR-XX/ACn` test.
