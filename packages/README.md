# packages/ — shared packages

Referenced by [`../CODEOWNERS`](../CODEOWNERS), [`../CLAUDE.md`](../CLAUDE.md) and
[`../contracts/README.md`](../contracts/README.md); the code itself is not part of this public repository.

| Package | Role | Who approves changes |
|---|---|---|
| `esl-model` | Schema/types of the standard library. **Part of the published contract** towards Downstream Studio. | `@architect` only |
| `ui` | Shared component library. | `@dev-team` |
| `excel-engine` | Excel read/write (TF-04): export (FR-08), external library import (W3), initial migration (TF-06). | `@dev-team` |
| `auth-rbac` | Role/capability model and enforcement (TF-02). | `@dev-team` |

`esl-model` is the one that matters for the operating model: it is under architect-only CODEOWNERS
precisely because a change there propagates through the contract into a downstream system. It is the
concrete case where the autonomy matrix says **human only**.
