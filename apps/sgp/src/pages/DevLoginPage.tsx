// apps/sgp/src/pages/DevLoginPage.tsx
// TEMPORARY login (development/demo only): role picker, no password.
// Replaced by the real SSO flow (ADR-0002 / TF-02). Deliberately minimal styling (a utility, not final UI).

import { useAuth, IS_DEV_AUTH } from "../auth/AuthContext";
import { DevAuthProvider, DEV_USERS } from "../auth/devAuthProvider";
import type { Role } from "../auth/types";

const ROLES: Role[] = ["viewer", "editor", "approver", "admin"];

export function DevLoginPage({ onLoggedIn }: { onLoggedIn?: () => void }) {
  const { provider, refresh } = useAuth();

  if (!IS_DEV_AUTH) {
    return <p>Access is managed by the Identity Provider (SSO).</p>;
  }

  async function loginAs(role: Role) {
    await (provider as DevAuthProvider).login(role);
    refresh();
    onLoggedIn?.();
  }

  return (
    <div style={{ maxWidth: 380, margin: "10vh auto", fontFamily: "system-ui, sans-serif" }}>
      <div style={{ background: "#FEF3D9", color: "#7A5310", padding: "8px 12px",
                    borderRadius: 8, fontSize: 13, marginBottom: 16 }}>
        ⚠ Development mode — temporary authentication. Do not use in production.
      </div>
      <h1 style={{ fontSize: 18, margin: "0 0 4px" }}>SGP — development access</h1>
      <p style={{ color: "#6B6A66", fontSize: 13, margin: "0 0 16px" }}>
        Pick a role to sign in and demonstrate the wave's work.
      </p>
      {ROLES.map((role) => (
        <button key={role} onClick={() => loginAs(role)}
          style={{ display: "block", width: "100%", textAlign: "left", padding: "10px 12px",
                   marginBottom: 8, borderRadius: 8, border: "1px solid #D6D4CC",
                   background: "#fff", cursor: "pointer" }}>
          <strong style={{ textTransform: "capitalize" }}>{role}</strong>
          <span style={{ color: "#6B6A66", fontSize: 12, marginLeft: 8 }}>{DEV_USERS[role].name}</span>
        </button>
      ))}
    </div>
  );
}
