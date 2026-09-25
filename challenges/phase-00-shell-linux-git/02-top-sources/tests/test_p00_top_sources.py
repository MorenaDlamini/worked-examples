"""Acceptance test for 02-top-sources.

Skipped until the stage is started. See challenges/README.md.
"""
import pytest
from harness import REPO, load, sh  # noqa: F401


def test_top_two_sources(solution, fixtures):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"), "2")
    assert r.returncode == 0, r.stderr
    lines = r.stdout.strip().splitlines()
    assert len(lines) == 2
    assert lines[0].split("\t")[0] == "api"
    assert lines[0].split("\t")[1] == "4"


@pytest.mark.parametrize("n", ["99", "3"])
def test_n_larger_than_the_data_is_not_an_error(solution, fixtures, n):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"), n)
    assert r.returncode == 0, r.stderr
    assert len(r.stdout.strip().splitlines()) <= 3
