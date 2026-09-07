# What was anonymized, and what wasn't

This repository is a faithful mirror of a live programme's Claude Code harness, with identifying
names systematically replaced. **Nothing structural was softened for publication** — the gates, the
autonomy matrix, the admitted weaknesses and the open inconsistency are exactly as they are in the
working repository. If we had smoothed those over, the feedback in [`FEEDBACK.md`](FEEDBACK.md)
would be worthless.

## What was replaced

| Category | Real | Published as |
|---|---|---|
| Client organisation | *(named EPC contractor)* | "the Client" / "an energy & utility EPC contractor" |
| Programme / standard library | *(3-letter internal acronym)* | **ESL** — Engineering Standard Library |
| The platform being built | *(evocative internal codename)* | **SGP** — Standards Governance Platform |
| App folder | `apps/<codename>` | `apps/sgp` |
| Shared model package | `packages/<acronym>-model` | `packages/esl-model` |
| Downstream consuming system | *(named internal product)* | **Downstream Studio** |
| Team handle of that system | *(real team handle)* | `@studio-team` |
| Central class entity | *(internal acronym)* | **SDC** — Standard Data Cluster |
| Client-model mapping entity | *(internal acronym)* | **CDC** — Client Data Cluster |
| Tool-model mapping entity | *(internal acronym)* | **TDC** — Tool Data Cluster |
| Classification hierarchy entity | *(internal acronym)* | **CT** — Classification Tree |
| Named third-party engineering tool | *(commercial P&ID product)* | "a P&ID authoring tool" |
| Traditional baseline estimate | *(actual figure)* | `<N>` person-days / `<M>` months |
| Client RBAC source document | *(deck, slide reference)* | "the client's RBAC matrix document" |
| Capability namespace | `<acronym>.consult` etc. | `esl.consult`, `esl.editDraft`, `esl.approve` |
| Domain skill name | `<acronym>-domain` | `esl-domain` |

The three cluster acronyms deserve a note: in the original they are opaque internal terms. We renamed
them to **S**tandard / **C**lient / **T**ool Data Cluster, which is both anonymous and more legible
than the original — the only place where the public version reads better than the real one.

## What was deliberately kept

- **All requirement, use-case, screen and wave identifiers** (`FR-01`, `TF-02`, `UC-01`, `SCR-14`, `W1`).
  They are opaque outside the programme and they carry the traceability structure that is the point.
- **`IMP-xx`** — open impediments blocking decisions (e.g. the client's identity provider not yet
  confirmed). Kept because the *shape* of "we designed around an unresolved external dependency" is
  part of what we want reviewed.
- **Verbatim English requirement text.** The "Description" section of every spec is quoted verbatim
  from the contract's functional annex — that fidelity rule is itself a design choice under review.
  Only the entity names inside it were substituted.
- **Team composition, counts and role definitions.** Non-identifying and essential to judging the model.
- **The ADR dates and reasoning**, including the database trade-off analysis that argues *against*
  our own choice on one dimension.
- **The known defect in [`spec/traceability.md`](spec/traceability.md)** (FR-08's use-case field
  contradicts the wave analysis). Left in place. It is real, we found it, we haven't fixed it, and
  hiding it would misrepresent how the harness behaves.

## What is not here

- Client data, engineering standards content, personal data, or anything from the actual library.
- Screens and Figma files (referenced by `SCR-xx` identifiers only).
- Contract terms, commercial figures, names of individuals other than the author.
- Application code beyond a thin auth/RBAC slice, included because it demonstrates the
  spec → RBAC matrix → typed code chain that the method claims to produce.

## Translation

The working repository is in Italian. This publication is in English throughout, to widen the pool of
reviewers. Translation was done for readability, not diplomacy: passages where we criticise our own
choices are translated as directly as the original states them.
