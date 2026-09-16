# Wave 0, executed — the scoreboard

Nine days ago this repository published fourteen bets about an AI-powered delivery harness, with a
banner saying **wave 0 had not been run through it yet**. It has now been run, demonstrated, and
measured.

This document is the scoreboard. It exists because the bets were published *before* the outcome was
known, which is the only thing that makes the answers worth anything.

**Three sections, in order of how much you should trust them:**

1. [What the data says](#what-the-data-says) — measured, small sample.
2. [The fourteen bets, scored](#the-fourteen-bets-scored) — four answered, one reframed, nine still open.
3. [The five findings that were not on the list](#the-five-findings-that-were-not-on-the-list) — the part we did not see coming, and the most useful thing here.

Then, importantly: [what this does **not** prove](#what-wave-0-does-not-prove).

---

## What the data says

**Read this caveat before the numbers, not after.**

> Wave 0 was executed **by the two people who designed the harness** — not by the seven-person team
> the operating model is written for. Maximum context, zero coordination overhead, no handover. The
> numbers below prove the harness works *for its authors*. That is a much weaker claim than the one
> the proof of concept has to make.

All effort figures are **indexed to the traditional baseline estimate = 100**. Absolute person-day
figures are commercial and stay out of this repository.

| Effort | Index |
|---|---:|
| Traditional baseline estimate | 100 |
| Estimate *with* Claude Code (planned) | 72 |
| **Actual** | **18** |

- **Uplift vs baseline: 82%**
- **Came in 75% under our own Claude-Code-assisted estimate** — i.e. our AI-adjusted plan was itself
  off by a factor of four, in the direction people will find suspicious.

**Process, wave 0:**

| | |
|---|---|
| Spec-first PRs | **6 / 6** |
| `/reconcile` invocations (code written without a spec) | **0** |
| Coherence gate contradictions — scope creep · spec-drift · test gap · orphan FR | **0 · 2 · 0 · 0** |
| Contradictions resolved **at root, before merge** | **2 / 2** |
| Data migration | first official version loaded; **~2% of rows rejected**, each with a traced reason |

The 2% rejection figure matters more than the volume it came from. The client's data owner signed off
on a version *because* the harness could state exactly what was in it and what was not.

---

## The fourteen bets, scored

Legend: **⬛ answered** · **◧ reframed — the question was wrong** · **⬜ still open**

### ⬛ Answered by the data

**#10 — Is defining metrics later pragmatic or self-serving?** *We were right, narrowly.*
The feared outcome was "wave passes, no baseline captured, PoC has a story and no evidence". The
baseline was captured. `metrics/dashboard.md` is now **generated** from a hand-filled actuals file by
`scripts/gen_metrics.py`. Designing the measurement after the flow existed produced six metrics we
actually collect, instead of twelve we would have abandoned. We will take the win and note the sample
is one wave.

**#7 — Do markdown specs in git survive 28 requirements across 4 waves?** *No — exactly as the bet
predicted, and faster.*
The bet said the hand-maintained index would drift and admitted "it already has, once". Within nine
days it drifted again, worse, and in company: spec statuses, inline totals, dead file references,
arithmetic that did not add up, and "X blocks Y" narratives that were no longer true. **The fix was
not discipline, it was generation**: `spec/traceability.md` is now produced from spec front-matter by
`scripts/gen_traceability.py`, with `--check` in CI. Markdown specs survive *if the derived artifacts
are never written by hand*. See finding **B** below — this turned out to be the dominant failure mode.

**#4 — Does `/reconcile` rescue vibecoding or legitimise it?** *No signal. Zero invocations.*
Six of six PRs were spec-first; nobody wrote orphan code. We are explicitly **not** claiming this as a
win: the operators were the people who wrote the rule. Zero is what perfect discipline looks like and
also what "nobody tested the boundary" looks like. Our own `metrics/README.md` says that early on a
*high* `/reconcile` count is good — orphan code re-entering the flow beats orphan code staying out.
By that standard zero is not yet a result.

**#13 — Are we shipping a security posture we have labelled as safe?** *The bet was too narrow.*
It asked only about dev auth reaching production. What happened is that security became a **pillar**:
a `security-by-design` skill, a `/security-review` command, a controls map, and a CI floor (SAST,
secrets scan, dependency scan) that has been **blocking since day one**. Authorization is enforced
server-side; UI gating is declared to be UX, not security. The original risk is still live, though —
the dev provider is what the client saw in the demo, and the real SSO is still unimplemented.

### ◧ Reframed — we were asking the wrong question

**#3 — Do advisory gates ever become blocking?**

The bet assumed advisory→blocking is a **maturity progression**: wait for the contradiction curve to
flatten, then tighten. Executing the wave replaced that with a **taxonomy**:

| Gate nature | Policy | Why |
|---|---|---|
| **Deterministic** (integration smoke, docs lint, security floor) | **Blocking from day one** | There is no judgment to calibrate — only a fact to verify |
| **LLM-reasoned** (the spec↔test↔code coherence check) | **Advisory, by design** | False positives and negatives are inherent; a human judges the report. *Never a merge blocked on AI judgment alone* |

Three new gates went straight to blocking during wave 0. The coherence gate stayed advisory — not out
of timidity, but because it is the one that reasons. The original framing would have had us waiting
for data before blocking on things that never needed data.

This is the correction we are most confident about, and nobody suggested it. It came out of running
the thing.

### ⬜ Still open — the team has not operated the model yet

**#5 (autonomy matrix too conservative)**, **#6 (governance layer three times too big)**,
**#14 (client as first-pass tester: gate or offload?)**, **#11 (does hybrid rigor hold?)**,
**#2 (is `FR-XX/ACn` traceability real or theatre?)**

These five need the actual team, under actual delivery pressure. Wave 0 ran with the designers as
operators, every spec at `rigor: full`, and the same people authoring specs and tests — which is
precisely the condition under which #2 cannot be tested.

**#9 (was refusing multi-agent orchestration right?)** — held, unchallenged. Still no subagents, still
five slash commands. Nothing broke, which is not the same as evidence.

**#8 (is "keep `CLAUDE.md` lean" right, and where is the line?)** — moved against us. `CLAUDE.md` grew:
a second golden rule and a block of security invariants. Both were added because the agent needed
them. The file asserts *"more text here = worse agent reasoning"* and is now materially longer than
when it asserted it. We still cannot locate the line.

**#12 (what actually makes the plan review happen?)** — **nothing changed, and that is the finding.**
Nine days, five new gates, zero structural protection for the one control we ourselves called the
highest-leverage and cheapest to skip. We protected everything that could be scripted and nothing that
could not. This is the single clearest thing wave 0 revealed about our own bias, and the bet we most
want answered by someone who has solved it.

---

## The five findings that were not on the list

The fourteen bets were the risks we could see. Wave 0 bit elsewhere. **This section is the reason to
read this repository.**

### A — "Green" does not mean "it runs"

Unit tests, type checks and lint were all green. The integrated stack had **never been started** until
the demo was prepared, at which point four blockers surfaced within an hour: CORS, an authenticated
export href returning 401, a missing dev script, and a missing server dependency.

A spec-driven harness with mechanical spec↔test traceability can ship something that does not start.
None of the gates were looking at the seam.

The fix was a blocking `demo-smoke` gate that boots both tiers and calls a protected route *through
the frontend proxy* — see [`scripts/demo-smoke.sh`](scripts/demo-smoke.sh). But the gate is the small
lesson. **The real lesson is cadence**: the integrated stack runs every wave, not only when it is
being demonstrated.

### B — The dominant drift was documentation, not code

Spec↔code coherence held: two contradictions, both resolved at root before merge. What drifted was
**document against document**: status fields, inline totals, dead references, stale "X blocks Y"
narratives, and a programme total whose arithmetic had stopped adding up.

We think this is **specific to AI-powered delivery**. The agent produces coherent, well-cross-referenced
documentation faster than humans can keep it mutually consistent. Every hand-maintained fact becomes a
drift site, and the volume of hand-maintained facts grows with agent throughput.

The response is now a golden rule in `CLAUDE.md`:

> **One fact, one home.** If a fact lives in two places, one is generated from the other. The
> hand-written fact is the recurring root cause of drift; generation is the cure, and the documentation
> coherence lint is the guard. The goal is **detectability** — drift announces itself instead of being
> discovered in an audit.

Gate 3b ([`scripts/coherence_docs_lint.py`](scripts/coherence_docs_lint.py)) is the guard. It is
deterministic, so by the taxonomy above it blocks from day one.

> **It caught drift while this document was being written.** Preparing this public repository meant
> removing a code slice, which left two documents pointing at files that no longer existed. The lint
> found both on the first run. More interestingly, both of those references ended with the phrase
> *"keep them aligned"* — a hand-maintained duplication described as a process. They now point at the
> check that enforces the alignment instead. You can reproduce this: `python
> scripts/coherence_docs_lint.py` in this repository.

### C — An ungated gate is worse than no gate

In the version of this repository published nine days ago, the verification commands in `CLAUDE.md`
were **placeholders**. The coherence gate and the security gate therefore executed nothing.

They were documented. They were reviewed. They were in the operating model. They ran zero checks.

That configuration is worse than having no gate, because it buys false confidence — a team believes it
is covered and stops looking. If you are reading a governance design that is not yet wired to CI,
assume this failure mode is present.

### D — A slide overrode an architecture decision record

`ADR-0001` chose PostgreSQL on internal criteria. Six days later the client kickoff deck showed a
different stack — the client's own platform standard — and **once a slide has been presented to the
client, it is a commitment**. `ADR-0003` ratified the deck and superseded `ADR-0001`.

The stack change is defensible; alignment to the client's platform is a legitimate dominant constraint.
**The governance failure is upstream of it.** `ADR-0001` was decided while the open-points register
still listed the client's infrastructure constraints as unresolved — and we already had the rule that
should have stopped it. Definition-of-Ready criterion 9 says work does not proceed while a Critical or
High open point is unresolved.

**That rule was scoped to specifications, not to architecture decisions.** The most expensive decision
in the programme walked past the control that existed to catch it.

If you take one transferable thing from this repository, consider making it this: *check what your
readiness criteria are scoped to, and whether your highest-consequence artifacts are inside that scope.*

### E — The mechanical gate found a contradiction it cannot resolve

The documentation lint surfaced a clean governance contradiction: the Definition of Ready makes the
client an approver, the RACI has the client only *consulted*, and no specification carries a client
approver.

Three documents, three different answers, all internally consistent. A script can detect the
disagreement. It cannot decide who signs — that is a human decision, and it is still open.

We are recording this as the **honest boundary of mechanization**: the gate's job is to make
contradictions undeniable, not to resolve them. Governance contradictions surface as documentation
drift, and that is the useful part.

---

## What wave 0 does **not** prove

Four things we want stated before anyone quotes the 82%.

**1. It is not the team's number.** It is the number produced by the harness's own designers. Every
bet about the operating model — autonomy, governance ratio, adoption, spec authorship under pressure —
remains untested. The proof of concept's central claim is unvalidated.

**2. The units are not comparable, and we knew it.** This is human *supervision* effort measured
against a traditional *build* estimate. It is the right measure for the commercial question being
asked, but it is not like-for-like, and it should never be quoted without that clause.

**3. Wave 0 is structurally anomalous.** Most of its cost was one-off investment in the harness
itself. We have been telling ourselves this does not recur — which is convenient, and which we are not
currently measuring. A wave that adds five gates is a wave that spent real effort on gates.

**4. Gate proliferation is now a live risk.** In one wave we added a documentation lint, an integration
smoke gate, a readiness criterion, a cross-FR check and a security gate — all authored by the only
people currently using them. The failure mode where the harness becomes the work is exactly the kind
a team cannot see from inside. The metric that would catch it is effort-on-harness versus
effort-on-features, and we are not collecting it.

---

## What we are asking now

The original six questions still stand — see [`FEEDBACK.md`](FEEDBACK.md). Wave 0 sharpens three of
them, and these are the ones worth your time:

1. **Bet #12, still unanswered.** We protect what is scriptable and leave the human controls bare. What
   have you seen actually make a plan review happen — a second reviewer, a written fidelity statement,
   a checklist, pairing? Something that survived delivery pressure.

2. **Finding B — is documentation drift the general case?** Our claim is that AI-powered delivery
   generates hand-maintained facts faster than humans can keep them coherent, and that generation plus
   a deterministic lint is the answer. If you have run agents on a documentation-heavy programme: is
   this what you saw, and did generation hold at scale?

3. **The 82%, attacked properly.** We have listed the four caveats we can see. Which one is
   load-bearing, and what breaks first when the seven-person team runs wave 1 instead of us?

And the standing question, which wave 0 just demonstrated is the one that matters:

> **What is missing from the list entirely?**

Findings A through E were all absent from fourteen bets and six named blind spots, written carefully by
two people who do this for a living. The list was not the problem — *having only our own eyes on it*
was.

---

*Everything here is anonymized; effort figures are indexed, not absolute. See
[`ANONYMIZATION.md`](ANONYMIZATION.md) for the mapping and the disclosure policy.*
