"""Acceptance test for 07-benchmark-honestly.

Skipped until the stage is started. See challenges/README.md.
"""
import re

from harness import REPO, load, sh  # noqa: F401


def test_a_benchmark_was_written(solution):
    docs = list(solution.glob("*.md"))
    assert docs, "write the benchmark up in a markdown file"
    text = "\n".join(p.read_text() for p in docs)
    assert re.search(r"\d", text), "a benchmark with no numbers is a paragraph"


def test_it_states_what_it_does_not_measure(solution):
    text = "\n".join(p.read_text() for p in solution.glob("*.md"))
    assert re.search(r"limitation|does not measure|caveat|not measured", text, re.IGNORECASE), \
        "a benchmark with no limitations section does not count"


def test_the_hardware_is_recorded(solution):
    text = "\n".join(p.read_text() for p in solution.glob("*.md"))
    assert re.search(r"cpu|core|ram|memory|ssd|nvme|laptop|machine", text, re.IGNORECASE), \
        "say what it ran on, or the numbers mean nothing"
