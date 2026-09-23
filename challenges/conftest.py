"""Shared harness for the challenge ladders.

A stage that has not been started is skipped, with a visible reason, so CI stays green and the
badge keeps meaning something. A stage that HAS been started must pass. Starting a stage is
therefore a commitment, which is the point.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def _started(stage: Path) -> bool:
    sol = stage / "solution"
    if not sol.is_dir():
        return False
    return any(
        p for p in sol.rglob("*")
        if p.is_file() and not p.name.startswith(".") and "__pycache__" not in p.parts
    )


@pytest.fixture
def stage(request) -> Path:
    """The directory of the stage whose test is running."""
    return Path(request.path).resolve().parent.parent


@pytest.fixture
def solution(stage: Path) -> Path:
    """Skip unless the stage has been started. Otherwise hand back its solution directory."""
    if not _started(stage):
        pytest.skip(f"not started: {stage.name} has no files in solution/")
    return stage / "solution"


@pytest.fixture
def fixtures(stage: Path) -> Path:
    return stage.parent / "fixtures"


@pytest.fixture
def base_url() -> str:
    """Black-box target for phases 2 and later. Skips unless the service is running."""
    url = os.environ.get("CHALLENGE_BASE_URL")
    if not url:
        pytest.skip("CHALLENGE_BASE_URL is not set, so the service is not running")
    return url.rstrip("/")
