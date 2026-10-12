# claude-code-team-collaboration

**A real modernization programme run with Claude Code: bets registered before each wave, scoreboards
published after it.**

One of a series documenting how I work with Claude Code, each repository focused on one topic.
This one is about **team collaboration**: how a mixed human team and Claude Code divide work,
decision rights and accountability on a digitalization programme for the engineering function
of an energy & utility EPC contractor.

> **This is not a showcase.** It is an operating model designed by two principal AI architects with
> strong traditional-delivery instincts. We published it with fourteen open bets **before running
> anything through it**, and asked to be taken apart.
>
> **Waves 0 and 1 have been executed, demonstrated and signed off**, out of five. After wave 1 an
> outside-in review found that the operating model on paper was not the one being executed. Then
> **trial 3** tested the question that leaves: does the method work without its author?
>
> **→ Start at [TRIAL-3-RESULTS.md](TRIAL-3-RESULTS.md).** The method transferred **construction**
> to a second developer, but not **governance**. The bets it was measured against are in
> [W2-BETS.md](W2-BETS.md), registered before the trial; the wave history is in
> [W1-RESULTS.md](W1-RESULTS.md) and [W0-RESULTS.md](W0-RESULTS.md).

---

## Where it stands, in one table

| | |
|---|---|
| **Measured build uplift vs traditional baseline** | **82%** in wave 0, **76%** in wave 1. Two caveats matter more than the numbers: every governed line was built by **the method's own author**, and only build effort is measured, so the uplift is a **ceiling** |
| **The strongest finding** | **The spec alone is not a control plane.** Two developers implementing the same approved spec produced two different systems. It took the spec **plus** architecture rules **plus** a versioned contract to make them converge |
| **What embarrassed us most** | The operating model document was never edited after the first commit, and the real one had drifted away from it. **No gate compared the declared model with git history** |
| **The pattern that keeps coming back** | Guards that are green while checking the wrong thing. The rule now: every new check is verified **by breaking it** |
| **What trial 3 showed** | A second developer built a full FR in 28 hours from the readiness gate: 2 questions to the architect against a cap of 5, zero structural defects, zero lines from the architect. **But** the PR was merged 24 seconds after opening, before review, and 0 of 10 later merges had a native review. Mechanical controls transferred; human procedures did not |
| **What is still unproven** | That the method is cheaper in someone else's hands (effort not yet measured), that governance transfers, and that the client signs off independently (bet **#17**) |

## The thesis this setup embodies

**The specification is the control plane.** Humans express intent and governance in the spec;
Claude Code produces inside declared boundaries; spec↔code coherence is an **invariant enforced
mechanically**, not an activity someone remembers to do.

The corollary we are betting on: in AI-powered delivery, humans move *up* the value chain, from
*producing* to *specifying, verifying, deciding*. Claude Code is connective tissue, **never** a
decision-maker. Recognition of authority belongs to the platform (SSO, git, CODEOWNERS, CI), never
to the model.

**What two waves changed:**

- The control plane turned out to need more than the spec: architecture rules and a versioned
  contract as well (finding **F**).
- Platform-enforced authority is **not yet available** to us, so today it is a convention checked
  after every merge (bet **#15**).

## The flow, in one diagram

```
spec (FA) ──G1──> plan (dev) ──> build+test (dev+AI) ──visual review 1b──gate 3──> PR
   └─ /reconcile ← orphan code (vibecoding) re-enters here
PR ──> merge ──contract test──> verification ──wave sign-off──> done
```

**Blocking** (by convention today: red does not go to `main`): G1, docs lint (3b), integration
smoke (S), security floor, contract test, wave sign-off.
**Advisory by design:** the coherence gate. It reasons, so a human judges its report. Whether that
should change is bet **#20**.

## How to navigate

| Where | What it holds |
|---|---|
| [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md) | **The latest scoreboard.** Trial 3: a second developer builds with the method. Findings M–R. Read first. |
| [`W2-BETS.md`](W2-BETS.md) | Bets #15–#23 on governance, registered before trial 3, with thresholds and the trial design. |
| [`W1-RESULTS.md`](W1-RESULTS.md) | The wave-1 scoreboard, the outside-in review, findings F–L. |
| [`W0-RESULTS.md`](W0-RESULTS.md) | The wave-0 scoreboard and findings A–E. |
| [`FEEDBACK.md`](FEEDBACK.md) | The original ask: the situation, bets #1–#14 in full, how to respond. |
| [`governance/`](governance/) | Operating model (today vs target), quality gates, Definition of Ready, open points, RBAC, security. |
| [`scripts/`](scripts/) | The mechanics of the gates: what turned a written model into an executing one. |
| [`metrics/`](metrics/) | The measurement. Actuals per wave, dashboard **generated** from them. |
| [`.claude/`](.claude/) | Agent context: `commands/` (the team's workflow) and `skills/` (domain, loaded on demand). |
| [`CLAUDE.md`](CLAUDE.md) | Root agent context. It claims to be lean; see bet #8, which we are losing. |
| [`spec/`](spec/) · [`docs/`](docs/) · [`contracts/`](contracts/) | Specifications, lifecycle and ADRs, the downstream contract. |
| [`ANONYMIZATION.md`](ANONYMIZATION.md) | Exactly what was renamed, and the disclosure policy for figures. |

## The team: designed vs actual

| | Designed | Actual, after trial 3 |
|---|---|---|
| Developers | 2 | 1 full-time; in wave 1, deliberate parallel trials not merged; in trial 3, one FR built and merged |
| Builder of governed code | the developers | mostly the **architect**, part-time, with Claude Code; since trial 3, also the developer |
| Functional analysts | 2 | a 3-person functional team; decides in chat and meetings, signs specs |
| Governance | 3 | 2, one of whom is the architect |
| Client | first-pass verification and sign-off | no named referent yet |

None of them had worked in an agent-driven flow before this programme. The gap between the two
columns is the main limit of everything measured so far. Trial 3 narrowed it for construction, not
yet for governance.

## Reading order we suggest

1. [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md): what happened when someone else built with the method.
2. [`W2-BETS.md`](W2-BETS.md): the governance bets it was measured against.
3. [`W1-RESULTS.md`](W1-RESULTS.md): what wave 1 taught, including what we got wrong.
4. [`governance/operating-model.md`](governance/operating-model.md): who does what today, and the target.
5. [`governance/quality-gates.md`](governance/quality-gates.md): the gate taxonomy, what the gates
   caught, and the rule for removing one.
6. [`W0-RESULTS.md`](W0-RESULTS.md) and [`FEEDBACK.md`](FEEDBACK.md): where it started.

---

*By Svitlana Matsutska. This repository shows a way of organising a human team around Claude Code
on an enterprise modernization programme, where accountability, traceability and client trust are
not negotiable. Published under MIT so you can lift any part of it.*
