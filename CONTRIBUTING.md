# The module standard

A module is finished when every box is ticked. Not before. The point of writing this down
is that in six months I will want to cut corners, and this file will be here.

## Required

- [ ] **One-sentence definition** at the top of `README.md`, written without jargon.
- [ ] **The problem it solves**, stated before the mechanism. If I cannot say what goes
      wrong without this thing, I do not understand it yet.
- [ ] **A minimal example** that runs.
- [ ] **A counter-example** — the thing people get wrong, and why it is wrong.
- [ ] **Exercises** meeting the tier's minimum, each with a failing test.
- [ ] **My solutions**, passing.
- [ ] **Failure modes**: at least three ways this breaks in production.
- [ ] **How you would measure it** — a test, a benchmark, a metric. If there is no way to
      tell whether it is working, I have learned a vibe, not a technique.
- [ ] **INTERVIEW.md**: a 20-second answer and a 90-second answer, written out.
- [ ] **Non-claims**: what this module does *not* prove I can do.
- [ ] **Sources**, with links. Credit what taught me.
- [ ] CI green.

## Forbidden

- Pasted documentation. If a paragraph could have been copied, rewrite it or cut it.
- An exercise whose test does not actually distinguish a correct answer from a wrong one.
- A solution I could not reproduce tomorrow on a blank file.
- "Non-claims: none." There are always non-claims.

## The real test

Two weeks after finishing a module, open only its `INTERVIEW.md` question and answer out
loud before reading anything. If the answer is not there, the module gets reopened rather
than a new one started. Coverage is worthless without retention.
