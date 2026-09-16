#!/usr/bin/env python3
"""coherence_docs_lint.py - Gate 3b: DOCUMENTATION coherence (doc<->doc, doc<->reality).

Catches the class of drift the coherence gate (spec<->test<->code) does NOT see. This gate exists
because of a wave-0 finding: spec/code coherence held, while documents drifted against each other.

Checks:
  1) a spec's front-matter status != the status reported in the traceability index
  2) hand-written totals "X + Y + Z = N" that are arithmetically wrong
  3) references to files that do not exist ([...](path), or `path` with an extension)
  4) "blocked by IMP-x" where IMP-x is recorded as resolved in the authoritative register
  5) role-mapping drift (App Role -> role) across files (backend vs frontend vs rbac-matrix)

DETERMINISTIC gate: it verifies facts, it does not reason. Per the gate taxonomy it therefore blocks
from day one (--strict in CI); no calibration period.

Usage: python scripts/coherence_docs_lint.py [--strict]
"""
import glob
import os
import re
import sys

ROOT = os.environ.get("REPO_ROOT", ".")
STRICT = "--strict" in sys.argv
EXCLUDE = ("node_modules", ".venv", ".git", "incoming", "dist")
findings = []


def add(kind, msg):
    findings.append((kind, msg))


def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""


def _excluded(p):
    parts = os.path.normpath(p).split(os.sep)
    return any(d in parts for d in EXCLUDE)


def md_files():
    return [p for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True) if not _excluded(p)]


# --- 1) spec status vs traceability index ---
def spec_status():
    st = {}
    for p in glob.glob(os.path.join(ROOT, "spec", "*.md")):
        if os.path.basename(p).startswith(("_", "traceability")):
            continue
        t = read(p)
        m = re.search(r"(?m)^id:\s*(\S+)", t)
        s = re.search(r"(?m)^status:\s*(\S+)", t)
        if m and s:
            st[m.group(1)] = s.group(1)
    return st


def check_status_vs_traceability():
    trace = read(os.path.join(ROOT, "spec", "traceability.md"))
    if not trace:
        return
    for fid, status in spec_status().items():
        # The spec's OWN row is the one carrying the id in the first cell (`| TF-02 |`),
        # not a row that merely mentions it in a "depends on" cell.
        for line in trace.splitlines():
            if re.match(rf"^\|\s*{re.escape(fid)}\s*\|", line):
                if status not in line:
                    add("status-drift", f"{fid}: spec status='{status}' does not appear in its traceability row")
                break


# --- 2) hand-written totals vs the actual sum ---
def check_manual_totals():
    for p in md_files():
        t = read(p)
        for m in re.finditer(
            r"([0-9]+(?:\.[0-9]+)?)\s*\+\s*([0-9]+(?:\.[0-9]+)?)\s*\+?\s*([0-9]+(?:\.[0-9]+)?)?\s*=\s*([0-9]+(?:\.[0-9]+)?)",
            t,
        ):
            a = float(m.group(1)); b = float(m.group(2)); c = float(m.group(3) or 0); tot = float(m.group(4))
            if abs((a + b + c) - tot) > 0.05:
                add("math", f"{os.path.relpath(p, ROOT)}: '{m.group(0)}' does not add up ({a}+{b}+{c}={a + b + c})")


# --- 3) references to non-existent files ---
def check_dead_refs():
    ext = r"(?:md|py|ts|tsx|yml|yaml|xlsx|svg|json|sh|toml)"
    for p in md_files():
        t = read(p); base = os.path.dirname(p)
        for m in re.finditer(rf"`([^`]+?\.{ext})`|\]\(([^)]+?\.{ext})\)", t):
            is_link = m.group(2) is not None  # markdown link ](path) vs backticked `path`
            ref = (m.group(1) or m.group(2)).split("#")[0].strip()
            # A space means prose or a command (`python scripts/x.py`), not a file path.
            if ref.startswith(("http", "mailto")) or any(c in ref for c in "<>$* "):
                continue
            # A backticked token is only a dead ref if it is a PATH (contains '/'); a bare filename is prose.
            if not is_link and "/" not in ref:
                continue
            target = ref.lstrip("/") if ref.startswith("/") else ref  # '/x' means repo-root-relative
            cand = [os.path.join(ROOT, target), os.path.join(base, ref)]
            if not any(os.path.exists(c) for c in cand):
                add("dead-ref", f"{os.path.relpath(p, ROOT)}: reference to non-existent file '{ref}'")


# --- 4) "blocked by" an open point that is already resolved ---
def resolved_imps():
    """Open points closed according to the AUTHORITATIVE register (governance/open-points.md).

    HARDENED after a false positive: an earlier version scanned every document and inferred closure
    from proximity, so prose like "TF-03 is already closed" sitting next to an IMP reference marked
    that IMP resolved. Only the register decides.
    """
    res = set()
    for line in read(os.path.join(ROOT, "governance", "open-points.md")).splitlines():
        if "|" not in line:
            continue
        m = re.search(r"(IMP-\d+)", line)
        if m and re.search(r"\b(resolved|closed|confirmed)", line, re.I):
            res.add(m.group(1).upper())
    return res


def check_blocked_by_resolved():
    res = resolved_imps()
    for p in md_files():
        # HARDENED: `(not\s+)?` captures the negation - "NOT blocked by IMP-x" is not a block.
        for m in re.finditer(r"(?i)(not\s+)?blocked by\s*(IMP-\d+)", read(p)):
            if m.group(1):
                continue
            imp = m.group(2).upper()
            if imp in res:
                add("stale-block", f"{os.path.relpath(p, ROOT)}: claims 'blocked by {imp}' but {imp} is resolved")


# --- 5) role-mapping drift across files ---
def role_maps():
    maps = {}
    for p in glob.glob(os.path.join(ROOT, "**", "*.*"), recursive=True):
        if not p.endswith((".py", ".ts", ".tsx", ".md")) or _excluded(p):
            continue
        pairs = dict(
            re.findall(
                r'["\']SGP\.(Admin|Approver|Editor|Viewer)["\']\s*[:=]?\s*(?:Role\.)?["\']?(admin|approver|editor|viewer)["\']?',
                read(p),
            )
        )
        if pairs:
            maps[os.path.relpath(p, ROOT)] = {"SGP." + k: v for k, v in pairs.items()}
    return maps


def check_role_map_drift():
    maps = role_maps()
    if len(maps) < 2:
        return
    ref_file, ref = next(iter(maps.items()))
    for f, m in maps.items():
        for k in set(m) & set(ref):
            if m[k] != ref[k]:
                add("rolemap-drift", f"role mapping diverges for {k}: {f}={m[k]} vs {ref_file}={ref[k]}")


for fn in (
    check_status_vs_traceability, check_manual_totals, check_dead_refs,
    check_blocked_by_resolved, check_role_map_drift,
):
    try:
        fn()
    except Exception as e:
        add("lint-error", f"{fn.__name__}: {e}")

if not findings:
    print("Coherence docs lint: no findings.")
    sys.exit(0)
print(f"Coherence docs lint: {len(findings)} finding(s)\n")
for kind, msg in sorted(findings):
    print(f"  [{kind}] {msg}")
sys.exit(1 if STRICT else 0)
