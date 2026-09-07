# apps/sgp — Standards Governance Platform (Phase 1)

Web application governing the ESL standard engineering data library. Phase 1 perimeter: the Standard
Domain (UC-01→UC-04) plus the technical foundations (TF-01→TF-06). The Project Domain (UC-05→08) is out
of perimeter.

Logical layers: UI (from the design files) · domain services (consultation, versioning, governance,
mapping, release) · data (PostgreSQL, see ADR-0001) · foundations (auth/RBAC, Excel engine,
environments/CI, migration).

> **What's published here.** Only the auth/RBAC slice, as a worked example of the chain this method
> claims to produce: `spec/TF-02-auth-rbac.md` → `governance/rbac-matrix.md` → the typed code below.
> The rest of the application is not part of this repository — see [`../../ANONYMIZATION.md`](../../ANONYMIZATION.md).
