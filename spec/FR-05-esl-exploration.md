---
id:              FR-05
title:           ESL Exploration
uc:              UC-01
section:         ESL Consultation – SDC
screens:         [SCR-08, SCR-09, SCR-10, SCR-11, SCR-12, SCR-13, SCR-14, SCR-15, SCR-16, SCR-17, SCR-22, SCR-23, SCR-24, SCR-25, SCR-26, SCR-27, SCR-28, SCR-29]
wave:            W1
size:            XL
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-03, FR-04]
entities:        [SDC, Attribute, Mapping]
roles:           [Viewer]
contract_impact: none
rigor:           full
---
<!-- SEED — refine with: /spec FR-05 · The most complex FR of the wave: give the ACs real care. -->

## Context
The heart of consultation: understanding a class in depth before any mapping activity. It shows the
relationships between entities, allows switching from the structural view to an Excel-like tabular view,
and shows the existing mappings towards external standards.

## Description
The platform shall visualize relationships among ESL entities (e.g., class-to-attribute links and other
relevant ESL relations) and allow users to navigate from the structural schema to a tabular, data-oriented
(Excel-like) view of the related entities, to support full understanding prior to mapping activities. The
platform shall also allow users to view mappings between ESL and external standards, where available, as
part of the ESL consultation process.

## Acceptance criteria
AC1 — Relationships between entities
  Given a selected class (SDC)
  Then  the user sees the relevant relationships (e.g. class -> attributes and other ESL relations)

AC2 — From schema view to tabular view
  Given the user is on the structural view of a class
  When  they switch to the tabular view
  Then  they see the related entities in tabular, data-oriented (Excel-like) form

AC3 — View of existing mappings
  Given a class with mappings towards external standards available
  Then  the user can view those mappings as part of consultation

AC4 — Mappings not available
  Given a class with no mappings
  Then  the mappings view is empty with an explicit state, not an error

AC5 — Version-scoped
  Given version V is selected
  Then  relationships, tabular view and mappings reflect V

## Out of scope
- Creating/editing mappings -> W3 (FR-19, FR-21..25)
- Editing data -> W2
- Export -> FR-08

## Edge cases / errors
- High volumes in the tabular view -> rendered performantly (known risk, IMP-04)
- Cyclic/deep relationships -> navigation without infinite loops

## Notes
- Read-only. Consultation of mappings (not editing): CDC (towards clients), TDC (towards tools).
- Tabular view = a data projection; watch the schema<->table impedance (see ADR-0001).
- This is the risk of the wave: review the plan carefully, tackle it after FR-04 is stable.
