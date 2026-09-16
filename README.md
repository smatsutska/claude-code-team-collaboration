# claude-code-team-collaboration

**Seven people and an agent on a real modernization programme — fourteen bets published before the
first wave, and the scoreboard after it.**

One of a series documenting how I work with Claude Code, each repository focused on one topic.
This one is about **team collaboration**: how a mixed human team and Claude Code divide work,
decision rights and accountability on a digitalization programme for the engineering function
of an energy & utility EPC contractor.

> **This is not a showcase.** It is an operating model designed by two principal AI architects with
> strong traditional-delivery instincts and limited scar tissue in AI-powered delivery. We published
> it with fourteen open bets **before running anything through it**, and asked to be taken apart.
>
> **Wave 0 has now been executed, demonstrated and measured.**
>
> **→ Start at [W0-RESULTS.md](W0-RESULTS.md).** Four bets answered, one reframed, nine still open —
> and five findings that were on nobody's list, including ours.

---

## What we got wrong, in one table

The short version of the scoreboard, because it is the reason to read further:

| | |
|---|---|
| **Measured uplift vs traditional baseline** | **82%** — and the caveat that matters more than the number: wave 0 was run by the harness's *designers*, not by the seven-person team the model is written for |
| **The bet we reframed** | "Advisory gates become blocking when the data says so" was the wrong question. Gates split by **nature**: deterministic ones block on day one, LLM-reasoned ones stay advisory by design |
| **The failure we did not predict** | Documentation drift, not code drift. The agent produces cross-referenced documents faster than humans keep them coherent |
| **The thing that embarrassed us most** | Our gates were **documented but not wired**. They executed nothing while passing every governance review |
| **Still unanswered after nine days and five new gates** | What actually makes a plan review happen. We protected everything scriptable and nothing that wasn't |

## The thesis this setup embodies

**The specification is the control plane.** Humans express intent and governance in the spec;
Claude Code produces inside declared boundaries; spec↔code coherence is an **invariant enforced
mechanically**, not an activity someone remembers to do.

The corollary we are betting on: in AI-powered delivery, humans move *up* the value chain — from
*producing* to *specifying, verifying, deciding*. Claude Code is connective tissue, **never** a
decision-maker. Recognition of authority is delegated to the platform (SSO, git, CODEOWNERS, CI),
never to the model.

Wave 0 supports the thesis and does not yet test it: the people who wrote it were the people who ran it.

## The flow, in one diagram

```
spec (FA) ──G1──> plan (dev) ──> build+test (dev+AI) ──gate 3──> PR
   └─ /reconcile ← orphan code (vibecoding) re-enters here
PR ──> merge ──contract test──> UAT (client) ──wave sign-off──> done
```

**Blocking:** G1 (incl. no open blocking point), docs lint (3b), demo-smoke (S), security floor,
contract test, wave sign-off.
**Advisory by design:** the coherence gate — it reasons, so a human judges its report.

## How to navigate

| Folder | What it holds |
|---|---|
| [`W0-RESULTS.md`](W0-RESULTS.md) | **The scoreboard.** What happened, which bets survived, what we did not see coming. Read first. |
| [`FEEDBACK.md`](FEEDBACK.md) | **The ask.** Situation, the fourteen bets in full, how to respond. |
| [`scripts/`](scripts/) | The mechanics of the gates — what turned a written model into an executing one. |
| [`governance/`](governance/) | Operating model, autonomy matrix, quality gates, Definition of Ready, coherence gate, open points, RBAC. |
| [`.claude/`](.claude/) | Agent context: `commands/` (the team's workflow) and `skills/` (domain, loaded on demand). |
| [`CLAUDE.md`](CLAUDE.md) | Root agent context. Was deliberately lean — see bet #8, which we are losing. |
| [`spec/`](spec/) | The specifications: the "new source code". Seeded specs + template + generated traceability. |
| [`docs/`](docs/) | FR lifecycle, testing convention, ADRs, wave planning. |
| [`metrics/`](metrics/) | The measurement. Actuals hand-filled, dashboard **generated** from them. |
| [`contracts/`](contracts/) | The versioned boundary towards the downstream consuming system. |
| [`ANONYMIZATION.md`](ANONYMIZATION.md) | Exactly what was renamed, and the disclosure policy for figures. |

## The team being designed for

| Role | Count | Owns |
|---|---|---|
| Developer | 2 | Spec-author, Claude Code orchestrator, reviewer. Technical integrity. |
| Functional Analyst / Tester | 2 | The spec and the acceptance criteria. Owns gate G1. |
| Governance / Supervisor | 3 | The harness itself: autonomy policy, gates, security, PoC metrics. |
| Client engineering team | — | First-pass functional verification and domain sign-off. |

None of them had worked in an agent-driven flow before this programme. That constraint shapes every
design choice here — and **none of them operated wave 0**, which is the main limit of everything
measured so far.

## Reading order we suggest

1. [`W0-RESULTS.md`](W0-RESULTS.md) — what happened, and the five findings nobody had on their list.
2. [`FEEDBACK.md`](FEEDBACK.md) — the fourteen bets in full, and what we are asking.
3. [`governance/quality-gates.md`](governance/quality-gates.md) — the gate taxonomy that replaced
   "advisory → blocking".
4. [`scripts/`](scripts/) — the four scripts that made the gates real.
5. [`governance/operating-model.md`](governance/operating-model.md) — roles, decision rights, autonomy matrix.
6. [`docs/adr/0003-architecture-stack-ratified-from-the-deck.md`](docs/adr/0003-architecture-stack-ratified-from-the-deck.md)
   — how a client slide overrode an architecture decision record, and why our own readiness gate missed it.

---

*By Svitlana Matsutska. This repository shows a way of organising a human team around Claude Code
on an enterprise modernization programme, where accountability, traceability and client trust are
not negotiable. Published under MIT so you can lift any part of it.*
