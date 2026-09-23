"""Acceptance test for 00-typed-cli.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

import subprocess
import sys


def test_the_package_imports(solution):
    load(solution)


def test_help_runs(solution):
    r = subprocess.run([sys.executable, "-m", "solution", "--help"],
                       cwd=solution.parent, capture_output=True, text=True, check=False)
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip(), "--help should say something"
