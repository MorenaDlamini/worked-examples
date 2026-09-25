"""Acceptance test for 03-reject-malformed.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import REPO, load, sh  # noqa: F401


def test_exits_two_and_counts_the_reject(solution, fixtures):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"))
    assert r.returncode == 2, "one line is malformed, so this is a partial success"
    assert "1" in r.stderr, f"the reject count belongs on stderr, got {r.stderr!r}"


def test_every_good_record_still_comes_out(solution, fixtures):
    r = sh(solution / "run.sh", str(fixtures / "sample.log"))
    assert len(r.stdout.strip().splitlines()) == 8, "all eight good records survive"
