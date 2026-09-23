"""Acceptance test for 07-bisect-the-bug.

Graded on the written finding, and on the commit actually existing.
Skipped until the stage is started. See challenges/README.md.
"""
import re
import subprocess

from harness import REPO


def test_a_finding_was_written(solution):
    notes = list(solution.glob("*.md"))
    assert notes, "write up what you found, in a markdown file in solution/"
    text = "\n".join(p.read_text() for p in notes)
    assert re.search(r"bisect", text, re.I), "say which command you used"
    assert re.search(r"\b[0-9a-f]{7,40}\b", text), "name the commit"


def test_the_named_commit_exists(solution):
    text = "\n".join(p.read_text() for p in solution.glob("*.md"))
    shas = re.findall(r"\b[0-9a-f]{7,40}\b", text)
    ok = False
    for sha in shas:
        r = subprocess.run(["git", "cat-file", "-t", sha], cwd=REPO,
                           capture_output=True, text=True, check=False)
        if r.stdout.strip() == "commit":
            ok = True
    assert ok, f"none of {shas} is a commit in this repository"
