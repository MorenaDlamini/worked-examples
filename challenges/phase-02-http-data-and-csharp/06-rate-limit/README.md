# Stage 06 — Rate limit

**Phase 2 — HTTP, data and the first slice** · builds `product backend`

## The goal

Implement a rate limit, not just obey one.

## Done means

429 with Retry-After under load, and a test that a well-behaved client never sees one.

## Not this stage

No distributed counter. One instance.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
