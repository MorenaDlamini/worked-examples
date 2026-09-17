"""Written before the solutions. Each test must be able to fail for a real reason."""
from __future__ import annotations

import pytest

from ..exercises.ex01_parse_line import Entry
from ..solutions import sol01, sol02, sol03, sol04, sol05

GOOD = "2026-09-14T08:12:03Z WARN auth 41.13.8.9 failed login for admin"
SAMPLE = [
    GOOD,
    "2026-09-14T08:12:04Z INFO auth 41.13.8.9 session opened",
    "2026-09-14T08:12:05Z ERROR db 10.0.0.4 connection refused",
    "",
    "malformed line",
    "2026-09-14T08:12:06Z ERROR db 10.0.0.4 connection refused",
]


class TestParseLine:
    def test_splits_message_containing_spaces(self):
        e = sol01.parse_line(GOOD)
        assert e == Entry("2026-09-14T08:12:03Z", "WARN", "auth", "41.13.8.9 failed login for admin")

    def test_strips_trailing_newline(self):
        assert sol01.parse_line(GOOD + "\n").message.endswith("admin")

    @pytest.mark.parametrize("bad", ["", "\n", "only two", "three parts here", "  "])
    def test_returns_none_never_raises(self, bad):
        assert sol01.parse_line(bad) is None


class TestParseLines:
    def test_invariant_holds(self):
        r = sol02.parse_lines(SAMPLE)
        assert r.lines_read == len(SAMPLE)
        assert len(r.entries) + len(r.rejected) == len(SAMPLE)

    def test_rejects_are_kept_verbatim(self):
        r = sol02.parse_lines(SAMPLE)
        assert "malformed line" in r.rejected
        assert len(r.rejected) == 2  # the empty line and the malformed one


class TestCountByLevel:
    def test_counts(self):
        entries = sol02.parse_lines(SAMPLE).entries
        assert sol03.count_by_level(entries) == {"WARN": 1, "INFO": 1, "ERROR": 2}

    def test_absent_levels_absent(self):
        entries = sol02.parse_lines([GOOD]).entries
        assert "ERROR" not in sol03.count_by_level(entries)


class TestTopSources:
    def test_orders_by_count_then_token(self):
        entries = sol02.parse_lines(SAMPLE).entries
        assert sol04.top_sources(entries, 2) == [("10.0.0.4", 2), ("41.13.8.9", 2)]

    def test_returns_fewer_when_fewer_exist(self):
        entries = sol02.parse_lines([GOOD]).entries
        assert len(sol04.top_sources(entries, 10)) == 1


class TestStreamParse:
    def test_is_lazy(self):
        consumed = []

        def source():
            for line in SAMPLE:
                consumed.append(line)
                yield line

        gen = sol05.stream_parse(source())
        next(gen)
        assert len(consumed) == 1, "generator materialised the input"

    def test_skips_rejects(self):
        assert len(list(sol05.stream_parse(SAMPLE))) == 4
