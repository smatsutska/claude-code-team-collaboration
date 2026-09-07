---
id:              FR-02
title:           ESL KPI Dashboard
uc:              UC-01
section:         Dashboard & KPI
screens:         [SCR-01, SCR-02, SCR-03]
wave:            W1
size:            L
scope:           In Scope
status:          Draft
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]
depends_on:      [TF-03]
entities:        [SDC, Attribute, Mapping, ESL Version]
roles:           [Viewer]
contract_impact: none
rigor:           full
---
<!-- SEED — refine with: /spec FR-02 -->

## Context
An informational dashboard (not advanced analytics) giving the consistency of the library: how many
classes, how many attributes, how much mapping coverage. It helps orient before detailed consultation.

## Description
The platform shall display KPIs on classes, attributes and mappings, including Functional and Physical
Classes count, attribute coverage and distribution, mapping coverage towards clients (CDC), tools (TDC)
and project libraries. The KPI shall be visualized for every version (by default latest released version).

## Acceptance criteria
AC1 — Class counts
  Given a selected ESL version
  Then  the dashboard shows the number of Functional Classes and Physical Classes in that version

AC2 — Attribute coverage and distribution
  Given a selected version
  Then  the dashboard shows attribute coverage and their distribution

AC3 — Mapping coverage
  Given a selected version
  Then  the dashboard shows mapping coverage towards clients (CDC), tools (TDC) and project libraries

AC4 — KPIs per version, defaulting to the latest official
  Given the user opens the dashboard without choosing a version
  Then  the KPIs are computed on the latest officially released version
  And   selecting another version recomputes the KPIs on that one

## Out of scope
- Project KPIs -> FR-55 (out of perimeter)
- Advanced analytical drill-down / exporting the KPIs alone

## Edge cases / errors
- Version with no mappings -> coverage shown as 0, not an error
- No official version -> empty dashboard with an explicit state

## Notes
- Data model: aggregations over SDC (Functional/Physical Class), Attribute, Mapping (CDC towards clients,
  TDC towards tools).
- The metrics are per-version: every query is version-scoped.
- Read-only.
