# Stage 03 — Reject malformed

**Phase 0 — Shell, Linux and git** · builds `logkit`

## The goal

Send bad lines to a reject stream instead of crashing, and report how many.

## Done means

Exit 2 when any line was rejected, the count on stderr, and every good record still on stdout.

## Not this stage

Do not try to repair a bad line. Rejecting is the feature.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
