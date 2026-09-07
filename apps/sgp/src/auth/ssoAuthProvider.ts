// apps/sgp/src/auth/ssoAuthProvider.ts
// PLACEHOLDER — to implement once the client's IdP is confirmed (IMP-06, spec TF-02).
// Typically: OIDC/OAuth2 authorization-code + mapping of IdP claims/groups onto SGP roles.

import type { AuthProvider, User } from "./types";

export class SsoAuthProvider implements AuthProvider {
  getCurrentUser(): User | null {
    throw new Error("SsoAuthProvider not implemented yet — see spec/TF-02-auth-rbac.md and ADR-0002.");
  }
  async login(): Promise<User> {
    throw new Error("SsoAuthProvider not implemented yet.");
  }
  async logout(): Promise<void> {
    throw new Error("SsoAuthProvider not implemented yet.");
  }
}
