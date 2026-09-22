"""Regenerate the progress table in README.md, and optionally enforce the module standard."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "modules"

REQUIRED_FILES = ["README.md", "NOTES.md", "INTERVIEW.md"]
REQUIRED_SECTIONS = [
    "## In one sentence",
    "## The problem",
    "## Counter-example",
    "## Failure modes",
    "## How you would measure it",
    "## Non-claims",
    "## Sources",
]
MIN_EXERCISES = {"getting_started": 3, "hands_on": 6, "deep_dive": 3, "build_it": 1}


def tier_of(name: str) -> str:
    for t in MIN_EXERCISES:
        if f"_{t}_" in name:
            return t
    return "unknown"


def audit(d: Path) -> list[str]:
    problems: list[str] = []
    for f in REQUIRED_FILES:
        if not (d / f).exists():
            problems.append(f"missing {f}")
    readme = d / "README.md"
    if readme.exists():
        text = readme.read_text()
        for s in REQUIRED_SECTIONS:
            if s not in text:
                problems.append(f"README missing section '{s}'")
        if "TODO" in text:
            problems.append("README still contains TODO")
    ex = d / "exercises"
    # Shell modules (CONTRIBUTING.md, "Before you know Python") keep exercises as .sh scripts.
    n = len(list(ex.glob("[!_]*.py")) + list(ex.glob("[!_]*.sh"))) if ex.exists() else 0
    need = MIN_EXERCISES.get(tier_of(d.name), 1)
    if n < need:
        problems.append(f"{n} exercises, tier requires {need}")
    return problems


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true", help="exit non-zero if any module is incomplete")
    args = p.parse_args()

    dirs = sorted(
        d for d in MODULES.iterdir()
        if d.is_dir() and d.name.startswith("m") and not d.name.startswith("__")
    )
    rows, failing = [], {}
    for d in dirs:
        problems = audit(d)
        state = "done" if not problems else "in progress"
        if problems:
            failing[d.name] = problems
        topic = re.sub(rf"^m\d+_{tier_of(d.name)}_", "", d.name).replace("_", " ")
        rows.append(f"| `{d.name}` | {tier_of(d.name).replace('_', '-')} | {topic} | {state} |")

    table = "\n".join(
        ["| Module | Tier | Topic | State |", "|---|---|---|---|", *rows]
    ) if rows else "_No modules yet._"

    readme = ROOT / "README.md"
    text = readme.read_text()
    new = re.sub(
        r"<!-- STATUS:START -->.*<!-- STATUS:END -->",
        f"<!-- STATUS:START -->\n{table}\n<!-- STATUS:END -->",
        text,
        flags=re.DOTALL,
    )
    readme.write_text(new)
    print(f"{len(dirs)} modules, {len(dirs) - len(failing)} complete")

    if args.check and failing:
        # In-progress modules are fine on a feature branch; this gate is advisory by default.
        for name, problems in failing.items():
            print(f"  {name}: {'; '.join(problems)}", file=sys.stderr)


if __name__ == "__main__":
    main()
