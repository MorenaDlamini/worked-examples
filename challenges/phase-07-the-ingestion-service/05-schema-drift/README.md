# Stage 05 — Schema drift

**Phase 7 — Data infrastructure: the ingestion service** · builds `platform`

## The goal

Survive the source adding and removing a column.

## Done means

The pipeline neither fails silently nor loses the new column. It alerts and continues.

## Not this stage

A blank downstream report is the bug to prevent.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
