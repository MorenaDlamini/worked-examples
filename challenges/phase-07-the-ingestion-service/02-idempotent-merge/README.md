# Stage 02 — Idempotent merge

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Land changes into Delta so replaying them changes nothing.

## Done means

The same batch applied twice leaves the table identical, byte for byte.

## Not this stage

No upsert-by-hope. A merge key and a test.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
