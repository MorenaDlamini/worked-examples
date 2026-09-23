"""Report challenge-ladder progress, and regenerate the table in challenges/README.md.

A stage counts as started when it has a file in `solution/`, and as done when its acceptance
test passes. This tool only reports what is started; CI decides what passes, because locally
green is where the environment lies to you.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "challenges"


def started(stage: Path) -> bool:
    sol = stage / "solution"
    if not sol.is_dir():
        return False
    return any(
        p for p in sol.rglob("*")
        if p.is_file() and not p.name.startswith(".") and "__pycache__" not in p.parts
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="print the summary and exit 0")
    ap.parse_args()

    ladders = json.loads((CH / "ladders.json").read_text(encoding="utf-8"))
    rows, total, begun = [], 0, 0
    for phase_dir in sorted(ladders):
        meta = ladders[phase_dir]
        stages = meta["stages"]
        n = sum(1 for s in stages if started(CH / phase_dir / s))
        total += len(stages)
        begun += n
        nxt = next((s for s in stages if not started(CH / phase_dir / s)), "\u2014 all started")
        pn = phase_dir.split("-")[1]
        bar = "#" * n + "." * (len(stages) - n)
        rows.append(
            f"| {pn} | {meta['phase']} | `{bar}` | {n}/{len(stages)} | `{nxt}` |"
        )

    table = "\n".join(
        ["| Phase | Ladder | Progress | Started | Next stage |", "|---|---|---|---|---|", *rows]
    )
    summary = f"\n**{begun} of {total} stages started.**\n"

    readme = CH / "README.md"
    text = readme.read_text(encoding="utf-8")
    new = re.sub(
        r"<!-- LADDER:START -->.*<!-- LADDER:END -->",
        "<!-- LADDER:START -->\n" + table + "\n" + summary + "<!-- LADDER:END -->",
        text,
        flags=re.DOTALL,
    )
    readme.write_text(new, encoding="utf-8", newline="\n")
    print(f"{total} stages across {len(ladders)} ladders, {begun} started")


if __name__ == "__main__":
    main()
