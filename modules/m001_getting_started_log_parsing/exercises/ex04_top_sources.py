"""Exercise 4 — ordering, with ties broken deterministically."""
from __future__ import annotations

from .ex01_parse_line import Entry


def top_sources(entries: list[Entry], n: int) -> list[tuple[str, int]]:
    """Return the n most frequent first whitespace-separated tokens of the message field.

    Sort by count descending, then by token ascending so the result is deterministic.
    Returning fewer than n items is correct when there are fewer distinct tokens.
    """
    raise NotImplementedError
