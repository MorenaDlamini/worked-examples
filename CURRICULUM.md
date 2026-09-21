# Curriculum

The plan for doing, and proving I can do, what senior systems engineering actually requires.
Evidence rather than claims.

Written 2026-09-17. Reassess at every phase gate and in every `horizon/` entry.
This file is allowed to be wrong. It is not allowed to be vague.

**No dates, no week counts, no estimated finish.** A phase is over when its exit test passes,
and not before. How long that takes is an output of the work, not an input to it.

## Why this file exists

I ship software that people at work depend on — field-service tooling, a data pipeline
between two systems that disagree, an internal platform behind single sign-on. This file
gives that work a direction: the requirements below. It exists so that every module, every
slice of `minicloud`, and every decision record answers to one list rather than to whatever
looked interesting that week.

## The requirements

Taken from senior postings read in full — see `research/` — and reduced to what they have in
common. The list is stable across them and it is mostly *not* about languages; only one of
the postings names a language at all.

- Production experience, not project experience
- Designing and operating APIs and services
- Reliability as an owned responsibility, including on-call
- Data modelling and storage
- Reasoning about distributed and asynchronous systems
- Working with ambiguity and rapid change — every posting says this in near-identical words
- Clear written and spoken communication
- Security and correctness judgment

The first item is the bar, and the plan is built to produce it — Phase 7 exists for exactly
that. No repository substitutes for it; `NON-CLAIMS.md` says the same thing from the other
side.

Notably absent: **ML or AI expertise.** Where it is mentioned at all it is explicitly waived.
I should stop treating "learn AI" as the path into systems work.

The stack — Python, JavaScript / TypeScript, React, Postgres — is the one the postings name
most often. I chose it after reading them.

## What this file is

- The phases, in order, each with the exit test that ends it
- The spine project, and the rule that keeps it honest
- The daily and weekly loop
- The practices that mimic actual work rather than technique

## What this file is not

- A schedule
- A CV — production proof lives in separate build repositories
- A record of what I have done; `worked-examples` modules and `decisions/` are that

## What every phase has to answer

1. **Can I build it?** — the `minicloud` slice
2. **Can I explain it cold?** — the module's `INTERVIEW.md`, answered aloud before reading
3. **Do I know how it fails?** — the module's non-claims and `NOTES.md`
4. **Did it pass?** — the exit test, on a day I did not choose

A phase that answers three of the four is not finished.

## The shape: two repositories

`NON-CLAIMS.md` already says production proof belongs in a separate build repository, so:

- **`worked-examples`** (this repo) — understanding. Modules, tiers, exercises, tests,
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

It is the only single artifact I could find that exercises the whole requirements list at
once:

| Requirement | What `minicloud` forces me to actually do |
|---|---|
| Data modelling and storage | Storage engines, durability, partitioning, offsets, compaction, benchmarks, the cost of a bad data model |
| Designing and operating APIs | HTTP semantics, error design, idempotency, pagination, rate limits, versioning, an SDK someone else could use |
| Security and correctness judgment | Request signing, policy evaluation, authorisation bugs, audit logging, and building the detections that catch abuse of my own system |
| Distributed and asynchronous reasoning | Ordering, replay, delivery semantics, late data, and what a crash mid-write leaves behind |
| Reliability as an owned responsibility | Phase 6 — operating it, breaking it, and writing down what happened |

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

**Status:** the remote exists and CI ran green on a push I made, 2026-09-21. What remains
of this exit test is the last clause — explaining the workflow file line by line.

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

This phase is what makes "full-stack" a claim I can defend rather than a line on a CV.

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

The requirements list starts with years of production work. Phases 0–6 sharpen it and give
me the evidence to show for it; they cannot substitute for it, and this file will not pretend
they can. So this phase is explicit work, not waiting:

- **Treat the job as the curriculum's main campus.** The production experience I have is
  real — technicians, payroll, a company behind one login — and it is the only kind that
  counts. Pull the work toward the list on purpose: the system boundaries, the auth, the
  data that has to be right.
- **Own something on-call.** Reliability as an owned responsibility is on the list and is the
  single hardest item to get outside a job.
- **Widen the consequences.** Real users is already true. Real money and real scale behind
  the same systems is the next line of "what this will not prove", and it is crossed off the
  only way it can be.
- **Sustained contribution to code I did not write.** Begins once Phase 3's exit test passes;
  before that I cannot read a stranger's codebase fast enough for it to be contribution
  rather than charity. Not floci itself — 4,430 Java files, PRs past #3800, and exactly one
  open good-first-issue that already has a PR on it. Its sibling `testcontainers-floci` is
  57 stars with the same maintainers, which is a room where a newcomer is visible rather than
  noise. Any small, active, well-tested project with a real CONTRIBUTING file will do.
- **Depth over breadth, in public.** The requirements reward someone who has gone
  unreasonably deep into storage, APIs or security — not someone who has touched all three
  lightly. Phases 4 and 5 decide which one; this phase lives there.

The gate on this phase, and on the curriculum, is meeting the list — in years and in kind —
with the evidence public.

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

Ambiguity tolerance is on the requirements list. This is how it gets practised.

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
- **Every `horizon/` entry.** Re-read the postings the requirements came from. Has the list
  moved? Roles get reposted, retitled and reworded; the versions in `research/` are snapshots
  and will go stale. Track what current ones ask for.
- **If an exit test fails three attempts running.** That is information about the plan, not
  about me. Cut the scope of the phase rather than the standard of the test; a narrower
  phase finished beats a broader one abandoned.
- **Never by elapsed time.** Slow is a reason to look at the daily loop, not to move a gate.

## Sources

- `research/2026-09-17-openai-target-roles.md` — the postings the requirements were reduced
  from, with URLs
- `research/2026-09-17-floci-local-build.md` — what floci is, and why it is a better model
  than a target
