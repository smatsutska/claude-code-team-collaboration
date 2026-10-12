# Wave 1 — actuals

Source for `scripts/gen_metrics.py` → `metrics/dashboard.md`. Derivable values come from git, the CI
run log and the change-request register. Effort is the people's own tally (declared, not tracked).

> **Disclosure policy:** as for wave 0, effort is **indexed to the traditional baseline = 100**.
> Absolute person-days, costs and per-person figures are not published (see `ANONYMIZATION.md`).

## Effort (indexed: traditional baseline = 100)
- build_baseline_index_w1: 100
- build_cc_estimate_index_w1: 65     # planned, with Claude Code
- build_actual_index_w1: 24          # declared; cut at the end of September, so it will rise

## Process (from git)
- pr_share_pct_w1: 22                # share of work that went through a PR; 100% in the following week
- direct_commits_main_peak_w1: 92    # in one five-day stretch, against 3 PRs
- ac_added_without_cr_w1: ≥20        # lower bound; first counted as 13 (tool missed two specs, and still sees only new AC headings); 9 on UI specs
- reconcile_invoked_w1: 0
- method_share_pct_w1: 28            # share of changed lines on specs, governance, scripts, CI (wave 0: 37)

## Gates (from the CI run log, waves 0–1 cumulative)
- ci_runs_w1: 226
- ci_red_w1: 39                      # 14 style, 7 security, 7 docs drift, 5 types, 3 tests, 1 smoke, 4 install noise
- review_defects_gates_green_w1: 13  # found by one human code review on code with every gate green

## Requirements
- change_requests_w1: 46             # most from screen reviews and the client demo
- first_pass_w1: 3/5                 # first verification internal; sign-off transcribed by the builder (bet #17)

## Not collected, and it should be
- functional_effort_w1:              # the functional team's effort; without it the build uplift is a ceiling (bet #22)
- harness_effort_w1:                 # proxied by method_share_pct; lines are not hours
