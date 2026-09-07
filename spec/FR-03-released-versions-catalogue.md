---
id:              FR-03
title:           ESL Released Versions Catalogue
uc:              UC-01
section:         Versions, Export & Notifications
screens:         [SCR-04]
wave:            W1
size:            S
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-03]
entities:        [ESL Version]
roles:           [Viewer]
contract_impact: none
rigor:           light
---
<!-- SEED — refine with: /spec FR-03 -->

## Context
The list of officially released versions, with identifiers and metadata, from which the user chooses
which version to work against during consultation.

## Description
The platform shall list all released ESL versions with clear identifiers and metadata for user navigation.

## Acceptance criteria
AC1 — List of released versions
  Given one or more officially released versions exist
  Then  the catalogue lists them all with a clear identifier (e.g. 1.1, 2.0)

AC2 — Version metadata
  Given a version in the list
  Then  its metadata is shown (e.g. release date, notes)

AC3 — Selection as context
  Given the user selects a version from the catalogue
  Then  that version becomes the consultation context

## Out of scope
- The draft (not released) -> does not appear in the catalogue
- Version comparison/diff -> FR-12 (absent by design)

## Edge cases / errors
- No released version -> empty list with an explicit state

## Notes
- Shows only released official versions; the draft is never listed here.
- Read-only.
