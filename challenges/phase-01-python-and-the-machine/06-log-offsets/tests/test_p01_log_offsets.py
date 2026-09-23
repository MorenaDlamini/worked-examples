"""Acceptance test for 06-log-offsets.

Skipped until the stage is started. See challenges/README.md.
"""
from harness import sh, load, REPO  # noqa: F401

def test_two_groups_read_independently(solution, tmp_path):
    mod = load(solution)
    log = mod.Log(tmp_path / "log", partitions=2)
    for i in range(10):
        log.append(b"k%d" % (i % 2), b"m%02d" % i)
    a = list(log.consume("group-a"))
    assert len(a) == 10
    b = list(log.consume("group-b"))
    assert len(b) == 10, "a second group starts from the beginning, not from group-a's offset"


def test_a_restart_resumes_from_the_stored_offset(solution, tmp_path):
    mod = load(solution)
    path = tmp_path / "log"
    log = mod.Log(path, partitions=2)
    for i in range(10):
        log.append(b"k%d" % (i % 2), b"m%02d" % i)
    list(log.consume("group-a"))
    log.append(b"k0", b"m10")
    again = list(mod.Log(path, partitions=2).consume("group-a"))
    assert [m for m in again] == [b"m10"], "only the new message should be replayed"


def test_ordering_holds_within_a_key(solution, tmp_path):
    mod = load(solution)
    log = mod.Log(tmp_path / "log", partitions=4)
    for i in range(20):
        log.append(b"same", b"m%02d" % i)
    got = [m for m in log.consume("g")]
    assert got == sorted(got), "messages for one key must keep their order"
