# Bets #15–#23: governance, registered before wave 2

The first fourteen bets ([`FEEDBACK.md`](FEEDBACK.md)) were about the **design** of the method, and
were published before wave 0 ran. Waves 0 and 1 have now run; the scoreboard is in
[`W0-RESULTS.md`](W0-RESULTS.md) and [`W1-RESULTS.md`](W1-RESULTS.md).

These nine bets are about **governing** the method: who decides, who verifies, what can be enforced,
when an AI judgement may block a merge, and whether governance can shrink as well as grow.

**Registration, stated precisely.** These thresholds were registered in the working repository on
**2026-10-08, before trial 3 started**. That commit's timestamp is the registration, and git history
shows the thresholds were never edited afterwards. **This public copy was published later, together
with the trial-3 results.** If you rely on pre-registration, rely on the working repository's history,
not on the date of this file.

**Results so far:** [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md). #15 and #18 were lost, #16 held (with
a hole in its threshold that we own), #19 shows no violation so far, and #17 and #20 are not yet
measurable.

Numbering continues from #14, so the record reads as one register, not two lists.

---

## Rules for the bets themselves

The same rules that govern the project apply to these bets:

- **Thresholds are frozen.** A threshold changes only through a dated amendment at the bottom of this
  file, with the reason. Git history shows any edit that skips that step. *"You moved the goalposts"*
  should be a checkable accusation, not a debate.
- **Measured by tools, not written by hand**, wherever possible: git history, the CI run log, the
  change-request register, and the process-metrics script. Where a human judgement is needed (is a
  coherence finding true?), the person judging is **not** the person who built the change.
- **Results are aggregate.** Defects found belong to the method, not to a person.
- **A bet with no measurement at the end of its window counts as lost**, not as open.

The working repository holds the authoritative, timestamped registration. This file is its public
translation; the thresholds are the same.

---

## Authority and independence

### #15 · Does authority hold without the platform?

The thesis says authority counts when the platform enforces it. In practice there is no branch
protection: the current git platform cannot enforce it until the project moves to the client's own
instance. Gates are therefore a convention, checked after each merge.

- **Bet:** the convention holds as long as it is measured.
- **Thresholds, wave 2:**
  - **100%** of merges to `main` go through a PR with green CI;
  - a red `main` is repaired within **1 working day**;
  - **0** merges of a change without a second person's review.
- **Proven wrong if:** a single merge to `main` bypasses the PR under delivery pressure.
- **Measured from:** git history (merge commits vs. direct commits) and the CI run log.

### #16 · Does separating builder, reviewer and signer remove the dependency on the architect? *(trial 3)*

In waves 0 and 1 every line of governed code went through one person (see finding **K** in
[`W1-RESULTS.md`](W1-RESULTS.md)). Trial 3 is designed to test exactly this. Its design is below.

- **Bet:** with the spec frozen and the full harness in place, a second developer lands one FR on
  `main` without the architect writing any code.
- **Thresholds:**
  - questions to the architect **≤ 1 for every 2 acceptance criteria** of the frozen spec, and none
    answered by changing the spec outside a change request;
  - CI green **before** the work is declared done, in **100%** of cases;
  - **0** structural defects found in review that the architecture lint or the contract check
    should have caught;
  - **0** lines of code on the trial branch written by the architect.
- **Proven wrong if:** the FR reaches `main` only after the architect rewrote it, wholly or partly.

### #17 · Can wave sign-off become independent without slowing the wave down?

Today wave sign-off is given in chat and transcribed into the repository by the architect, who also
built the wave. The acceptance gate is signed, in effect, from inside the build.

- **Bet:** once a client referent is named, wave 2 is signed by **someone who did not build it**.
- **Thresholds, wave 2:**
  - the signatory is outside the build team;
  - **≤ 5 working days** from "wave built" to "wave signed";
  - first-pass acceptance, judged by the client, **≥ 60%**. That is the wave-1 level, now on
    write-side features and with an external judge.
- **Proven wrong if:** the signature stays internal, or first-pass acceptance collapses as soon as
  the client is the judge.

## The human controls no script protected

### #18 · Does the plan review become evidence? *(makes bet #12 measurable)*

Bet #12 has been open since before wave 0. Two waves and many new gates later, nothing structural
protects the plan review, which is the cheapest control and the first to be skipped.

- **Bet:** once the approved plan is an artefact in the PR, the review stops being an intention.
- **Threshold, wave 2:** in **100%** of PRs the written plan is approved by someone other than the
  builder **before** the first code commit. Verified from git and PR timestamps.
- **Proven wrong if:** plans appear after the code, or get approved in batches a few minutes apart.

### #19 · Does the spec hold still when someone looks at the screen?

In wave 1, **at least 20 acceptance criteria were added to already-approved specs without a change
request**, the largest group (nine) on the two UI specs. The first count said 13; the counting tool
had missed two specs (finding **Q** in [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md)). Visual requirements are discovered by looking, and they came in
through the `fix` commit (finding **H**). Gate 1b (visual review, with the change request opened
*before* the fix) is the response.

- **Bet:** gate 1b brings this number to zero.
- **Threshold, wave 2:** acceptance criteria added to `Approved` specs without a change request =
  **0**, counted by the process-metrics script.
- **Proven wrong if:** visual requirements keep entering through the `fix` commit.

## AI judgement

### #20 · When may an AI judgement block a merge?

The coherence check (gate 3) is LLM-reasoned and advisory by design: no merge is blocked on AI
judgement alone. This bet asks what evidence would justify changing that.

- **Bet:** the coherence check becomes blocking, but **only for high-confidence findings** and only
  once its precision justifies it.
- **Thresholds:**
  - across **at least 10 findings** (accumulated over wave 2), the share confirmed as true by a
    reviewer who did not build the change is **≥ 80%**;
  - if so, high-confidence findings block from wave 3;
  - if not, the gate stays advisory, as a stated decision.
- **Proven wrong if:** precision stays below the threshold and the gate is hardened anyway, or
  precision is never measured.

## The economics of governance

### #21 · Can governance shrink?

Gates are usually added and rarely removed. The project now has a written pruning rule: a gate is
removed when it has not been red in CI, and no PR has declared it caught something, for two waves in
a row.

- **Bet:** the pruning rule removes or merges **at least one gate by the end of wave 3**.
- **Thresholds:** the gate count never exceeds **9**, and documentation words per delivered FR go
  down.
- **Proven wrong if:** at the end of wave 3 there are more gates and none has been removed.

### #22 · Does the uplift survive full-cost accounting?

The measured uplift is on **build** only. The functional team's effort is not measured, and in wave 1
it absorbed 30 change requests and six meetings. An uplift that moves cost upstream is a transfer,
not a gain (finding **J**).

- **Bet:** with functional effort measured from wave 2, **total** cost (build plus analysis) stays
  **≤ 60%** of the total traditional baseline.
- **Proven wrong if:** the functional side absorbs what the build side saves.

### #23 · Does the autonomy ladder actually move on data? *(makes bet #5 measurable)*

The autonomy matrix was meant to widen as data came in. After two waves, no class of work has moved.

- **Bet:** by the end of wave 3, at least **one** class of work moves to "AI alone". The move follows
  a rule written before it is applied, for example two waves with no review defects of that class.
- **Proven wrong if:** autonomy stays frozen out of caution, or widens without data behind it.

---

## Trial 3: the design, registered before it ran

**Question:** does the method work without its author?

**Design:**

- **One FR, built only by the second developer** using the method (readiness check, plan,
  implementation, PR), with no second implementation alongside it.
- **The architect reviews and does not write code.** While the trial runs, the architect works on
  other specs. Two people on two different things, not two implementations of the same thing.
- **The spec is frozen.** It passes the readiness gate (G1) with human signatures and is then tagged.
  The builder, the reviewer and the measurement all refer to that tagged version. Any change goes
  through a change request, and every such change counts against bet #19. This is the lesson of
  trials 1 and 2, where the spec kept moving under the builder.
- **Every question to the architect is written in the PR**, one line each. That count is the
  measurement of dependency, not an inconvenience.

**Preconditions, before the first line of code:**

- the spec passes G1 and is tagged;
- `main` is green;
- CI runs on the trial branch from the first push;
- the builder has read the 30-minute reading path;
- the synthetic test library already contains the spec's hard cases.

**What is recorded:**

| Measure | Bet |
|---|---|
| time from approved spec to first PR | (baseline, no threshold) |
| written plan approved before the first code commit | #18 |
| questions to the architect, and how each was resolved | #16 |
| CI green before "done" | #16, #15 |
| change requests and acceptance criteria added during the build | #19 |
| coherence findings, each judged true or false by the reviewer | #20 |
| defects found in review, by class | #16 |
| first-pass acceptance of the FR at its first verification | #17 |
| lines of code on the branch written by anyone other than the builder | #16 |

The results are published in [`TRIAL-3-RESULTS.md`](TRIAL-3-RESULTS.md), aggregate and against these
thresholds.

---

## Amendments

*None. Any change to a threshold above is recorded here with its date and reason.*
