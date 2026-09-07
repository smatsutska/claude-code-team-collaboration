---
description: Write or update the specification of an FR through a guided interview
argument-hint: FR-XX
---

You must produce (or update) the specification of requirement **$ARGUMENTS**, conforming to `spec/_TEMPLATE.md`.

Role of whoever invokes you: **Functional Analyst**. You are a thought partner: do NOT invent the
requirements — extract them by interviewing.

Proceed as follows:
1. Start from the verbatim text of the FR (ask for it, or retrieve it from `spec/traceability.md` / the Functional Annex).
2. Load the `esl-domain` skill if the FR touches SDC/CDC/TDC, versioning or mapping.
3. **Interview** the analyst, one question at a time, until you can fill every field. Cover at least:
   - preconditions and actions for each acceptance criterion;
   - the observable outcome of every AC (if it isn't verifiable, reformulate until it is);
   - what is **out of scope** (the boundaries that prevent scope creep);
   - edge cases and errors;
   - data model entities, RBAC roles, impact on the contract towards Downstream Studio (`contract_impact`).
4. Determine `rigor`: `full` for versioning / mapping workbench / release; `light` otherwise.
   With `full`, insist on ACs that also cover the edge cases.
5. Write every AC in **Given/When/Then**. Remember: each AC will become a test named `FR-XX/ACn`.
6. Save to `spec/FR-XX-<slug>.md` with `status: Draft`.
7. At the end, list what is still missing to pass G1 (defer to `/ready $ARGUMENTS`).

Do not move on to code. This command produces the spec only.
