---
id:              FR-06
title:           ESL Search & Filtering
uc:              UC-01
section:         ESL Consultation – SDC
screens:         [SCR-09, SCR-14]
wave:            W1
size:            M
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [FR-04]
entities:        [SDC, Attribute]
roles:           [Viewer]
contract_impact: none
rigor:           light
---
<!-- SEED — refine with: /spec FR-06 -->

## Context
Finding classes and attributes quickly without walking the whole hierarchy, using meaningful keys.

## Description
The platform shall support search and filtering across ESL content using meaningful keys
(e.g., code, name, description and other structural keys).

## Acceptance criteria
AC1 — Search by keys
  Given a selected version
  When  the user searches by code, name or description
  Then  they see the matching results within the ESL content

AC2 — Filters
  Given a set of results
  When  the user applies a filter (e.g. by structural key)
  Then  the results narrow accordingly

AC3 — Navigable results
  Given a search result
  When  the user selects it
  Then  they reach that element in the model (navigating to it, cf. FR-04)

## Out of scope
- Search over external libraries / mappings -> W3
- Cross-version search (search is within the selected version's context)

## Edge cases / errors
- No results -> "no results" state, not an error
- Empty query -> no search executed

## Notes
- Version-scoped. Read-only.
- Data: full-text/trigram over code, name, description (Postgres, see ADR-0001).
