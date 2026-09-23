# Stage 03 — Wal append

**Phase 1 — Python and the machine underneath** · builds `Python`

## The goal

Build an append-only write-ahead log that survives reopening.

## Done means

Records written then reopened read back identically, verified by a checksum per record.

## Not this stage

No indexes, no compaction, no deletes.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
