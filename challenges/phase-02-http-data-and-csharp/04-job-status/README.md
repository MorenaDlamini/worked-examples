# Stage 04 — Job status

**Phase 2 — HTTP, data and the first slice** · builds `product backend`

## The goal

Turn a slow load into a job with a status endpoint.

## Done means

202 with a job URL, progress while running, a terminal state, and the job survives a restart.

## Not this stage

No websockets. Polling is correct here.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
