"""Acceptance test for 05-wal-compact.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

def test_compaction_keeps_every_committed_key(solution, tmp_path):
    mod = load(solution)
    store = mod.Store(tmp_path / "db")
    for i in range(100):
        store.put(b"k%02d" % (i % 10), b"v%02d" % i)
    before = {k: store.get(k) for k in (b"k%02d" % i for i in range(10))}
    store.compact()
    after = {k: store.get(k) for k in (b"k%02d" % i for i in range(10))}
    assert before == after


def test_compaction_actually_shrinks_the_file(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "db"
    store = mod.Store(path)
    for i in range(500):
        store.put(b"same-key", b"v%03d" % i)
    big = sum(p.stat().st_size for p in path.parent.rglob("*") if p.is_file())
    store.compact()
    small = sum(p.stat().st_size for p in path.parent.rglob("*") if p.is_file())
    assert small < big, "500 writes to one key should compact to roughly one"
