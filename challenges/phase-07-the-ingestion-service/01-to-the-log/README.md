# Stage 01 — To the log

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Publish changes into the broker with a partition key that makes sense.

## Done means

Ordering holds per key under concurrent writes, proven by a test.

## Not this stage

One topic. Partition count is a later problem.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
