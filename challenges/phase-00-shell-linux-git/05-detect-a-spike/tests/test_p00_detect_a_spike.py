"""Acceptance test for 05-detect-a-spike.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import REPO, load, sh  # noqa: F401


def test_a_quiet_file_reports_nothing(solution, tmp_path):
    quiet = tmp_path / "quiet.log"
    quiet.write_text("2026-09-01T08:00:01Z INFO api ok\n" * 50)
    r = sh(solution / "run.sh", str(quiet), "0.5")
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "", "no window breaches the threshold, so there is nothing to say"


def test_a_spike_is_found(solution, tmp_path):
    noisy = tmp_path / "noisy.log"
    lines = [f"2026-09-01T08:00:{i:02d}Z INFO api ok" for i in range(30)]
    lines += [f"2026-09-01T08:01:{i:02d}Z ERROR api boom" for i in range(30)]
    noisy.write_text("\n".join(lines) + "\n")
    r = sh(solution / "run.sh", str(noisy), "0.5")
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip(), "the second minute is all errors and should be flagged"
    assert "08:01" in r.stdout
