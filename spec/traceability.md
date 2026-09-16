# Traceability — index FR ↔ UC ↔ SCR ↔ wave ↔ scope

The index the **coherence gate** measures coverage against.

> **The table below is GENERATED** from the specs' front-matter by
> [`../scripts/gen_traceability.py`](../scripts/gen_traceability.py) — do not edit it by hand.
> `--check` runs in CI as part of gate 3b.
>
> It used to be hand-maintained, and it drifted twice in the first two weeks. That is the origin of the
> *one fact, one home* rule in [`../CLAUDE.md`](../CLAUDE.md), and of bet #7 in
> [`../FEEDBACK.md`](../FEEDBACK.md) — which we lost. See [`../W0-RESULTS.md`](../W0-RESULTS.md).

## Specs on the ground (files present)

<!-- GEN:traceability:start -->
| FR/TF | Title | UC | Wave | Scope | Rigor | Status | Depends on | Spec |
|---|---|---|---|---|---|---|---|---|
| FR-01 | ESL Dedicated Area | UC-01 | W1 | In Scope | light | Draft | [TF-02] | `spec/FR-01-esl-dedicated-area.md` |
| FR-02 | ESL KPI Dashboard | UC-01 | W1 | In Scope | full | Draft | [TF-03] | `spec/FR-02-esl-kpi-dashboard.md` |
| FR-03 | ESL Released Versions Catalogue | UC-01 | W1 | In Scope | light | Draft | [TF-03] | `spec/FR-03-released-versions-catalogue.md` |
| FR-04 | ESL Data Model Navigation | UC-01 | W1 | In Scope | full | Draft | [TF-03, FR-01] | `spec/FR-04-data-model-navigation.md` |
| FR-05 | ESL Exploration | UC-01 | W1 | In Scope | full | Draft | [TF-03, FR-04] | `spec/FR-05-esl-exploration.md` |
| FR-06 | ESL Search & Filtering | UC-01 | W1 | In Scope | light | Draft | [FR-04] | `spec/FR-06-search-filtering.md` |
| FR-08 | ESL Internal Data Export | UC-01 | W1 | In Scope | light | Draft | [TF-04] | `spec/FR-08-internal-data-export.md` |
| FR-11 | Draft ESL Version | UC-02 | W2 | In Scope | full | Draft | [TF-03, TF-06] | `spec/FR-11-draft-standard-version.md` |
| TF-02 | Authentication & RBAC Framework | — | W0 | In Scope | full | Approved | [TF-01] | `spec/TF-02-auth-rbac.md` |

**Specs on the ground:** 9 (1 Approved). Table **generated** by `scripts/gen_traceability.py` from front-matter - do not edit by hand.
<!-- GEN:traceability:end -->

> ⚠ **Known inconsistency, deliberately left visible.** The FR-08 spec carries `uc: UC-01`, but FR-08
> belongs to **UC-02** (ESL Internal Data Management). The generated table above now shows what the
> front-matter actually says, rather than what a hand-written index used to claim — the previous
> version of this file silently displayed `UC-02`, which means the index and the spec disagreed and the
> index was quietly winning. Generation made the disagreement visible. Fixing it is a spec edit.
>
> (FR-08 is still delivered in W1 even though it belongs to UC-02: waves and use cases are different
> groupings.)

## Full perimeter by wave (from the Functional Annex analysis)

| Wave | Content | FR / TF |
|---|---|---|
| **W0** | Foundation — **executed** | TF-01, TF-01b*, TF-02, TF-03, TF-04, TF-06, TF-07 |
| **W1** | UC-01 · Explore & Standard Insights | FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-08 |
| **W2** | UC-02 · Internal Data Management | FR-09, FR-10*, FR-11, FR-12, FR-13 |
| **W3** | UC-03 · External Standards & Mapping | FR-14, FR-15, FR-16, FR-17, FR-18, FR-19, FR-20, FR-21*, FR-22, FR-23, FR-25 |
| **W4** | UC-04 · Release & Communication | FR-26, FR-27, FR-28, FR-29, FR-30, FR-31, FR-32, TF-05 |
| **Out of scope (Phase 1)** | Project Domain + import via UI | FR-07, FR-24, FR-33 → FR-55 |

`*` = partially in scope, or not yet closed. FR-10 on editing only; FR-21 aligned to bulk approval;
TF-01b (cloud environments) remains the one W0 spec still `Draft`, blocked on external dependencies.

**Counts:** 28 In Scope · 2 Partial · 25 Out = 55 FR.

> **Note on scope.** Only a subset of the W0 specs is published in this repository — the foundation
> stories are heavily client-specific. The wave table above reflects the real programme; the generated
> table reflects the files present here. The two are deliberately different, and
> [`../ANONYMIZATION.md`](../ANONYMIZATION.md) says why.

## Convention

Every in-scope FR → one `spec/FR-XX-*.md` file. The coherence gate verifies that every PR is attached to
an FR present in this index, and that every AC is covered by an `FR-XX/ACn` test.
