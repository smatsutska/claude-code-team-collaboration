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
| **Named individuals** (client team members appearing in wave planning) | *(real surnames)* | replaced by role — "the data owner", "the client's functional team" |
| **Named individuals** (delivery team, from wave 1) | *(real names)* | replaced by role: "the developer", "the functional team". The architect is the author of this repository and is referred to by role |
| Client's security-by-design checklist | *(named internal standard)* | "the client's security-by-design checklist" |

The three cluster acronyms deserve a note: in the original they are opaque internal terms. We renamed
them to **S**tandard / **C**lient / **T**ool Data Cluster, which is both anonymous and more legible
than the original — the only place where the public version reads better than the real one.

## Disclosure policy for figures

Added when wave-0 results were published, because that is when the repository first carried numbers
worth protecting.

| Figure | Treatment | Why |
|---|---|---|
| Effort (baseline, estimate, actual) | **Indexed to the traditional baseline = 100** | Every ratio the argument rests on survives indexing. Absolute person-days are commercial |
| Programme totals, capacity, cost | **Not published** | Close to contract terms |
| Data volumes (rows loaded/rejected) | **Proportions only** (`~2% rejected`) | Absolute counts describe the size of the client's data estate |
| Process counts (spec-first PRs, contradictions by kind, `/reconcile` invocations, CI runs, change requests) | **Published verbatim** | They describe our own process, not the client, and they are the actual evidence |
| Per-person effort | **Never published**, and since wave 1 also removed from the working repository, which is bound for the client's platform | Hours of identifiable people are not evidence about the method |
| Staffing | **"part-time" / "full-time"** instead of allocation percentages | Enough to read the team shape; not a staffing plan |
| Investment and cost per person-day | **Not published** | Commercial. Ratios such as "31% of the plan" are published instead |

`scripts/gen_metrics.py` in this repository computes from indexed inputs. The working version reads
absolute person-days. The arithmetic is otherwise identical.

## Attribution policy (from trial 3)

Trial 3 measured one named role doing one piece of work, which makes individuals easy to identify
from the inside even without names. So from trial 3 onwards:

- **Defects and lapses are attributed to the method**, and described as what the flow allowed, not
  as what a person did. A PR "was merged before review"; the text does not say by whom.
- **The only decisions attributed to someone are the author's own**: the architect's waivers and
  approvals, which she owns.
- **No platform handles, PR authors or commit authors** are reproduced. PR counts and timings are
  published; who opened or merged a given PR is not.
- **No working conditions of individuals** (tools, connectivity, allocation) are described, only
  their effect on the evidence ("review happened outside the platform and was transcribed").
- **No client-side systems** outside the stated technology stack are named: ticketing, identity
  registrations and similar operational details stay out.
- **Reviews of the trial's own results** are reported as having taken place, without saying who
  reviewed what.

## What was kept that you might expect to be removed

**The technology stack is real**: Oracle, AKS, Azure API Management, Microsoft Entra ID, React. These
are a common enterprise platform combination and identify nobody. More to the point,
[ADR-0003](docs/adr/0003-architecture-stack-ratified-from-the-deck.md) is only instructive if the
stack is concrete — the finding is that a client slide overrode an architecture decision record, and
that story does not survive abstraction into "a database" and "a cloud".

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
- **Application code.** The working repository now contains a data model, a migration engine, an Excel
  engine and API services. None of it is here: it is domain-specific to the client's data estate and
  carries anonymization risk out of proportion to what it would teach.
  What *is* published is [`scripts/`](scripts/) — the four scripts that implement the gates. Those are
  the transferable part, and they are reproduced with their logic intact, including the two
  `HARDENED` fixes made after the gate produced false positives on real documents.
  *(An earlier version of this repository carried a thin auth/RBAC slice. It was removed when the
  harness scripts were added, to keep the code perimeter to one honest purpose.)*
- **The scripts added in wave 1.** The working repository now has more generators and guards than
  the four published here: views of the open-points and change-request registers, an architecture
  lint, an interface-contract check, a process-metrics counter, a CI runner shared by two platforms.
  They are described in [`W1-RESULTS.md`](W1-RESULTS.md) and
  [`governance/quality-gates.md`](governance/quality-gates.md) but not reproduced, because they are
  tied to the client's data model. `scripts/gen_metrics.py` is the exception: it was extended here
  to cover several waves.

## Translation

The working repository is in Italian. This publication is in English throughout, to widen the pool of
reviewers. Translation was done for readability, not diplomacy: passages where we criticise our own
choices are translated as directly as the original states them.
