# ADR-0001 — Database: PostgreSQL as the primary store

- **Status:** Accepted
- **Date:** 2026-09-04
- **Deciders:** architect (Principal AI Architect), SGP team

## Context
The ESL domain is naturally a graph (classes, hierarchies, attributes, mappings between standards). The
primary store for SGP has to be chosen. The *critical* requirements, however, are not graph-shaped:
official/draft versioning with version retention (FR-11/12/27/29), Excel-like tabular views (FR-05),
Excel round-trip (FR-08/14/15/25, migration TF-06), governance and audit.

## Options considered
- **PostgreSQL** — mature relational. Hierarchies via `ltree`/closure table; mappings via an association
  table (many-to-one and class/attribute level are native); flexible attributes in JSONB; versioning
  with proven patterns; tabular views and Excel export are direct; RLS + audit columns.
- **Neo4j** — graph DB. Excellent for the Mapping Workbench (mappings *are* edges) and for exploration
  (variable-depth traversals). But: versioning is not native (copy-on-write of subgraphs, or
  edge/node versioning — complex); impedance with the tabular/Excel nature of the work; graph modelling
  is a specialist skill; weaker Claude Code support; clustering/backup/DB-level RBAC only in Enterprise
  (licensing).

## Decision
**PostgreSQL** as the primary store. The deciding factor is not mapping (where Neo4j would win) but the
combination of **versioning + tabular/Excel nature + team skills + AI support**, which weighs in favour
of relational.

## Consequences
- Positive: versioning and Excel are straightforward; team and ops are comfortable; Claude Code is very
  effective; free.
- Negative: exploration and the workbench require more modelling work (closure table, mapping table,
  recursive queries) than the elegance of Cypher — acceptable at the expected volumes.

## When to reconsider
If these recur **together**: (a) exploration/mapping become the dominant use case and measurably
expensive; (b) volumes (IMP-04) grow by orders of magnitude; (c) the team acquires graph skills. In that
case evaluate **polyglot persistence**: Postgres as the truth + a read-only graph layer for traversals
and the workbench (introduced only when a *measured* problem calls for it).
