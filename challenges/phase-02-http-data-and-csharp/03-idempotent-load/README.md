# Stage 03 — Idempotent load

**Phase 2 — HTTP, data and the first slice** · builds `product backend`

## The goal

Make a load safe to run twice.

## Done means

The same idempotency key posted twice produces one effect and the same response body.

## Not this stage

No distributed locking. A key and a constraint.

## Before I start

- [ ] The previous stage is green on CI, not just locally
- [ ] I can say in one sentence what this stage teaches that the last one did not

## After it is green

- [ ] A line in the phase's `NOTES.md` on what surprised me
- [ ] A decision record, if I made a real choice
