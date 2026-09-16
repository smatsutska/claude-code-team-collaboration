# scripts/ — the mechanics of the gates

This is what turned a written governance model into an executing one. In the version of this
repository published before wave 0, the gates were documented and the verification commands in
[`../CLAUDE.md`](../CLAUDE.md) were **placeholders** — so the coherence gate and the security gate
executed nothing. See finding **C** in [`../W0-RESULTS.md`](../W0-RESULTS.md): *an ungated gate is
worse than no gate, because it buys false confidence.*

These four scripts are the fix. They are small on purpose.

| Script | Gate | Nature | Policy |
|---|---|---|---|
| [`demo-smoke.sh`](demo-smoke.sh) | **S** — integration smoke | deterministic | **blocking from day one** |
| [`coherence_docs_lint.py`](coherence_docs_lint.py) | **3b** — documentation coherence | deterministic | **blocking from day one** |
| [`gen_traceability.py`](gen_traceability.py) | feeds 3b (`--check` in CI) | deterministic | **blocking from day one** |
| [`gen_metrics.py`](gen_metrics.py) | — (generates the dashboard) | deterministic | not a gate |

Note what is **not** here: the spec↔test↔code coherence check. That one reasons, so it is a prompt
([`../.claude/commands/coherence.md`](../.claude/commands/coherence.md)) and it is **advisory by
design** — a human judges its report, and no merge is ever blocked on AI judgment alone. The split
between these two kinds of gate is the correction wave 0 forced on us; see bet #3 in the scoreboard.

## The two rules these scripts encode

**One fact, one home.** If a fact lives in two places, one is generated from the other. The
hand-written fact is the recurring root cause of drift. `gen_traceability.py` and `gen_metrics.py`
generate; `coherence_docs_lint.py` guards what cannot be generated. The goal is **detectability**:
drift announces itself instead of being discovered in an audit.

**Deterministic gates do not need a calibration period.** There is no judgment to tune — only a fact
to verify — so they block immediately. We did tune `coherence_docs_lint.py` twice in its first days,
against two false positives it found by being run on real documents; both fixes are marked `HARDENED`
in the source. Worth being honest about: those fixes landed while the gate was already blocking.

## Running them

```bash
python scripts/gen_traceability.py            # regenerate the index from spec front-matter
python scripts/gen_traceability.py --check    # CI: fail if the index drifted
python scripts/coherence_docs_lint.py         # advisory run, prints findings
python scripts/coherence_docs_lint.py --strict  # CI: non-zero exit on any finding
python scripts/gen_metrics.py                 # regenerate metrics/dashboard.md from the actuals
bash scripts/demo-smoke.sh                    # boot both tiers, verify the seam
```

No dependencies beyond the standard library, deliberately. A gate that needs its own toolchain is a
gate that stops running.

## What `demo-smoke.sh` is really checking

Not "does the backend work" — unit tests cover that. It checks **the seam**: that a protected backend
route is reachable *through the frontend's proxy*. That single call is what catches CORS
misconfiguration, a broken proxy target, a missing dev script and a missing server dependency — the
four things that were green in every other check and still made the stack unstartable.

It accepts `200`, `401` or `403` as success. Reachability is the assertion; the auth outcome is not.
