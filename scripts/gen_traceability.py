#!/usr/bin/env python3
"""gen_traceability.py - generates the "specs on the ground" table in spec/traceability.md from
spec front-matter.

Wave-0 lesson, "one fact, one home": a file-derived index is NEVER hand-written. This index had
already drifted twice before it was generated - it is the reason the rule exists.

The generated region is delimited by markers; the rest of the file (the full requirement perimeter
from the functional annex, plus notes) stays hand-curated, because it is not derivable from the spec
files - many requirements do not have a spec file yet.

Usage: python scripts/gen_traceability.py [--check]
  --check: does not rewrite; exits !=0 if the generated region differs from the front-matter.
           This is what runs in CI, inside gate 3b.
"""
import glob
import os
import re
import sys

SPEC_DIR = os.environ.get("SPEC_DIR", "spec")
OUT = os.path.join(SPEC_DIR, "traceability.md")
START = "<!-- GEN:traceability:start -->"
END = "<!-- GEN:traceability:end -->"


def _val(fm: dict, key: str) -> str:
    """Front-matter value, stripped of any inline comment (`status: Approved  # G1 ...` -> `Approved`)."""
    return fm.get(key, "").split("#")[0].strip()


def _parse_frontmatter(path: str) -> dict | None:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return None
    fm: dict = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1).strip()] = mm.group(2).strip()
    return fm


def _build_block() -> str:
    specs = []
    for p in sorted(glob.glob(os.path.join(SPEC_DIR, "*.md"))):
        base = os.path.basename(p)
        if base.startswith("_") or base == "traceability.md":
            continue
        fm = _parse_frontmatter(p)
        if fm and fm.get("id"):
            fm["_file"] = os.path.relpath(p).replace("\\", "/")
            specs.append(fm)
    specs.sort(key=lambda x: _val(x, "id"))

    rows = [
        "| FR/TF | Title | UC | Wave | Scope | Rigor | Status | Depends on | Spec |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for fm in specs:
        rows.append(
            "| {id} | {title} | {uc} | {wave} | {scope} | {rigor} | {status} | {dep} | `{f}` |".format(
                id=_val(fm, "id"), title=_val(fm, "title"), uc=_val(fm, "uc") or "-",
                wave=_val(fm, "wave"), scope=_val(fm, "scope"), rigor=_val(fm, "rigor"),
                status=_val(fm, "status"), dep=_val(fm, "depends_on") or "-", f=fm["_file"],
            )
        )
    n = len(specs)
    n_appr = sum(1 for s in specs if _val(s, "status").lower().startswith("approved"))
    rows.append("")
    rows.append(
        f"**Specs on the ground:** {n} ({n_appr} Approved). Table **generated** by "
        "`scripts/gen_traceability.py` from front-matter - do not edit by hand."
    )
    return "\n".join(rows)


def main() -> None:
    if not os.path.exists(OUT):
        print(f"ERROR: {OUT} is missing."); sys.exit(2)
    text = open(OUT, encoding="utf-8").read()
    if START not in text or END not in text:
        print(f"ERROR: markers {START} / {END} not found in {OUT}."); sys.exit(2)
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        START + "\n" + _build_block() + "\n" + END,
        text, flags=re.S,
    )
    if "--check" in sys.argv:
        if new != text:
            print("DRIFT: spec/traceability.md is not aligned with front-matter. Regenerate it.")
            sys.exit(1)
        print("OK: traceability aligned with front-matter.")
        return
    open(OUT, "w", encoding="utf-8").write(new)
    print(f"updated the generated region of {OUT}")


if __name__ == "__main__":
    main()
