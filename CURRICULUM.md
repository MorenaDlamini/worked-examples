# Curriculum

The plan for becoming, and proving I am, competent across four pillars: full-stack software
engineering, data, applied AI, and security. Data is the deep one. Evidence rather than claims.

Written 2026-09-17. Rebuilt 2026-09-22 around the roles in `research/`. Reassess at every
phase gate and in every `horizon/` entry. This file is allowed to be wrong. It is not allowed
to be vague.

**No dates, no week counts, no estimated finish.** A phase is over when its exit test passes,
and not before. How long that takes is an output of the work, not an input to it.

## Why this file exists

Production work counts wherever it happens, and I have some. What it does not give me on its
own is a direction. This file is the direction: four pillars, two systems, and one list of
requirements taken from postings read in full. It exists so that every module, every slice of
the two systems, and every decision record answers to that list rather than to whatever looked
interesting that week.

## The requirements

Taken from postings read in full — see `research/` — and reduced to what they agree on. The
list is mostly about verbs: build, operate, integrate, review, explain.

1. Production experience, stated in years
2. A typed, tested backend in a language the market names — C# and ASP.NET Core, or Python
3. Designing and operating REST APIs, including auth, idempotency and job status
4. Docker, CI/CD, and a cloud; AWS and Azure are both named
5. Integrating LLM features: calling model APIs, retrieval-augmented generation, vector search
6. Using coding assistants, and critically reviewing what they produce — named in a fifth of
   South African listings and a third of remote ones, always with the review clause attached
7. Working from specs, design docs and ADRs; code review; clear communication; mentoring
8. Relational modelling on Postgres; Spark, Delta, and replatforming legacy SQL with parity
   evidence
9. Observability, and resolving incidents in production
10. Security and privacy judgment inside the product: OAuth2 and OIDC, secrets, POPIA

The first item is the bar. No repository substitutes for it; `NON-CLAIMS.md` says the same
thing from the other side, and Phase 11 exists for it.

Three things the postings made me change my mind about:

- **AI is required, not waived.** Two of three make LLM integration a must. Applied AI
  engineering — building products on model APIs — is a pillar. Model research and training are
  not.
- **Security is not a track.** None of the roles has one. It is auth protocols, secrets,
  privacy law and correctness, inside the product. That is how it is scoped here. Detection as
  code stays as an optional deep-dive at the overlap with data, which `horizon/` still argues
  for.
- **Data is the differentiator.** The one posting that pays for depth pays for Spark, Delta,
  and replatforming legacy SQL with proof that the numbers still agree.

## What the plan is standing on

Five years of production C# and ASP.NET Core. The first version of this file left that out and
planned a Python web backend instead, which was a mistake twice over: it threw away the only
production depth I have, and it ignored the market I am standing in. C# and .NET is the largest
single backend ask in South Africa — a third of listings, ahead of Java and well ahead of
Python — while Python is under a fifth locally
(`research/2026-09-23-full-stack-tooling.md`).

So the languages divide by job, and the rule is one line:

**C# and ASP.NET Core build the product. Python is for data and AI. TypeScript and React are
the front.**

That is not a compromise. It is what the evidence says a full-stack engineer in Johannesburg
who wants the data depth should actually be: a .NET product engineer whose data and AI work is
in Python, which is the only serious language for either. Python still carries Phases 1, 6, 7
and 8 — PySpark, the ingestion service, its FastAPI job-status API, and the assistant — so the
Python-backend experience the postings name gets built where it belongs rather than bolted onto
a web app.

The stack: C# and ASP.NET Core with Postgres; TypeScript and React with Vite; Python with
PySpark, Delta and FastAPI; DuckDB for judgment. Azure throughout, with AWS equivalents noted
on every cloud module because two of the three postings name it.

## Depth

Four pillars is breadth, and depth over breadth is the rule. So:

| Pillar | Tier I am aiming at | Where the proof lives |
|---|---|---|
| Data | `deep-dive` — the one to go unreasonably deep in | `platform`: replatform, parity, ingestion |
| Full-stack | `build-it` — defendable, not distinguished | `product`: the ASP.NET Core API, the React explorer, the client package |
| Applied AI | `build-it`, with evals as the deep part | the assistant inside `product`, evals gating CI |
| Security | judgment; deep only where it meets data | OIDC, policy, audit log, POPIA across both systems |

This plan is longer than the one it replaces. That is the price of the fourth pillar. If the
daily loop stops fitting, the lever is cutting a pillar, never lowering a standard.

## What this file is

- The phases, in order, each with the project it builds and the exit test that ends it
- The two systems, the tests a project has to pass to be worth building, and the rule that
  keeps them honest
- The daily and weekly loop
- The practices that mimic actual work rather than technique

## What this file is not

- A schedule
- A CV — production proof lives in the two build repositories
- A record of what I have done; `worked-examples` modules and `decisions/` are that

## What every phase has to answer

1. **Can I build it?** — the phase's project slice
2. **Can I explain it cold?** — the module's `INTERVIEW.md`, answered aloud before reading
3. **Do I know how it fails?** — the module's non-claims and `NOTES.md`
4. **Did it pass?** — the exit test, on a day I did not choose
5. **Did someone else see it?** — a stranger installed it, a peer reviewed it, or a human heard
   the answer

A phase that answers four of the five is not finished. No gate is graded only by the one
person with a motive to pass it.

## The shape: three repositories

`NON-CLAIMS.md` says production proof belongs outside a learning repo, so:

- **`worked-examples`** (this repo) — understanding. Modules, tiers, exercises, tests,
  interview answers.
- **`platform`** (working name) — data proof. A replatform, a parity tool, an ingestion
  service.
- **`product`** (working name) — full-stack, AI, security and operations proof. A public
  product with real data and real users.

Every non-trivial thing the two systems need, I first learn as a module here.

## The two systems

### What makes a project worth building

Four tests, all required:

1. **It is the work the roles do.** Not an analogy for it.
2. **Someone else could use it.** A library on PyPI, a service a team could run, a site a
   stranger visits.
3. **It forces the hard parts.** Durability, ordering, idempotency, auth, parity, evals.
4. **It has an oracle.** "Is this correct" has an answer that is not my opinion.

The first version of this plan had a local emulator of a small cloud as its spine. It passed
the third and fourth tests and failed the first two: these roles build on cloud services, not
copies of them. It is gone. The lessons it carried — durability, ordering, replay, delivery
semantics, durable jobs — moved into the ingestion service and two deep-dive modules.

### `platform` — a data platform a team could use

Three parts, added in this order:

1. **The replatform.** WideWorldImporters, Microsoft's SQL Server sample, ships an OLTP
   database, a data warehouse, and the T-SQL procedures that load it. Rebuild that ETL on
   PySpark and Delta: bronze, silver, gold; orchestrated; every layer tested; governed. The
   oracle is the shipped warehouse. Gold has to match it to the cent.
2. **`parity`.** A CLI and library that compares two SQL-queryable sources with tolerances and
   produces an evidence report fit for CI and for a reviewer who wants it to be wrong. One of
   the postings asks for "parity evidence" by name. Published to PyPI.
3. **The ingestion service.** Change data capture on the SQL Server source and polling of the
   Municipal Money API, into Redpanda (the Kafka API, in Docker), landed in Delta by idempotent
   merge. Offsets, replay, backfill versus live, late data, schema drift, dead letters, a
   job-status API. Service Bus or Event Hubs is the cloud shape. This is where the emulator's
   lessons now live, on infrastructure a data team would recognise.

### `product` — a municipal finance explorer for South Africa

National Treasury publishes every municipality's budgets, spending, and audit outcomes through
the Municipal Money API. Nobody has built a good explorer over it with an assistant. So:

- Where a municipality's money comes from and goes, audit outcomes, comparisons across years
  and peers. Public site.
- A typed client package, `MunicipalMoney.Client`, on NuGet.
- An ASP.NET Core REST API with OIDC login for saved views.
- An assistant that answers questions with citations to the rows and the budget documents it
  retrieved, with evals gating deploys.

Journalists, councillors and residents are real users. The oracle is Treasury's own published
figures.

### How they connect

Ingestion feeds both the replatform's bronze layer and the product's data. The product reads
gold. The assistant reads gold and the document corpus. Auth and audit cover all of it.
Everything is deployed and operated together. One architecture that fits on a whiteboard,
which is the interview answer.

### Storage and log internals

Two `deep-dive` modules in this repo, not products: a crash-safe key-value store with a
write-ahead log, and an append-only partitioned log with consumer offsets. From scratch,
benchmarked. They exist so that when the ingestion service misbehaves I know what the broker
is doing underneath.

### The oracle, named

| System | What "correct" means |
|---|---|
| Replatform | Gold matches the shipped WideWorldImporters warehouse to the cent |
| Ingestion | A replay from offset zero reproduces gold byte for byte |
| Product | Figures match Treasury's published ones and the API's own totals |
| Assistant | The eval set passes, with the judge's limits written down |

### The rule that keeps it honest

**Thin vertical slices, always.** The first version of the product's backend loads one
municipality's budget into Postgres and ships. Then it gets a worker. Then a job-status
endpoint. A slice is finished when it has a test, a README paragraph, and a note on what it
still gets wrong. Never build a layer I cannot yet demonstrate end to end.

**A design doc before a service.** One page in `designs/`: the API or schema, the data model,
the failure modes, and what it deliberately will not do. Two of the postings say "work from
specs, design documents and ADRs". This is how I get good at reading them.

## What ships at the end

Five things a stranger can open, ordered by how much they prove. A reader who has time for one
should be sent to the third.

| # | Project | What it proves | Ships as |
|---|---|---|---|
| 1 | `worked-examples` | Learning rate, and that the standard is enforced rather than claimed — modules, challenge ladders, green CI on every push | This repo |
| 2 | `parity` | Comparing two SQL-queryable sources and producing evidence a sceptic accepts. One posting asks for "parity evidence" by name | A PyPI package and a CLI |
| 3 | `platform` | The data depth: a shipped T-SQL warehouse replatformed to PySpark and Delta, plus a change-capture ingestion service with replay | A repo, and a runbook a stranger can follow |
| 4 | `product` | Full-stack and applied AI: an ASP.NET Core API, a React explorer, an assistant that cites its rows, OIDC, deployed and operated | A repo, a NuGet package, and a live URL |
| 5 | Reserved | A fifth, at the overlap of data and security. Decided by research, not by appetite — see `research/` | To be decided |

The fifth is deliberately empty rather than filled with something plausible. If it is not
worth building by the four tests above, `platform` splits into the replatform and the ingestion
service, which is honest because they have different oracles and different readers.

## The daily loop

About an hour and three-quarters. Designed to survive a bad day, because most days are
ordinary and the plan has to work on those.

| Minutes | What | Why |
|---|---|---|
| 25 | **Cold retrieval.** Open one old `INTERVIEW.md` question. Answer aloud before reading anything. | This is the only part that fights forgetting. It is also the part I will want to skip. |
| 50 | **Build.** One exercise, or one thin slice of `product` or `platform`. Test first, always. | The struggle is the mechanism. |
| 20 | **Write.** Update `NOTES.md`, or the module README, in my own words. | Writing is where I find out I did not understand it. |
| 10 | **Commit and push.** One decision logged if I made one. | Green CI, or it did not happen. |

If a day collapses, the 25 minutes of retrieval is the part to keep. Missing a build day
costs a day. Missing retrieval repeatedly costs the module.

## The weekly loop

- **One module finished** to the `CONTRIBUTING.md` standard. Not two, and not a half.
- **One decision record** in `decisions/`, on a real choice I made that week.
- **One work scenario** from `scenarios/` — see below.
- **One postmortem or engineering write-up read**, with a paragraph on what I would have asked.
- **Friday reproduce-from-scratch check**, per `AI_USAGE.md`. Blank file, no assistant.
- **Every other week: an incident.** Also below.

## Phases

Ordered, not scheduled. Each one is finished when its exit test passes — cold, honestly, and
on a day I did not cherry-pick. Moving on early is the failure mode this table exists to
prevent, and it is the only way the plan can actually fail.

### Phase 0 — Shell, git, and a green badge

The repo already supports this via `tools/shelltest.py` and the note in `CONTRIBUTING.md`.

| Modules | Project | Exit test |
|---|---|---|
| Linux — the filesystem, processes, permissions and services, without hand-holding; shell navigation and pipes; grep, sed, cut and awk on real log files; git branching, history and rebase; finding a planted bug with `git bisect run`; GitHub, remotes, pull requests and CI; GitHub Actions — workflows, matrix builds, caching and secrets; working with an assistant at the command line | **`logkit`**, a shell toolkit over a messy real log: parse a line, count by level, rank sources, detect a spike, reject malformed input with a non-zero exit, and stream rather than buffer. Tested by `tools/shelltest.py`, built by a CI matrix, with a bug planted in its history that has to be found using `git bisect run` | CI is green on a push I made, and I have explained what the workflow file does, line by line, to another person |

**Status:** the remote exists and CI ran green on a push I made, 2026-09-21. What remains is
`logkit` and the last clause of the exit test — the explanation, to a person.

`logkit` exists because a phase with no artifact leaves nothing to commit, and Phase 0 was the
only phase in that state. It is small on purpose. It is also the first thing in this repo that
another person could run.

### Phase 1 — Python that holds up, and the machine underneath

| Modules | Project | Exit test |
|---|---|---|
| Types and data structures; functions and scope; files and encodings; exceptions and what to do with them; classes and when not to use them; modules and packaging with `uv`; `pytest` properly; type hints with Pyright in CI; iterators and generators; `dataclasses`; the standard library worth knowing; complexity and the standard structures, with timed exercises; `asyncio`, threads and the GIL; processes, file descriptors, signals, `fsync` and atomic rename; property-based testing with Hypothesis | Three standalone builds: a typed, packaged log-triage CLI; the crash-safe key-value store with a write-ahead log; the append-only log with consumer offsets. The last two are `deep-dive` modules and are benchmarked | Reproduce three `hands-on` module solutions from blank files, cold, in one sitting; and the key-value store survives a kill mid-write, proven by a test |

`m001` already covers log parsing. It is the right first module and it stays.

### Phase 2 — HTTP, data, and the first slice

Where `product` starts, in C#.

Five years of shipping C# is not the same as depth in it, so the language modules here are real
modules and not revision. Async, LINQ, dependency injection and testable design are the four
that separate someone who writes C# from someone who is good at it, and all four are things I
have used for years without ever being examined on.

| Modules | Project | Exit test |
|---|---|---|
| HTTP semantics; TCP, DNS, TLS and timeouts; REST and its arguments; JSON and schemas; API versioning as a strategy rather than a word; pagination over data I do not control; rate limits and quotas as something I implement rather than obey; webhooks, their delivery guarantees and replay; ASP.NET Core minimal APIs; C# depth — `async`/`await` properly, LINQ, dependency injection, nullable reference types; xUnit and integration testing in ASP.NET Core; unit against integration, and what is not worth testing; test doubles, and when a fake beats a mock; test-driven development; data structures and algorithms in C#, timed, because this is the language the interviews will be in; Entity Framework Core, and when Dapper is the better answer; background processing; retries, backoff and idempotency; OAuth2 and OIDC as protocols; SQL; Postgres; indexes; transactions and isolation levels; reading a query plan; data modelling; migrations; containers | Product backend v0: `MunicipalMoney.Client` on NuGet; an ASP.NET Core service loading it into Postgres with EF Core migrations; a background worker with idempotency keys and a job-status endpoint driving the loads; an OpenAPI spec; a generated TypeScript client for Phase 3; a CLI; a Dockerfile | Someone else can install it from my README and pull one municipality's budget, without asking me anything |

### Phase 3 — The full-stack half

| Modules | Project | Exit test |
|---|---|---|
| JavaScript fundamentals; TypeScript; the type system as a design tool; React; server state with TanStack Query and client state with Zustand, and why they are different problems; forms and validation; accessibility; a small design system — tokens, accessible primitives, Tailwind CSS, and Storybook as its documentation; build tooling with Vite; Vitest for unit and component tests, Playwright for end to end | The explorer: pick a municipality, see revenue, spend and audit outcome, compare across years and peers; honest error surfaces; Playwright tests; an `AGENTS.md` a stranger's assistant could work from | The explorer surfaces a server error in a way a stranger could act on, and that error is reachable by keyboard and screen reader |

This phase is what makes "full-stack" a claim I can defend rather than a line on a CV.

**React and Vite, not Next.js.** react.dev recommends starting with a framework. The hiring
market does not: Next.js was named in one of 64 remote listings and four of 105 South African
ones, and of the 23 remote listings naming React, 22 named no meta-framework at all. Server
Components appeared in none of the 169 listing bodies read. Vite's React plugin outdownloads
Next on npm. The explorer is a single-page app served by the ASP.NET Core API, and the reasons
go in `decisions/` during this phase, because this is the kind of choice an interviewer probes.

**Not Angular, and here is the trigger to revisit.** Angular is genuinely co-equal with React
in South Africa — 48% of listings against 47% — so the instinct to learn both is sound, and I
am still not doing it. Remotely Angular is 5%, most South African listings say Angular *or*
React, and a second framework costs a whole phase that the data pillar needs more. Revisit only
if I am turned down twice for a role where Angular was the stated blocker.

### Phase 4 — Design patterns and architecture

Patterns are judgment, not vocabulary. The exam is whether I can tell when one earns its place
and when it is decoration, so every module here ends in a refactor of code that already works.

| Modules | Project | Exit test |
|---|---|---|
| Creational patterns, and when they are overkill; structural patterns; behavioural patterns; SOLID as a heuristic rather than a law; refactoring to a pattern without changing behaviour; the pattern I rejected, and what it would have cost; event sourcing, and when an audit trail justifies it; modular monoliths, and the seam that lets you split later; microservices, and the cost nobody prices; the reverse migration, microservices back to a modular monolith; event-driven architecture; solution architecture as a document someone else can build from | Refactor the Phase 2 product backend. Extract one real seam; apply patterns only where they earn their place; event-source one aggregate so the audit trail is derivable rather than written twice; write the module boundaries down as a modular monolith with the split points named | I refactor working code to a pattern and every behaviour test passes unchanged, and a reviewer agrees the pattern earned its place. I can also name a pattern I rejected and say what it would have cost |

The reverse-migration module is deliberate. Knowing why a team went back from microservices to
a modular monolith is worth more in an interview than knowing how they left.

### Phase 5 — System design

One posting names system design as a fundamental, the interview processes in `research/` grade
it directly, and it is the phase most likely to be skipped because nothing compiles.

| Modules | Project | Exit test |
|---|---|---|
| The vocabulary; estimating load and capacity before designing anything; caching layers and what they hide; queues and back-pressure; consistency against availability, with a real choice made and defended; sharding and partitioning; gateways, rate limits and quotas; the classic intermediate problems; multi-region and failure domains; system design on Azure with named services and what they cost; writing the design doc; defending it aloud under time | Four documents in `designs/`. Three write up systems already built — the product backend, the explorer, the replatform — as if before the fact, which is the only honest way to find out what I would have got wrong. The fourth is greenfield from a brief with no code attached, which is the interview shape | I design a system aloud in forty-five minutes to someone who pushes back, and the written version survives their objections. The Azure one names real services and what they cost |

Writing up a system after building it is not cheating. The value is the gap between the design
I would have written and the thing I actually built, and that gap is the phase's real output.

### Phase 6 — Data engineering: the replatform

The deep phase. Everything here is the day job of the data posting in `research/`.

| Modules | Project | Exit test |
|---|---|---|
| SQL depth on SQL Server — T-SQL, stored procedures, query plans, and the dialect differences that break a migration; PySpark and its execution model — partitions, shuffles, the Spark UI; Spark SQL; Delta Lake, with Iceberg as the comparison; Medallion layers and what each may contain; dimensional modelling and Data Vault, and when each is wrong; replatforming T-SQL to Spark SQL with parity evidence; Spark Declarative Pipelines, open source in Spark 4.1 and therefore learnable on local Spark; Spark 4's ANSI SQL mode, on by default, and what it silently breaks in a migration; orchestration with Airflow, ADF as the Azure shape; transformation as code, with tests; data quality and reconciliation; governance, PII tagging and POPIA; lineage with OpenLineage; catalogs — Unity Catalog and the Iceberg REST Catalog, with Hive Metastore as the legacy it now is; Microsoft Fabric — OneLake, shortcuts, mirroring Unity Catalog, Direct Lake, and why Microsoft's own guidance keeps the pipeline in Databricks; DuckDB and "does this need distribution"; Parquet and columnar storage; cost per GB stored and scanned | The replatform: SQL Server in Docker with the shipped OLTP, warehouse and ETL procedures; bronze to gold on Delta with local Spark or Databricks free edition; silver as Data Vault or star, decision recorded; Airflow; tested transforms; `parity` v1 comparing gold to the shipped warehouse; OpenLineage; PII masking on customer data; a cutover runbook; a DuckDB-versus-Spark benchmark on the same workload, with cost | The parity report is accepted by someone who wants it to be wrong; a stakeholder-shaped question is answered from gold and traced to the raw rows; a stranger runs the migration from my runbook without asking me anything |

The "does this need distribution" module is already in the `horizon/` queue. It belongs here.

**A reference implementation, read late.** `iobruno/data-engineering-labs` is one person's
original implementations across ingestion, orchestration, warehousing, dbt, batch and stream
processing, on current versions — Airflow 3, Spark 4 with Spark Connect, dbt against five
warehouses, Flink and Kafka. It is good for exactly one thing: seeing how a competent person
lays a project out, which is the part no course teaches and no documentation covers. It serves
Phase 7 as well as this one.

Per `AI_USAGE.md`, it gets opened *after* I have built my own version and want to compare —
never before. Reading a finished implementation first is the same mistake as reading a
solution first, and it feels just as much like progress. It does not cover Delta Lake or
Databricks; those come from Databricks Academy's free Data Engineer plan.

### Phase 7 — Data infrastructure: the ingestion service

The ingestion service is Python, and its job-status API is FastAPI. That is deliberate: the
data posting asks for "REST APIs using FastAPI or equivalent" in the same breath as
"authentication, idempotency and job-status functionality", so FastAPI belongs on the data side
rather than in front of a web app.

| Modules | Project | Exit test |
|---|---|---|
| Append-only logs; partitioning; offsets and consumer groups; delivery semantics and idempotent sinks; watermarks and late data; change data capture; schema evolution; serialisation formats; event-driven architecture, and when to split a service; system design — stating a trade-off, writing it down, and defending it aloud; benchmarking honestly | The ingestion service: SQL Server CDC and Municipal Money polling into Redpanda, landed in Delta by idempotent merge; offsets, replay, backfill versus live, late data, schema drift, dead letters, a job-status API; the product switches to reading gold; Service Bus or Event Hubs documented as the cloud shape; a benchmark harness and a written analysis of where it falls over | A replay from offset zero reproduces gold byte for byte; and a benchmark I would defend to someone who disagreed with it, including its limitations |

### Phase 8 — Applied AI

| Modules | Project | Exit test |
|---|---|---|
| Model API fundamentals — messages, structured outputs, tool use, streaming; retrieval-augmented generation and vector search with pgvector, retrieval measured separately from generation; agents and tool orchestration, and when a plain function is better; **evals** — golden sets, LLM-as-judge and its limits, regression as a CI gate; guardrails and prompt injection in systems that read untrusted text; local serving with Ollama or vLLM; cost, latency and caching; observability of LLM systems; versioning prompts and models, serving an endpoint, monitoring it; working with coding assistants critically — `AI_USAGE.md` extended from learning to building | The assistant: a Python service behind the ASP.NET Core product, called over HTTP — a real service boundary, and the microservice shape one posting names. Question to tool call or generated SQL to answer, with row citations; pgvector retrieval over municipal budget documents and Treasury reports; a golden eval set and judge run in CI; injection tests using poisoned document text; hosted API or local model; a cost and latency panel; pinned prompt and model versions | The eval suite catches a regression I introduce on purpose before I notice it by hand; and an injection planted in stored data is blocked by a test that existed first |

Evals are the deep module. Anyone can call a model API; the skill the roles pay for is
knowing, with evidence, whether the answers got worse.

### Phase 9 — Security and privacy judgment

| Modules | Project | Exit test |
|---|---|---|
| Authentication versus authorisation; OAuth2, OIDC, Entra ID and Cognito; request signing; secrets and Key Vault; the OWASP failures that actually recur; privacy engineering and POPIA; audit logging; supply chain — dependency scanning and SBOMs as CI jobs; threat modelling. Optional deep-dive: detection as code | Across both systems: OIDC login via Entra ID or Keycloak; API keys and request signing for the public API; a policy layer for who sees what; an audit log; secrets in Key Vault or a local vault; SBOM and dependency scanning in CI; a threat model of the assistant; POPIA masking verified on the replatform. Optional: detection rules over the audit log, tested in CI | I find a real authorisation bug in my own policy layer by writing a test that should have existed |

### Phase 10 — Operate it

The phase that attacks `NON-CLAIMS.md` directly. Starts as soon as there is something worth
operating — it overlaps every phase after Phase 2 — and it does not end.

| Modules | Project | Exit test |
|---|---|---|
| Structured logging; OpenTelemetry traces and metrics; SLOs; alerting; Terraform and deployment; load testing; fault injection; incident response and postmortems | Both systems deployed to Azure with Terraform — Container Apps, Postgres Flexible, Storage — with AWS equivalents documented; OpenTelemetry to a dashboard; SLOs; alerts; runbooks; a load test to breakage; fault injection — kill mid-write, full disk, clock skew, slow client; incident drills with postmortems; one dependency upgrade that breaks something, fixed | An alert I wrote fires on a failure I injected before I look at the logs, and the postmortem names the test that now prevents it |

### Phase 11 — Production experience, which is the actual bar

The requirements list starts with years of production work. Phases 0–10 sharpen it and give
me the evidence to show for it; they cannot substitute for it, and this file will not pretend
they can. So this phase is explicit work, not waiting:

- **The product in production is the campus.** Published, used by strangers, with an uptime
  commitment and a pager I carry. Real users, real consequences, on something I own end to
  end.
- **Years count wherever they were earned.** Employment counts toward the first requirement.
  So do mentoring, stakeholder ownership and incident history — claimed with evidence, from
  wherever they happened. This file does not name an employer, and does not need to.
- **Sustained contribution to code I did not write.** Begins once Phase 3's exit test passes;
  before that I cannot read a stranger's codebase fast enough for it to be contribution
  rather than charity. Treasury's own open-source municipal-data project is the natural first
  candidate. Any small, active, well-tested project with a real CONTRIBUTING file will do.
- **Certifications are not gates.** They are sat as a by-product of the phases, per
  "Certifications" below — never instead of a module.
- **Depth over breadth, in public.** Data is the depth. This phase lives there.

The gate on this phase, and on the curriculum, is meeting the list — in years and in kind —
with the evidence public.

## Practices that mimic actual work

Modules teach technique. These teach the parts of the job that are not technique, and they
are the reason a portfolio of exercises usually fails to convert into an offer.

### Decision records — `decisions/`

One file per real decision. The postings call them ADRs. The format is deliberately short, and
the last line is the one that matters:

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

### Challenge ladders — `challenges/`

Courses are watched and forgotten. Each phase's project is broken into numbered stages, and
each stage is gated by an acceptance test that has to pass on CI. Modelled on CodeCrafters:
stage N+1 does not start until stage N is green, and green means green on a push, not on my
laptop, because my laptop is where the environment lies to me.

Eighty-eight stages across the twelve phases. `modules/` teaches a topic; `challenges/` proves
I can build the thing. The rule from `AI_USAGE.md` applies with a sharp edge here: the spec and
the acceptance test may be assistant-written, and the solution may not.

A stage nobody has started is skipped rather than failed, so the badge keeps meaning something.
Starting a stage is therefore a commitment, which is the whole design.

### Design docs — `designs/`

One page before any service starts: the API or schema, the data model, the failure modes, what
it will not do. Reviewed by someone else before the first commit. This is the document senior
engineers write; the modules are what makes it possible to write one.

### Work scenarios — `scenarios/`

A weekly ticket written the way tickets actually arrive: ambiguous, from a stakeholder with
a goal rather than a spec, sometimes wrong about the cause.

> "Finance says the gold total is R40k off from the source. Can you look at it this week?"

The exercise is not to fix it. It is to write down: what I would ask before starting, what
I would measure first, what I think the three plausible causes are, and which one I would
rule out most cheaply. Then do that. Then record where my guess was wrong.

Ambiguity tolerance is on the requirements list. This is how it gets practised.

### Incidents — every other week

I break one of the two systems on purpose — or better, have someone else break it — and then
diagnose it under a clock without reading the commit that did it. Afterwards, a postmortem:
timeline, what I believed at each step and why it was wrong, the actual cause, and the test
that would have caught it.

Blameless postmortems are a genuine professional skill and almost nobody arrives with one.

### Code review — monthly

Open a pull request against my own repo and review it a week later as a stranger would,
against `CONTRIBUTING.md`. Then get a human to review one. Then review one
assistant-generated pull request against the same bar; one of the postings asks for exactly
that, "critically reviewing and validating AI-generated code". Review given and received is on
the `NON-CLAIMS.md` list and this is the cheapest way to start crossing it off.

### Interview rehearsal — every phase

The hiring processes in `research/` are pair coding, take-homes, and hours of final
interviews graded on design, code quality, performance and test coverage. Practising alone
does not rehearse any of that. So, once per phase: one take-home-shaped exercise graded by
another person against those four criteria; one system design done aloud to a human in
forty-five minutes; one pair-coding session where I talk while I type.

### Reading — weekly

One postmortem or engineering write-up, with a paragraph on what I would have asked the
authors. Senior engineers read; the reading is where the vocabulary for the design docs comes
from.

## Where the material comes from

**A course is the reading before a module, never the module.** `AI_USAGE.md` says guided
tools are worst used for first exposure and best used for drilling something already
understood; a video has the same failure mode. Watch it, close it, then build the exercises
cold. The module's tests are what proves it stuck.

One course open at a time, tied to the module being built. None open on a day the build slot
was skipped.

| Phase | Dometrain | Free, and usually better |
|---|---|---|
| 0 | Hands-On Learn Linux; Learn Bash; Hands-On Learn Git From Scratch; From Zero to Hero GitHub Actions; From Zero to Hero Working with GitHub Copilot; Getting Started and Deep Dive Claude Code | the `git bisect` and GitHub Actions documentation |
| 1 | Learn Python; Python Interview Questions | CMU 15-445 for storage, indexes, transactions and recovery — the course behind the two deep-dive modules |
| 2 | C# Deep Dive, Asynchronous Programming in C#, LINQ in C#, Dependency Injection in .NET, Writing Testable Code in C#, ASP.NET Core, REST APIs in .NET, Minimal APIs in .NET, Entity Framework Core, Dapper, Unit testing for C# Developers, Integration testing in ASP.NET Core, Learn PostgreSQL, Docker for Developers; From Zero to Hero Testing with xUnit in C#; From Zero to Hero Unit testing for C# Developers; From Zero to Hero Test-Driven Development in C#; Hands-On Data Structures & Algorithms in C#; C# Interview Questions | the ASP.NET Core and EF Core documentation |
| 3 | Getting Started TypeScript; Hands-On Learn TypeScript; Deep Dive TypeScript; Multi-Tenant SaaS App in TypeScript; Learn JavaScript; JavaScript and TypeScript Interview Questions | react.dev and its interactive tutorial; the Vite, TanStack Query, Tailwind and Playwright documentation |
| 4 | Hands-On Creational, Structural and Behavioral Design Patterns in C#; Getting Started and Deep Dive Event Sourcing in .NET; Getting Started and Deep Dive Modular Monoliths in .NET; Getting Started and Deep Dive Microservices Architecture; From Zero to Hero From Microservices to Modular Monoliths; From Zero to Hero Event-Driven Architecture; Getting Started and Deep Dive Solution Architecture | the refactoring catalogue, and the original Gang of Four book for what the patterns were actually for |
| 5 | Hands-On System Design for Beginners; Hands-On System Design for Intermediate Engineers; Hands-On Advanced System Design; Hands-On System Design for Azure; From Zero to Hero Cloud Architecture in Azure | Designing Data-Intensive Applications, read alongside; the Azure pricing calculator, which is the part most designs skip |
| 6 | SQL Server | Data Engineering Zoomcamp; Databricks Academy's free Data Engineer plan for Delta and Databricks; Astronomer Academy for Airflow; dbt Learn for dbt; `iobruno/data-engineering-labs` for layout, read late |
| 7 | Domain-Driven Design | the Zoomcamp's streaming module. Event-driven architecture and microservices are covered in Phase 4 |
| 8 | Getting Started AI Agents in C#; Getting Started and Deep Dive Boosting Developer Productivity with AI; Getting Started Model Context Protocol; AI for .NET Developers and AI Chatbot with RAG in .NET, for the concepts and the comparison | LLM Zoomcamp — Python, pgvector, and a module on measuring retrieval and answer quality; Anthropic's own courses for tool use and evals; the FastAPI documentation |
| 9 | Authentication and Authorization | OWASP, and the OAuth2 and OIDC specifications |
| 10 | Azure for Developers, Cloud Architecture in Azure, Kubernetes for Developers, Bicep, OpenTelemetry | Terraform documentation; Microsoft Learn for the Azure services |
| Practices | Nailing the Behavioral Interview; Mastering Communication & Collaboration for Software Engineers; Career Management for Software Engineers; Building a Resume/CV & LinkedIn Profile | the weekly reading, below |

Dometrain is .NET-centred, which used to be a mismatch and is now the point: it carries Phase 2
outright, and its architecture, security and cloud courses carry the concepts elsewhere. The
Claude Code courses are not a luxury — using an assistant well and reviewing its output
critically is requirement 6, and Claude Code is the assistant most often named by product name
in South African listings. Dometrain still cannot carry Phase 6 or Phase 8; those are the free
sources.

**On the interview-question courses.** They are in the table because they are cheap and they
surface gaps. They also rehearse recall, and recall is not what the processes in `research/`
grade — four to six hours with four to six people, scored on design, code quality, performance
and test coverage. Watch one, then do the rehearsal practice with a person. A question bank is
not a rehearsal.

**The three books.** Designing Data-Intensive Applications is the one to read first, because
storage, partitioning, transactions, batch and stream processing are Phases 1, 6 and 7 in a
single volume. Fundamentals of Data Engineering gives the field's map. The Data Warehouse
Toolkit gives the modelling Phase 6 needs. These outlast every platform on this page.

## Certifications

**The rule.** A certification is sat *after* the phase's exit test passes, using that phase's
work as the preparation. If I have to study separately for one, the phase did not teach me
enough, and the fix is the module, not the cram. None of them appears on the requirements
list; exactly one is named in a posting at all, and there as a nice-to-have.

Cloud is Azure. Where Microsoft's own path has moved away from what I am building, I follow
what I am building.

How little they matter, measured: of 28 listings read end to end, six mentioned a certification
at all and **not one named a specific exam code**. One recruiter wrote that certifications
"are valued rather than required and are achievable after appointment"
(`research/2026-09-23-data-stack-and-certifications.md`).

| Phase | Certification | Why it follows from the work |
|---|---|---|
| 2 | Azure Data Fundamentals (DP-900) | Already begun. Fundamentals-level, and the Postgres, modelling and storage work covers it |
| 6 | **Azure Databricks Data Engineer Associate (DP-750)** | The Microsoft badge that matches what I am actually building: Unity Catalog, Lakeflow declarative pipelines, Auto Loader, Delta `OPTIMIZE` and `VACUUM`, Spark UI debugging. Live and bookable; English only for now |
| 6 | **Databricks Certified Associate Developer for Apache Spark** | The only certification any target posting names. The replatform *is* the preparation: DataFrame API, partitions, shuffles, Spark Connect, tuning |
| 6 | Databricks Certified Data Engineer Associate | Medallion layers, Delta, batch and streaming pipelines — the phase's project, examined |
| 6 | Astronomer's Apache Airflow 3 Fundamentals | Narrow and tied to a tool the phase uses daily. Not free: one attempt per purchase, and it is named in zero listings, so it is the first to cut |
| 7 | Databricks Certified Data Engineer Professional | The depth badge. Sit it after the ingestion service, not before |
| 8 | Databricks Certified Generative AI Engineer Associate | After the assistant ships with evals gating CI. It matches the stack |
| 9 | Identity and Access Administrator (SC-300) | After OIDC, the policy layer and the audit log are built and a threat model exists |
| 10 | **Azure AI Cloud Developer Associate (AI-200)**; HashiCorp Terraform Associate (exam 004) | AI-200 is what replaced AZ-204. Its own skills list is Container Apps, Service Bus, Key Vault, OpenTelemetry and pgvector on Azure Postgres, which is Phases 8 to 10 almost exactly |

**Two exams this file used to name no longer exist.** AZ-204 retired on 31 July 2026 and AI-102
retired with it; each page now reads "This certification and the renewal assessment are
retired." AI-200 is the stated successor to AZ-204 and is the one in the table above.

**There is no C# certification worth taking.** Microsoft does not examine the language, and
AZ-204, the nearest thing to a .NET developer badge, is gone. The evidence for C# is the
product: an ASP.NET Core service with tests, running in production, reviewed by someone else.
That is a better credential than any exam would have been.

**On Fabric, correcting what this page used to say.** An earlier version claimed DP-700
examines "a different platform" from Spark and Delta. That was wrong, and it was wrong because
I trusted a summary instead of the source. Fabric's lakehouse *is* Delta Lake, its Data
Engineering workload *is* Apache Spark, and DP-700's own skills list includes transforming data
with PySpark, Spark structured streaming, and configuring Airflow. Fabric is a different
packaging of the same engine. I am still not sitting DP-700, because DP-750 examines the exact
platform I build on and Fabric gets one module rather than a certification. But the reason is
now preference, not a platform gap.

AZ-900 is below where I already am. AZ-305 and Kubernetes certificates are beyond what either
system needs. dbt's certificate is optional at best: dbt appeared in one of 105 South African
listings and its certificate in none.

## What this curriculum still will not prove

Kept here for the same reason `NON-CLAIMS.md` is kept at top level. Phases 0–10 close none
of these; Phase 11 is the only thing that touches them, which is why it is on the page.

- Working under real money and real consequences at any scale an employer would call scale
- Operating Spark or Kafka as a platform for other people at the scale the postings name.
  `platform` is the laptop-and-one-VM-sized version of what those systems do
- A replatform with real money behind the cutover
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
- **If `decisions/` has fewer records than there have been real decisions.** The practice is
  being skipped. Write the missing ones, dated today and marked late.
- **If the daily loop stops fitting.** Cut a pillar. Never lower a standard.
- **Never by elapsed time.** Slow is a reason to look at the daily loop, not to move a gate.

## Sources

- `research/2026-09-22-sa-target-roles.md` — the three postings the requirements were reduced
  from, with URLs
- `research/2026-09-23-data-stack-and-certifications.md` — whether the Spark, Delta and
  Databricks bet still holds, and which certifications are real. It says the stack is right
- `research/2026-09-23-full-stack-tooling.md` — React against Angular, .NET against Python, and
  the counts behind the language split above
- `research/2026-09-22-data-role-example.md` — a fourth posting, the example of what data roles
  pay for
- `research/2026-09-17-openai-target-roles.md` — the postings the first version of this plan
  was reduced from; still the source for the interview process and for "production, not
  projects"
- `research/2026-09-17-floci-local-build.md` — what shaped the first version's spine, and why
  an emulator was the wrong project for these roles
