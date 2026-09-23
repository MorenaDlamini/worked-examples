"""Acceptance test for 06-ci-matrix.

This stage is graded on the workflow file itself, because that is the artifact.
Skipped until the stage is started. See challenges/README.md.
"""
import re

import pytest

from harness import REPO

yaml = pytest.importorskip("yaml", reason="pyyaml not installed")


def _workflows():
    d = REPO / ".github" / "workflows"
    return list(d.glob("*.yml")) + list(d.glob("*.yaml"))


def test_some_job_runs_on_a_matrix(solution):
    found = False
    for f in _workflows():
        doc = yaml.safe_load(f.read_text()) or {}
        for job in (doc.get("jobs") or {}).values():
            m = ((job or {}).get("strategy") or {}).get("matrix")
            if m and any(isinstance(v, list) and len(v) > 1 for v in m.values()):
                found = True
    assert found, "no job defines a matrix with more than one leg"


def test_dependencies_are_cached(solution):
    text = "\n".join(f.read_text() for f in _workflows())
    assert re.search(r"actions/cache@|cache:\s*\S", text), \
        "nothing in the workflows caches dependencies"
