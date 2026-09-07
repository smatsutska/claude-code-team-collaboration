---
id:              FR-08
title:           ESL Internal Data Export
uc:              UC-01
section:         Versions, Export & Notifications
screens:         [SCR-04, SCR-05]
wave:            W1
size:            S
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-04]
entities:        [SDC, Attribute, ESL Version]
roles:           [Viewer]
contract_impact: none
rigor:           light
---
<!-- SEED — refine with: /spec FR-08 -->

## Context
Getting ESL data out in a controlled and reproducible format (Excel), consistent with how the work is
done today.

## Description
The platform shall allow authorized users to export ESL internal data in a controlled and reproducible
format (e.g., Excel).

## Acceptance criteria
AC1 — Export to Excel
  Given a selected ESL version
  When  an authorized user requests the export
  Then  they obtain an Excel file with that version's ESL data

AC2 — Controlled and reproducible format
  Given two exports of the same version with no changes in between
  Then  they produce the same file structure (deterministic)

AC3 — Authorization
  Given a user with an enabled role (Viewer or above)
  Then  they can export; roles that are not enabled cannot

## Out of scope
- ESL import via UI -> FR-07 (out of Phase 1 scope)
- Export of external libraries / mappings -> FR-15 / FR-25 (W3)
- Formats other than Excel -> Phase 3

## Edge cases / errors
- Version with no data -> a valid but empty file, with headers
- High volumes -> export handled without timing out

## Notes
- Uses the shared Excel engine (TF-04). Format consistent with the Data Library structure.
- Read-only on the data source.
