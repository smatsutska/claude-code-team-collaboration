---
id:              FR-01
title:           ESL Dedicated Area
uc:              UC-01
section:         Dashboard & KPI
screens:         [SCR-01, SCR-02, SCR-03, SCR-04, SCR-08, SCR-09, SCR-22]
wave:            W1
size:            M
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-02]
entities:        [ESL Version]
roles:           [Admin, Approver, Editor, Viewer]
contract_impact: none
rigor:           light
---
<!-- SEED — refine with: /spec FR-01 -->

## Context
The entry point of SGP: the dedicated area from which the user reaches the ESL standard and its
functions (KPIs, consultation, versions). It is the container the other W1 features render into.

## Description
The platform shall provide a dedicated ESL area access to the standard data.

## Acceptance criteria
AC1 — Access to the area
  Given an authenticated user with an enabled role (Viewer or above)
  When  they access SGP
  Then  they see the ESL area with access to the standard's data

AC2 — Navigation to the sections
  Given the user is in the ESL area
  Then  they can reach KPIs, model consultation and the versions catalogue

AC3 — Default version
  Given the user opens the ESL area
  Then  the context is set to the latest officially released version

## Out of scope
- Editing content / drafts -> W2 (FR-09..13)
- External libraries and mapping -> W3
- Detail of the individual KPIs -> FR-02

## Edge cases / errors
- User without an enabled role -> access denied
- No official version present -> "no version" state (depends on TF-06)

## Notes
- RBAC: all enabled roles access the area (the actions inside it remain governed by the individual FRs).
- Read-only in W1.
