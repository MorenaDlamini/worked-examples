# Horizon — 2026 Q3

First entry. Written as a starting baseline rather than a review, since there is no
previous quarter to compare against. Reassess honestly in December and note what I got wrong.

## Data infrastructure

**Happening**

- **The open table format is now assumed.** Iceberg and Delta are no longer a differentiator
  but a baseline expectation, and job descriptions name them directly. The interesting work
  has moved up a level: catalogs, metadata scale, compaction economics, and multi-engine
  interoperability. Metadata is the scaling problem, not data.
- **Separation of storage and compute is finished as a debate.** Every serious platform does
  it. The consequence is that cost engineering has become a data engineering skill, not a
  finance one.
- **Python and SQL remain the floor, not the ceiling.** The differentiated roles want someone
  who can also read the JVM stack trace coming out of a Spark executor.

**Consolidating**

- **Single-node is respectable again.** DuckDB and similar engines handle workloads that
  would have required a cluster five years ago. The judgment call "does this actually need
  distribution" is now a real question with a real answer, and asking it is a senior signal.
- **Streaming and batch are converging** rather than one winning. The lakehouse absorbs both.
  Knowing where the seam is — watermarks, late data, reconciliation between the two paths —
  is more valuable than picking a side.
- **Declarative and asset-based orchestration** over imperative DAGs. Partitions, lineage and
  invalidation as first-class concepts rather than dates in a config.

**Noisy**

- Fully autonomous agentic data pipelines. Interesting, unproven, and the failure modes are
  expensive in a domain where wrong answers are worse than missing ones. Worth watching,
  not worth betting a year on.
- The perennial "SQL is dead" and "the warehouse is dead" claims. They were wrong the last
  four times.

## Security

**Happening**

- **Identity is the perimeter.** The majority of incidents that matter start with credentials
  rather than an exploit. Practical consequence: authentication, authorisation, session
  handling and secrets management are worth more study time than exploit development.
- **Detection as code.** Rules in version control, tested in CI, reviewed like software. This
  is the single clearest convergence of security and data engineering and the reason those
  two tracks belong in the same curriculum.
- **Supply chain.** Dependency provenance, SBOMs, signed artifacts. Driven by regulation as
  much as by engineering, which means it is not going away.

**Consolidating**

- **eBPF** for runtime visibility on Linux, displacing older agent architectures.
- **AI-assisted triage in the SOC** — summarisation, correlation, drafting. The pattern that
  is working is model-proposes, human-disposes. The pattern that is failing is automated
  response.
- **Prompt injection as a genuine vulnerability class.** Any system where a model reads
  attacker-influenced text and can then act has a new attack surface, and the defences are
  immature. This is underexplored and therefore a good place to be early.
- **Post-quantum migration planning.** Slow, mandated, and mostly about inventory rather
  than cryptography. Unglamorous, and someone will be paid well to do it.

**Noisy**

- Autonomous offensive agents. Loud, and largely demonstrations rather than deployments.
- Each quarter's new acronym for "the same telemetry, in a different vendor's product".

## Where the two fields meet

The most defensible position over the next few years is not "data engineer" or "security
engineer" but the overlap: someone who can build the pipeline that ingests security
telemetry at scale, reason about its correctness, and write the detections as tested code.
That is a data engineering problem with an adversary attached, and the supply of people who
can do both halves is much smaller than the demand.

## Queue changes

- **Add:** a module on prompt injection in systems that read untrusted text.
- **Add:** a module on the "does this need distribution" judgment, with a DuckDB versus
  Spark benchmark on the same workload.
- **Stop tracking:** vendor announcements. Release notes only.

## What I will check in December

- Did single-node processing keep gaining, or did it plateau?
- Has anything real shipped in autonomous incident response, or is it still demos?
- How many of the roles I want now ask for Iceberg by name, compared with today?
