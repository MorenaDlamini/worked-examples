# Curriculum

A day-to-day plan from where I am now — a beginner — to the point where I can do, and prove
I can do, the work in three specific OpenAI postings. Evidence rather than claims.

Written 2026-09-17. Reassess at every phase gate and in every `horizon/` entry.
This file is allowed to be wrong. It is not allowed to be vague.

**No dates, no week counts, no estimated finish.** A phase is over when its exit test passes,
and not before. How long that takes is an output of the work, not an input to it. Anyone who
tells me the number — including me on a confident day — is guessing.

## The target

These three, and this file exists to reach them:

| Role | Stated bar |
|---|---|
| Software Engineer, Data Infrastructure (SF) | 4+ years |
| Full-Stack Software Engineer, API Experience (NYC) | 5+ years, explicitly excluding internships |
| Full-Stack Software Engineer, Cybersecurity Products (SF) | shipping production full-stack products |

They are senior. That is a statement about what has to be built, not about whether to aim
here. The bars are years of *production* experience, so the plan has to produce production
experience — that is what Phase 7 is for, and it is the reason it is a phase rather than a
footnote. No repository, however good, substitutes for it. Pretending otherwise would be the
exact failure mode `NON-CLAIMS.md` exists to prevent.

The stack the curriculum teaches — Python, JavaScript / TypeScript, React, Postgres — is the
stack these three postings and their nearer siblings name. That is not a coincidence; I chose
it after reading the postings.

## What all three roles have in common

This is the list worth optimising against, because it is stable across all three and it is
mostly *not* about languages. Only one of the three postings names a language at all.

- Production experience, not project experience
- Designing and operating APIs and services
- Reliability as an owned responsibility, including on-call
- Data modelling and storage
- Reasoning about distributed and asynchronous systems
- Working with ambiguity and rapid change — all three say this in near-identical words
- Clear written and spoken communication
- Security and correctness judgment

Notably absent: **ML or AI expertise is not required by any of them.** Two explicitly waive
it. I should stop treating "learn AI" as the path into an AI company.

## The shape: two repositories

`NON-CLAIMS.md` already says production proof belongs in a separate build repository, so:

- **`learn-in-public`** (this repo) — understanding. Modules, tiers, exercises, tests,
  interview answers. Unchanged.
- **`minicloud`** (new repo) — proof. One system, built slowly, operated badly at first and
  then better. Rename it to whatever I like; the name matters less than it being *one*
  system rather than twelve abandoned ones.

The two are linked: every non-trivial thing `minicloud` needs, I first learn as a module here.

## The spine project

**`minicloud` is a local emulator of a small cloud**, in the shape of floci — the thing I
read first — but in my own stack and at a size one person can actually hold in their head.

Three services, added in this order:

1. **An object store** with an HTTP API. Buckets, keys, PUT/GET/DELETE/LIST, ranged reads,
   content hashing, durability on crash.
2. **A stream** — append-only, partitioned, with offsets and consumer groups. The thing that
   teaches ordering, replay, at-least-once delivery and late data.
3. **An auth layer** — request signing, and a policy engine that decides whether a signed
   request is allowed to do what it asked.

Plus **a web console** in TypeScript and React, and **a CLI**.

### Why this project and not another

It is the only single artifact I could find that produces honest evidence for all three
target roles at once:

| Role | What `minicloud` forces me to actually do |
|---|---|
| Data Infrastructure | Storage engines, durability, partitioning, offsets, compaction, benchmarks, the cost of a bad data model |
| API Experience | HTTP semantics, error design, idempotency, pagination, rate limits, versioning, an SDK someone else could use |
| Cybersecurity Products | Request signing, policy evaluation, authorisation bugs, audit logging, and building the detections that catch abuse of my own system |

It also fails usefully. An emulator has an oracle — the real service it emulates — so
"is my behaviour correct" has an answer that is not my opinion. That is rare in learning
projects and it is the reason this shape was worth borrowing.

### The rule that keeps it honest

**Thin vertical slices, always.** The first version of the object store is PUT and GET for
one bucket, in memory, with no auth, and it ships. Then it gets a disk. Then it gets crash
safety. A slice is finished when it has a test, a README paragraph, and a note on what it
still gets wrong. Never build a layer I cannot yet demonstrate end to end.

## The daily loop

About an hour and three-quarters. Designed to survive a bad day, because most days are
ordinary and the plan has to work on those.

| Minutes | What | Why |
|---|---|---|
| 25 | **Cold retrieval.** Open one old `INTERVIEW.md` question. Answer aloud before reading anything. | This is the only part that fights forgetting. It is also the part I will want to skip. |
| 50 | **Build.** One exercise, or one thin slice of `minicloud`. Test first, always. | The struggle is the mechanism. |
| 20 | **Write.** Update `NOTES.md`, or the module README, in my own words. | Writing is where I find out I did not understand it. |
| 10 | **Commit and push.** One decision logged if I made one. | Green CI, or it did not happen. |

If a day collapses, the 25 minutes of retrieval is the part to keep. Missing a build day
costs a day. Missing retrieval repeatedly costs the module.

## The weekly loop

- **One module finished** to the `CONTRIBUTING.md` standard. Not two, and not a half.
- **One decision record** in `decisions/`, on a real choice I made that week.
- **One work scenario** from `scenarios/` — see below.
- **Friday reproduce-from-scratch check**, per `AI_USAGE.md`. Blank file, no assistant.
- **Every other week: an incident.** Also below.

## Phases

Ordered, not scheduled. Each one is finished when its exit test passes — cold, honestly, and
on a day I did not cherry-pick. Moving on early is the failure mode this table exists to
prevent, and it is the only way the plan can actually fail.

### Phase 0 — Shell, git, and a green badge

The repo already supports this via `tools/shelltest.py` and the note in `CONTRIBUTING.md`.

| Modules | Exit test |
|---|---|
| Shell navigation and pipes; grep, sed, cut on real log files; git branching and history; GitHub, remotes and CI | This repo is on GitHub, CI is green on a push I made, and I can explain what the workflow file does line by line |

**Blocker to clear first:** this repo currently has no git remote and its CI has therefore
never run. The badge premise is unproven until it does.

### Phase 1 — Python that holds up

| Modules | Exit test |
|---|---|
| Types and data structures; functions and scope; files and encodings; exceptions and what to do with them; classes and when not to use them; modules and packaging; `pytest` properly; type hints; iterators and generators; `dataclasses`; the standard library worth knowing | Reproduce three `hands-on` module solutions from blank files, cold, in one sitting |

`m001` already covers log parsing. It is the right first module and it stays.

### Phase 2 — HTTP, data, and the first slice

Where `minicloud` starts.

| Modules | `minicloud` slice | Exit test |
|---|---|---|
| HTTP semantics; REST and its arguments; JSON and schemas; FastAPI; SQL; Postgres; indexes; transactions; data modelling | Object store: in-memory, then on disk. PUT, GET, DELETE, LIST. Ranged reads. A CLI that talks to it. | Someone else can install it from my README and store a file, without asking me anything |

### Phase 3 — The full-stack half

| Modules | `minicloud` slice | Exit test |
|---|---|---|
| JavaScript fundamentals; TypeScript; the type system as a design tool; React; state; data fetching; forms and validation; build tooling; end-to-end testing | The console: browse buckets, upload, view objects, see errors honestly | The console surfaces a server error in a way a stranger could act on |

This phase is what makes "full-stack" — the word in two of the three postings — a claim I can
defend rather than a line on a CV.

### Phase 4 — Data infrastructure depth

| Modules | `minicloud` slice | Exit test |
|---|---|---|
| Append-only logs; partitioning; offsets and consumer groups; delivery semantics; watermarks and late data; serialisation formats; columnar storage and Parquet; DuckDB; "does this need distribution"; benchmarking honestly | The stream service, with replay. A benchmark harness. A written analysis of where it falls over. | A benchmark I would defend to someone who disagreed with it, including its limitations |

The "does this need distribution" module is already in the `horizon/` queue. It belongs here.

### Phase 5 — Security depth

| Modules | `minicloud` slice | Exit test |
|---|---|---|
| Authentication vs authorisation; request signing; secrets handling; the OWASP failures that actually recur; threat modelling; audit logging; detection as code; supply chain and SBOMs; prompt injection in systems that read untrusted text | The auth layer: signed requests, a policy engine, an audit log. Then a detection pipeline over that audit log, with tested rules in CI. | I find a real authorisation bug in my own policy engine by writing a test that should have existed |

This is where the two fields meet, which the `horizon/` entry already identifies as the most
defensible position available to me. It is deliberately the deepest phase.

### Phase 6 — Operate it

The phase that attacks `NON-CLAIMS.md` directly. Starts as soon as there is something worth
operating — it overlaps every phase after Phase 2, and it does not end.

- Load it until it breaks, and write down where and why
- Inject failures deliberately: full disk, killed process mid-write, clock skew, slow client
- Run it continuously and keep an uptime log
- Take a real dependency upgrade that breaks something, and fix it

### Phase 7 — Production experience, which is the actual bar

Every posting asks for years of production work. Phases 0–6 make me *capable* of it and give
me the evidence to be let near it; they cannot substitute for it, and this file will not
pretend they can. So this phase is explicit work, not waiting:

- **Get paid to write software**, at whatever level will have me, and treat that job as the
  curriculum's main campus. Production experience is something employers hand out, and the
  first one hands it out at a lower bar than these three do.
- **Own something on-call.** Reliability as an owned responsibility is on all three lists and
  is the single hardest item to get outside a job.
- **Ship to real users, with real money and real consequences behind it** — the top line of
  "what this will not prove", crossed off the only way it can be.
- **Sustained contribution to code I did not write.** Begins once Phase 3's exit test passes;
  before that I cannot read a stranger's codebase fast enough for it to be contribution
  rather than charity. Not floci itself — 4,430 Java files, PRs past #3800, and exactly one
  open good-first-issue that already has a PR on it. Its sibling `testcontainers-floci` is
  57 stars with the same maintainers, which is a room where a newcomer is visible rather than
  noise. Any small, active, well-tested project with a real CONTRIBUTING file will do.
- **Depth over breadth, in public.** These postings reward someone who has gone unreasonably
  deep into storage, APIs or security — not someone who has touched all three lightly.
  Phases 4 and 5 decide which one; this phase lives there.

The gate on this phase, and on the curriculum, is the application itself: I meet the stated
bar of one of the three postings, in years and in kind, and the evidence is public.

## Practices that mimic actual work

Modules teach technique. These teach the parts of the job that are not technique, and they
are the reason a portfolio of exercises usually fails to convert into an offer.

### Decision records — `decisions/`

One file per real decision. The format is deliberately short, and the last line is the one
that matters:

```
# NNN — <the decision>
Date, status.
## Context      what was true that forced a choice
## Options      at least two, each stated fairly enough that a proponent would recognise it
## Decision     what I chose
## Consequences what this now costs me, including the bad parts
## What would change my mind
```

Writing the options fairly is the skill. A decision record where one option is a straw man
is a record of a rationalisation, not a decision.

### Work scenarios — `scenarios/`

A weekly ticket written the way tickets actually arrive: ambiguous, from a stakeholder with
a goal rather than a spec, sometimes wrong about the cause.

> "Uploads are slow for the Johannesburg office. Can you look at it this week?"

The exercise is not to fix it. It is to write down: what I would ask before starting, what
I would measure first, what I think the three plausible causes are, and which one I would
rule out most cheaply. Then do that. Then record where my guess was wrong.

Ambiguity tolerance is named in all three postings. This is how it gets practised.

### Incidents — every other week

I break `minicloud` on purpose — or better, have someone else break it — and then diagnose
it under a clock without reading the commit that did it. Afterwards, a postmortem: timeline,
what I believed at each step and why it was wrong, the actual cause, and the test that would
have caught it.

Blameless postmortems are a genuine professional skill and almost nobody arrives with one.

### Code review — monthly

Open a pull request against my own repo and review it a week later as a stranger would,
against `CONTRIBUTING.md`. Then get a human to review one. Review given and received is on
the `NON-CLAIMS.md` list and this is the cheapest way to start crossing it off.

## What this curriculum still will not prove

Kept here for the same reason `NON-CLAIMS.md` is kept at top level. Phases 0–6 close none of
these; Phase 7 is the only thing that touches them, which is why it is on the page.

- Working under real users, real money, and real consequences
- Scale that any employer would call scale
- Sustained collaboration inside a team with competing priorities
- That I am employable. It proves I can learn and ship, which is necessary and not sufficient

## When to reassess

- **At every phase gate.** Did the exit test pass, honestly, or did I talk myself past it?
- **Every `horizon/` entry.** Re-read the three postings. Have the requirements moved? Roles
  get reposted, retitled and reworded; the versions in `research/` are snapshots and will go
  stale. Track what the current ones ask for.
- **If an exit test fails three attempts running.** That is information about the plan, not
  about me. Cut the scope of the phase rather than the standard of the test; a narrower
  phase finished beats a broader one abandoned.
- **Never by elapsed time.** Slow is a reason to look at the daily loop, not to move a gate.

## Sources

- `research/2026-09-17-openai-target-roles.md` — the three postings and OpenAI's own
  interview guide, with URLs
- `research/2026-09-17-floci-local-build.md` — what floci is, and why it is a better model
  than a target
