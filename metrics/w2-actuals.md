# Wave 2 — actuals (in progress: trial 3 window)

Source for `scripts/gen_metrics.py` → `metrics/dashboard.md`. Wave 2 is not closed: these are the
values measured over the trial-3 window, from git, the CI run log and the platform's PR record.

> **Disclosure policy:** no effort figures yet (not measured for the trial), no data volumes,
> no individual named. Defects are attributed to the method.

## Status
- status_w2: in progress — trial 3 window only

## Trial 3 (one FR, built by the second developer, reviewed by the architect)
- questions_to_architect_w2: 2 of a cap of 5   # one became a change request
- lead_time_gate_to_pr_hours_w2: 28            # calendar time, readiness gate → first PR
- architect_lines_on_branch_w2: 0
- review_defects_structural_w2: 0
- review_defects_behaviour_w2: 3               # stayed on main three days; fixed in a second PR
- coherence_findings_true_w2: 2/2              # judged by someone who did not build; missed the worst defect

## Merges since bet registration (10 PRs)
- pr_share_pct_w2: 100
- merges_native_review_w2: 0/10
- merges_second_person_before_merge_w2: 4/10   # as comments, or transcribed from chat
- merges_declared_waiver_w2: 3/10
- merges_no_review_no_waiver_w2: 1/10

## Requirements
- ac_added_without_cr_w2: 0 (lower bound)   # lower bound: the tool sees only new AC headings, not clauses added to existing ones

## Not collected yet
- builder_effort_w2:                           # effort of the trial; the strongest utility number within reach
- functional_effort_w2:                        # needed for bet #22
- first_pass_w2:                               # first verification of the FR requested; bet #17 window open
