# ADR-0002 — Authentication: pluggable provider (dev stub now, SSO later)

- **Status:** Accepted
- **Date:** 2026-09-05
- **Deciders:** architect (Principal AI Architect), SGP team

## Context
To demonstrate the W1 work (the read side, gated by RBAC) we need to be able to "log in" with a role.
Real authentication (the client's SSO/IdP) is part of TF-02 but depends on the client's Identity
Provider (**IMP-06**, still open): it is not available at this stage. We need to unblock development
and demos **without** creating debt or a security hole.

## Options considered
- **Wait for SSO** — blocks every demo until IMP-06 is closed. No.
- **No auth / hardcoded user** — makes it impossible to demonstrate RBAC, and risks reaching
  production. No.
- **Pluggable AuthProvider** — a stable abstraction with two interchangeable implementations per
  environment: `DevAuthProvider` (role picker, development only) now, `SsoAuthProvider` (OIDC against
  the client IdP) later.

## Decision
Adopt the **pluggable AuthProvider**. The **RBAC model** (roles → capabilities, in
`governance/rbac-matrix.md`) is **permanent** and provider-independent. The provider is chosen per
environment (`AUTH_MODE`). The application depends **only** on the abstraction and on the capability
model — never on the concrete provider.

**What is temporary:** only the *identity source* (the dev login). **What is permanent:** the
role/capability model and the enforcement.

## Consequences
- Demos unblocked immediately; RBAC is real from now on (only *how* identity is obtained changes).
- Clean swap to SSO without touching application code.
- **Security constraints (mandatory):** `DevAuthProvider` must NEVER reach production — build-time guard
  (`AUTH_MODE=dev` in prod → error), a permanently visible "development mode" banner, no real secrets.
- **Known limitation:** frontend gating is UX only. Real RBAC enforcement must be done **server-side**
  once the backend exists (never trust the client). In W1 (frontend-only, no backend) the dev provider
  is sufficient; TF-02 tracks the real server-side enforcement.

## When to reconsider / remove
When the client's IdP is confirmed (IMP-06 closed): implement `SsoAuthProvider` (mapping IdP
claims/groups → SGP roles) and **remove** `DevAuthProvider` from production builds. The spec
`spec/TF-02-auth-rbac.md` governs the definitive implementation.
