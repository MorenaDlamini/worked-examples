"""Acceptance test for 01-records-and-rejects.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

import pytest


def test_returns_two_streams(solution):
    mod = load(solution)
    fn = getattr(mod, "parse_lines", None)
    assert fn, "expose parse_lines(iterable) -> (records, rejects)"
    records, rejects = fn(["2026-09-01T08:00:01Z INFO api ok", "rubbish"])
    assert len(list(records)) == 1
    assert len(list(rejects)) == 1


def test_one_bad_line_does_not_stop_the_run(solution):
    mod = load(solution)
    lines = ["2026-09-01T08:00:01Z INFO api ok"] * 1000
    lines[500] = "rubbish"
    records, rejects = mod.parse_lines(lines)
    assert len(list(records)) == 999, "a bad line is a counter, not an exception"
    assert len(list(rejects)) == 1


def test_it_never_raises_on_bad_input(solution):
    mod = load(solution)
    for bad in ["", "   ", "\x00", "a" * 10000]:
        try:
            mod.parse_lines([bad])
        except Exception as exc:  # noqa: BLE001
            pytest.fail(f"raised on {bad[:20]!r}: {exc}")
