# RBAC matrix — roles × capabilities

The authoritative source of SGP permissions (from the client's RBAC matrix document, plus the FRs).
Independent of the authentication provider (see ADR-0002). Enforcement: server-side once the backend
exists; UI gating is UX only.

## Roles
- **Viewer** — read-only consultation.
- **ESL Editor** — Viewer + draft editing.
- **ESL Approver** — Editor + approval/release. (⊇ Editor)
- **Admin** — superset of everything.

## Capabilities × roles

| Capability (code) | What it covers (FR) | Viewer | Editor | Approver | Admin |
|---|---|:---:|:---:|:---:|:---:|
| `esl.consult` | area, navigation, exploration, search, KPI, versions catalogue, export (FR-01,02,03,04,05,06,08) | ✓ | ✓ | ✓ | ✓ |
| `esl.editDraft` | create/edit/revert draft, edit data, import external libraries, workbench, create/edit mappings (FR-09,10,11,13,14,16,19,21,22,23) | ✗ | ✓ | ✓ | ✓ |
| `esl.approve` | approve draft, publish/release official version, release eligibility (FR-09 approval, FR-26,27) | ✗ | ✗ | ✓ | ✓ |
| `admin` | administration (e.g. user management) | ✗ | ✗ | ✗ | ✓ |

## Notes
- Hierarchy: Admin ⊇ Approver ⊇ Editor ⊇ Viewer (capabilities accumulate).
- **Wave 1** uses only `esl.consult` (everything read-only) — but the full model is defined from the
  start, so later waves don't require RBAC rework.
- The **draft** is not visible to a Viewer (FR-11): consulting it requires `esl.editDraft`.
- This matrix is implemented in `apps/sgp/src/auth/types.ts` (`ROLE_CAPABILITIES`). If it changes here,
  it changes there (and vice versa): keep them aligned.
