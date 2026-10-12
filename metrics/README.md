# metrics/ — the measurement of the proof of concept

You do not design the measurement at a desk before the flow is moving. Wave 0 was the **first
collection**, and it exists to do one concrete thing: replace the *assumed* uplift in the plan with a
**measured** one.

Principle: **few metrics; non-derivable actuals are recorded by hand** ([`w0-actuals.md`](w0-actuals.md)),
and the **dashboard is generated** from them ([`dashboard.md`](dashboard.md), via
[`../scripts/gen_metrics.py`](../scripts/gen_metrics.py)). No hand-written presentation that can drift —
*one fact, one home*. Reviewed at the end of each wave.

> **Bet #10 in [`../FEEDBACK.md`](../FEEDBACK.md) asked whether defining metrics late was pragmatism or
> self-serving.** The feared outcome was "the wave passes and nobody captured a baseline". It did not
> happen: the baseline exists and the dashboard is generated. Designing after the flow existed produced
> six metrics we actually collect instead of twelve we would have abandoned. Sample size: one wave.

## The six metrics

| # | Metric | How it is derived | Why |
|---|---|---|---|
| **1** | **Effort per FR/TF** | From commits — every branch and commit cites an FR-ID (gate 2). The team records effort at story close | The numerator of the uplift. Without it the rest is garnish |
| **2** | **Real uplift on build** | `1 − (actual ÷ baseline estimate)`, per wave | The PoC hypothesis |
| **3** | **Spec-first share** | PRs with an `Approved` spec upstream ÷ total PRs | Measures migration from vibecoding to spec-driven. *This* is the curve to show management |
| **4** | **Coherence gate contradictions** | From the `/coherence` report, by kind: scope creep · spec-drift · test gap · orphan FR | Finding precision is tuned on this data, before the gate's weight increases |
| **5** | **`/reconcile` invocations** | Count | Early on, **high is good**: orphan code re-entering the flow beats orphan code staying outside it |
| **6** | **First-pass acceptance** | ACs accepted without rework at client verification ÷ total ACs | Measures whether the specs were genuinely ready — i.e. whether G1 works |

## Waves 0 and 1, and how to read them

Numbers in [`dashboard.md`](dashboard.md), generated from [`w0-actuals.md`](w0-actuals.md) and
[`w1-actuals.md`](w1-actuals.md). Effort is **indexed to the traditional baseline = 100**; absolute
person-days and costs are not published in this repository (see
[`../ANONYMIZATION.md`](../ANONYMIZATION.md)).

**The caveats are part of the metric, not a disclaimer appended to it.** Every governed line was built
by the method's author, not by the team the model is written for. Only **build** effort is measured,
so the uplift is a ceiling. Wave 0 is anomalous because of one-off investment in the gates. All of
this is stated in the generated dashboard so it travels with the number.

**Metric 5 still has a reading problem.** Zero `/reconcile` invocations in both waves. In wave 1 the
code written outside the flow (the parallel trials) was mined for rules instead of reconciled, so the
recovery path was bypassed by a different practice (finding **F**).

**Metric 6 is now measured**, and has a validity problem: the first verification was internal, and the
wave sign-off was transcribed by the person who built the wave. Bet **#17** is about making it
independent.

**Wave 2 is in progress.** [`w2-actuals.md`](w2-actuals.md) holds the trial-3 window only: process
counts, review counts and defect classes, but no effort yet. Merges are counted by kind of review
(native, second person before merge, waiver, none) because a binary "with review / without" hid the
pattern (finding **P** in [`../TRIAL-3-RESULTS.md`](../TRIAL-3-RESULTS.md)).

**Per-person effort left the working repository after wave 1.** That repository is bound for the
client's platform, and hours of identifiable people are not evidence about the method. Wave totals
stay in the plan.

## The metrics we are not collecting, and should be

**Effort on the harness versus effort on features.** Since wave 1 it is proxied by the share of
changed lines spent on specs, governance, scripts and CI: 37% in wave 0, 28% in wave 1, 22% in the
following week. Lines are not hours, so this is a trend, not a measurement.

**The functional team's effort.** Without it, an uplift on build could simply be cost moved upstream
(finding **J**). From wave 2 it is measured, and bet **#22** depends on it.

## The two questions these numbers must answer

**To management, about value.** Not *"the AI writes code"* — they know, and it proves nothing. Rather:
*"spec↔code coherence is a mechanical invariant, and the team has migrated from vibecoding to
spec-driven"*. The evidence is metric 3 rising and metric 4 falling. The effort saving (metric 2) is
the consequence, not the argument.

**To us, about the plan.** If the measured uplift diverges from the hypothesis, the plan is rewritten
**immediately**, not at the end. It diverged — favourably and by a wide margin — which is why the
caveats above matter more than the number: re-planning on a figure produced under non-repeatable
conditions is how a proof of concept turns into an overcommitment.

## What we do not measure, and why

Lines of code, commits per day, percentage of AI-generated code. Easy to optimise, and they say nothing
about outcomes. If someone asks for them, the answer is metric 6: **first-pass acceptance** — how much
of what we deliver is accepted the first time.
