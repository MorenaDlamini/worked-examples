"""Tests are written before the solution. A test that cannot fail teaches nothing."""
import pytest

from ..exercises import ex01_rename_me


@pytest.mark.xfail(reason="exercise not yet attempted", strict=False)
def test_ex01():
    assert ex01_rename_me.solve(None) is not None
