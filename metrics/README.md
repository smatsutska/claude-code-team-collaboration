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

## Wave 0, and how to read it

Numbers in [`dashboard.md`](dashboard.md). Effort is **indexed to the traditional baseline = 100**;
absolute person-days are commercial and are not published in this repository (see
[`../ANONYMIZATION.md`](../ANONYMIZATION.md)).

**The caveats are part of the metric, not a disclaimer appended to it.** Wave 0 was executed by the
harness's designers, not by the seven-person team; it is structurally anomalous because most of its
cost was one-off harness investment; and it compares human *supervision* effort against a traditional
*build* estimate. All three are stated in the generated dashboard so they travel with the number.

**Metric 5 has a reading problem right now.** Zero `/reconcile` invocations is what perfect discipline
looks like and also what "nobody tested the boundary" looks like. With the designers as the only
operators, it is the second. The metric becomes informative when the real team runs a wave.

## The metric we are not collecting, and should be

**Effort on the harness versus effort on features.** Wave 0 added five gates. We assert that this is
one-off investment that will not recur — which is convenient, and unmeasured. The failure mode where
the harness becomes the work is exactly the kind a team cannot see from inside. Recorded as a gap in
[`w0-actuals.md`](w0-actuals.md) rather than quietly omitted.

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
