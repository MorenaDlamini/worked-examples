"""Run a shell exercise and capture its result, so weeks-one-and-two modules can have
real tests before you know any Python.

    from tools.shelltest import run

    def test_counts_error_lines():
        r = run("exercises/ex01_count_errors.sh", "sample.log")
        assert r.ok, r.stderr
        assert r.stdout.strip() == "3"
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Result:
    code: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.code == 0

    @property
    def lines(self) -> list[str]:
        return self.stdout.strip().splitlines()


def run(script: str, *args: str, cwd: str | Path | None = None, stdin: str = "") -> Result:
    """Execute a shell script relative to the calling module's directory."""
    path = Path(script)
    if not path.is_absolute():
        path = Path(cwd or Path.cwd()) / path
    if not path.exists():
        raise FileNotFoundError(path)
    proc = subprocess.run(  # noqa: S603
        ["bash", str(path), *args],
        capture_output=True,
        text=True,
        input=stdin,
        cwd=path.parent,
        timeout=30,
        check=False,
    )
    return Result(proc.returncode, proc.stdout, proc.stderr)
