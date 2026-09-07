---
id:              FR-11
title:           Draft ESL Version
uc:              UC-02
section:         SDC Editing
screens:         [SCR-18, SCR-19, SCR-20, SCR-21]
wave:            W2
size:            L
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-03, TF-06]
entities:        [ESL Version]
roles:           [Editor, Approver, Viewer]
contract_impact: none
rigor:           full
---

## Context
Changes to the standard never touch the published version: work happens on an isolated copy (the draft)
until it is ready. This protects the official version that is in use downstream.

## Description
The platform shall support a clear separation between draft (work-in-progress) standard content
and official ESL content. A draft shall be created by duplicating an official version, and all
modifications shall be applied and approved within the draft. The platform shall allow the
management of only one draft version at a time.

## Acceptance criteria

AC1 — Creating a draft as a copy
  Given an official version V exists and no draft exists
  When  an Editor creates a draft
  Then  a draft is created as a complete copy of V, in state Draft

AC2 — Only one draft at a time
  Given a draft already exists
  When  a user tries to create another
  Then  the system prevents it and reports that a draft already exists

AC3 — Draft isolation
  Given a draft created from V exists
  When  an Editor modifies content in the draft
  Then  the official version V remains unchanged

AC4 — Baseline reference
  Given a draft created from V
  Then  the draft records V as its version of origin (baseline_ref)

## Out of scope
- Draft approval and publication workflow -> FR-09, FR-27
- Comparison/diff between versions -> FR-12 (explicitly absent)
- Multiple concurrent drafts

## Edge cases / errors
- No official version exists -> creating a draft is not allowed
  (the first official version comes from the initial migration, TF-06)
- Draft access from a Viewer role -> denied

## Notes
- Data model: ESL Version entity with state {official, draft} and a baseline_ref field.
- RBAC: Editor creates/edits the draft; Viewer does not see it; Approver edits and publishes (FR-09).
- Contract: the draft is NOT exposed via the Release API — Downstream Studio consumes only officially
  released versions.
