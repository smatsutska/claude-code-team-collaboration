// apps/sgp/src/auth/AuthContext.tsx
// React auth context. Selects the provider per environment and enforces that the dev provider
// never reaches production. (Vite-style env vars: adapt to CRA/Next if needed.)

import { createContext, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import type { AuthProvider, Capability, User } from "./types";
import { hasCapability } from "./types";
import { DevAuthProvider } from "./devAuthProvider";
import { SsoAuthProvider } from "./ssoAuthProvider";

const AUTH_MODE = ((import.meta as any).env?.VITE_AUTH_MODE ?? "dev") as "dev" | "sso";
const IS_PROD = (import.meta as any).env?.PROD === true;

// Security guard (ADR-0002): dev auth is FORBIDDEN in production.
if (IS_PROD && AUTH_MODE === "dev") {
  throw new Error("AUTH_MODE=dev is not allowed in production. Set VITE_AUTH_MODE=sso.");
}

export const IS_DEV_AUTH = AUTH_MODE === "dev";
const provider: AuthProvider = AUTH_MODE === "sso" ? new SsoAuthProvider() : new DevAuthProvider();

interface AuthCtx {
  user: User | null;
  can: (cap: Capability) => boolean;
  refresh: () => void;
  logout: () => Promise<void>;
  provider: AuthProvider;
}

const Ctx = createContext<AuthCtx | null>(null);

export function AuthContextProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(() => provider.getCurrentUser());
  const refresh = () => setUser(provider.getCurrentUser());
  useEffect(() => { refresh(); }, []);

  const value = useMemo<AuthCtx>(() => ({
    user,
    can: (cap) => hasCapability(user, cap),
    refresh,
    logout: async () => { await provider.logout(); refresh(); },
    provider,
  }), [user]);

  return <Ctx.Provider value={value}>{children}</Ctx.Provider>;
}

export function useAuth(): AuthCtx {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error("useAuth must be used inside <AuthContextProvider>.");
  return ctx;
}

// Declarative guard: renders children only if the user holds the required capability.
// NB: this is UX gating. Real security must also be enforced server-side.
export function RequireCapability(
  { cap, children, fallback = null }:
  { cap: Capability; children: ReactNode; fallback?: ReactNode }
) {
  const { can } = useAuth();
  return <>{can(cap) ? children : fallback}</>;
}
