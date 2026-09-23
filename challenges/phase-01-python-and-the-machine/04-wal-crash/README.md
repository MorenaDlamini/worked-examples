# Stage 04 — Wal crash

**Phase 1 — Python and the machine underneath** · builds `Python`

## The goal

Survive a kill mid-write, losing at most the partial record.

## Done means

A test that kills the process during a write and reopens cleanly, run a hundred times without a false pass.

## Not this stage

Do not catch the signal. Survive it.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
