# Stage 05 — Detect a spike

**Phase 0 — Shell, Linux and git** · builds `logkit`

## The goal

Flag any time window where the error rate exceeds a threshold.

## Done means

The planted spike in the fixture is found, and a quiet file produces no output and exit 0.

## Not this stage

No statistics beyond a rate and a threshold.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
