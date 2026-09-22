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
2. Python as the primary backend, typed and tested — `pytest`, Pyright, `uv`
3. Designing and operating REST APIs, including auth, idempotency and job status
4. Docker, CI/CD, and a cloud; AWS and Azure are both named
5. Integrating LLM features: calling model APIs, retrieval-augmented generation, vector search
6. Using coding assistants, and critically reviewing what they produce
7. Working from specs, design docs and ADRs; code review; clear communication; mentoring
8. Relational modelling on Postgres; Spark, Delta, and replatforming legacy SQL with parity
   evidence
9. Observability, and resolving incidents in production
10. Security and privacy judgment inside the product: OAuth2 and OIDC, secrets, POPIA

The first item is the bar. No repository substitutes for it; `NON-CLAIMS.md` says the same
thing from the other side, and Phase 9 exists for it.

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

The stack: Python, TypeScript and React, Postgres, PySpark and Delta, DuckDB for judgment.
Azure first, because the data posting names its services; AWS equivalents on every cloud
module, because the other two name it.

## Depth

Four pillars is breadth, and depth over breadth is the rule. So:

| Pillar | Tier I am aiming at | Where the proof lives |
|---|---|---|
| Data | `deep-dive` — the one to go unreasonably deep in | `platform`: replatform, parity, ingestion |
| Full-stack | `build-it` — defendable, not distinguished | `product`: API, explorer, SDK |
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
- A typed Python client library, `municipal-money`, on PyPI.
- A REST API with OIDC login for saved views.
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
| Shell navigation and pipes; grep, sed, cut on real log files; git branching and history; GitHub, remotes and CI | This repo on GitHub with green CI; a shell log-triage script over real log files | CI is green on a push I made, and I have explained what the workflow file does, line by line, to another person |

**Status:** the remote exists and CI ran green on a push I made, 2026-09-21. What remains is
the last clause — the explanation, to a person.

### Phase 1 — Python that holds up, and the machine underneath

| Modules | Project | Exit test |
|---|---|---|
| Types and data structures; functions and scope; files and encodings; exceptions and what to do with them; classes and when not to use them; modules and packaging with `uv`; `pytest` properly; type hints with Pyright in CI; iterators and generators; `dataclasses`; the standard library worth knowing; complexity and the standard structures, with timed exercises; `asyncio`, threads and the GIL; processes, file descriptors, signals, `fsync` and atomic rename; property-based testing with Hypothesis | Three standalone builds: a typed, packaged log-triage CLI; the crash-safe key-value store with a write-ahead log; the append-only log with consumer offsets. The last two are `deep-dive` modules and are benchmarked | Reproduce three `hands-on` module solutions from blank files, cold, in one sitting; and the key-value store survives a kill mid-write, proven by a test |

`m001` already covers log parsing. It is the right first module and it stays.

### Phase 2 — HTTP, data, and the first slice

Where `product` starts.

| Modules | Project | Exit test |
|---|---|---|
| HTTP semantics; TCP, DNS, TLS and timeouts; REST and its arguments; JSON and schemas; FastAPI; retries, backoff and idempotency; OAuth2 and OIDC as protocols; SQL; Postgres; indexes; transactions; data modelling; schema migrations; containers | Product backend v0: the `municipal-money` typed client on PyPI; a FastAPI service loading it into Postgres with migrations; a worker with idempotency keys and a job-status endpoint driving the loads; an OpenAPI spec; a generated SDK; a CLI; a Dockerfile | Someone else can install it from my README and pull one municipality's budget, without asking me anything |

### Phase 3 — The full-stack half

| Modules | Project | Exit test |
|---|---|---|
| JavaScript fundamentals; TypeScript; the type system as a design tool; React; state; data fetching; forms and validation; accessibility; a small component library; build tooling; end-to-end testing | The explorer: pick a municipality, see revenue, spend and audit outcome, compare across years and peers; honest error surfaces; Playwright tests; an `AGENTS.md` a stranger's assistant could work from | The explorer surfaces a server error in a way a stranger could act on, and that error is reachable by keyboard and screen reader |

This phase is what makes "full-stack" a claim I can defend rather than a line on a CV.

### Phase 4 — Data engineering: the replatform

The deep phase. Everything here is the day job of the data posting in `research/`.

| Modules | Project | Exit test |
|---|---|---|
| SQL depth, including reading T-SQL; PySpark and its execution model — partitions, shuffles, the Spark UI; Spark SQL; Delta Lake, with Iceberg as the comparison; Medallion layers and what each may contain; dimensional modelling and Data Vault, and when each is wrong; replatforming T-SQL to Spark SQL with parity evidence; orchestration with Airflow, ADF as the Azure shape; transformation as code, with tests; data quality and reconciliation; governance, PII tagging and POPIA; lineage with OpenLineage; catalog concepts — Hive Metastore, Unity Catalog; DuckDB and "does this need distribution"; Parquet and columnar storage; cost per GB stored and scanned | The replatform: SQL Server in Docker with the shipped OLTP, warehouse and ETL procedures; bronze to gold on Delta with local Spark or Databricks free edition; silver as Data Vault or star, decision recorded; Airflow; tested transforms; `parity` v1 comparing gold to the shipped warehouse; OpenLineage; PII masking on customer data; a cutover runbook; a DuckDB-versus-Spark benchmark on the same workload, with cost | The parity report is accepted by someone who wants it to be wrong; a stakeholder-shaped question is answered from gold and traced to the raw rows; a stranger runs the migration from my runbook without asking me anything |

The "does this need distribution" module is already in the `horizon/` queue. It belongs here.

**A reference implementation, read late.** `iobruno/data-engineering-labs` is one person's
original implementations across ingestion, orchestration, warehousing, dbt, batch and stream
processing, on current versions — Airflow 3, Spark 4 with Spark Connect, dbt against five
warehouses, Flink and Kafka. It is good for exactly one thing: seeing how a competent person
lays a project out, which is the part no course teaches and no documentation covers. It serves
Phase 5 as well as this one.

Per `AI_USAGE.md`, it gets opened *after* I have built my own version and want to compare —
never before. Reading a finished implementation first is the same mistake as reading a
solution first, and it feels just as much like progress. It does not cover Delta Lake or
Databricks; those come from Databricks Academy's free Data Engineer plan.

### Phase 5 — Data infrastructure: the ingestion service

| Modules | Project | Exit test |
|---|---|---|
| Append-only logs; partitioning; offsets and consumer groups; delivery semantics and idempotent sinks; watermarks and late data; change data capture; schema evolution; serialisation formats; event-driven architecture, and when to split a service; benchmarking honestly | The ingestion service: SQL Server CDC and Municipal Money polling into Redpanda, landed in Delta by idempotent merge; offsets, replay, backfill versus live, late data, schema drift, dead letters, a job-status API; the product switches to reading gold; Service Bus or Event Hubs documented as the cloud shape; a benchmark harness and a written analysis of where it falls over | A replay from offset zero reproduces gold byte for byte; and a benchmark I would defend to someone who disagreed with it, including its limitations |

### Phase 6 — Applied AI

| Modules | Project | Exit test |
|---|---|---|
| Model API fundamentals — messages, structured outputs, tool use, streaming; retrieval-augmented generation and vector search with pgvector, retrieval measured separately from generation; agents and tool orchestration, and when a plain function is better; **evals** — golden sets, LLM-as-judge and its limits, regression as a CI gate; guardrails and prompt injection in systems that read untrusted text; local serving with Ollama or vLLM; cost, latency and caching; observability of LLM systems; versioning prompts and models, serving an endpoint, monitoring it; working with coding assistants critically — `AI_USAGE.md` extended from learning to building | The assistant inside the product: question to tool call or generated SQL to answer, with row citations; pgvector retrieval over municipal budget documents and Treasury reports; a golden eval set and judge run in CI; injection tests using poisoned document text; hosted API or local model; a cost and latency panel; pinned prompt and model versions | The eval suite catches a regression I introduce on purpose before I notice it by hand; and an injection planted in stored data is blocked by a test that existed first |

Evals are the deep module. Anyone can call a model API; the skill the roles pay for is
knowing, with evidence, whether the answers got worse.

### Phase 7 — Security and privacy judgment

| Modules | Project | Exit test |
|---|---|---|
| Authentication versus authorisation; OAuth2, OIDC, Entra ID and Cognito; request signing; secrets and Key Vault; the OWASP failures that actually recur; privacy engineering and POPIA; audit logging; supply chain — dependency scanning and SBOMs as CI jobs; threat modelling. Optional deep-dive: detection as code | Across both systems: OIDC login via Entra ID or Keycloak; API keys and request signing for the public API; a policy layer for who sees what; an audit log; secrets in Key Vault or a local vault; SBOM and dependency scanning in CI; a threat model of the assistant; POPIA masking verified on the replatform. Optional: detection rules over the audit log, tested in CI | I find a real authorisation bug in my own policy layer by writing a test that should have existed |

### Phase 8 — Operate it

The phase that attacks `NON-CLAIMS.md` directly. Starts as soon as there is something worth
operating — it overlaps every phase after Phase 2 — and it does not end.

| Modules | Project | Exit test |
|---|---|---|
| Structured logging; OpenTelemetry traces and metrics; SLOs; alerting; Terraform and deployment; load testing; fault injection; incident response and postmortems | Both systems deployed to Azure with Terraform — Container Apps, Postgres Flexible, Storage — with AWS equivalents documented; OpenTelemetry to a dashboard; SLOs; alerts; runbooks; a load test to breakage; fault injection — kill mid-write, full disk, clock skew, slow client; incident drills with postmortems; one dependency upgrade that breaks something, fixed | An alert I wrote fires on a failure I injected before I look at the logs, and the postmortem names the test that now prevents it |

### Phase 9 — Production experience, which is the actual bar

The requirements list starts with years of production work. Phases 0–8 sharpen it and give
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
- **Certifications are not gates.** DP-900 and the Databricks Spark Developer certificate align
  with the data pillar and are taken if they fall out of the work — never instead of a module.
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

## What this curriculum still will not prove

Kept here for the same reason `NON-CLAIMS.md` is kept at top level. Phases 0–8 close none of
these; Phase 9 is the only thing that touches them, which is why it is on the page.

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
- `research/2026-09-22-data-role-example.md` — a fourth posting, the example of what data roles
  pay for
- `research/2026-09-17-openai-target-roles.md` — the postings the first version of this plan
  was reduced from; still the source for the interview process and for "production, not
  projects"
- `research/2026-09-17-floci-local-build.md` — what shaped the first version's spine, and why
  an emulator was the wrong project for these roles
