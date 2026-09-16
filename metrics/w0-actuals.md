# Wave 0 — actuals

Source for `scripts/gen_metrics.py` → `metrics/dashboard.md`. **Derivable** values come from git and
from the migration report; **effort** is a human tally, because it is not derivable.

> **Disclosure policy for this public repository.** Effort is **indexed to the traditional baseline
> estimate = 100**. Absolute person-days, programme totals and capacity figures are commercial and are
> not published. Data volumes are expressed as proportions. Every ratio the proof of concept argues
> from survives this; nothing else does.

## Effort (indexed: traditional baseline = 100)
- build_baseline_index_w0: 100      # traditional estimate, wave 0 build
- build_cc_estimate_index_w0: 72    # planned, with Claude Code
- build_actual_index_w0: 18         # measured. "So far": wave 0 is not yet signed off by the client

## Process (from git)
- pr_spec_first_w0: 6               # all six feature PRs had an Approved spec before the first feat commit
- pr_total_w0: 6
- reconcile_invoked_w0: 0           # no code written without a spec

## Coherence gate contradictions (from git: root-fix commits)
- contradictions_scope_creep_w0: 0
- contradictions_spec_drift_w0: 2   # a hierarchy table and a set of tables nothing populated
- contradictions_test_gap_w0: 0
- orphan_fr_w0: 0
- contradictions_resolved_pre_merge_w0: 2/2

## Delivery (from the migration reconciliation report)
- rows_rejected_pct_w0: ~2%         # every rejected row carries a traced reason

## Not yet available
- first_pass_acceptance_pct_w0:     # requires client UAT / sign-off (has not happened yet)
- uat_defects_w0:                   # idem
- mean_lead_time_days_w0:           # measurable (spec Approved → merge), to be consolidated

## Not collected, and it should be
- harness_effort_share_w0:          # effort on the harness vs effort on features.
                                    # Wave 0 added five gates. We assert this is one-off investment
                                    # that will not recur — and we are not measuring whether that is
                                    # true. See "gate proliferation" in W0-RESULTS.md.
