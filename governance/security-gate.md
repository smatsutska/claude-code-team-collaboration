# Security gate

Security is not a wave. It is a **floor that is always on**, plus a **review at every wave sign-off**.

This became a pillar during wave 0. In the previous version of this repository security was a single
bet (#13: "are we shipping a dev auth provider we have labelled as safe?") and a line in the Definition
of Done. That was too narrow — see [`../W0-RESULTS.md`](../W0-RESULTS.md).

## The two layers

**1. The floor — automated, blocking since day one**

Runs in CI on every PR, alongside test / lint / type-check:

| Check | Fails the build on |
|---|---|
| Secrets scan | any secret in the repository |
| SAST | unresolved High/Critical findings |
| Dependency scan | known unresolved Critical/High vulnerabilities |

These are **deterministic** gates. Per the taxonomy in [`quality-gates.md`](quality-gates.md) they block
immediately: there is no judgment to calibrate, only a fact to verify.

**2. The review — reasoned, at wave sign-off**

`/security-review` produces a report against the applicable application controls, with **Pass / Fail /
N/A (with reason)** for each. It is **LLM-reasoned**, so it follows the other half of the taxonomy:
the report is evidence for a human decision, never an automatic verdict. Whoever reviews decides.

A wave does not pass sign-off with an open **Fail**.

## The invariants that apply without being asked

These live in [`../CLAUDE.md`](../CLAUDE.md) so the agent carries them into every task, rather than
being reminded per-PR:

- No hardcoded secrets, ever; no secrets in logs.
- **Authorization is server-side.** UI gating is UX, not security. Hiding a button is not access control.
- Validate and sanitise all input; no stack traces to users; no sensitive data in URLs.
- Append-only logs; user-management and governance actions logged with who and when.
- TLS ≥ 1.2; session cookies Secure + HttpOnly.
- No backdoors or default accounts. The dev login is env-gated and forbidden in production (ADR-0002).

The detailed rules load on demand via the `security-by-design` skill; the review procedure is
[`/security-review`](../.claude/commands/security-review.md).

## Declaring N/A is mandatory, ignoring is not allowed

If a control does not apply to the scope under review, it is recorded as **N/A with a reason**. A
control that is silently skipped is indistinguishable, in a report, from one that passed — and the
whole point of the gate is that the client's security function can read the output and accept it
without re-doing the work.

## What this gate does not cover

Infrastructure controls — IDPS, WAF, DNSSEC, anti-malware, backup, HA, disk/database encryption at
rest, environment separation — belong to platform and operations, and are frequently N/A because the
client hosts. SSO, MFA, password policy and CA certificates belong to the auth spec and the client's
IT. See [`security-controls-map.md`](security-controls-map.md).

## The open risk this gate does not close

The demo the client saw ran on the **development** auth provider, because the real SSO is still
unimplemented and blocked on an external dependency. Every guardrail is in place — env gating, a
build-time failure in production, a permanent dev-mode banner, server-side enforcement — and bet #13
is still live precisely because guardrails like these are what everyone has in place right before a
temporary provider reaches production anyway.
