"""Scaffold a new module from the template."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIERS = ("getting-started", "hands-on", "deep-dive", "build-it")


def next_number() -> str:
    existing = [d.name for d in (ROOT / "modules").iterdir() if d.is_dir()]
    nums = [int(m.group(1)) for n in existing if (m := re.match(r"m(\d+)", n))]
    return f"{max(nums, default=0) + 1:03d}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tier", required=True, choices=TIERS)
    p.add_argument("--topic", required=True, help="kebab-case, e.g. window-functions")
    args = p.parse_args()

    # Directory names must be valid Python identifiers: pytest imports them as packages.
    slug = re.sub(r"[^a-z0-9_]", "", args.topic.lower().replace("-", "_").replace(" ", "_"))
    tier = args.tier.replace("-", "_")
    name = f"m{next_number()}_{tier}_{slug}"
    dest = ROOT / "modules" / name
    if dest.exists():
        raise SystemExit(f"{dest} already exists")

    shutil.copytree(ROOT / "templates" / "module", dest)
    (dest / "__init__.py").touch()

    title = slug.replace("_", " ").title()
    today = dt.datetime.now(tz=dt.UTC).date().isoformat()
    for f in dest.rglob("*.md"):
        f.write_text(
            f.read_text()
            .replace("{{TITLE}}", title)
            .replace("{{TIER}}", args.tier)
            .replace("{{DATE}}", today)
        )
    print(f"created modules/{name}")
    print("next: write README.md before writing a single test")


if __name__ == "__main__":
    main()
