---
description: Security review — application security controls (wave-end gate, or on a PR)
argument-hint: [wave WX | FR-XX ...]
---

Run the **security review** per `governance/security-gate.md` and the `security-by-design` skill.
Always load the `security-by-design` skill. Scope: the wave or the FRs given ($ARGUMENTS); if absent,
infer it from the diff.

Produce a **report** with an outcome for each control applicable to the scope: **Pass · Fail · N/A
(with reason)**. **High-confidence findings only.** For every Fail, say where and how to remediate.

Check the application controls relevant to the scope (map in `governance/security-controls-map.md`):

**Always (every PR/wave):**
- Hardcoded secrets/credentials in code or versioned files? (6, 11, 28) → must be **Pass**
- Secrets or sensitive data logged without masking/hashing? (6) → **Pass**
- Unvalidated/unsanitised input; missing exception handling? (28) → **Pass**
- Stack trace or internal detail shown to the user on error? (24) → **Pass**
- Sensitive data/credentials in URLs or query strings? (25) → **Pass**

**If the scope touches auth/RBAC/sessions:**
- Authorization verified server-side (not only UI)? least-privilege RBAC enforcement? (9, 10, 23)
- Session timeout; session id random ≥128 bit without PII; cookies Secure + HttpOnly? (13, 23)
- No backdoor/default/bypass mechanism? dev login env-gated out of production? (19, ADR-0002)
- Local passwords with bcrypt/PBKDF2/scrypt? (12)
- Anti-CSRF on state-changing actions? (17)

**If the scope touches logging/governance:**
- Logs append-only (no delete/modify path)? (2)
- User-management and governance actions logged with who/when/summary? (7, 8)

**If the scope touches cryptography/transport/data:**
- No deprecated algorithms; TLS ≥ 1.2; strong encryption where done in code? (20, 22)

**If the scope touches file import or export:**
- Robust validation of imported files; exports that do not expose secrets or unauthorised data? (28, 6)

**Automated scans (report their status, do not run them yourself):**
- SAST: unresolved **High/Critical** findings? (32) → if yes, **Fail**
- Secrets scan: secrets in the repo? → if yes, **Fail**
- Dependencies: known unresolved **Critical/High** vulnerabilities? → if yes, **Fail**

Close the report with: the list of **Fails** (blocking for the gate), the list of **justified N/As**,
and the **evidence** to retain (log samples, SAST report) for the client's security form.

**Human-in-the-lead:** the outcome is decided by whoever reviews. You provide the report.
