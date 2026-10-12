# Wave 1, executed — and the review that followed it

Wave 1 delivered the read side of the platform: version catalogue, data-model navigation,
exploration, search and filtering, export, plus a design-token system and an error-handling model.
It was demonstrated to the client and signed off.

Then we ran an **outside-in review** of the working repository: Claude Code with read-only access,
told to read it the way a principal-level reviewer would. The review found that the operating
model on paper was not the one being executed. The repository was realigned in a day.

This document covers both. Four sections, in order of how much you should trust them:

1. [What the data says](#what-the-data-says): measured, still a small sample.
2. [The fourteen bets after wave 1](#the-fourteen-bets-after-wave-1).
3. [Findings F–L](#findings-fl): what wave 1 taught that wave 0 had not.
4. [What wave 1 does not prove](#what-wave-1-does-not-prove), which became the next set of bets in
   [`W2-BETS.md`](W2-BETS.md).

---

## What the data says

**The caveat comes first, again.**

> Every line of governed code in waves 0 and 1 was built by **the architect who designed the method**,
> working part-time with Claude Code. The one full-time developer spent wave 1 on deliberate
> parallel trials whose code was, by design, not merged (finding **F**). So the numbers below show
> what the method does **in its author's hands**. Whether it works without her is bet #16.

Effort is indexed to the traditional baseline estimate = 100, as in wave 0. Absolute person-days and
costs stay out of this repository.

| Effort (build) | Wave 0 | Wave 1 |
|---|---:|---:|
| Traditional baseline estimate | 100 | 100 |
| Plan with Claude Code | 72 | 65 |
| **Actual (declared)** | **18** | **24** |

- Waves 0 and 1 together cost **31% of the AI-assisted plan**.
- Wave 1 was built about **seven weeks ahead** of the plan date.
- **Effect on scope:** the original plan could not fit the full phase 1 into the funded window, and
  one feature wave was set to be cut. With the measured uplift, **even halved**, the full phase 1 fits.
  The plan now uses the halved figure. It is the highest one the caveats below let us defend.

**Read the effort numbers with three caveats:**

- **Declared, not tracked.** Effort comes from the people's own tally.
- **Build only.** The functional team's effort is not measured. In wave 1 it absorbed 30 change
  requests and six meetings. The build uplift is therefore a **ceiling**, not a result (finding **J**).
- **Wave 1 is cut at the end of September.** The days after it, which include rework on one FR, are
  not in the number. It will go up.

**Process, wave 1:**

| | |
|---|---|
| Direct commits to `main` in one five-day stretch | **92**, against 3 PRs, so no coherence check at the right moment |
| Share of work that went through a PR | **22%** in wave 1, then **100%** in the following week |
| Acceptance criteria added to *approved* specs without a change request | **at least 20**, the largest group (9) on the two UI specs. First published as 13: the counting tool missed two specs ([finding Q](TRIAL-3-RESULTS.md#q--measuring-instruments-need-the-same-scrutiny-as-the-gates)) |
| Change requests registered | **46**, most from screen reviews and the client demo |
| Defects found by human code review **with every gate green** | **13** in one review |
| Share of changed lines spent on the method itself (specs, governance, scripts, CI) | **37%** in wave 0 → **28%** in wave 1 → **22%** in the following week |

The method measured all of these violations **on itself**, from git. None was reported by a person.

**What the gates caught**, out of 226 CI runs, 39 of them red:

| Stopped by | Runs | Real defects? |
|---|---:|---|
| Format and style | 14 | style |
| Security floor | 7 | **yes**: published vulnerabilities in a dependency |
| Documentation coherence lint | 7 | **yes**: real drift |
| Type check | 5 | **yes** |
| Tests | 3 | yes |
| Integration smoke | 1 | yes |
| Install failures | 4 | noise |

Never red: the frontend job, the FE↔BE contract check, the architecture lint. A red run in CI is a
**lower bound**, because most catches happen locally before the push.

**Acceptance.** First-pass acceptance was **6 of 6** in wave 0 and **3 of 5** in wave 1. Both came from
the first verification by the functional team, read from the change-request register rather than
written by hand. **Caveat:** that verification was internal, and the wave sign-off was given in chat
and transcribed by the person who built the wave. Bet #17 is about fixing exactly that.

---

## The fourteen bets after wave 1

| Bet | After wave 0 | After wave 1 |
|---|---|---|
| #1 LLM coherence check as a gate | partial | **found real drifts** on three FRs, all of the spec lagging the code. Precision still unmeasured → **#20** |
| #2 `FR-XX/ACn` traceability: real or theatre | untested | **the risk is real.** A round-trip test passed on eight empty sheets. The test named the AC and proved nothing. Human review caught it |
| #3 Do advisory gates become blocking | reframed | the taxonomy held: three more deterministic checks went straight to blocking |
| #4 `/reconcile`: rescue or legitimise | no signal | **bypassed by another practice.** The parallel trials produced code outside the flow, and it was mined for rules instead of reconciled |
| #5 Autonomy matrix too conservative | untested | **no class of work has moved** → **#23** |
| #6 Governance three times too big | untested | **answered the other way.** Governance shrank to two people, one of them the builder. The problem is not size, it is **independence** → **#15, #17** |
| #7 Markdown specs survive | lost | generation extended to six derived views; narrative drift remains (finding **G**) |
| #8 Keep `CLAUDE.md` lean | losing | **still losing**: about twice the length it had when it made the claim, plus five skills |
| #9 No multi-agent orchestration | held | held. The "second agent" turned out to be a second human (finding **F**) |
| #10 Define metrics late | right | measured again. Per-person hours were then **removed from the client-bound repository** for privacy; wave totals stay in the plan |
| #11 Hybrid rigor holds | untested | **reversed.** Rigor inflated instead of drifting (finding **I**) |
| #12 What makes plan review happen | still open | **still nothing structural** → made measurable as **#18** |
| #13 Security labelled safe | changed shape | the floor caught real vulnerabilities; production SSO is still not implemented |
| #14 Client as first-pass tester | untested | the client has not yet verified a wave, and has no named referent → **#17** |

---

## Findings F–L

Findings A–E are in [`W0-RESULTS.md`](W0-RESULTS.md). Like those, none of these was on any list.

### F — Same spec, two implementers, two systems

Two FRs were deliberately re-implemented in parallel by a second developer from **the same approved
spec**. The results:

- a backend structured differently, with its own conventions, importing a private symbol from
  another module and writing temporary files to disk;
- frontend–backend payloads that were incompatible with each other;
- CI red while the work was declared complete;
- and a spec that kept changing under the person building against it.

Lint and type checks were green on both sides. Nobody was wrong, because no rule covered any of it.

**The spec alone is not a control plane.** It took the spec **plus written architecture rules plus a
versioned interface contract** for two implementers to converge. The comparison produced eleven
changes to the method: an architecture lint, a contract check that runs without the database, CI on
every branch, "done" defined as a green CI run, the branch choice as a mandatory question, and more.

Two costs, stated plainly. The parallel code never reached `main`. And the trials were not written
down as an experiment, with a hypothesis and success criteria, until after they had happened.
Trial 3 ([`W2-BETS.md`](W2-BETS.md)) is designed the other way round.

### G — Guardians go green on the wrong set

These were all green while checking the wrong thing:

- the dependency scan audited an environment that did not contain the application's dependencies;
- a coverage check matched text inside comments;
- a role-mapping guard watched a format the repository no longer used;
- the round-trip test passed on empty sheets.

On one day, a commit message counted "the sixth time today that a guardian trips over the prose that
explains it".

The response is a rule: **every new check is verified by breaking it**. Introduce the defect it
guards against and confirm it turns red. Do this before trusting it, and again after any fix to it.

It happened again during the clean-up. A check added to stop the same fact (an FR's size) living in
two places did not read tables. The wave-plan table it was meant to clean kept six stale rows, and
the lint stayed green. The pattern is structural, not occasional. It recurred in trial 3, inside a
measuring instrument (finding **Q** in [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md)).

### H — Requirements discovered by looking enter through the `fix` commit

At least twenty acceptance criteria were added to approved specs without a change request. The
largest group, nine, was on the two UI specs. (This finding first said thirteen. A later repair of
the counting tool found the rest, and the true figure may be higher still: see finding **Q** in
[`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md).) This was not carelessness. A visual requirement is discovered by **looking at the screen**,
and the flow had no step where someone looks. The discovery went into a `fix` commit that changed
the spec and the code together. That is the golden rule broken, and nobody chose to break it.

The response is gate **1b**, visual review before the PR, with two obligations: write down what you
looked at, and open the change request **before** the fix, not inside it. Bet #19 tests it.

### I — Rigor inflated instead of drifting

Bet #11 feared that, under deadline pressure, every spec would drift to `light`. The opposite
happened: specs drifted to **`full`**, until 17 of 19 were `full` and the label no longer told anyone
anything. One spec still labelled `light` ran to six thousand words.

The fix was a criterion that can be checked: rigor is set by the **consequence of a defect** (data,
security, published contract), not by how important the feature feels. Result: 11 `full`, 8 `light`.

### J — A build uplift can move cost upstream

The functional team absorbed 30 change requests and six meetings in wave 1, and none of that effort
is measured. An uplift that shifts cost from build to analysis is a transfer, not a saving.

Until functional effort is measured, the build uplift is a **ceiling**. We wrote this down before
anyone asked. Bet #22 is the test.

### K — The operating model on paper was not the one being executed

The outside-in review compared the operating model document against git history. It found that the
document had **never been edited since the first commit**. Meanwhile:

| Declared | Executed |
|---|---|
| 2 developers, 2 analysts, 3 governance | 1 part-time architect, 1 full-time developer, a 3-person functional team |
| developers build through the flow | all governed code built by the architect, who also sat in governance |
| authority enforced by the platform | **not enforceable** on the current git platform, so a convention checked after merge |
| client verifies and signs | no client referent named yet; wave sign-off internal |

**No gate could have found this.** The gates compare documents with documents, and documents with
code. Nothing compared the *declared operating model* with *who actually committed and merged what*.
The gap was found by reading git history with an outsider's eyes.

The realignment took one day and 12 commits:

- the operating model now states **"today" next to "target"**;
- the README is one page, with a 30-minute reading path;
- the plan was redone on measured effort;
- the parallel trials were written up as experiments;
- wave sign-off has a written minute;
- each new check was verified by breaking it.

The fact that a repository built on *one fact, one home* could be brought back to the truth in a day
is itself evidence for the method's governability.

### L — A decision criterion was applied once, and then not

[ADR-0003](docs/adr/0003-architecture-stack-ratified-from-the-deck.md) chose the database because
**the client's platform standard is the dominant constraint**. Later, the client's IT recommended a
different database as their standard. The first response was to park the question because the code
already existed. That is the same criterion, with the opposite outcome, and a reviewer would call it
sunk cost.

It was corrected. The question is now decided at the point of entry onto the client's
infrastructure, on the client's binding answer and on the **measured** cost of switching, not on the
code that happens to exist. The ADR gained the review condition it had been missing.

---

## What wave 1 does not prove

1. **That the method works without its author.** Every governed line went through one person. → **#16**
2. **That acceptance is independent.** The wave sign-off was given from inside the build. → **#17**
3. **That the uplift is real at full cost.** The functional effort is unmeasured. → **#22**
4. **That governance can shrink.** Gates and documents have only grown: about 141,000 words of
   markdown for about 17,000 lines of application code. → **#21**
5. **That the client gets value, not just us.** The business case says what the money buys, not what
   it returns to the client. The client's value metrics have not been agreed yet.

The first four are now bets, with thresholds, registered in the working repository before the wave
that tests them (the public copy, and the first results, came later):
[`W2-BETS.md`](W2-BETS.md). The fifth has no bet yet, because it is not ours to define. It has to be
agreed with the client.

---

*Everything here is anonymized. Effort is indexed, costs are not published, and no individual is
named. See [`ANONYMIZATION.md`](ANONYMIZATION.md).*
