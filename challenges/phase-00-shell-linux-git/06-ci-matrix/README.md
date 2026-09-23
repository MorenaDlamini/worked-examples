# Stage 06 — Ci matrix

**Phase 0 — Shell, Linux and git** · builds `logkit`

## The goal

Make the workflow run the suite on two runners, with dependency caching.

## Done means

Both matrix legs are green on a real push, and the second run is measurably faster than the first.

## Not this stage

No deployment. Tests and caching only.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
