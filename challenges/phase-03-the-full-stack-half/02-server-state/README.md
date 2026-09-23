# Stage 02 — Server state

**Phase 3 — The full-stack half** · builds `explorer`

## The goal

Move fetching to TanStack Query and stop duplicating requests.

## Done means

Two components asking for the same data produce one network call, and stale data refetches.

## Not this stage

No global store for server data. That is the point.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
