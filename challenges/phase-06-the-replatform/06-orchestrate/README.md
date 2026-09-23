# Stage 06 — Orchestrate

**Phase 6 — Data engineering: the replatform** · builds `platform`

## The goal

Put the pipeline under Airflow with real failure handling.

## Done means

A mid-pipeline failure leaves no partial gold, and a rerun is safe.

## Not this stage

No retries-as-a-strategy. Idempotence first.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
