"""Acceptance test for 04-wal-crash.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import REPO, load, sh  # noqa: F401


def test_a_torn_tail_costs_only_the_partial_record(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "wal"
    w = mod.Wal(path)
    for i in range(20):
        w.append(b"record-%02d" % i)
    w.close()
    whole = path.read_bytes()
    path.write_bytes(whole[: len(whole) - 3])
    out = list(mod.Wal(path).read())
    assert len(out) == 19, f"expected to lose exactly the torn record, kept {len(out)}"
    assert out[0] == b"record-00"


def test_an_empty_file_opens_cleanly(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "wal"
    path.write_bytes(b"")
    assert list(mod.Wal(path).read()) == []
