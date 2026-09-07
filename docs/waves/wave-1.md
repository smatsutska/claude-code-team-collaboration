# Wave 1 — UC-01 · ESL Explore & Standard Insights

**Objective.** Deliver the **read side** of SGP: the user enters the ESL area, sees the KPIs, navigates
the data model, explores a class down to its attributes and mappings, searches and exports — all against
a selected version (default: latest officially released). It is the first wave with visible functional
value and the first demo for the client.

**Perimeter.** FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-08. All **In Scope**, all **read-only** (no
editing/draft: that is W2; no external libraries/mapping editing: that is W3).

## Dependency on W0 (prerequisite)
W1 does not close without the foundations: **TF-01** (environments/CI), **TF-02** (auth & RBAC),
**TF-03** (data model + data migrated via **TF-06**), **TF-04** (Excel engine, needed by FR-08). Run W0
first, or overlapping with the start of the W1 specs.

## Backlog (the stories = the specs)

| Story | Title | Size | Rigor | Depends on | Build order |
|---|---|---|---|---|---|
| **FR-01** | ESL Dedicated Area | M | light | TF-02 | 1 |
| **FR-03** | ESL Released Versions Catalogue | S | light | TF-03 | 2 |
| **FR-04** | ESL Data Model Navigation | L | **full** | TF-03, FR-01 | 2 |
| **FR-06** | ESL Search & Filtering | M | light | FR-04 | 3 |
| **FR-05** | ESL Exploration | XL | **full** | FR-04 | 4 |
| **FR-02** | ESL KPI Dashboard | L | **full** | TF-03 | 5 (parallelisable) |
| **FR-08** | ESL Internal Data Export | S | light | TF-04 | 6 |

**Suggested sequence.** FR-01 (area/shell) → FR-03 + FR-04 (navigation backbone) → FR-06 (search over
navigable content) → FR-05 (exploration, the biggest piece, resting on FR-04) → FR-02 (KPIs, startable in
parallel as soon as the data model is queryable) → FR-08 (export). With 2 developers this is largely
sequential; FR-02 is the natural candidate for parallelism.

**Watch the big one.** FR-05 (Exploration, XL) is the risk of the wave: relationships + schema↔tabular
Excel-like view + mapping view. `full` rigor, non-negotiable plan review, and best tackled *after* FR-04
is stable.

## Definition of Ready for the wave (G1 on every story)
Every spec `Approved` before build: mandatory fields filled, ACs in verifiable Given/When/Then form,
"out of scope" filled in, `contract_impact` assessed (all `none` in W1), AC coverage adequate to `rigor`,
approved by FA-lead + architect (+ client on the functional part). See
`governance/definition-of-ready.md`.

## Definition of Done for the wave
Per FR: ACs satisfied, every AC with a green `FR-XX/ACn` test, lint/types green, code review
(CODEOWNERS), context updated. Coherence check run (advisory: findings tracked). At wave level: an
end-to-end consultation flow working on real ESL data + first-pass by the client team + sign-off.

## Roles in this wave
- **Functional Analyst ×2** — highest load here: they write the 7 specs with `/spec`, define the ACs,
  design the acceptance tests. This is the wave in which the functional team *really enters* the flow.
- **Developer ×2** — build the read side (version-scoped queries, UI from the design files). FR-05 and
  FR-02 are the most demanding.
- **Client team** — first functional verification: they validate that consultation, KPIs and exploration
  reflect the real ESL domain.
- **Governance ×3** — observe the first coherence reports (baseline!), and verify that plan review is
  genuinely happening.

## Demo & sign-off (the wave's acceptance criterion)
The path demonstrated to the client, on a real official version:
1. I enter the ESL area (FR-01) → 2. I see the KPIs of that version (FR-02) → 3. I browse the versions
catalogue (FR-03) → 4. I navigate the model: discipline → class → attributes (FR-04) → 5. I explore a
class: relationships, Excel-like tabular view, existing mappings (FR-05) → 6. I search by code/name
(FR-06) → 7. I export to Excel (FR-08).

## PoC note
W1 is the first complete lap of the flow: this is where the **baseline** metrics are collected
(spec-first share, coherence-gate contradictions, `/reconcile` invocations). Governance tracks them from
day one — they are needed to demonstrate value, not at the end of the project.
