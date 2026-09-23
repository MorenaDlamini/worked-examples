# Stage 06 — Log offsets

**Phase 1 — Python and the machine underneath** · builds `Python`

## The goal

Turn the log into a partitioned append-only log with consumer offsets.

## Done means

Two consumer groups read independently, and a restart resumes from the stored offset.

## Not this stage

No network. In-process.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
