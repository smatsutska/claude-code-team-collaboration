# Test convention — the AC → test hook

What makes "the spec executable" and the coherence gate operational.

## The rule (single, rigid)
**Every AC has at least one test naming it**, with the prefix `FR-XX/ACn` in the test name/description.
Nothing else is mandatory. That prefix is what lets the coherence gate compare spec↔test mechanically
(the "test gap" becomes: which ACs do not appear in any test name?).

## The Given/When/Then → arrange/act/assert mapping
The GWT structure of the AC maps 1:1 onto the test. That is why we use GWT in the template.

```
AC2 — Only one draft at a time
  Given a draft already exists
  When  a user tries to create another
  Then  the system prevents it and reports that a draft already exists
```
becomes
```
test("FR-11/AC2 · prevents a second draft when one already exists", () => {
  // Given
  const v = createOfficialVersion();
  createDraftFrom(v);
  // When
  const result = tryCreateDraftFrom(v);
  // Then
  expect(result.ok).toBe(false);
  expect(result.error).toBe("DRAFT_ALREADY_EXISTS");
});
```

## Who writes them and when
- In the **plan** (`/implement` phase 1) Claude generates the **test skeletons** from the ACs — one per
  AC, with GWT in the comments and assertions to be completed. The developer reviews them (a second
  fidelity check, at low cost).
- Healthy sequence: **test-first** (complete the tests, then implement until they pass). It isn't dogma:
  the invariant is on the **result** (at PR time every AC has its test), not on the ritual.

## What we do NOT do (for now)
No BDD/Gherkin/Cucumber framework. Just the unit/integration framework the team already uses, with this
naming convention. The `FR-XX/ACn` convention is 90% of the value at zero tooling cost. We add more only
if the operational reviews call for it.

## Declared limitation
The AC↔test correspondence is traceable **by existence** (is there a test naming AC2?), not **by
semantic correctness** (does that test actually verify AC2?). The first is mechanical and guaranteed;
the second is guaranteed by human code review. The coherence gate will say "AC3 has no test" with
certainty; "this test doesn't cover AC3 well" remains human judgement.
