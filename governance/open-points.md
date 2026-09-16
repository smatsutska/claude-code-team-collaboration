# Open points register

The authoritative source for unresolved points that **condition the build**. Reconciled 1:1 with the
delivery estimation workbook and extended with the points that emerged from setting up governance.

## Why this file exists

The register used to live in a spreadsheet: no tracked owner, no dates, **no hook into the gates**. The
consequence is that a specification could pass G1 while depending on an unresolved high-priority point.
Moving it here makes the register **executable context**: it is read by whoever verifies G1, and it is
read by the agent.

## The rule (hook into G1)

> A spec **does not pass G1** if its FR/TF appears in the *Blocks* column of an open point that is
> **Critical** or **High** priority and still **Open**. Two exits only: close the point, or narrow the
> spec in a documented way (`Out of scope`) so the point no longer touches it.

## Two levels of blocking — do not conflate them

Some points block a *specification* (they list FR/TF ids). Others block the *programme* — capacity,
RACI, signing authority — and no single specification can resolve them. Applying criterion 9 to the
second kind would deadlock G1 permanently, which is noise, not control.

| Level | Where it bites |
|---|---|
| **Spec (G1)** | Criterion 9 of the Definition of Ready |
| **Programme** | Wave sign-off and signing authority — *not* criterion 9 |

## The scoping failure this register did not prevent

Criterion 9 is scoped to **specifications**. It is not scoped to **architecture decisions**.

During wave 0 an architecture decision record was approved while the client's infrastructure
constraints were still listed here as open — exactly the condition criterion 9 exists to prevent. Six
days later the client kickoff deck showed a different stack, and the ADR was superseded. See
[`../docs/adr/0003-architecture-stack-ratified-from-the-deck.md`](../docs/adr/0003-architecture-stack-ratified-from-the-deck.md)
and finding **D** in [`../W0-RESULTS.md`](../W0-RESULTS.md).

The register worked. The hook was attached to the wrong set of artifacts.

**If you are copying this pattern:** check what your readiness criteria are scoped to, and whether your
highest-consequence artifacts fall inside that scope. Ours did not, and the most expensive decision in
the programme walked past the control built to catch it.

## What changed during wave 0

- A database provisioning point was **resolved**, which unblocked and merged the data model and the
  migration specs.
- Auth was merged in **dev mode**: the identity-provider point blocks only the real SSO implementation
  (marked `Out of scope` on that spec), not the acceptance criteria.
- A database-capability point stopped blocking the data model — it was built against the development
  database — and now remains relevant only to **production**.

The real blocks remaining are the cloud environments spec and the real SSO implementation. The
appointment of named approvers is still open, and it conditions sign-offs.

## Maintenance

This file is hand-curated and therefore a drift site by definition. It is one of the inputs to the
documentation coherence lint (gate 3b), which flags any document claiming to be *blocked by* a point
this register records as resolved — see
[`../scripts/coherence_docs_lint.py`](../scripts/coherence_docs_lint.py).

That check is also where the lint produced its first false positive: an earlier version inferred closure
from proximity across all documents, so prose like *"that spec is already closed"* sitting next to a
point reference marked the point resolved. Only this register decides now.
