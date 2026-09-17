"""Exercise 2 — separate records from rejects, and count both."""
from __future__ import annotations

from dataclasses import dataclass

from .ex01_parse_line import Entry


@dataclass
class ParseResult:
    entries: list[Entry]
    rejected: list[str]

    @property
    def lines_read(self) -> int:
        return len(self.entries) + len(self.rejected)


def parse_lines(lines: list[str]) -> ParseResult:
    """Parse every line. Rejected lines are kept verbatim, not discarded.

    The invariant `lines_read == len(entries) + len(rejected)` must always hold.
    """
    raise NotImplementedError
