"""Exercise 1 — return a failure value instead of raising."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    timestamp: str
    level: str
    service: str
    message: str


def parse_line(line: str) -> Entry | None:
    """Parse `TIMESTAMP LEVEL SERVICE MESSAGE...` into an Entry.

    The message may contain spaces. Trailing newlines are ignored.
    Return None for any line that does not fit. Never raise.
    """
    raise NotImplementedError
