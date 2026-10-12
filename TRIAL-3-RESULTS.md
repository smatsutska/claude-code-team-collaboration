# Trial 3, executed: does the method work without its author?

In waves 0 and 1, every line of governed code went through the architect who designed the method
(finding **K** in [`W1-RESULTS.md`](W1-RESULTS.md)). Trial 3 tested the obvious question that
leaves: **can someone else build with it?**

**The design:**

- one FR, built by the second developer alone, through the method;
- the architect reviews but writes no code;
- the spec is frozen at a tagged version;
- every question to the architect is counted.

The design and thresholds are in [`W2-BETS.md`](W2-BETS.md).

**The short answer.** **Building** without the author works. **Governing** without her does not
yet. Every control that held was mechanical. Every control that gave way was a human procedure.
That is the same pattern as waves 0 and 1, now observed with a second person, and it is the most
important thing this programme has learned so far.

> **How to read this document.** The results come from git, the CI run log and the platform's PR
> record. They were then checked a second time by an outside-in, read-only review of the working
> repository. Where that review disagreed with our own reading, both readings are given.
> Defects are attributed **to the method, not to people**: when the method lets something through,
> the method is what needs changing.

---

## The registration, stated precisely

The thresholds were **registered in the working repository on 2026-10-08, before trial 3 started**.
The commit's timestamp is the registration. Git history shows the thresholds were never edited
afterwards.

This public copy was **not** published before the trial. It is being published now, together with
the results. If you want to rely on pre-registration, rely on the working repository's history, not
on the date of this file. We say this because the earlier version of [`W2-BETS.md`](W2-BETS.md)
claimed public pre-registration, and that claim would have been false.

---

## What the data says

| Measure | Value |
|---|---|
| FR built | one FR of size L: two dashboard views, server-side aggregation, about +3,100 lines including tests |
| Time from readiness gate to first PR | **28 hours** of calendar time |
| Questions to the architect | **2**, against a cap of 5 (one per two of the 11 frozen acceptance criteria). One became a change request |
| CI green before "done" | **yes**, on every commit and on the PR |
| Lines on the branch written by anyone but the builder | **0**, in the first build and in the correction |
| Defects found in review | structural **0** · behaviour **3** · visual 1 (to confirm on screen) · minor 2 |
| Coherence-check findings | **2**, both confirmed true by someone who did not build the change |
| Spec changes during the build | **1**, through a change request and a new spec tag. No change outside one |
| Merges to `main` through a PR | **100%**. `main` was never red |
| **The PR** | opened with an empty description and merged **24 seconds** later, **before any review** |
| Correction cycle | the 3 behaviour defects fixed in a new PR that passed CI, review, real-data verification and visual review **before** merge |

**What the frozen spec did.** Trials 1 and 2 failed partly because the spec moved under the person
building against it. This time it did not. One clarification went through a change request and a
new tag, and nothing else changed.

---

## The bets

Thresholds as registered; nothing was amended. The second column is our own reading. The third is
the outside-in review's reading, where it differs.

| Bet | Our verdict | Outside-in reading |
|---|---|---|
| **#15** Authority without the platform | **lost** | lost. Also measured as a rate (finding **P**) |
| **#16** Works without the architect | **held** | held, **but the threshold had a hole**: it counted structural defects only, and three behaviour defects stayed on `main` for three days. We wrote that threshold, and the hole is ours |
| **#17** Independent sign-off | not yet measurable | (window still open) |
| **#18** Plan review becomes evidence | **lost** | lost. The plan was approved before the production code, but only in chat |
| **#19** The spec holds still | **held** | **no violation so far, not "held"**: the bet covers all of wave 2, and four days have passed. The counting tool is also partly blind (finding **Q**) |
| **#20** When AI judgement may block | not yet measurable | 2 of 2 findings true, but it missed the worst defect: precision is not completeness |

**Merges since registration, and who reviewed them:**

| | PRs, out of 10 |
|---|---|
| Native review on the platform | **0** |
| Second-person review **before** merge (as comments, or transcribed from chat) | **4** |
| Review after merge | 1 |
| Reviewed only by the author | 1 |
| Merged under a declared waiver | 3 |
| No review and no declared waiver | 1 |

---

## Findings M–R

Findings A–E are in [`W0-RESULTS.md`](W0-RESULTS.md) and F–L in [`W1-RESULTS.md`](W1-RESULTS.md).

### M — The method transfers construction, not governance

| Held (mechanical) | Gave way (human procedure) |
|---|---|
| CI on every branch, "done = green" | the PR as a place to work, not a merge button |
| architecture lint, interface-contract check | the written plan, approved before code |
| the frozen, tagged spec | review before merge |
| the change request + new tag for any spec change | who signs a change request (finding **R**) |

Finding F in wave 1 said **the spec alone** does not make two implementers converge. Trial 3 adds the
positive half: **spec plus architecture rules plus a versioned contract** is enough for a second person
to *build* a full FR, with few questions and no structural defects. It is not yet enough to make the
surrounding governance happen without someone enforcing it.

### N — "Done = CI green" skips the real data, and the dependency moved

The worst defect was a dashboard grouping that showed seven families instead of six. It existed
because some group names in the real data differ only by letter case. The synthetic test data was
consistent by construction, and the real-data tests are skipped in CI by design. No gate could see it.
It was found by **running the feature against the real database during review**, and the architect
was the one who did that.

So the dependency on the architect did not disappear: it **moved from building to verifying on real
data**. Our definition of done is weaker than it reads. The fix is to make real-data verification part
of the builder's evidence in the PR, not a reviewer's private step.

### O — The PR became a merge button, and the evidence stayed in chat

The work was real every time. Plan approval, both questions, the visual review and several reviews all
happened, in chat and in calls. None of it reached the PR at the moment it happened, because the flow
had no step that required it. The PR itself was opened at the end and merged within seconds.

The interim remedy is a **dated transcription**: a PR comment that says it is a transcription, of what,
from which channel, and when. It records the truth without pretending to be something else. But it is
**not** a native platform review, and it does not count as one. That is why bet #15 stays lost even
where a review genuinely took place.

### P — Binary bets create a moral hazard

After bet #15 was lost, two later merges were justified with *"#15 is already lost, and a lost bet
cannot get worse"*. That is true of the bet as we wrote it, and it is exactly the flaw. **Once a binary
rule-bet is lost, breaking the rule again costs nothing.** Four more PRs merged without a second person
after the bet was lost.

A behavioural bet needs a **rate over the whole window** next to its verdict. Here that is merges with
a second-person review before merge, out of all merges: today **4 of 10**, and **0 of 10** natively.
The verdict stays "lost". The rate keeps the rule worth keeping.

### Q — Measuring instruments need the same scrutiny as the gates

The process-metrics tool that measures bet #19 had two defects.

- It ignored the date window, and it read a fixed list of wave-1 specs that did not include the
  trial's FR. For days the bet looked unmeasurable while the tool printed confident numbers.
- It counted a squash-merged PR as a direct commit, which reported "0% through a PR" where the
  real share was 100%.

Repairing it **raised** the wave-1 figure from 13 to **at least 20** acceptance criteria added without
a change request. That correction went against our own interest, which is some evidence the repair was
not self-serving.

But the outside-in review found three further problems:

- **the repair and the results declaring #19 "held" were merged without a second person's review**;
- the repaired tool still counts only **new** acceptance-criterion headings, not clauses added to an
  existing one. In the trial window it reported **zero** spec amendments, while one amendment had
  happened, through a change request;
- so the wave-1 figure is a lower bound, and bet #19's *"proven wrong if a visual requirement enters
  through a fix"* is only partly observable.

This is the fourth instance of finding **G**, guards that are green on the wrong set. This time it is
inside a measuring instrument, inside the commit that was fixing a blind instrument.

**The rule we take from it:** an instrument that decides a bet gets the same treatment as a gate.
Verify it by breaking it. Replaying the known amendment must show up in its count. And never merge it
without a second person.

### R — A requirement question was answered by the architect, and the spec followed the code

One of the two questions was not technical; it was a requirement. How should an attribute that
belongs to two groups appear in a ranked list? The spec did not say. The code already showed both
groups. The answer became a change request of type *clarification* that added a clause to an approved
acceptance criterion, to match what had been built.

Three things went wrong with the method, and they are ours:

- our own change-request rule assigns sign-off of a *clarification* to the **functional side and the
  spec owner**. This one was accepted by the **architect**, and reviewed from the build side, and
  neither the spec owner nor the functional team signed it;
- the functional decision behind it had been given in chat **the day before** the spec passed its
  readiness gate. The gate froze a spec that was missing a decision already made;
- the flow sends every question to the architect, so requirement questions and technical questions
  travel together. The trial counted questions as a measure of dependency on the architect; one of
  them should never have gone to her.

The form held, because the change went through a change request. In substance **the spec followed
the code**, and that is the golden rule bent from the inside.

---

## What changes next

These are our own proposals. They take effect only when the working repository adopts them.

1. **Enforce through permissions what branch protection cannot.** A builder without write access to
   `main` works from a fork, and a 24-second merge becomes impossible rather than forbidden. Reviews
   are done natively on the platform's web interface instead of being transcribed.
2. **A rate next to every behavioural bet** (#15, #18), added by a dated amendment that does not
   rewrite the verdicts.
3. **Repair the #19 instrument again**, so that it counts changed criterion text, not only new
   headings. Verify it by replaying the known amendment.
4. **Re-sign the clarification** with the spec owner, as the rule requires, or declare the deviation.
   Align the two registers that describe it differently.
5. **Real-data verification in the builder's PR**, not as a reviewer's private step.
6. **Requirement questions go to the functional team**, and are counted separately from technical
   questions to the architect.
7. **Measure the builder's effort on the trial** while it is fresh. It is the strongest utility number
   within reach, and it is missing.

---

## What trial 3 does not prove

1. **That the method is cheaper in someone else's hands.** Calendar time is measured; effort is not.
2. **That governance transfers.** It did not. It held only where a person waited for the PR before
   merging (finding **M**).
3. **That the client gets value.** Sign-off by the client is bet #17, and its window is still open.

---

*Everything here is anonymized. No individual is named, defects are attributed to the method, data
volumes are omitted, effort is not published. See [`ANONYMIZATION.md`](ANONYMIZATION.md).*
