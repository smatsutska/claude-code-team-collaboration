// apps/sgp/src/auth/devAuthProvider.ts
// TEMPORARY — development/demo only. No IdP, no password.
// To be removed from production builds (ADR-0002). Replaced by SsoAuthProvider.

import type { AuthProvider, Role, User } from "./types";

// One seed user per role, to demonstrate RBAC.
export const DEV_USERS: Record<Role, User> = {
  viewer:   { id: "dev-viewer",   name: "Dev Viewer",   roles: ["viewer"] },
  editor:   { id: "dev-editor",   name: "Dev Editor",   roles: ["editor"] },
  approver: { id: "dev-approver", name: "Dev Approver", roles: ["approver"] },
  admin:    { id: "dev-admin",    name: "Dev Admin",    roles: ["admin"] },
};

const SESSION_KEY = "sgp.devUser";

export class DevAuthProvider implements AuthProvider {
  getCurrentUser(): User | null {
    const raw = sessionStorage.getItem(SESSION_KEY);
    return raw ? (JSON.parse(raw) as User) : null;
  }

  async login(role: Role = "viewer"): Promise<User> {
    const user = DEV_USERS[role];
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(user));
    return user;
  }

  async logout(): Promise<void> {
    sessionStorage.removeItem(SESSION_KEY);
  }
}
