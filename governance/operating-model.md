# Operating model — roles, decision rights, AI autonomy

## Principle
In AI-powered delivery humans **move up the value chain**: from "producing" to "specifying, verifying,
deciding". Claude Code is connective tissue, **never** a decision-maker. Recognition of authority is
delegated to the platform (SSO, git, CODEOWNERS, CI), not to the AI.

## Roles and what they own

| Role | In the AI-powered model | Owns (objective) | Gate they own |
|---|---|---|---|
| **Developer** ×2 | Spec-author, Claude Code orchestrator, **reviewer** | Technical integrity: PRs, green gates, ADRs respected; code *accepted first time round* | Plan review, PR |
| **Functional Analyst / Tester** ×2 | Owner of the **spec** and the acceptance criteria; designs the tests | Traceability FR→spec→test→demo; executable ACs | G1 (Definition of Ready) |
| **Governance / Supervisor** ×3 | Custodians of the harness: autonomy policy, quality gates, security, PoC metrics | AI inside its boundaries; every decision traced; evidence of value | Wave sign-off, metrics |
| **Client engineering team** | **Tester and first functional verification** | First-pass acceptance; domain sign-off | UAT, wave sign-off |

## Autonomy matrix (human-in-the-lead)
A **conservative** starting point (assist → augment → autonomy). It widens only where the metrics show
reliability.

| Activity | AI alone | AI recommends, human approves | Human only |
|---|:---:|:---:|:---:|
| Scaffolding, boilerplate, CRUD screens | ● | | |
| Unit tests, local refactors, technical docs | ● | | |
| Feature implementation against an approved spec | | ● (PR + review) | |
| Changes to the data model / the published contract | | | ● (ADR + architect) |
| Business rules (versioning, workflow) | | ● | |
| Merge to main, release, deploy | | ● (gates + approval) | |
| Defining requirements and acceptance criteria | | | ● (FA + client) |
| Functional wave sign-off | | | ● (client + governance) |

## Recognising "who is who" (three distinct layers)
1. **Identity & role** — single sign-on per person; `roles` mapped as above. The truth about
   "who you are / what you decide".
2. **Authority enforced by the platform** — `CODEOWNERS` + branch protection: certain paths *require*
   certain signatures (e.g. `packages/esl-model` → architect; `spec/` → FA + client). It's the repo
   that enforces, not the AI.
3. **Intent declared to the AI** — expressed by the command invoked (`/spec`, `/implement`,
   `/coherence`, …). The AI recognises the intent; it does **not** authenticate the role.

## How autonomy evolves
Driven by **data**, not by the calendar: when the coherence-gate metrics show reliability
(fewer contradictions, more spec-first), activities move from the "recommends" column to "AI alone",
starting with the least critical FRs. See `quality-gates.md` for the advisory → blocking progression.
