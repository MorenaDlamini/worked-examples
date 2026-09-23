# Stage 04 — Stream not buffer

**Phase 0 — Shell, Linux and git** · builds `logkit`

## The goal

Process a file larger than available memory without loading it.

## Done means

A generated file of at least 2 GB completes, and peak resident memory stays under 50 MB.

## Not this stage

No memory-mapping tricks. A pipeline that streams.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
