# worked-examples

[![modules](https://github.com/MorenaDlamini/worked-examples/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/MorenaDlamini/worked-examples/actions/workflows/ci.yml)

A self-verifying learning repository. Every topic I study becomes a **module**: a written
lesson, a set of failing tests, my solutions, and an honest note about what I still cannot do.

CI runs every module's tests on every push. A module is not finished because I say so.
It is finished when the tests pass and the checklist in `CONTRIBUTING.md` is met.

## Why this exists

Notes decay. Tutorials are forgotten within a fortnight. What survives is material you
had to *produce* rather than consume — so this repository is structured around authoring
the lesson I wish I had found, for each thing I learn.

Two side effects, both deliberate:

- **Retrieval.** Writing exercises for a topic forces the kind of retrieval practice that
  actually moves knowledge into long-term memory. Reading does not.
- **Evidence.** The output is a public artifact that shows understanding, not just activity.
  A green CI badge over sixty modules is a different claim from a green commit graph.

## Tiers

Borrowed from how good course catalogues stage material, renamed for honesty about what
each level actually proves.

| Tier | Question it answers | Proof required |
|---|---|---|
| `getting-started` | Can I use this at all? | 3+ exercises passing |
| `hands-on` | Can I do it under pressure, without notes? | 6+ exercises, one timed |
| `deep-dive` | Do I know how it works underneath? | An implementation from scratch, or a benchmark |
| `build-it` | Can I ship one end to end? | A working thing with a README and failure handling |

A topic can have several modules at rising tiers. `deep-dive` is where most of the value is,
and where almost everybody stops short.

## Layout

```
modules/NNN-tier-topic/
  README.md        the lesson, written by me, for someone who does not know this yet
  NOTES.md         my working understanding, updated over time
  INTERVIEW.md     20-second and 90-second spoken answers
  exercises/       stubs that fail
  solutions/       my solutions
  tests/           pytest that verifies both
challenges/        the build ladders: one per phase, gated stage by stage
decisions/         one record per real decision, written at the time
designs/           one page before any service starts
scenarios/         ambiguous tickets, practised the way they actually arrive
horizon/           quarterly review: what is changing in data and security
research/          the postings and the evidence the curriculum answers to
templates/         module scaffold
tools/             new_module.py, status.py, challenges.py
.local/            private, gitignored: weak attempts, half-formed thinking
```

## Commands

```bash
make new t=hands-on topic=window-functions   # scaffold a module
make test                                    # run every module's tests
make test m=012                              # run one module
make status                                  # regenerate the progress table below
make challenge p=0 s=01                      # run one challenge stage
make challenges                              # run every started stage
make ladder                                  # regenerate the ladder table
```

## Progress

<!-- STATUS:START -->
| Module | Tier | Topic | State |
|---|---|---|---|
| `m001_getting_started_log_parsing` | getting-started | log parsing | done |
<!-- STATUS:END -->

## Challenges

Modules teach a topic. `challenges/` builds each phase's project in numbered stages, each gated
by an acceptance test, in the shape CodeCrafters uses. A stage is done when its test passes on
a push, so finishing one always leaves a commit behind. Stages nobody has started are skipped
rather than failed, which is why the badge above still means something.

Acceptance tests are Python and black-box wherever the thing being built is not: shell stages
are graded through `tools/shelltest.py`, and services are graded over HTTP against a running
container. See `challenges/README.md` for the rules and the current ladder.

## Standards

See `CONTRIBUTING.md` for the bar every module must clear, `AI_USAGE.md` for the rules I
hold myself to when using an assistant, and `NON-CLAIMS.md` for what this repository does
not prove.
