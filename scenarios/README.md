# Work scenarios

A weekly exercise in the part of the job that is not typing.

## Why these exist

Exercises arrive as a specification with a known answer. Work does not. Work arrives as a
sentence from someone who wants an outcome, is not sure what is wrong, and is sometimes
confidently wrong about the cause. All three target roles name ambiguity explicitly — "thrive
in ambiguity", "rapidly changing environment" — and no amount of passing tests practises it.

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

Written against `minicloud`. Add more as the system grows; the best ones come from things
that actually surprised me.

**001 — "Uploads are slow for the Johannesburg office."**
No numbers, no timeframe, one complainant. Slow compared with what?

**002 — "Can we get a report of everything user X did last month?"**
Asked by someone who does not know whether the audit log retains that long, or whether it
records enough to answer the question. It probably does not.

**003 — "The nightly job finished in four minutes yesterday and forty this morning."**
Nothing was deployed. Something changed anyway.

**004 — "A customer says they uploaded a file and it is not there."**
Exactly one report. The logs show a 200. Both of those facts can be true at once.

**005 — "Security wants us to log every request. Can you add that by Friday?"**
A reasonable request with an unreasonable second-order cost. The exercise is the conversation,
not the logging.

**006 — "Can you make the console show which files changed recently?"**
The data model does not record modification time. The feature is an afternoon; the migration
is not.
