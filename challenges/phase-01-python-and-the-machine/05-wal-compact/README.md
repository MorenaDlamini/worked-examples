# Stage 05 — Wal compact

**Phase 1 — Python and the machine underneath** · builds `Python`

## The goal

Compact the log without losing a committed record.

## Done means

Compaction under concurrent reads, with a test proving no committed key disappeared.

## Not this stage

Single-writer is fine. No transactions.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
