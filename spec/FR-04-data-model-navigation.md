---
id:              FR-04
title:           ESL Data Model Navigation
uc:              UC-01
section:         ESL Consultation – SDC
screens:         [SCR-08, SCR-09, SCR-10, SCR-11, SCR-12, SCR-13, SCR-14, SCR-15, SCR-16, SCR-17, SCR-22, SCR-23, SCR-24, SCR-25, SCR-26, SCR-27, SCR-28, SCR-29]
wave:            W1
size:            L
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-03, FR-01]
entities:        [SDC, Attribute, CT]
roles:           [Viewer]
contract_impact: none
rigor:           full
---
<!-- SEED — refine with: /spec FR-04 -->

## Context
The primary way a user explores the logical structure of the ESL: disciplines, classes, hierarchies,
clusters, attributes. It is the navigation backbone that search (FR-06) and exploration (FR-05) rest on.

## Description
The platform shall enable navigation across the ESL logical structure (e.g., disciplines, classes,
hierarchies, clusters, attributes and related structures) for the selected version.

## Acceptance criteria
AC1 — Navigating the hierarchy
  Given a selected version
  When  the user navigates the model
  Then  they can walk the multi-level classification hierarchy (e.g. equipment -> rotating equipment -> pump)

AC2 — From class to attributes
  Given the user has selected a class (SDC)
  Then  they see the attributes associated with that class

AC3 — Version-scoped navigation
  Given version V is selected
  Then  the structure shown is that of V (changing version changes the structure)

AC4 — Navigable elements
  Given the user navigates the model
  Then  disciplines, classes, clusters and attributes are selectable/expandable elements

## Out of scope
- Modifying the structure -> W2
- Excel-like tabular view and relationships/mappings -> FR-05
- Search/filters -> FR-06

## Edge cases / errors
- Class with no attributes -> shown with an empty attribute list
- Deep hierarchy -> stays navigable without degrading (watch volumes, IMP-04)

## Notes
- Data model: SDC with Functional/Physical Class; hierarchy (CT / closure table); linked attributes.
- Version-scoped queries. Read-only.
