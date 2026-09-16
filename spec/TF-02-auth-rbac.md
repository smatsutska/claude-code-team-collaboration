---
id:              TF-02
title:           Authentication & RBAC Framework
uc:              —
section:         Foundation
screens:         []
wave:            W0
size:            L
scope:           In Scope
status:          Approved  # dev-mode: the real SSO impl is Out of scope, blocked on an open point
owner:           <architect>
approvers:       [architect, FA-lead]
depends_on:      [TF-01]
entities:        [User, Role]
roles:           [Admin, Approver, Editor, Viewer]
contract_impact: none
rigor:           full
---
<!-- Approved and merged in wave 0, dev-mode. The real SSO implementation is Out of scope on this
     spec (blocked on an external dependency) and does not gate its acceptance criteria. -->

## Context
The authentication and authorization foundation of SGP. The role/capability model is permanent; the
identity source is pluggable: `DevAuthProvider` (temporary, for development/demo) now, `SsoAuthProvider`
(the client's IdP) once IMP-06 is closed. See ADR-0002 and `governance/rbac-matrix.md`.

## Description
The platform shall authenticate users and enforce role-based access control across ESL functionality,
supporting four roles (Admin, ESL Approver, ESL Editor, Viewer). Authentication shall be provided
through a pluggable provider: a development-only provider during build-out, and an SSO/IdP provider for
production.

## Acceptance criteria
AC1 — Role model
  Given the four roles (Viewer, Editor, Approver, Admin)
  Then  each is associated with the capabilities defined in governance/rbac-matrix.md (Approver ⊇ Editor; Admin ⊇ everything)

AC2 — Capability enforcement
  Given a user lacking a capability
  When  they attempt the corresponding action
  Then  the action is denied (server-side enforcement once the backend exists; UI-gated client-side)

AC3 — Temporary provider (dev)
  Given AUTH_MODE=dev
  When  a user opens the development login
  Then  they can pick a role and enter as the seed user of that role, with no IdP

AC4 — Exclusion from production
  Given a production build
  When  AUTH_MODE=dev
  Then  the build fails; and in dev mode a "development mode" banner is always visible

AC5 — Swap to SSO without touching the app
  Given AUTH_MODE=sso
  Then  the app uses SsoAuthProvider through the same AuthProvider abstraction, with no changes to application code

## Out of scope
- The concrete OIDC/OAuth2 implementation of SSO -> once IMP-06 is closed (AC5 remains as the contract)
- Administration UI / user provisioning
- Project-level RBAC (Project Editor/Approver) -> Project Domain (out of Phase 1 perimeter)

## Edge cases / errors
- Missing/expired session -> user unauthenticated, redirect to login
- IdP claims/groups not mappable to a role (in SSO) -> access denied with an explicit message

## Notes
- Capability model: `governance/rbac-matrix.md` is **authoritative**; the `ROLE_CAPABILITIES` map in
  application code mirrors it. The duplication is guarded by check 5 of the documentation coherence
  lint (role-mapping drift), not by anyone remembering to keep them aligned.
- Frontend gating is UX; real security is server-side.
- `DevAuthProvider` is disposable (ADR-0002); remove it from production builds when SSO arrives.
