#!/usr/bin/env bash
# demo-smoke - integration gate: boot backend + frontend and verify that the thing actually starts.
#
# WHY THIS EXISTS (wave-0 finding A, "green does not mean it runs"):
# unit tests, type checks and lint were all green, but the integrated stack had never been started
# until the demo was being prepared. Four blockers surfaced within an hour: CORS, an authenticated
# export href returning 401, a missing frontend dev script, and a missing server dependency. None of
# them is visible to any check that looks at one tier in isolation.
#
# The gate is the small lesson. The real lesson is CADENCE: the integrated stack runs every wave,
# not only when it is being demonstrated.
#
# Deterministic gate -> blocking from day one. No database required: the liveness probe does not
# depend on the DB, and the protected route answers 401 (no identity) before touching it. Runs
# identically locally and in CI with dummy DB env vars.
set -uo pipefail

# ---------- CONFIG ----------
BACKEND_CMD="${BACKEND_CMD:-uv run uvicorn sgp_api.main:create_app --factory --host 127.0.0.1 --port 8090}"
BACKEND_URL="${BACKEND_URL:-http://127.0.0.1:8090}"
HEALTH_PATH="${HEALTH_PATH:-/health}"                 # liveness: must NOT depend on the database
FRONTEND_CMD="${FRONTEND_CMD:-pnpm --dir apps/sgp dev --port 8080 --strictPort --host 127.0.0.1}"
FRONTEND_URL="${FRONTEND_URL:-http://127.0.0.1:8080}"
PROXIED_PATH="${PROXIED_PATH:-/versions}"             # a backend route reached VIA the frontend proxy
TIMEOUT="${TIMEOUT:-60}"

# Env that lets the backend boot with no database (lazy engine: no connection until a query runs,
# and the unauthenticated request is rejected before any query).
export AUTH_MODE="${AUTH_MODE:-dev}"
export SGP_ENV="${SGP_ENV:-local}"
export SGP_DB_DSN="${SGP_DB_DSN:-127.0.0.1:1521/smoke}"
export SGP_DB_USER="${SGP_DB_USER:-smoke}"
export SGP_DB_PASSWORD="${SGP_DB_PASSWORD:-smoke}"

# Preflight: the ports must be free. A zombie process holding the port would be hit by the proxy
# instead of the backend we just started, producing a misleading 404. Fail early and readably.
be_port="${BACKEND_URL##*:}"; fe_port="${FRONTEND_URL##*:}"
for p in "$be_port" "$fe_port"; do
  if (timeout 1 bash -c "</dev/tcp/127.0.0.1/$p") 2>/dev/null; then
    echo "FAIL: port $p already in use - stop the running stack (or pass different BACKEND_URL/FRONTEND_URL)."; exit 1
  fi
done

BE_PID=""; FE_PID=""
cleanup(){ [ -n "$FE_PID" ] && kill "$FE_PID" 2>/dev/null; [ -n "$BE_PID" ] && kill "$BE_PID" 2>/dev/null; }
trap cleanup EXIT

wait_for(){ # url, timeout - any HTTP response counts (401 included): we need reachability, not success
  local url="$1" t="$2" i=0
  until curl -fsS -o /dev/null "$url" || curl -s -o /dev/null -w '%{http_code}' "$url" | grep -qE '^[1-5][0-9][0-9]$'; do
    i=$((i+1)); [ "$i" -ge "$t" ] && return 1; sleep 1
  done
}

echo "==> starting backend: $BACKEND_CMD"
$BACKEND_CMD & BE_PID=$!
if ! wait_for "$BACKEND_URL$HEALTH_PATH" "$TIMEOUT"; then
  echo "FAIL: backend not responding on $HEALTH_PATH (missing server dep? crash on boot? DB required by liveness?)"; exit 1
fi
echo "OK: backend health ($(curl -s -o /dev/null -w '%{http_code}' "$BACKEND_URL$HEALTH_PATH"))"

echo "==> starting frontend: $FRONTEND_CMD"
$FRONTEND_CMD & FE_PID=$!
if ! wait_for "$FRONTEND_URL" "$TIMEOUT"; then
  echo "FAIL: frontend does not start / does not serve (missing dev script?)"; exit 1
fi
echo "OK: frontend up"

echo "==> protected route via the frontend proxy: $FRONTEND_URL$PROXIED_PATH"
code=$(curl -s -o /dev/null -w '%{http_code}' "$FRONTEND_URL$PROXIED_PATH")
# 200 (data) or 401/403 (auth active) = reachable through the proxy.
# 000/404/502 = proxy, CORS or routing is broken - exactly the wave-0 failure.
case "$code" in
  200|401|403) echo "OK: route reachable via proxy (HTTP $code)";;
  *) echo "FAIL: route NOT reachable via proxy (HTTP $code) - check proxy / CORS / route"; exit 1;;
esac

echo "==> DEMO-SMOKE: PASS"
