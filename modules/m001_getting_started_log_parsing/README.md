# Log Parsing

`tier: getting-started` · `started: 2026-09-17` · `status: done`

## In one sentence

Turning lines of text that a program wrote for a human into structured records a program
can count, filter and query.

## The problem

A server writes millions of lines like `2026-09-14T08:12:03Z WARN auth 41.13.8.9 failed login`.
Nobody can read those. Every question worth asking — which address is failing most, when did
the error rate spike, did this user do anything unusual — requires the lines to become records
with named fields first.

Without parsing you are stuck with `grep`, which answers "does this string appear" and nothing
else. You cannot ask "how many" or "when" or "grouped by what" until the text has structure.

Everything downstream depends on this step: dashboards, alerts, detection rules, billing.
And it is where pipelines break most often, because logs are written by people who were not
thinking about you.

## The mental model

Parsing is a funnel with a hole in it. Lines go in; structured records come out; some lines
do not fit and fall through. **The hole is the important part.** A parser that silently drops
what it cannot understand will happily report zero errors during an outage, because the outage
changed the log format.

So a parser has two outputs, not one: the records, and the rejects. Both get counted.

## Minimal example

```python
from dataclasses import dataclass

@dataclass
class Entry:
    timestamp: str
    level: str
    service: str
    message: str

def parse(line: str) -> Entry | None:
    parts = line.rstrip("\n").split(" ", 3)
    if len(parts) != 4:
        return None
    ts, level, service, message = parts
    return Entry(ts, level, service, message)
```

`None` means "did not fit" — not "no error". The caller decides what to do about it,
and the caller must count them.

## Counter-example

The version almost everyone writes first:

```python
def parse(line):
    ts, level, service, message = line.split(" ", 3)   # crashes on a malformed line
    return {"timestamp": ts, "level": level, "service": service, "message": message}
```

Two bugs, both invisible in testing:

1. It raises on any line that does not have exactly four parts. One malformed line
   ends the job — and logs contain stack traces, blank lines and truncated final writes
   as a matter of routine.
2. Wrapping it in a bare `try/except: pass` to "fix" that is worse, because the failure
   becomes silent. You now have a parser that reports success while discarding data.

The distinction between *crashing loudly* and *failing silently* matters more than either.
The correct third option is: keep going, and count what you skipped.

## Exercises

Stubs in `exercises/`, tests in `tests/`. Run with `make test m=001`.

| # | Exercise | What it forces |
|---|---|---|
| 1 | `parse_line` | Returning a failure instead of raising |
| 2 | `parse_lines` | Separating good records from rejects, counting both |
| 3 | `count_by_level` | Aggregating structured records |
| 4 | `top_sources` | Ordering with ties broken deterministically |
| 5 | `stream_parse` | Processing a file larger than memory with a generator |

## Failure modes

1. **Silent drops.** Malformed lines swallowed by a bare `except`, so a format change
   looks like a quiet period rather than a broken parser.
2. **Format drift.** The application adds a field; positional splitting shifts every
   subsequent field by one; the data is now wrong but not obviously wrong.
3. **Encoding.** A single invalid UTF-8 byte, often from a truncated write, kills a job
   that reads the whole file at once. `errors="replace"` and a counter is the usual answer.
4. **Memory.** `open(f).readlines()` on a 40GB file. Generators exist for this.
5. **Multi-line records.** Stack traces span many lines; a line-oriented parser turns one
   event into thirty and your error counts become fiction.

## How you would measure it

Emit three counters and treat them as first-class output:

- `lines_read`
- `records_parsed`
- `lines_rejected`, with a sample of the rejects

Then assert `lines_read == records_parsed + lines_rejected` in a test. A rejection *rate*
that moves is the earliest signal that an upstream format changed, and it is the single
most useful alert on any ingestion pipeline. Throughput in lines/second on a known file
gives you the second number worth having.

## Non-claims

This module does not prove I can parse real-world logs at scale. It handles one fixed
format with whitespace separation. It does not cover multi-line records, structured
JSON logs, timestamp normalisation across timezones, or any log shipper. Those are
separate modules.

## Sources

- Python `re` and `dataclasses` documentation
- My own reading of nginx and sshd log formats
