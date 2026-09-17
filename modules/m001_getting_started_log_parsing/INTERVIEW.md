# Spoken answers — Log Parsing

## 20 seconds

> Log parsing turns human-readable lines into structured records so you can aggregate them.
> The part people get wrong is error handling: a parser needs to emit both records and
> rejects, and count the rejects, because a silent drop makes a format change look like
> a quiet period instead of a broken pipeline.

## 90 seconds

> Logs are written for humans, so before you can ask any quantitative question you have to
> give the lines structure. The naive version splits on whitespace and unpacks into fields,
> which raises on anything malformed — and real logs always contain malformed lines, from
> truncated final writes to stack traces. So people wrap it in a try/except, and now the
> parser fails silently, which is worse.
>
> The design I use has two outputs: parsed records and rejected lines, with counters for
> both, and an invariant that lines read equals records parsed plus lines rejected. That
> invariant is testable, and the rejection rate is the single most useful alert on an
> ingestion pipeline — it is the earliest warning that an upstream service changed its
> format.
>
> The trade-off is that positional parsing is fast but fragile to field insertion, while
> regex or key-value parsing is more robust and slower. At low volume I would take the
> robust one; at high volume I would measure before deciding, and I have not yet.

## Likely follow-up

**Q:** How would you handle multi-line stack traces?
**A:** Line-oriented parsing turns one event into many, so error counts become wrong. The
usual approach is a continuation heuristic — a line that does not start with a timestamp
belongs to the previous record — which is a heuristic and will sometimes be wrong. If I
controlled the producer I would emit structured JSON instead and delete the problem.

## What I would say if I did not know

> I have not worked with a log shipper in production, so I would not want to guess at how
> Fluent Bit or Vector handle back-pressure specifically. What I would check first is
> whether it buffers to disk or memory when the destination is unavailable, because that
> determines what you lose in an outage.
