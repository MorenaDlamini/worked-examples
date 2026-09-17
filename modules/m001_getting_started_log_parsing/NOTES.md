# Working notes — Log Parsing

## Current understanding

Parsing produces two streams — records and rejects — and a parser that produces only one
is broken regardless of how well it works on good input.

## What confused me, and the correction

- **I thought:** a parser should raise on bad input so you find out immediately.
- **Actually:** in a batch over millions of lines, raising means one bad line destroys the
  whole run. You want per-line failure with a counter, and an alert on the *rate*.
- **Why I got it wrong:** I was thinking about a function called once, not a function called
  ten million times. The right error strategy depends on the call pattern, which is a more
  general lesson than this module.

- **I thought:** `split()` with no arguments is fine.
- **Actually:** it collapses runs of whitespace and splits on tabs too, which silently
  repairs some malformed lines and silently mangles others. `split(" ", 3)` is explicit
  about both the separator and the field count.

## Open questions

- At what volume does regex parsing become the bottleneck rather than I/O? Worth measuring
  in a later benchmarking module.
- How do real shippers handle multi-line records — is it always a heuristic?

## Revisited

- 2026-09-17 — first pass
