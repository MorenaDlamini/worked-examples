# Stage 01 — Records and rejects

**Phase 1 — Python and the machine underneath** · builds `Python`

## The goal

Return two streams from the parser, records and rejects, never raising on bad input.

## Done means

Ten million lines with one bad line in the middle completes, and the reject is counted not fatal.

## Not this stage

No logging framework. Return values.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
