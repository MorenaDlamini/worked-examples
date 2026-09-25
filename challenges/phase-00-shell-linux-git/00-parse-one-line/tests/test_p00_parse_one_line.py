"""Acceptance test for 00-parse-one-line.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import REPO, load, sh  # noqa: F401


def test_good_line_gives_three_tab_separated_fields(solution):
    r = sh(solution / "run.sh", stdin="2026-09-01T08:00:01Z INFO api request ok\n")
    assert r.returncode == 0, r.stderr
    parts = r.stdout.strip().split("\t")
    assert len(parts) == 3, f"expected 3 tab-separated fields, got {parts!r}"
    assert parts[0] == "2026-09-01T08:00:01Z"
    assert parts[1] == "INFO"
    assert parts[2].startswith("request ok")


def test_malformed_line_exits_two(solution):
    r = sh(solution / "run.sh", stdin="not a log line\n")
    assert r.returncode == 2, f"expected exit 2 on a malformed line, got {r.returncode}"
