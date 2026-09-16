# Security controls map

Maps the client's own security-by-design checklist onto **where each control is satisfied** in this
programme: application code, platform/operations, the client's IT, or not applicable.

> **Not reproduced here.** The control list itself is the client's internal document and is not
> published in this repository. What is published is the *shape* of the mapping and the reasoning
> behind it, because that is the transferable part. The control ids referenced in the
> `security-by-design` skill and in `/security-review` are kept as opaque numbers.

## Why a map rather than a checklist copy

An enterprise security checklist is written for a whole organisation. Most of its controls are not the
application's job, and a team that treats it as a to-do list either fakes compliance on infrastructure
controls it does not own, or stalls.

The map assigns every control exactly one owner:

| Owner | Typical controls | How it is evidenced |
|---|---|---|
| **Application code** | secrets handling, authz enforcement, input validation, error handling, logging, session and cookie policy, crypto in code, dependencies | `/security-review` report + CI floor |
| **Platform / operations** | IDPS, WAF, DNSSEC, anti-malware, backup, HA, encryption at rest, environment separation | the foundation spec; often **N/A — client-hosted** |
| **Client IT** | SSO, MFA, password policy, CA certificates, identity lifecycle | the auth spec + the client's own processes |
| **N/A** | controls that do not apply to this workload | recorded **with a reason**, never silently dropped |

## The rule that makes it usable

**One control, one owner.** A control owned by two parties is owned by neither — it is the security
equivalent of the drift problem described in *one fact, one home*
([`../CLAUDE.md`](../CLAUDE.md)). If ownership is genuinely shared, the map splits the control into
the part the code satisfies and the part the platform satisfies, and names both.

## How this is used at a wave gate

`/security-review` walks only the controls whose owner is **application code**, scoped to what the
wave actually touched. Controls owned elsewhere appear in the report as N/A with their owner named, so
the client's security function can see that they were considered rather than missed.

That distinction — *considered and assigned* versus *not mentioned* — is what makes the report
acceptable to a conservative client without a second review cycle.
