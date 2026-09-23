# Stage 04 — Event source one aggregate

**Phase 4 — Design patterns and architecture** · builds `refactor`

## The goal

Make one aggregate's audit trail derivable rather than written twice.

## Done means

State rebuilds from events, and the old audit table is provably redundant.

## Not this stage

One aggregate. Event sourcing everything is the trap.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
