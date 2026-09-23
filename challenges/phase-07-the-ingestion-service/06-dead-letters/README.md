# Stage 06 — Dead letters

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Give unprocessable messages somewhere to go and a way back.

## Done means

A poisoned message is quarantined with its reason, and can be replayed after a fix.

## Not this stage

Never drop. Never block the partition.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
