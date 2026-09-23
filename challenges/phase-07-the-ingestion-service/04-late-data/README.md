# Stage 04 — Late data

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Handle an event that arrives after its window closed.

## Done means

A watermark policy, a test with a late event, and a written note on what is dropped.

## Not this stage

Dropping late data silently is the failure mode.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
