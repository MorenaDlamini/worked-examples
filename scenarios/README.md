# Work scenarios

A weekly exercise in the part of the job that is not typing.

## Why these exist

Exercises arrive as a specification with a known answer. Work does not. Work arrives as a
sentence from someone who wants an outcome, is not sure what is wrong, and is sometimes
confidently wrong about the cause. Every target role names ambiguity explicitly — "loosely
defined problems", "rapidly changing environment", "own the outcome, not just the code" — and
no amount of passing tests practises it.

## The method

For each scenario, before writing any code, write `NNN-response.md`:

1. **What I would ask first**, and who I would ask. Usually two or three questions. If my
   first move is to open an editor, I have already lost the exercise.
2. **What I would measure**, and how I would know the measurement is trustworthy.
3. **Three plausible causes**, ranked by likelihood, each with the cheapest observation that
   would rule it out.
4. **What I would do this week** versus what I would put in the backlog, and what I would
   tell the person who asked.

Then do it. Then add:

5. **What actually happened**, and where my ranking was wrong.

Step five is the whole exercise. A scenario where my first guess was right taught me nothing.

## Rules

- No scenario is solved by adding code in the first hour.
- Some scenarios have no bug. The correct answer to a few of these is "the system is behaving
  correctly and the expectation is wrong" — and saying so, tactfully, in writing.
- Some scenarios are not worth fixing. Saying "I would not do this, and here is what I would
  do instead" is a valid answer and a senior one.

## Starter scenarios

Written against `product` and `platform`. Add more as the systems grow; the best ones come
from things that actually surprised me.

**001 — "The site is slow for the Johannesburg office."**
No numbers, no timeframe, one complainant. Slow compared with what?

**002 — "Can we get a report of everything user X did last month?"**
Asked by someone who does not know whether the audit log retains that long, or whether it
records enough to answer the question. It probably does not.

**003 — "The nightly job finished in four minutes yesterday and forty this morning."**
Nothing was deployed. Something changed anyway.

**004 — "A user says they saved a view and it is not there."**
Exactly one report. The logs show a 200. Both of those facts can be true at once.

**005 — "Security wants us to log every request. Can you add that by Friday?"**
A reasonable request with an unreasonable second-order cost. The exercise is the conversation,
not the logging.

**006 — "Can the explorer show which figures Treasury has restated?"**
The data model does not record versions. The feature is an afternoon; the migration is not.

**007 — "Finance says the gold total is R40k off from the source."**
Gold, the source, and the site disagree with each other. At least one of them is right. The
parity report says everything passed.

**008 — "The nightly Spark job costs three times what it did last month."**
Same code, same schedule, same data volume as far as anyone knows. The bill disagrees.

**009 — "The source added a column and nobody told us."**
Discovered because a downstream report went blank. The pipeline did not fail. That is the
problem.
