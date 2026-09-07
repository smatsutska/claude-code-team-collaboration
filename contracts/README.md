# contracts/ — the boundary towards Downstream Studio

SGP is the **system of record** of the ESL; Downstream Studio (team `@studio-team`) **consumes** it.
One-way dependency: Studio → SGP.

Published contract (versioned, semver + deprecation):
- **Release API (read)** — *officially released* ESL versions, entities, mappings, metadata. The draft is
  never exposed.
- **esl-model** — schema/types (compile-time contract).
- **New version notification** — FR-32: signals a release newer than the consumer's baseline, without
  forcing migration.

Rules: no shared database; integration by contract only; **consumer-driven contract tests** (Studio's
expectations run in SGP's CI). If a PR has `contract_impact ≠ none`, the contract tests are blocking.
