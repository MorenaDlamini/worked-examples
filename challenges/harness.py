"""Helpers the stage tests import. Kept out of conftest so the import is explicit."""
from __future__ import annotations

import importlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def sh(script: Path, *args: str, stdin: str = "", timeout: int = 60):
    """Run a shell solution and hand back the completed process."""
    return subprocess.run(
        ["bash", str(script), *args],
        capture_output=True, text=True, input=stdin,
        cwd=script.parent, timeout=timeout, check=False,
    )


def load(solution: Path):
    """Import a stage's Python solution package by path."""
    sys.path.insert(0, str(solution.parent))
    try:
        for name in [m for m in sys.modules if m == "solution" or m.startswith("solution.")]:
            del sys.modules[name]
        return importlib.import_module("solution")
    finally:
        sys.path.pop(0)
