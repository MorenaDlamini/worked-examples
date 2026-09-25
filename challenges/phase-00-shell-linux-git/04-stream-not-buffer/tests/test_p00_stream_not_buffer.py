"""Acceptance test for 04-stream-not-buffer.

Skipped until the stage is started. See challenges/README.md.
"""
import shutil
import subprocess

import pytest
from harness import REPO, load, sh  # noqa: F401

BIG = 400_000


def test_handles_a_file_far_larger_than_the_fixture(solution, fixtures, tmp_path):
    big = tmp_path / "big.log"
    one = (fixtures / "sample.log").read_text().splitlines()[0] + "\n"
    with big.open("w") as fh:
        for _ in range(BIG):
            fh.write(one)
    r = sh(solution / "run.sh", str(big), timeout=300)
    assert r.returncode == 0, r.stderr


@pytest.mark.skipif(shutil.which("/usr/bin/time") is None, reason="GNU time not available")
def test_peak_memory_stays_flat(solution, fixtures, tmp_path):
    big = tmp_path / "big.log"
    one = (fixtures / "sample.log").read_text().splitlines()[0] + "\n"
    with big.open("w") as fh:
        for _ in range(BIG):
            fh.write(one)
    proc = subprocess.run(
        ["/usr/bin/time", "-v", "bash", str(solution / "run.sh"), str(big)],
        capture_output=True, text=True, cwd=solution, timeout=300, check=False,
    )
    peak = [ln for ln in proc.stderr.splitlines() if "Maximum resident" in ln]
    if not peak:
        pytest.skip("this build of time does not report maximum resident set size")
    kb = int(peak[0].split(":")[1].strip())
    assert kb < 200_000, f"peak {kb} KB suggests the file was buffered, not streamed"
