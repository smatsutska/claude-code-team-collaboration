// apps/sgp/src/auth/types.ts
// Permanent RBAC model. Authoritative source: governance/rbac-matrix.md — keep them aligned.
// (TypeScript reference; adapt the types to your stack if you don't use TS.)

export type Role = "viewer" | "editor" | "approver" | "admin";

export type Capability =
  | "esl.consult"    // area, navigation, exploration, search, KPI, versions, export (W1 read side)
  | "esl.editDraft"  // create/edit/revert draft, edit data, external imports, workbench, mapping (W2/W3)
  | "esl.approve"    // approve draft / publish-release an official version (W4)
  | "admin";         // administration

// Roles -> capabilities. Capabilities accumulate: Approver ⊇ Editor; Admin ⊇ everything.
export const ROLE_CAPABILITIES: Record<Role, Capability[]> = {
  viewer:   ["esl.consult"],
  editor:   ["esl.consult", "esl.editDraft"],
  approver: ["esl.consult", "esl.editDraft", "esl.approve"],
  admin:    ["esl.consult", "esl.editDraft", "esl.approve", "admin"],
};

export interface User {
  id: string;
  name: string;
  roles: Role[];
}

// Stable abstraction: the app depends ONLY on this (never on the concrete provider). See ADR-0002.
export interface AuthProvider {
  getCurrentUser(): User | null;
  login(input?: unknown): Promise<User>;
  logout(): Promise<void>;
}

export function hasCapability(user: User | null, cap: Capability): boolean {
  if (!user) return false;
  return user.roles.some((r) => ROLE_CAPABILITIES[r]?.includes(cap));
}
