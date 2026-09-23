"""Acceptance test for 03-wal-append.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

def test_records_survive_a_reopen(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "wal"
    w = mod.Wal(path)
    w.append(b"one")
    w.append(b"two")
    w.close()
    assert list(mod.Wal(path).read()) == [b"one", b"two"]


def test_each_record_is_checksummed(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "wal"
    w = mod.Wal(path)
    w.append(b"payload")
    w.close()
    raw = bytearray(path.read_bytes())
    raw[-1] ^= 0xFF
    path.write_bytes(bytes(raw))
    try:
        out = list(mod.Wal(path).read())
    except Exception:
        return
    assert out != [b"payload"], "a corrupted record must not read back as though it were fine"
