# Challenges

Courses are watched and forgotten. This directory is where what I learned turns into something
that either passes or does not, in public, on a machine that is not mine.

Modelled on CodeCrafters: one build per phase, broken into numbered stages, each gated by an
acceptance test. `modules/` teaches a topic. `challenges/` builds the phase's project one
provable step at a time.

## The rules

- **Stages are sequential.** Stage N+1 does not start until stage N is green.
- **Green means green on CI.** A stage is done when its acceptance test passes on a push, which
  means a commit on GitHub. Locally green does not count, because locally green is where the
  environment lies to you.
- **Each stage says what it does not ask for.** Scope creep is the most common way a ladder
  stalls, so every spec names the thing to leave alone.
- **The spec and the test may be assistant-written. The solution may not.** This is
  `AI_USAGE.md` applied here: generating exercises and the tests that check them is allowed,
  and generating the answer is not.
- **Cold re-run.** A stage green for two weeks gets rebuilt once from an empty directory. If it
  cannot be, it goes back to red and the module behind it gets reopened.

## How the tests work

Acceptance tests are Python, and black-box wherever the thing being built is not Python. That
keeps .NET and Node out of CI and makes the tests contracts rather than unit tests of my own
shapes, which is how CodeCrafters grades too.

| Phase | How it is graded |
|---|---|
| 0 | `tools/shelltest.py`, asserting on exit codes and output |
| 1 | pytest, directly against the package |
| 2 and later | pytest over HTTP against the running service, started by compose |

Tests from Phase 2 onward carry the `acceptance` marker and skip unless `CHALLENGE_BASE_URL` is
set, so CI stays green before a service exists. The skip is visible in the run; a silently
absent test is worse than a red one.

```bash
make challenge p=0 s=01      # run one stage
make challenges              # run every stage that has a solution
python tools/challenges.py   # regenerate the table below
```

## Progress

<!-- LADDER:START -->
| Phase | Ladder | Progress | Started | Next stage |
|---|---|---|---|---|
| 00 | Shell, Linux and git | `........` | 0/8 | `00-parse-one-line` |
| 01 | Python and the machine underneath | `........` | 0/8 | `00-typed-cli` |
| 02 | HTTP, data and the first slice | `.........` | 0/9 | `00-hello-endpoint` |
| 03 | The full-stack half | `.......` | 0/7 | `00-render-a-municipality` |
| 04 | Design patterns and architecture | `......` | 0/6 | `00-characterisation-tests` |
| 05 | System design | `......` | 0/6 | `00-estimate-the-load` |
| 06 | Data engineering: the replatform | `.........` | 0/9 | `00-source-up` |
| 07 | Data infrastructure: the ingestion service | `........` | 0/8 | `00-cdc-on` |
| 08 | Applied AI | `........` | 0/8 | `00-structured-output` |
| 09 | Security and privacy judgment | `.......` | 0/7 | `00-oidc-login` |
| 10 | Operate it | `........` | 0/8 | `00-structured-logs` |
| 11 | Production experience | `....` | 0/4 | `00-publish-it` |

**0 of 88 stages started.**
<!-- LADDER:END -->

## Why the later ladders have specs but no tests

A test written far ahead of the learning it checks drifts, and a drifted test is worse than no
test because it looks like a gate. Phases 0 to 3 ship with runnable tests. The rest ship with
specs, and their tests get written on arrival.
