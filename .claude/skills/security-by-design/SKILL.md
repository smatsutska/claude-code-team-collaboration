---
name: security-by-design
description: >
  Secure coding rules derived from the client's Security by Design checklist. Load when writing or
  reviewing code that touches authentication, authorization (RBAC), data/secret handling, logging,
  cryptography, user input, sessions/cookies, error handling or exports. Do not load for purely
  layout/CSS or documentation work.
---

# Secure coding — rules

Guiding principles: least privilege · minimize attack surface · secure defaults · defense in depth ·
separation of duties · no security-by-obscurity · fix properly. Apply these **by default**, not on
request. When in doubt, the safer choice wins.

> The numbers in brackets are control ids in the client's own security-by-design checklist. Keeping
> them makes `/security-review` reports map 1:1 onto the form the client's security function expects —
> which is the difference between a review they can accept and one they have to re-do.

## Secrets and credentials (6, 11, 28) — non-negotiable
- **Never** hardcode credentials or secrets in code or versioned files. Use environment variables / a vault.
- **Never** log secrets (passwords, tokens, certificates, keys). Sensitive data in logs only masked or hashed.
- Credentials towards backends/databases are always encrypted, never in clear.

## Authentication & authorization (9, 10, 12, 13, 19, 23)
- Authority is verified **server-side**; UI gating is UX only, not security.
- Enforce RBAC with least privilege and need-to-know per `governance/rbac-matrix.md`; respect separation of duties.
- Local passwords (if ever present) with **bcrypt / PBKDF2 / scrypt** — never simple or reversible hashing.
- Sessions: inactivity timeout; **session id** with a generic name, random ≥128 bit, no PII.
- Session cookies with **Secure** and **HttpOnly** flags.
- **No backdoor, default account or mechanism that bypasses the controls.** The dev login is env-gated
  and forbidden in production (ADR-0002).

## Input, output, errors (24, 25, 28)
- **Validate and sanitise** every input and output — including the spreadsheets read during migration
  and any externally supplied library. Assume hostile input: the source data library already contains
  a material share of malformed cells, and a parser that trusts produces corrupt data long before
  there is an attacker.
- Explicit exception handling; the application does not crash uncontrolled.
- On error show a **generic error page**; **never** a stack trace or internal detail to the user.
- **Never** put sensitive data or credentials in URLs or query strings (no GET for auth); use POST.
- **CSRF** protection on state-changing actions (one-time token / re-auth).

## Logging & audit (2, 6, 7, 8)
- Logs are **append-only**: the code offers no path to delete or modify them.
- Every event: source, timestamp, outcome/summary (for non-repudiation).
- Log all **user management** and **governance** actions (grant/revoke, create/update/delete,
  approvals, releases) with who and when.

## Cryptography & transport (20, 22)
- No deprecated algorithms. Strong at-rest encryption (e.g. AES-256-GCM) where applicable in code.
- All traffic over **TLS ≥ 1.2**. No cleartext channel.

## Dependencies & supply chain (43, code side)
- Do not introduce unnecessary dependencies (minimize attack surface). Prefer maintained libraries.
- No dependency with known unresolved **Critical/High** vulnerabilities.

## What is NOT the code's job (defer)
Infrastructure (IDPS, WAF, DNSSEC, anti-malware, backup, HA, disk/DB-level encryption at rest,
environment separation) → **Platform/Ops**, often N/A when the client hosts. SSO/MFA, password policy
and CA certificates → **the auth spec + the client's IT**. See `governance/security-controls-map.md`.

## Operating rule
Every PR touching one of these areas must be able to pass the security gate (`/security-review`). If a
requirement does not apply to the PR, **declare it explicitly** (N/A + reason) rather than ignoring it.
