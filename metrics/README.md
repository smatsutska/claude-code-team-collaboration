# metrics/ — the PoC dashboard

**To be defined on real operational data.** You don't design the measurement at a desk before the flow
is in motion.

The curves this folder will have to collect (candidates, to be confirmed at the first operational review):
- **spec-first** share (PRs with an FR-ID and an approved spec upstream, vs orphans);
- **contradictions** at the coherence gate per PR, by kind (scope creep / spec drift / test gap);
- number of `/reconcile` invocations (early on, high = good adoption of the tool);
- traditional baseline (estimated `<N>` person-days / `<M>` months) vs AI-powered actual;
- client team first-pass acceptance; lead time per wave; defects found in UAT.

The *curve* of these numbers over time is the proof for management: not "AI writes code", but
"production-grade coherence is a mechanical invariant, and the team has migrated from vibecoding to
spec-driven".

> **Under review.** See bet #10 in [`../FEEDBACK.md`](../FEEDBACK.md): defining the measurement after the
> flow starts is either sound pragmatism or the reason a baseline never gets captured. We are not sure which.
