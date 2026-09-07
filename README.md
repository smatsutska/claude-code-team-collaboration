# claude-code-team-collaboration

**Seven people and an agent, on a real modernization programme — published as a request for critique.**

One of a series documenting how I work with Claude Code, each repository focused on one topic.
This one is about **team collaboration**: how a mixed human team and Claude Code divide work,
decision rights and accountability on a digitalization programme for the engineering function
of an energy & utility EPC contractor.

> **This is not a showcase.** It is an operating model designed on paper by two principal AI
> architects with strong traditional-delivery instincts and limited scar tissue in AI-powered
> delivery. The harness is built and seeded; **wave 1 has not yet been run through it**. Before we
> commit a real team and a real client to it, we want it taken apart.
>
> **→ Start at [FEEDBACK.md](FEEDBACK.md).** It states the situation, and lists the fourteen bets
> we are least sure about — including the ones we suspect are wrong.

---

## The thesis this setup embodies

**The specification is the control plane.** Humans express intent and governance in the spec;
Claude Code produces inside declared boundaries; spec↔code coherence is an **invariant enforced
mechanically**, not an activity someone remembers to do.

The corollary we are betting on: in AI-powered delivery, humans move *up* the value chain — from
*producing* to *specifying, verifying, deciding*. Claude Code is connective tissue, **never** a
decision-maker. Recognition of authority is delegated to the platform (SSO, git, CODEOWNERS, CI),
never to the model.

If that thesis is wrong, most of this repository is wrong with it. That is one of the things we
are asking about.

## The flow, in one diagram

```
spec (FA) ──G1──> plan (dev) ──> build+test (dev+AI) ──gate 3──> PR
   └─ /reconcile ← orphan code (vibecoding) re-enters here
PR ──> merge ──contract test──> UAT (client) ──wave sign-off──> done
```

**Blocking** gates: G1 (spec ready), contract test, wave sign-off.
**Advisory** gate (deliberately, at the start): the coherence gate.

## How to navigate

| Folder | What it holds |
|---|---|
| [`FEEDBACK.md`](FEEDBACK.md) | **The ask.** Situation, open bets, how to respond. Read first. |
| [`governance/`](governance/) | Operating model, autonomy matrix, quality gates, Definition of Ready, coherence gate, RBAC. |
| [`.claude/`](.claude/) | Agent context: `commands/` (the team's workflow) and `skills/` (domain, loaded on demand). |
| [`CLAUDE.md`](CLAUDE.md) | Root agent context. Deliberately lean — see bet #8. |
| [`spec/`](spec/) | The specifications: the "new source code". Nine seeded specs + template + traceability. |
| [`docs/`](docs/) | FR lifecycle, testing convention, ADRs, wave planning. |
| [`apps/sgp/`](apps/sgp/) | A thin reference slice (auth/RBAC) showing how a spec reaches code. |
| [`contracts/`](contracts/) | The versioned boundary towards the downstream consuming system. |
| [`metrics/`](metrics/) | The PoC dashboard — deliberately undefined until the flow runs. See bet #10. |
| [`ANONYMIZATION.md`](ANONYMIZATION.md) | Exactly what was renamed and why, so you can read this as the real thing. |

## The team being designed for

| Role | Count | Owns |
|---|---|---|
| Developer | 2 | Spec-author, Claude Code orchestrator, reviewer. Technical integrity. |
| Functional Analyst / Tester | 2 | The spec and the acceptance criteria. Owns gate G1. |
| Governance / Supervisor | 3 | The harness itself: autonomy policy, gates, security, PoC metrics. |
| Client engineering team | — | First-pass functional verification and domain sign-off. |

None of them had worked in an agent-driven flow before this programme. That constraint shapes
every design choice here — and is why several of them may be over-cautious.

## Reading order we suggest

1. [`FEEDBACK.md`](FEEDBACK.md) — the situation and what we are asking.
2. [`governance/operating-model.md`](governance/operating-model.md) — roles, decision rights, autonomy matrix.
3. [`docs/lifecycle.md`](docs/lifecycle.md) — one requirement, end to end.
4. [`governance/coherence-gate.md`](governance/coherence-gate.md) + [`.claude/commands/coherence.md`](.claude/commands/coherence.md) — the mechanism we are least sure of.
5. [`spec/_TEMPLATE.md`](spec/_TEMPLATE.md) + [`spec/FR-11-draft-standard-version.md`](spec/FR-11-draft-standard-version.md) — what a spec actually looks like.

---

*By Svitlana Matsutska. This repository shows a way of organising a human team around Claude Code
on an enterprise modernization programme, where accountability, traceability and client trust are
not negotiable. Published under MIT so you can lift any part of it.*
