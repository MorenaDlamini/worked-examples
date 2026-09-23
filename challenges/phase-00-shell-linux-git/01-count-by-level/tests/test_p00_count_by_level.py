"""Acceptance test for 01-count-by-level.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

def test_counts_match_the_fixture(solution, fixtures):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"))
    assert r.returncode == 0, r.stderr
    got = dict(line.split("\t")[:2] for line in r.stdout.strip().splitlines())
    assert got == {"INFO": "4", "ERROR": "2", "WARN": "1", "DEBUG": "1"}


def test_ordered_by_count_then_alphabetically(solution, fixtures):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"))
    levels = [line.split("\t")[0] for line in r.stdout.strip().splitlines()]
    assert levels[0] == "INFO", "highest count first"
    assert levels[1] == "ERROR"
    assert levels[2:] == ["DEBUG", "WARN"], "ties break alphabetically, so the output is stable"
