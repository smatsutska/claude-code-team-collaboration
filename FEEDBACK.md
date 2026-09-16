# Tear this apart

> **Update — wave 0 has now been executed.** This document is unchanged in substance: the fourteen
> bets below are exactly as published *before* the first wave ran, which is the only thing that makes
> the answers worth anything. Each bet now carries its outcome.
> **The scoreboard, the caveats and the five findings that were on nobody's list are in
> [`W0-RESULTS.md`](W0-RESULTS.md).** Read that first; come back here for the full reasoning.

We are two principal AI architects setting up a digitalization and modernization programme for the
engineering function of an energy & utility EPC contractor. We know the sector. We know how to run
programmes the traditional way. We have designed the operating model in this repository to run that
programme **with Claude Code as the production layer and humans in the lead** — and we have far less
scar tissue in agent-driven delivery than the confidence of these documents suggests.

So we are publishing the whole harness and asking, plainly:

1. **What did we get right?**
2. **What did we get wrong?**
3. **What should we improve?**
4. **What should we learn** — concepts, practices, prior art we clearly haven't absorbed?
5. **What are our blind spots** — the things we didn't even think to put on this list?
6. **What could we have done better, or differently?**

Answers that say "this is good" are the least useful thing you can give us. Answers that say
"you will discover in week three that X collapses, here is why" are worth the most.

---

## The situation you're judging

| | |
|---|---|
| **Domain** | Engineering data standardization for EPC (Engineering, Procurement, Construction). A library of standard classes and attributes, versioned and released, consumed downstream by another engineering system. |
| **Product** | SGP — a web platform that governs, versions and releases that library. Phase 1 covers four use cases; a second domain is explicitly out of scope. |
| **Scale of the spec** | 55 functional requirements analysed; 28 in scope, 2 partial, 25 out. Four delivery waves plus a foundation wave. |
| **The team** | 2 developers, 2 functional analysts/testers, 3 governance/supervision, plus the client's own engineering team as first-pass testers. |
| **Prior experience** | **None of them has worked in an agent-driven flow before.** Traditional waterfall-ish and Scrum backgrounds. |
| **Commercial frame** | A proof of concept that must demonstrate value against a traditional baseline estimate of roughly `<N>` person-days over `<M>` months. The PoC has to *prove* the delivery model, not just ship the software. |
| **Client posture** | Conservative. Engineering data governance is high-consequence: a wrong standard released downstream propagates into plant design. |
| **Status when the bets were written** | The harness was built and nine specs seeded. **Wave 0 had not been executed through it.** All specs `Draft`, CI not wired, metrics deliberately undefined. We asked *before* the first real cycle. |
| **Status now** | **Wave 0 executed, demonstrated to the client, measured.** Six foundation specs Approved and merged, CI wired and blocking, first official data version loaded, three new gates. Measured uplift 82% vs baseline — [with caveats that matter more than the number](W0-RESULTS.md#what-the-data-says). **The seven-person team has still not operated the model.** |

## What we believe we got right (please attack these first)

- **The spec as control plane, not documentation.** Behaviour changes require a spec change first,
  code second. See [`CLAUDE.md`](CLAUDE.md), [`spec/README.md`](spec/README.md).
- **One mechanical hook that makes the whole thing computable:** every acceptance criterion gets a
  test whose name contains `FR-XX/ACn`. That single naming convention is what lets a gate compare
  spec against tests without a BDD framework. See [`docs/testing-convention.md`](docs/testing-convention.md).
- **Gates that start advisory and harden on data, not on a date.** See [`governance/quality-gates.md`](governance/quality-gates.md).
- **A recovery path instead of a punishment.** Code written without a spec is *reconciled* back into
  the flow, not rejected. See [`.claude/commands/reconcile.md`](.claude/commands/reconcile.md).
- **Authority enforced by the platform, not by the model.** CODEOWNERS and branch protection impose
  who signs what; the agent only recognises *declared intent* via the invoked command. See
  [`governance/operating-model.md`](governance/operating-model.md), [`CODEOWNERS`](CODEOWNERS).
- **Simple control loops over multi-agent orchestration.** The coherence gate is one job, one prompt.

## What we already suspect is wrong

We would rather list these than have you discover we were pretending.

> **How these four aged through wave 0:** the first is still untested — the governance layer was barely
> exercised. The second is **unchanged and unaddressed**: nine days, five new gates, nothing for the
> plan review. The third resolved in our favour. The fourth got worse before it got fixed.

- The **governance-to-builder ratio is 3:2**. Three supervisors for two developers. On paper it is
  "the harness needs custodians". In practice it may be a committee inspecting a two-person team.
- **We wrote our own escape hatch.** [`docs/lifecycle.md`](docs/lifecycle.md) says the plan review is
  "the cheapest link and the easiest to skip when in a hurry" — and then we did nothing structural to
  make it happen. We named the failure and left it unaddressed.
- **We designed the measurement last.** [`metrics/`](metrics/) says "to be defined on real operational
  data". That is defensible pragmatism and also exactly what a team that never gets a baseline says.
- **There is a known inconsistency sitting in the traceability index** (FR-08's use case field). We
  left it visible on purpose, but we have no process that guarantees it gets closed.
  *Wave 0 answered this one the hard way: the index drifted again, in company — statuses, inline
  totals, dead references, arithmetic that stopped adding up. The fix was not discipline. The index is
  now **generated** from spec front-matter, with a drift check in CI.*

---

## The fourteen open bets

Each one: what we chose, why, and **what would prove us wrong**. Cite the number when you respond.

**Where each one stands after wave 0** — full reasoning in [`W0-RESULTS.md`](W0-RESULTS.md):

| Bet | Outcome |
|---|---|
| #1 LLM coherence check as a gate | **partial** — caught 2 spec-drifts, missed an entire drift class; we added a deterministic lint beside it |
| #2 `FR-XX/ACn` traceability real or theatre | **untested** — same people wrote specs and tests, which is the one condition that cannot test it |
| #3 Do advisory gates ever become blocking | **reframed** — wrong question. Gates split by nature, not by maturity |
| #4 `/reconcile` rescues or legitimises vibecoding | **no signal** — 0 invocations, 6/6 spec-first, and the operators wrote the rule |
| #5 Autonomy matrix too conservative | **untested** — the team has not operated it |
| #6 Governance layer three times too big | **untested** — the governance layer was barely exercised |
| #7 Markdown specs survive 28 requirements | **no, as predicted** — the index drifted again within days. Fix: generate it, never write it |
| #8 Keep `CLAUDE.md` lean, and where is the line | **losing** — it grew, because the agent needed it to |
| #9 Refusing multi-agent orchestration | **held** — nothing broke, which is not evidence |
| #10 Defining metrics later | **we were right** — the baseline was captured, the dashboard is generated |
| #11 Does hybrid rigor hold | **untested** — every wave-0 spec was `rigor: full`; the pressure has not arrived |
| #12 What makes plan review happen | **still open, nothing added** — and that is the finding |
| #13 Security posture labelled safe | **changed shape** — security became a pillar; the original risk is still live |
| #14 Client as first-pass tester | **untested**, and a related contradiction surfaced: three documents disagree on whether the client approves |

### 1. Can an LLM coherence check actually work as a gate?
`/coherence` gives Claude three inputs — the referenced specs, the touched tests, the diff — and asks
for contradictions of exactly four kinds. We ask for *high-confidence findings only*: "3 true beats 30
possible".
**Proven wrong if:** precision on real PRs is low enough that developers start ignoring the report, or
the model's semantic findings (scope creep, spec-drift) turn out to be near-worthless compared to the
deterministic ones (orphan FR, test gap) — in which case we built a prompt where we needed a script.
→ [`governance/coherence-gate.md`](governance/coherence-gate.md)

### 2. Is `FR-XX/ACn` traceability real, or is it theatre?
We admit openly that the link is guaranteed **by existence**, not by semantic correctness: the gate can
prove AC3 has *a* test, never that the test actually verifies AC3.
**Proven wrong if:** developers learn to satisfy the naming convention with hollow tests and the metric
goes green while quality doesn't. We claim human code review catches this. Does it, in practice?
→ [`docs/testing-convention.md`](docs/testing-convention.md)

### 3. Do advisory gates ever become blocking?
Our promotion criterion is "a number, not a date": when contradictions trend down and the spec-first
share passes an agreed threshold, the gate starts blocking — critical FRs first.
**Proven wrong if:** in your experience advisory gates are permanent. The threshold is never agreed, the
curve never looks clean enough, and the gate becomes background noise everyone filters out.
→ [`governance/quality-gates.md`](governance/quality-gates.md)

### 4. Does `/reconcile` rescue vibecoding, or legitimise it?
Code without a spec gets its spec *inferred by Claude*, reviewed by the analyst, then re-enters at G1.
We consider this humane and realistic.
**Proven wrong if:** it becomes the default path. Why write a spec up front when the agent will
retro-fit one that passes? We may have built a legitimate bypass around our own golden rule.
→ [`.claude/commands/reconcile.md`](.claude/commands/reconcile.md)

### 5. Is the autonomy matrix far too conservative?
Today the agent works alone only on scaffolding, CRUD screens, unit tests, local refactors and technical
docs. Feature implementation against an approved spec is "AI recommends, human approves".
**Proven wrong if:** this is 2023 thinking. Teams shipping today may be several rungs higher, and our
caution may be costing exactly the value the PoC is supposed to demonstrate.
→ [`governance/operating-model.md`](governance/operating-model.md)

### 6. Is the governance layer three times too big?
3 governance/supervision people, 2 developers, 2 analysts.
**Proven wrong if:** the right shape is one part-time custodian and more capacity in spec authoring —
which our own wave plan says is the actual bottleneck ("the analysts carry the highest load in W1").
→ [`docs/waves/wave-1.md`](docs/waves/wave-1.md)

### 7. Do markdown specs in git survive 28 requirements across 4 waves?
No requirements tool. Specs are markdown files with YAML front-matter, versioned in git, indexed by a
hand-maintained [`spec/traceability.md`](spec/traceability.md).
**Proven wrong if:** the index drifts from the front-matter (it already has, once), cross-FR
dependencies become unmanageable by hand, or the client refuses to review requirements in a repo.

### 8. Is "keep CLAUDE.md lean" right, and where is the line?
Our root [`CLAUDE.md`](CLAUDE.md) is ~35 lines and asserts *"more text here = worse agent reasoning"*.
Detail is pushed into on-demand skills and specs. We also use a scoped `CLAUDE.md` per app.
**Proven wrong if:** the agent keeps missing constraints that a longer file would have carried, or the
skill-loading heuristic ("load `esl-domain` when relevant") doesn't fire reliably enough.

### 9. Was refusing multi-agent orchestration the right call?
Deliberate: "simple control loops beat orchestrations". Five slash commands, one domain skill, no
subagents, no orchestrator.
**Proven wrong if:** a reviewer-subagent with a separate context window catches things a single-context
run cannot — particularly on the coherence check, where we're asking one prompt to hold spec, tests and
diff simultaneously.

### 10. Is defining metrics later pragmatic or self-serving?
[`metrics/`](metrics/) lists candidate curves (spec-first share, contradictions per PR, `/reconcile`
invocations, first-pass acceptance, lead time) but commits to none until the flow runs.
**Proven wrong if:** wave 1 passes and no baseline was captured, because nobody had instrumented
anything. The PoC then has a story and no evidence.

### 11. Does hybrid rigor hold, or does everything drift to `light`?
One template; two depths. `rigor: full` for critical requirements (versioning, workbench, release),
`light` for the rest. Who decides is the analyst, under delivery pressure.
**Proven wrong if:** `full` quietly disappears from new specs after the first slipped deadline.

### 12. What actually makes the plan review happen?
We identified it as the highest-leverage, lowest-cost control against drift — `/implement` hard-stops
after the plan — and then protected it with nothing but a retrospective reminder.
**Proven wrong if:** developers approve plans reflexively. What have you seen make plan review real:
a second pair of eyes, a checklist, a written fidelity statement, something else?
→ [`.claude/commands/implement.md`](.claude/commands/implement.md)

### 13. Are we shipping a security posture we've labelled as safe?
Wave 1 is frontend-only. Auth is a pluggable provider with a **development-only** implementation
(role picker, no IdP) until the client's SSO is confirmed. We guard it with a build-time failure and a
permanent dev-mode banner, and we state that frontend gating is UX only.
**Proven wrong if:** you've watched a "temporary" dev auth provider reach production despite exactly
these guardrails. What actually stopped it?
→ [`docs/adr/0002-auth-strategy-pluggable-provider.md`](docs/adr/0002-auth-strategy-pluggable-provider.md)

### 14. Is "client team as first-pass tester" a gate or an offload?
We put the client's engineers in the flow as first functional verification, before formal UAT. We frame
it as domain expertise where it matters most.
**Proven wrong if:** the client reads it as us outsourcing QA to them — a serious problem in a
conservative account, and one we would not see coming from inside.

---

## The blind spots we're asking you to name

The fourteen above are the ones we can see. The question that matters more:

> **What is missing from that list entirely?**

Some directions we suspect we're weak in, without being able to judge ourselves:

- **Change management and adoption.** We designed a system. We wrote almost nothing about how seven
  people who have never worked this way actually *learn* it. There is no onboarding path, no pairing
  model, no ramp.
- **Cost and token economics.** Not modelled anywhere. Not once.
- **Failure modes of the agent itself.** No documented procedure for what happens when Claude Code is
  confidently wrong at scale — how it gets detected, contained, rolled back.
- **The client's side of the contract.** Nothing here says what we tell the client about AI in the
  delivery, what they've agreed to, or how liability and IP were framed.
- **Data handling.** The library contains the client's engineering standards. Nothing in this repo
  states what may or may not be sent to a model.
- **The exit.** No statement of what happens to this harness when we leave and the client's own team
  takes over.

If your reaction to any of those is "that's the one that will actually hurt you" — say so, and say why.

> **Wave 0 settled the value of this question.** Five findings emerged that were absent from both the
> fourteen bets *and* the six blind spots above — a stack that passed every check and would not start,
> documentation drift as the dominant failure mode, gates that were documented but wired to nothing, a
> client slide overriding an architecture decision record, and a governance contradiction a script can
> detect but not resolve. See [`W0-RESULTS.md`](W0-RESULTS.md).
> The list was not the problem. *Having only our own eyes on it* was.
>
> All six blind spots above remain unaddressed, including change management — which is now the
> load-bearing one, because the seven-person team is next.

## How to give feedback

**→ [Open an issue](../../issues/new/choose).** There is a template with the questions above, and the
bet numbers are stable references.
Prose in an issue is perfectly fine; a pull request that edits the document you disagree with is even
better, because it shows us the alternative rather than describing it.

Useful shapes for a response:

- *"Bet #N is wrong because [what happened when I tried it]."*
- *"You're missing X entirely, and it will surface at [moment]."*
- *"We solved this differently: [approach], trade-off was [cost]."*
- *"Read [prior art]. You are re-deriving something with a known answer."*

Blunt is welcome. This document exists because being corrected here is much cheaper than being
corrected in front of the client.

## What we will do with it

Every substantive response gets read and answered. Where feedback changes the design, we will change
the files in this repository and note what changed and who prompted it — so the repo stays an honest
record of the operating model, not a marketing artefact for it.

---

*Everything here is anonymized. Client, product, programme and domain-entity names have been
systematically replaced; the structure, the reasoning and the trade-offs are untouched. See
[`ANONYMIZATION.md`](ANONYMIZATION.md) for the exact mapping, so you can judge the real thing.*
