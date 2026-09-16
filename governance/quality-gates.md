# Quality gates (consolidated — after wave 0)

Controls run at **increasing frequency and decreasing cost** (shift-left). Not one heavy check at deploy.

> **A gate that is not wired is worse than no gate: it buys false confidence.** (wave-0 lesson)
> In the previous version of this document the verification commands in [`../CLAUDE.md`](../CLAUDE.md)
> were placeholders, so the coherence gate and the security gate executed nothing while appearing in
> every governance review. The status column below is therefore load-bearing.

## Terminology (harmonised)

- **Blocking** — prevents merge or a state transition. In CI: no `allow_failure` / `continue-on-error`.
- **Advisory** — measures and shows, does not block. In CI: `allow_failure: true`.
- **Practice** — expected in the flow, not automated.

## The gates

| # | Gate | When | What it verifies | Status |
|---|---|---|---|---|
| 1 | Plan review | pre-code | The AI's plan is faithful to the spec | practice |
| 2 | FR-ID convention | every commit | Branch/commit cites an FR-ID (or TF-ID) | convention |
| 3 | **Coherence gate** | every PR | spec ↔ test ↔ code (4 kinds) | **advisory — by design** |
| **3b** | **Documentation coherence lint** | every PR | doc ↔ doc / doc ↔ reality (status, inline totals, dead refs, resolved open points, role-mapping drift) | **blocking** — [`gen_traceability.py`](../scripts/gen_traceability.py), [`coherence_docs_lint.py`](../scripts/coherence_docs_lint.py) |
| **S** | **demo-smoke** | every PR | Backend + frontend boot; `/health` and a protected route through the proxy | **blocking** — [`demo-smoke.sh`](../scripts/demo-smoke.sh) |
| G1 | Definition of Ready | pre-build | The spec is ready, **incl. criterion 9** (no blocking open point) | **blocking** |
| 4 | Contract test + **cross-FR** | pre-deploy | The downstream contract holds, **plus** conflicts between different FRs that a per-PR check cannot see | **blocking** |
| 5 | Wave sign-off (+ security gate) | end of wave | Wave accepted (client + governance + security review) | **blocking** |

Standard automated gates in CI — **blocking since day one**, because the stack is wired: test, lint,
type-check, **SAST / secrets scan / dependency scan** (the security floor).

## The taxonomy that replaced "advisory → blocking"

This is the correction wave 0 forced. The previous version of this document treated advisory→blocking as
a **maturity progression**: wait for the contradiction curve to flatten, then tighten everything. That
framing was wrong. Gates divide by **nature**, and the two kinds have opposite policies:

| Nature | Examples | Policy | Why |
|---|---|---|---|
| **Deterministic** | demo-smoke, docs lint, security floor, contract test | **Blocking from day one** | There is no judgment to calibrate — only a fact to verify. A calibration period would just be a period without the gate |
| **LLM-reasoned** | the coherence gate (3) | **Advisory, by design** | False positives and negatives are inherent. The outcome is a **report a human judges** — never a merge blocked on AI judgment alone (human-in-the-lead) |

So gate 3 staying advisory is **not** a maturity stage it will grow out of. It may stay advisory
permanently, and that is the correct design. What could change is its *weight* in review, once the
contradiction curve and the spec-first share justify it — a number, not a date.

**Honest note on our own compliance:** the documentation lint (3b) was made blocking immediately, per
the rule above, and then hardened twice in its first days against false positives it found by being run
on real documents. The principle held; the execution shipped a blocking gate that was still learning.
Both fixes are marked `HARDENED` in the source.

## What was wired during wave 0

- **demo-smoke (gate S)** — new. Closes *"green does not mean it runs"*: unit/type/lint were green
  while CORS, a 401 export href, a missing dev script and a missing server dependency made the
  integrated stack unstartable. **The gate is the small lesson; the cadence is the real one** — the
  stack runs integrated every wave, not only when it is demonstrated.
- **Documentation coherence lint (3b)** — new. Catches the drift class found in the wave-0 audit.
  Version 0 covers spec status vs index, inline totals, dead path references, resolved open points and
  role-mapping drift. It does **not** yet cover column totals or "X blocks Y" narratives; those were
  remediated by hand, which is precisely the debt this gate exists to remove.
- **Cross-FR checks given a home** — they are part of **gate 4** (pre-deploy) rather than floating
  unowned. A per-PR coherence check cannot see a conflict between two different FRs.
- **Generated indices** — `spec/traceability.md` and its counts are no longer hand-written:
  [`gen_traceability.py`](../scripts/gen_traceability.py), with `--check` in CI. *One fact, one home.*
- **Criterion 9 wired into `/ready`** — a spec does not pass G1 while a Critical or High open point
  listing it is unresolved. See [`open-points.md`](open-points.md).

## Definition of Done (evolves with the gates)

- **v0 (now):** acceptance criteria satisfied · every AC has a green `FR-XX/ACn` test · lint/types green ·
  code review approved (CODEOWNERS) · context updated (spec / skill / `CLAUDE.md`) ·
  **demo-smoke green** · **docs lint (3b) with no findings**.
- **v1 (if and when the coherence gate's weight increases):** v0 **+** no open high-confidence
  contradiction in the coherence report.

**Rule:** gates and the Definition of Done harden **at the same moment**.

## Two honest notes

**On traceability.** The AC↔test link is guaranteed **by existence** (is there a test naming the AC?),
not by semantic correctness (does that test actually cover it?). The second remains the job of human
code review. The coherence gate **augments** review, it does not replace it — it hands review a
coherence checklist already filled in.

**On the limit of mechanization.** During wave 0 the documentation lint surfaced a governance
contradiction it cannot resolve: the Definition of Ready makes the client an approver, the RACI has the
client only *consulted*, and no specification carries a client approver. Three documents, three answers,
each internally consistent. A script can make the disagreement undeniable. Deciding who signs is human
work, and it is still open.
