---
description: Code written without a spec (vibecoding) -> infer its spec and bring it back into the flow
argument-hint: [path/file or a description of what was written]
---

Some code was written **without an attached spec** (or with a spec that has since diverged). We don't
reject it: we **bring it back in**. You are an assistant tidying up the work, not an examiner.

Proceed:
1. Read the indicated code ($ARGUMENTS) or the current diff. Load the `esl-domain` skill if relevant.
2. **Infer the spec** that code implies: propose a file conforming to `spec/_TEMPLATE.md`
   — description of the observed behaviour, acceptance criteria in Given/When/Then reflecting
   what the code actually does, edge cases handled, and what appears to be out of scope.
3. **Surface the contradictions**: where this behaviour conflicts with existing specs or with other FRs,
   or where it implements something it shouldn't (e.g. touches the draft or the contract towards
   Downstream Studio).
4. Present the inferred spec to the analyst for review and correction. Make clear that it must be
   **approved** (FA-lead + architect, + client on the functional part) like any spec, and that it then
   has to pass G1 (`/ready`).
5. If the code lacks tests for the inferred ACs, list the `FR-XX/ACn` skeletons to be added.

Outcome: the formerly orphan code gets an anchor (an FR with an approved spec) and re-enters the normal
cycle. Remember the golden rule: from here on, spec first, then code.
