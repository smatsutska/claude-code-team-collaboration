# ADR-0003 — Target stack and architecture: ratified from the kickoff deck

- **Status:** Accepted
- **Supersedes:** [ADR-0001](0001-database-postgresql.md) (PostgreSQL as the primary store)

> **Read this one for the governance failure, not for the stack choice.** The stack decision is
> defensible. How it was reached is the finding — see **D** in [`../../W0-RESULTS.md`](../../W0-RESULTS.md).

## Context

The client kickoff deck presents the target architecture of SGP: **Oracle DB** as the single
authoritative store, containerised **Python microservices on AKS**, **Azure API Management** as the
gateway, **Microsoft Entra ID** for SSO/RBAC, a **React SPA** frontend.

Once a slide has been presented to the client, **that slide is a commitment.**

[ADR-0001](0001-database-postgresql.md) had chosen PostgreSQL days earlier, on internal criteria —
versioning model, tabular nature of the data, team skills, AI support — and **in the absence of the
client's infrastructure constraints**, which the open points register still classified as unresolved.

The real constraint was never a technical preference. It is **the client's standard platform**.

## The governance failure

We had the rule that should have stopped this. Definition-of-Ready criterion 9 says work does not
proceed while a Critical or High open point is unresolved, and the relevant infrastructure points were
open and recorded as such.

**Criterion 9 was scoped to specifications, not to architecture decision records.** The most expensive
decision in the programme was made by the one artifact class the readiness gate did not cover.

Note what did *not* fail: the register was accurate, the points were correctly classified, and the
contradiction was visible to anyone who read both documents. The control existed and pointed at the
wrong set of files.

## Options considered

- **Keep PostgreSQL and correct the deck.** Consistent with ADR-0001, but requires defending a
  divergence from the client's infrastructure standard at the kickoff, with a concrete risk of delaying
  environment provisioning — already on the critical path of wave 0.
- **Defer: an ADR with open options.** Honest about the unresolved points, but leaves the data model
  and the migration without a target for the whole of wave 0. Not viable — they are most of the wave.
- **Ratify the deck.** Aligns decision, presentation and client platform. Costs more in foundations and
  introduces architectural tensions that must go on the record.

## Decision

**Ratify the deck.** The dominant constraint is alignment to the client's platform and operations, not
the team's technical preference. On that criterion, ADR-0001 was deciding with incomplete information.

## Consequences

### Positive

- Environments, backup, HA and operations fall inside the client's standards: the foundation spec
  negotiates less.
- The identity provider now has a concrete target, so the pluggable `SsoAuthProvider` of
  [ADR-0002](0002-auth-strategy-pluggable-provider.md) has something real to point at.
- The API gateway is the natural place to expose the Release API towards the downstream system, giving
  the versioned contract in [`../../contracts/`](../../contracts/) a home.

### Negative, and on the record

1. **Microservices with a shared database.** The deck declares both "a *single* authoritative store"
   and "no message broker in phase 1". It follows that the services share one database. This *solves*
   the real problem — bulk publication of a draft touches several entity families atomically, and
   without a broker there would be no saga and no outbox — but it **cancels the independent
   evolvability** claimed on the detail slide.
   > Operating rule that follows: **deploy independently, do not evolve the schema independently.**
   > Schema ownership stays central, architect-only via CODEOWNERS.

2. **Capability substitutions** relative to ADR-0001, several of which are sensitive to database
   edition and licensing and must be confirmed with the client's IT:

   | Needed (PostgreSQL) | Oracle equivalent | Note |
   |---|---|---|
   | `ltree` / closure table (hierarchies) | `CONNECT BY` or recursive CTE, or closure table | no issue |
   | JSONB (flexible attributes) | `JSON` type, or `CLOB` + `IS JSON` | depends on version |
   | full-text / trigram (search) | Oracle Text | availability to verify |
   | row-level security | VPD | edition-sensitive |

3. **Local development and CI.** Oracle is not as friction-free as PostgreSQL on dev and CI. The
   foundation spec has to solve this **before** it is meaningful to talk about gates at all: while the
   verification commands in [`../../CLAUDE.md`](../../CLAUDE.md) stay placeholders, the coherence gate
   and the security gate execute nothing. *(This is finding **C**, predicted here and confirmed later.)*

4. **The Claude Code uplift assumption must be revised downward.** The estimate assumed standard
   scaffolding. This stack is less standard, so the foundation wave should benefit less.
   *(Outcome: the uplift was dramatically higher than assumed. The assumption was wrong in the
   opposite direction, which is not the same as being right.)*

5. **Effort impact.** The foundation story grows a size class, plus an integration overhead across the
   feature waves. This worsens the recorded capacity gap — not an accounting detail, it is the line
   that moves the end date.

### Unchanged

**ADR-0002 remains valid in substance.** The pluggable `AuthProvider` abstraction does not change; only
the concrete target of `SsoAuthProvider` does. The capability model in
[`../../governance/rbac-matrix.md`](../../governance/rbac-matrix.md) is provider-independent, as designed.

## Mitigation: the slide is the target, not the day-1 topology

The multi-service diagram is the architecture **at the end of phase 1**. We do not build all of them in
wave 0. We start with the services the wave genuinely requires and grow toward the target wave by wave.
This keeps the slide true without paying in wave 0 for a topology needed in wave 4, and it is the only
reading compatible with the project's stated posture — *simple beats complex*. Every new service is an
explicit choice at wave planning, never a default.

## When to reconsider

- The client's IT declares the database unavailable or unlicensed for this workload, or the required
  text-search / row-security capabilities absent.
- The shared-database constraint **blocks** draft/official versioning in a later wave: then either a
  broker enters (and the "no broker in phase 1" assumption falls), or we consolidate toward a modular
  monolith behind the same gateway.
- Cloud onboarding delays the foundation beyond the end of wave 0: at that point the cost of alignment
  exceeds the benefit and the target has to be renegotiated.
