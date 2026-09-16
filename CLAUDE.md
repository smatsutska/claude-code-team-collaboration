# CLAUDE.md — root context

> This file is **executable context**, not documentation. Keep it **lean and accurate**:
> more text here = worse agent reasoning. Detail lives in skills (loaded on demand) and in specs.
>
> *This file has grown since wave 0 — a second golden rule and a security block. Both were added
> because the agent needed them. It is now materially longer than when it first asserted the sentence
> above. We still cannot locate the line: see bet #8 in [`FEEDBACK.md`](FEEDBACK.md).*

## What we're building
SGP (Standards Governance Platform): a web application governing the **ESL** standard engineering
data library for EPC engineering. Phase 1 = Standard Domain (UC-01→UC-04). The Project Domain
(UC-05→08) is **out of scope**.

## Golden rule
**The spec is the truth; the code follows it.** A behaviour change requires a spec change *first*
(approved), *then* code. Never the other way round.

## One fact, one home (wave-0 lesson)
If a fact lives in two places, **one is generated from the other** (indices from front-matter, totals
from sums, status from real status). The hand-written fact is the recurring root cause of drift;
generation is the cure, and the documentation coherence lint (gate **3b**) is the guard. The goal is
**detectability** — drift announces itself instead of being discovered by hand in an audit.

## How we work (workflow)
- `/spec FR-XX` — write or update a spec (guided interview). Owner: Functional Analyst.
- `/ready FR-XX` — check the Definition of Ready (G1) before build, **incl. criterion 9** (no open
  Critical/High point listing this FR/TF — see `governance/open-points.md`).
- `/implement FR-XX` — plan → test skeletons from the ACs → build. **Review the plan before writing code.**
- `/coherence` — spec↔test↔code coherence check on a PR (gate 3, advisory by design).
- `/reconcile` — code written without a spec: infer its spec and bring it back into the flow.
- `/security-review` — security review of a wave or of a PR touching the security perimeter.

## Hard boundaries
- Do not modify `spec/` or `packages/esl-model` without the required approvals (see CODEOWNERS / operating-model).
- Every branch/commit/PR references an **FR-ID** (or TF-ID).
- Every AC (acceptance criterion) must have at least one test naming it: `FR-XX/ACn` (see `docs/testing-convention.md`).
- The contract towards Downstream Studio (`contracts/`) is versioned: if you touch it, the contract tests run.

## Security (by design) — invariants
Apply **by default**, not on request:
- **Never** hardcode secrets or credentials in code or versioned files; **never** log secrets.
- Authorization is enforced **server-side**; UI gating is UX only, not security.
- Validate and sanitise every input; handle exceptions; **never** show a stack trace to the user;
  **never** put sensitive data in URLs.
- Logs are append-only; user-management and governance actions are logged with who and when.
- TLS ≥ 1.2 everywhere; no deprecated algorithms; session cookies Secure + HttpOnly.
- No backdoors or default accounts — the dev login is env-gated and forbidden in production (ADR-0002).

When writing code that touches auth, data/secrets, logging, cryptography, input, sessions or exports,
**load the `security-by-design` skill**. Every PR in the security perimeter must be able to pass
`/security-review`.

## Verification (always run before saying "done")
**Backend** (from the root) · Test: `uv run pytest` · Lint: `uv run ruff check .` · Type: `uv run mypy`
**Frontend** (from `apps/sgp`) · Test: `pnpm test` · Lint: `pnpm lint` · Type: `pnpm typecheck`
**Gates** · `bash scripts/demo-smoke.sh` · `python scripts/coherence_docs_lint.py --strict`
· `python scripts/gen_traceability.py --check`

> These were **placeholders** until wave 0 wired them, which meant the coherence and security gates
> executed nothing while appearing in every governance review. *An ungated gate is worse than no gate.*

## Decisions & boundaries
- Architecture and the "why": `docs/adr/`  · Operating model and AI autonomy: `governance/operating-model.md`
- **Open points that block the build**: `governance/open-points.md` (criterion 9 of G1)
- Domain semantics (SDC/CDC/TDC, versioning): skill `esl-domain` (loads when needed).

## Posture
You are a **thought partner**, not a code generator. Propose, explain trade-offs, ask when the spec is
ambiguous. Simple beats complex: simple control loops, no over-engineering.
