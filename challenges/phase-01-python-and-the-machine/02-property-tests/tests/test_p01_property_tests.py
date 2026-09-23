"""Acceptance test for 02-property-tests.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

import re


def test_a_property_test_exists_and_uses_given(solution):
    files = list(solution.rglob("test_*.py"))
    assert files, "write the properties as a test file in solution/"
    text = "\n".join(p.read_text() for p in files)
    assert "@given" in text, "use Hypothesis @given, not a loop over examples"


def test_the_found_case_was_written_down(solution):
    notes = "\n".join(p.read_text() for p in solution.glob("*.md"))
    assert notes.strip(), "record the case Hypothesis found and the fix, in a markdown file"
    assert re.search(r"shrink|shrunk|minimal", notes, re.I), \
        "record the shrunk case, which is the useful part"
