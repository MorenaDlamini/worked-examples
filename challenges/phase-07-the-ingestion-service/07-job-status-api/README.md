# Stage 07 — Job status api

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Expose ingestion state over FastAPI.

## Done means

Lag, last offset, dead-letter count, and a job's progress, all from a running service.

## Not this stage

No dashboard. The API the dashboard would call.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
