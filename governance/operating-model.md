# Operating model: who does what, and how much is enforced

> **Provisional, as of the end of wave 1.** This file states **how it is today**, with the
> **target** next to it. The target applies once the project moves onto the client's own git
> platform.
>
> Until wave 1 this file described only the target, and it had not been edited since the first
> commit. An outside-in review found the gap by comparing it with git history (finding **K** in
> [`../W1-RESULTS.md`](../W1-RESULTS.md)). A design document that is never compared with what
> actually happens drifts like any other hand-written fact.

## Principle

Humans **specify, verify and decide**. Claude Code produces inside written boundaries and does not
decide. An authority counts when the platform enforces it (identity, git, CI), not when the AI
declares it.

## Roles, today

| Role | Today | Target |
|---|---|---|
| **Architect** | Also governance **and the builder**: orchestrates Claude Code, writes specs, reviews on screen, merges to `main`. Part-time | As today, but with specs written by the functional team |
| **Developer** | One person, full-time. In wave 1, parallel trials not merged. **In trial 3, built one FR alone through the method, merged to `main`** | Builds through the same flow, and the work reaches `main` after a second person's review |
| **Functional team** (three people; one signature is enough) | **Decides and reviews.** Input arrives in chat and meetings; the architect writes it into the repository. Signs specs | Writes and signs specs and acceptance criteria directly, on the client's platform |
| **Governance** | Two people, one of whom is the architect | Custodians of gates and metrics, **separate from whoever builds** |
| **Client** | **No named referent yet.** Wave sign-off has not been requested from the client | First functional verification and domain sign-off |

**The consequence, stated plainly:** today the person who builds, the person who writes the specs and
the person who guards the gates are **largely the same person**. The method makes that traceable,
because every decision sits in a change request or an ADR. It does not make it independent. Whether
the method works without its author is not yet supported by any data: that is bet **#16**.

## Trial 3: does it work without the architect?

Trials 1 and 2 had the developer re-implement two FRs in parallel **without merging them**. Their
value was the comparison, and it produced eleven changes to the method (finding **F**). Trial 3 is
designed so the work **does** reach `main`:

- **one FR, built only by the developer**, through the method, with no second implementation;
- the architect **reviews and does not write code**;
- the spec is **frozen at a tagged version**, so builder, reviewer and measurement all refer to the
  same text;
- every question to the architect is **written in the PR**. That count is the measurement of
  dependency.

Full design, preconditions and thresholds: [`../W2-BETS.md`](../W2-BETS.md).

**Result** ([`../TRIAL-3-RESULTS.md`](../TRIAL-3-RESULTS.md)): **construction transferred**, with 2
questions to the architect against a cap of 5, no structural defects and no lines from the architect.
**Governance did not.** The PR was merged before review, review evidence stayed in chat, and
real-data verification still depended on the architect. The dependency moved from *building* to
*verifying*; it did not disappear.

## How much is enforced

| What | Today | Target |
|---|---|---|
| CI on PRs and `main` | **runs**, but **does not block merges**: branch protection is not available on the current platform | blocks merges |
| `CODEOWNERS` | declares who must sign what, but is **not enforced**, for the same reason | enforced |
| Merge to `main` | intended: only after a second person's review, then a check that `main` is green. **Measured in trial 3: 4 of 10 merges had a second-person review before merge, 0 of 10 a native one** | builder without write access to `main`; review native on the platform |
| G1 (Definition of Ready) | human signatures of the functional team and the architect; the automated part of `/ready` is an aid | as today |
| Coherence check (gate 3) | **advisory** | blocking on high-confidence findings **if** their precision justifies it (bet **#20**) |
| Wave sign-off | given in chat, transcribed by the architect into a written minute | signed by the client on the client's platform (bet **#17**) |

## AI autonomy

| Activity | Who decides today |
|---|---|
| Scaffolding, tests, local refactors, technical docs | the AI proposes; whoever reviews the PR sees it |
| Implementation against an approved spec | the AI implements; a human reviews plan, code and screen |
| Data model, published contract, versioning | only via a signed ADR or change request |
| Requirements and acceptance criteria | the functional team signs; the AI does not decide |
| Merge, release, deploy | a human, explicitly |

Autonomy widens **on data, not on the calendar**: when the gates show that a class of work passes
without defects, that class moves towards more autonomy. **None has moved so far.** Bet **#23** says
at least one will, by the end of wave 3, under a rule written before it is applied.

## Recognising who is who (three distinct layers)

1. **Identity and role**: one identity per person; roles resolve to people in a single file.
2. **Authority enforced by the platform**: `CODEOWNERS` and branch protection. **Today this layer is
   missing**, and the gates are a convention, checked after merge (bet **#15**).
3. **Intent declared to the AI**: expressed by the command invoked (`/spec`, `/implement`,
   `/coherence`, …). The AI recognises the intent; it does **not** authenticate the role.
