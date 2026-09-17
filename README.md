# learn-in-public

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
horizon/           quarterly review: what is changing in data and security
templates/         module scaffold
tools/             new_module.py, status.py
.local/            private, gitignored: weak attempts, half-formed thinking
```

## Commands

```bash
make new t=hands-on topic=window-functions   # scaffold a module
make test                                    # run every module's tests
make test m=012                              # run one module
make status                                  # regenerate the progress table below
```

## Progress

<!-- STATUS:START -->
| Module | Tier | Topic | State |
|---|---|---|---|
| `m001_getting_started_log_parsing` | getting-started | log parsing | done |
<!-- STATUS:END -->

## Standards

See `CONTRIBUTING.md` for the bar every module must clear, `AI_USAGE.md` for the rules I
hold myself to when using an assistant, and `NON-CLAIMS.md` for what this repository does
not prove.
