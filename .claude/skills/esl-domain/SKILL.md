---
name: esl-domain
description: >
  ESL domain semantics for SGP: entities (SDC, CDC, TDC, mapping), classification hierarchies,
  and the versioning model (official/draft). Load when writing specs, implementing or reviewing
  features that touch the data model, versions or the mapping workbench. Do not load for purely
  UI, infrastructure or CI work.
---

# ESL domain

## What it is
The ESL (Engineering Standard Library) is the official catalogue of the Client's standardized
engineering classes and attributes. SGP is its **system of record**: it governs it, versions it,
releases it. It serves the handover of engineering data in EPC (Engineering, Procurement, Construction).

## Core entities
- **SDC (Standard Data Cluster)** — the central class, carrying a *Functional Class* and a
  *Physical Class*. Identified by an SDC ID. Plant objects are classified in a multi-level hierarchy
  (e.g. equipment → rotating equipment → pump → pump type).
- **Attributes** — properties of a class (pressure, temperature, flow rate, unit of measure, allowed
  value lists), each with a data type, unit and allowed values.
- **Mapping** — associations between the Client's model and external models:
  - **CDC** = mapping towards **customer** models (client data cluster);
  - **TDC** = mapping towards **tools** (application/tool, e.g. a P&ID authoring tool).
  Mappings exist at **class** and **attribute** level, and can be **many-to-one**
  (several external elements → one ESL element).
- **CT (Classification Tree)** — the classification hierarchy/tree.

## Versioning model (critical)
- There are **official versions** (V1, V2, …) and **exactly one draft** at a time.
- A draft is a **copy** of an official version; all modifications happen inside the draft.
- Publication happens **in bulk**: approving the draft promotes it to a new official version and
  releases all changes together. Individual changes are not approved one by one.
- **No diff/compare engine** between versions (an explicit choice): only the version a piece of data
  refers to is indicated.
- Previous versions are **retained** and stay consultable.

## Boundaries
- **External** libraries (client/tool) are **read-only**: they are versioned by uploading new versions.
- The initial load of the existing Data Library (multi-sheet Excel) is a **one-off** migration (TF-06);
  after that, the ESL evolves inside SGP.
- Towards **Downstream Studio** only the Release API is exposed, carrying **officially released**
  versions (the draft is never exposed).

## Persistence
The database is **PostgreSQL** (see `docs/adr/0001-database-postgresql.md`): hierarchies via closure
table/`ltree`, mappings via an association table (handling many-to-one and class/attribute level),
flexible attributes in JSONB, versioning with proven patterns and "draft = copy".
