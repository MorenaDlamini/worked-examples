"""Acceptance test for 07-benchmark-honestly.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

import re


def test_a_benchmark_was_written(solution):
    docs = list(solution.glob("*.md"))
    assert docs, "write the benchmark up in a markdown file"
    text = "\n".join(p.read_text() for p in docs)
    assert re.search(r"\d", text), "a benchmark with no numbers is a paragraph"


def test_it_states_what_it_does_not_measure(solution):
    text = "\n".join(p.read_text() for p in solution.glob("*.md"))
    assert re.search(r"limitation|does not measure|caveat|not measured", text, re.I), \
        "a benchmark with no limitations section does not count"


def test_the_hardware_is_recorded(solution):
    text = "\n".join(p.read_text() for p in solution.glob("*.md"))
    assert re.search(r"cpu|core|ram|memory|ssd|nvme|laptop|machine", text, re.I), \
        "say what it ran on, or the numbers mean nothing"
