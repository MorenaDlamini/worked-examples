"""Acceptance test for 00-typed-cli.

Skipped until the stage is started. See challenges/README.md.
"""
import subprocess
import sys

from harness import REPO, load, sh  # noqa: F401


def test_the_package_imports(solution):
    load(solution)


def test_help_runs(solution):
    r = subprocess.run([sys.executable, "-m", "solution", "--help"],
                       cwd=solution.parent, capture_output=True, text=True, check=False)
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip(), "--help should say something"
