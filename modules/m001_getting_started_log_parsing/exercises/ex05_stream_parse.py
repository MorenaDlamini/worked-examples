"""Exercise 5 — process input larger than memory."""
from __future__ import annotations

from collections.abc import Iterable, Iterator

from .ex01_parse_line import Entry


def stream_parse(lines: Iterable[str]) -> Iterator[Entry]:
    """Yield entries lazily, skipping rejects.

    Must not materialise the input. Consuming one item from the result must read at most
    a bounded number of items from the source.
    """
    raise NotImplementedError
