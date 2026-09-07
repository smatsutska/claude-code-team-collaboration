---
id:              FR-XX                    # hook into the traceability index
title:           <verbatim from the Functional Annex>
uc:              UC-XX
section:         <functional section>
screens:         [SCR-..]                 # link the design files, don't re-describe the UI
wave:            WX
size:            S|M|L|XL
scope:           In Scope | Partial
status:          Draft                    # Draft -> Ready (passes G1) -> Approved
owner:           <Functional Analyst>
approvers:       [FA-lead, architect]     # + client on the functional part
depends_on:      []                       # [FR-.., TF-..]
entities:        []                       # data model entities touched
roles:           []                       # RBAC roles involved
contract_impact: none                     # none | <description of Release API impact on Downstream Studio>
rigor:           full | light             # full on critical FRs (versioning, workbench, release); light on the rest
---

## Context
<Why it's needed. 1-2 sentences. It is the "why" that orients both the agent and the reviewer.>

## Description
<Verbatim text of the FR from the Functional Annex.>

## Acceptance criteria
<Every AC in Given/When/Then form. The outcome ("Then") must be OBSERVABLE and VERIFIABLE.
Every AC will become at least one test named FR-XX/ACn.>

AC1 — <title>
  Given <precondition>
  When  <action>
  Then  <verifiable outcome>

## Out of scope
<What this FR does NOT do. Draws the boundaries that prevent scope creep.>
- ...

## Edge cases / errors
<Boundary conditions and expected behaviour.>
- <condition> -> <behaviour>

## Notes
<Data model · RBAC · contract impact. Keep it terse.>
