# The 2026 data stack and certification landscape, from a South African seat

Primary-source research, done on 2026-09-23, to answer one question: is `CURRICULUM.md`'s
Phase 4 bet — Spark, Delta, Databricks, Airflow, on Azure — still the right bet, and which
certifications are worth sitting?

Everything factual here is cited to the page that owns the fact. Vendor documentation,
official certification pages, Apache project sites, release notes, and job listing bodies I
opened and read. A blog post summarising a retirement is not the source; the certification
page is. Where I am inferring rather than quoting, it is marked **Unverified**.

The job-listing counts are a snapshot taken on one day. They will go stale. Say so out loud
whenever they are quoted.

---

## The verdict

**The stack is right. Do not change it.** Microsoft's own architecture guidance, updated
2026-08-18, puts Azure Databricks at the centre of the modern Azure data platform and uses
Fabric beside it for serving, not instead of it
([Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture)).
Microsoft's Fabric documentation says, in its own words, "Azure Databricks and Fabric are
better together"
([Microsoft Learn](https://learn.microsoft.com/en-us/fabric/mirroring/azure-databricks)).
Spark, Delta, PySpark and medallion layers are the engine under both products. Nothing in the
evidence says stop.

**But the reasoning in `CURRICULUM.md`'s certification section is wrong on two counts, and
one of them is a real miss.**

1. The page says DP-700 "examines Microsoft Fabric — a different platform from the Spark,
   Delta and Databricks stack this plan is built on." That is half wrong. Fabric's lakehouse
   *is* Delta Lake, its Data Engineering workload *is* Apache Spark, and DP-700's own skills
   list includes "Transform data by using PySpark, SQL, and KQL", "Process data by using Spark
   structured streaming", "Optimize Spark performance" and "Configure Apache Airflow workspace
   settings"
   ([DP-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)).
   Fabric is a different *packaging* of the same engine, not a different engine.
2. Microsoft has since shipped **DP-750, Microsoft Certified: Azure Databricks Data Engineer
   Associate**, a live, bookable certification that examines exactly the stack this plan
   builds: Unity Catalog, Lakeflow Spark Declarative Pipelines, Auto Loader, Delta `OPTIMIZE`
   and `VACUUM`, Spark UI and DAG debugging, Declarative Automation Bundles via the Databricks
   CLI
   ([certification page](https://learn.microsoft.com/en-us/credentials/certifications/implementing-data-engineering-solutions-using-azure-databricks/),
   [DP-750 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750)).
   The curriculum's claim that Microsoft's path "has moved away from what I am building" is no
   longer true. It moved back.

**And two certifications the plan intends to sit no longer exist.** AZ-204 and AI-102 are both
retired; each certification page now carries the banner "This certification and the renewal
assessment are retired"
([AZ-204](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/),
[AI-102](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/)).

One more thing the evidence says, and it is uncomfortable: in a 47-listing South African
snapshot, **Microsoft Fabric was named slightly more often than Databricks** — 32% against
30%. Fabric is not a thing SA employers are about to adopt. It is a thing they have adopted.
The plan does not need to move to Fabric. It does need to stop describing Fabric as somebody
else's platform.

---

## Part 1 — Fabric versus Databricks, per first-party documentation

### What each one is, in the vendor's own words

| | Microsoft Fabric | Azure Databricks |
|---|---|---|
| Vendor definition | "an analytics platform that supports end-to-end data workflows, including data ingestion, transformation, real-time stream processing, analytics, and reporting" ([Learn](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview)) | "a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale" ([Learn](https://learn.microsoft.com/en-us/azure/databricks/introduction/)) |
| Delivery model | "delivered as a software-as-a-service (SaaS) platform" | PaaS; "integrates with cloud storage and security in your cloud account" |
| Storage | OneLake, "built on ADLS (Azure Data Lake Storage) Gen2" | Customer's ADLS Gen2, governed by Unity Catalog |
| Table format | Delta Lake. The lakehouse gives you "**Delta Lake format** for ACID transactions, schema enforcement, and time travel" ([Learn](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview)) | Delta Lake by default; Iceberg on request. "To create an Apache Iceberg table, explicitly specify `USING iceberg`. Otherwise, Azure Databricks creates a Delta Lake table by default." ([Learn](https://learn.microsoft.com/en-us/azure/databricks/tables/managed)) |
| Compute for data engineering | "Fabric Data Engineering provides Apache Spark for processing large datasets" ([Learn](https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview)) | Apache Spark, Photon, serverless, SQL warehouses |
| Centre of gravity | Power BI, Microsoft 365, business analysts, "role-specific workloads" | ETL, ML, streaming, governance; "an unrivaled ETL experience" |

The important row is the table-format row. **Both products write Delta Lake onto ADLS Gen2 and
process it with Apache Spark.** Fabric's lakehouse documentation says you "store structured and
unstructured data in a single location, manage it with Delta Lake, and analyze it with both
Apache Spark and SQL". Fabric's warehouse "natively stores data in the open Delta Lake format".
A PySpark notebook writing a Delta table is the same skill in both products.

### Competitors or complements? Microsoft says complements, explicitly

Microsoft's Fabric documentation states it in one sentence:

> "Many organizations today register their data in Unity Catalog within Azure Databricks. A
> mirrored Unity Catalog in Fabric enables customer to read data managed by Unity Catalog from
> Fabric workloads. **Azure Databricks and Fabric are better together.**"
>
> — [Microsoft Fabric mirrored catalog from Azure Databricks](https://learn.microsoft.com/en-us/fabric/mirroring/azure-databricks)

Note the direction of travel. The Azure Databricks integration page makes it unmistakable:

> "Azure Databricks integrates with Microsoft Fabric in two ways. **Both result in Unity Catalog
> tables being in Fabric as a read-only mirrored catalog with no data movement.** The choice is
> mostly about which team drives the integration."
>
> — [Microsoft Fabric with Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/partners/bi/fabric)

Databricks writes. Fabric reads. One integration path (Fabric-initiated, "Mirrored Azure
Databricks catalog") is Generally Available; the other (Databricks-initiated, "Publish to
OneLake") is in Public Preview. Neither copies data: "Only the Azure Databricks catalog
structure is mirrored to Fabric and the underlying catalog data is accessed through shortcuts."

### What the Azure Architecture Center recommends

The reference article "Create a Modern Analytics Architecture by Using Azure Databricks" was
updated 2026-08-18 and is the clearest statement of Microsoft's own position
([source](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture)):

> "In this architecture, **Azure Databricks serves as the central tool for data ingestion,
> processing, and serving.** It provides a unified environment for managing the entire data life
> cycle."

Fabric's role in that same architecture is scoped tightly:

> "This architecture mirrors Unity Catalog tables into OneLake and uses Direct Lake mode in
> Power BI for better performance."

And the "use this architecture if you" list names the situation directly:

> "Have data engineers and data science teams that already use Azure Databricks for scalable
> data processing, advanced analytics, and machine learning."
> "Have analytics and business user communities that depend on Power BI for standardized,
> governed reporting and self-service insights."
> "Want to avoid data duplication or the creation of parallel pipelines solely to satisfy
> different analytics workloads."

That is Microsoft telling customers not to rebuild a Databricks pipeline in Fabric.

### Is Fabric displacing Databricks in enterprise?

There is no first-party evidence of displacement, and clear first-party evidence of growth on
both sides.

- Azure Databricks is a first-party Azure service, documented on Microsoft Learn under
  `/azure/databricks/`, available in `southafricanorth` — Johannesburg
  ([supported regions](https://learn.microsoft.com/en-us/azure/databricks/resources/supported-regions)).
- Databricks reported crossing "$7 billion revenue run-rate" with ">80% year-over-year growth",
  "over 1,000 customers at $1M+ revenue run-rate" and "20,000+ organizations", on 2026-08-13
  ([Databricks press release](https://www.databricks.com/company/newsroom/press-releases/databricks-grows-80-yoy-surpasses-7b-revenue-run-rate-scales)).
- Microsoft's FY26 Q4 earnings press release states "Azure revenue surpassed $100 billion for
  the first time" and does not mention Fabric at all
  ([Microsoft IR](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast)).
  **Unverified:** I could not find a Fabric customer count in any Microsoft press release I
  could reach. Fabric adoption figures circulate widely; none of the ones I found traced to a
  first-party document.

Coexistence, not displacement. Microsoft ships the mirroring, Microsoft ships the architecture
that puts Databricks at the centre, and Microsoft sells Azure Databricks.

One thing that is *not* true, and the curriculum currently implies it: that Microsoft's
certification path abandoned Databricks. It did, for about eighteen months, and then it
shipped DP-750. See Part 3.

### Azure Synapse

Still in support. Microsoft's lifecycle page lists Azure Synapse Analytics with a start date of
11/16/2022 and a retirement date of "In Support"
([Microsoft Lifecycle](https://learn.microsoft.com/en-us/lifecycle/products/azure-synapse-analytics)).
Individual components have been retired — Synapse Data Explorer (preview) was retired on
2025-10-07 with migration guidance to Fabric Eventhouse
([Learn](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/migrate-synapse-data-explorer))
— but the service as a whole has no announced end date. Do not write that Synapse is dead. It
is in 28% of the SA listings I read, usually alongside Fabric, in mid-migration.

---

## Part 2 — What South African listings actually ask for

**Snapshot taken 2026-09-23. It will go stale. It is not statistically rigorous.**

47 listings whose body text was read in full. Listing post-dates run 2026-03-16 to 2026-09-21,
majority July to September 2026. Boards that were readable: IT-Online, Datafin,
ExecutivePlacements, PNet, CareerJunction, Hire Resolve, e-Merge. Boards that were not:
Careers24 (HTTP 403), Indeed SA (HTTP 403), OfferZen (404 on both job-board paths), GoldmanTech
(connection refused), JobMail (search returned unrelated roles). LinkedIn returned 60 SA job
titles but no body text, so **zero LinkedIn listings are in these counts**.

### Frequency, out of 47 listings read

| Technology | Count | Share |
|---|---|---|
| SQL | 42 | 89% |
| Python | 34 | 72% |
| Azure | 28 | 60% |
| Spark / PySpark | 22 | 47% |
| AWS | 18 | 38% |
| Azure Data Factory | 17 | 36% |
| **Microsoft Fabric** | **15** | **32%** |
| Power BI | 15 | 32% |
| **Databricks** | **14** | **30%** |
| Azure Synapse | 13 | 28% |
| Kafka | 13 | 28% |
| GCP | 9 | 19% |
| Airflow | 7 | 15% |
| Snowflake | 6 | 13% |
| Hadoop | 6 | 13% |
| SSIS (legacy ETL) | 5 | 11% |
| Delta Lake | 5 | 11% |
| Java | 5 | 11% |
| Terraform | 3 | 6% |
| Unity Catalog | 3 | 6% |
| Scala | 3 | 6% |
| Apache Iceberg | 1 | 2% |
| Dagster | 1 | 2% |
| dbt | 1 | 2% |
| Flink | 1 | 2% |
| Kestra | 0 | 0% |
| DuckDB | 0 | 0% |
| Informatica | 0 | 0% |

### The listing text itself

Fabric named as a first-class platform, with a hard gate:

> "Candidates without demonstrable, hands on Fabric delivery experience will not be
> considered." … "moving workloads from platforms such as Teradata and on premises SQL Server
> into Fabric and Azure." … "Apply AI native engineering practices to accelerate delivery,
> including agentic workflows and the Model Context Protocol." … "Relevant Microsoft
> certifications in the Fabric, Azure data or Power BI tracks."
>
> — Senior/Lead Fabric Data Engineer, 2026-09-14
> ([IT-Online](https://it-online.co.za/2026/09/14/senior-lead-fabric-data-engineer-microsoft-fabric-lakehouse-data-factory-power-bi-dax-remote/))

Databricks named with real depth — the single most current Databricks-native listing in the
sample:

> "Platform: Azure Databricks (Serverless + SQL Warehouses + Instance Pools)" … "Languages:
> Python (primary), SQL (heavy — aggregation scripts), some Trino SQL" … "Data: Unity Catalog,
> Delta Lake" … "Orchestration: Lakeflow Jobs (parameterised multi-task DAGs, task values,
> run_job_task chaining)" … "SDKs: Databricks SDK, databricks-SQL-connector, Pandas" …
> "Relevant certifications (e.g. TOGAF, CDMP, DAMA-DMBOK)."
>
> — Data Engineer, 2026-07-24
> ([IT-Online](https://it-online.co.za/2026/07/24/data-engineer-365/))

Both platforms in one listing, which was common:

> "Build solutions using Azure, Microsoft Fabric, Databricks, Azure Data Factory, Synapse,
> Python, PySpark, and SQL"
>
> — Data Engineer (Cloud), 2026-07-23
> ([IT-Online](https://it-online.co.za/2026/07/23/data-engineer-cloud-gauteng-johannesburg/))

> "Databricks (PySpark, Delta Lake, Unity Catalog, Delta Live Tables, Workflows, SQL & ML)" and
> "Microsoft Fabric (OneLake, Lakehouse, Warehouse, Semantic Models, Direct Lake, Pipelines)"
> … "Cloud certifications (AWS, Microsoft, Databricks preferred)"
>
> — Data Engineers x 5
> ([PNet](https://www.pnet.co.za/jobs--Data-Engineers-x-5-Johannesburg-or-Cape-Town-cloudandthings-io--4186302-inline.html))

Legacy is still being hired as "Data Engineer" in September 2026:

> "Senior SQL / Database Engineer to join their team. The ideal candidate will bring extensive
> hands-on experience in SQL Server, T-SQL, SSIS, ETL, Oracle..." … "Strong knowledge of
> analytic and data platforms such as Denodo, Netezza, Ab Initio, Tableau, Power BI, QlikView,
> Qlik Sense, Python, Oracle, AWS Data Analysis, Snowflake/Snowpark"
>
> — Data Engineer, Centurion, 2026-09-21, R530.00 per hour, six-month renewable contract
> ([IT-Online](https://it-online.co.za/2026/09/21/data-engineer-370/) ·
> [CareerJunction](https://www.careerjunction.co.za/data-engineer-job-2645311.aspx))

The only dbt mention in the whole sample:

> "Airflow, dbt" … "Great Expectations, Marquez, Monte Carlo" … "Docker, Terraform"
>
> — Senior Data Engineer (AI-Driven Engineer), 7–8 years
> ([Datafin](https://datafin.com/jobs/senior-data-engineer-ai-driven-engineer-cpt-hybrid/))

The only Dagster mention, and one of only five Delta Lake mentions:

> "6+ years of experience with Spark/PySpark" … "code-first orchestration (Airflow, Dagster)"
> … "Medallion Architecture (Bronze/Silver/Gold) layers with Delta Lake"
>
> — Senior Data Engineer (Spark & Python Specialist), 2026-03-16
> ([IT-Online](https://it-online.co.za/2026/03/16/senior-data-engineer-spark-python-specialist/))

The only Iceberg mention, in a JVM role:

> "Apache Iceberg", alongside "Java, Scala, Gradle, Maven, HDFS, AWS (S3, EKS/Kubernetes), GCP,
> Azure, Databricks" … "large-scale data migrations across multi-petabyte datasets"
>
> — Senior Java Engineer (Data Engineering), 10–12 years
> ([Datafin](https://datafin.com/jobs/senior-data-engineer-java-scala-cpt-hybrid/))

And the sentence that says most about where 2026 is going:

> "Experience specifically with Claude Code." … "Build LLM-powered workflows and agentic AI
> solutions using: Tool calling, Structured outputs, Retrieval-Augmented Generation (RAG), API
> and database integrations" … "Experience building agentic workflows involving: Tool use, Task
> decomposition, Retrieval systems, Memory, Human-in-the-loop workflows"
>
> — Claude Code AI Data Engineer (Agentic AI & Large-Scale Data), remote, R650 per hour
> ([e-Merge](https://e-merge.co.za/claude-code-ai-data-engineer-agentic-ai-large-scale-data-remote-r650-per-hour-2/))

### What the counts mean, and what they do not

**The near-zero counts are the most trustworthy numbers here.** dbt, Airflow, Dagster, Iceberg
and Snowflake were all searched for by name, and the searches still returned almost nothing.
The "modern data stack" that dominates US and European postings is a rounding error in South
Africa. Absence of Kestra and DuckDB is weaker evidence, because they were not searched by
name.

**The Fabric, Databricks and Synapse counts are upward-biased.** Some of the searches that
assembled this sample contained those words. Most of the sample was harvested by enumerating
generic "data engineer" listings in date order, but the bias is real and unquantified. Do not
read 32% as market share.

Salary, where stated — only e-Merge, ExecutivePlacements and Hire Resolve publish numbers:
R840,000, R900,000, R950,000, R1.08m and R1.2m per annum for senior roles; R530 and R650 per
hour for contract. POPIA is named in at least five listings. Two banking listings require a
"clear criminal and credit record".

### Sample caveats, stated plainly

1. **Board skew.** 21 of 47 came from IT-Online alone, an aggregator of agency listings. Direct
   employers are badly under-represented.
2. **The employers I could not read are the ones that matter most.** LinkedIn's index showed
   the SA banking, insurance and FMCG employers hiring directly. None of that segment is in any
   count.
3. **OfferZen's absence probably depresses dbt, Airflow, Snowflake and Terraform**, because it
   skews startup and scale-up.
4. **Template reuse inflates counts.** Three listings carried near-identical technology lists
   (Azure + Fabric + ADF + Databricks + Synapse + Python + PySpark + Ab Initio + Kafka). Likely
   one client brief circulated by different agencies. That alone could move Fabric and
   Databricks by up to three each — which is the entire gap between them.
5. **Deduplication was a judgement call.** Roughly 60 pages collapsed to 47 unique roles. A
   reader recomputing from the URLs could reasonably land on 45–48.

---

## Part 3 — Certifications: status, and what employers actually name

### Status, verified against the vendor's own certification page

| Certification | Exam | Status on 2026-09-23 | Source |
|---|---|---|---|
| Azure Data Engineer Associate | DP-203 | **Retired 2025-03-31**, 11:59 PM CST. "This certification and the renewal assessment are retired." | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-engineer/), [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-203) |
| **Azure Databricks Data Engineer Associate** | **DP-750** | **Live**, bookable via Pearson VUE, 120 min, English only. Updating 2026-10-19. | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/implementing-data-engineering-solutions-using-azure-databricks/) |
| Fabric Data Engineer Associate | DP-700 | Live, 100 min, updating 2026-10-19 | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/) |
| Fabric Analytics Engineer Associate | DP-600 | Live, 100 min, 12-month renewal | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-analytics-engineer-associate/) |
| Azure Data Fundamentals | DP-900 | Live, 45 min, fundamentals do not expire | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) |
| Azure Developer Associate | AZ-204 | **Retired.** "This certification and the renewal assessment are retired." No date published. | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/) |
| Azure AI Engineer Associate | AI-102 | **Retired.** Same banner. No date published. | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/) |
| Azure Solutions Architect Expert | AZ-305 | Live. Requires Azure Administrator Associate first. Updated 2026-04-17. | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) |
| Identity and Access Administrator | SC-300 | Live, 100 min, 12-month renewal | [cert page](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/) |
| Certified Associate Developer for Apache Spark | — | Live. $200. 90 min, 45 questions, 2-year validity. Spark Connect is 5% of the exam. | [exam page](https://www.databricks.com/learn/certification/apache-spark-developer-associate) |
| Databricks Certified Data Engineer Associate | — | Live. $200. 90 min, 45 questions, 2-year validity. A shorter renewal exam exists. | [exam page](https://www.databricks.com/learn/certification/data-engineer-associate) |
| Databricks Certified Data Engineer Professional | — | Live. $200. 120 min, 59 questions, 2-year validity. | [exam page](https://www.databricks.com/learn/certification/data-engineer-professional) |
| Databricks Certified Generative AI Engineer Associate | — | Live. $200. 90 min, 45 questions. | [exam page](https://www.databricks.com/learn/certification/genai-engineer-associate) |
| Databricks Certified Context Engineer Associate | — | **New in 2026.** Live. $200. Context for agent systems. | [exam page](https://www.databricks.com/learn/certification/context-engineer-associate) |
| AWS Certified Data Engineer – Associate | DEA-C01 | Live. $150. 130 min, 65 questions, 3-year validity. | [cert page](https://aws.amazon.com/certification/certified-data-engineer-associate/) |
| AWS Certified Data Analytics – Specialty | DAS-C01 | **Retired.** Page 301-redirects to the catalogue; absent from the list. | [AWS catalogue](https://aws.amazon.com/certification/) |
| HashiCorp Terraform Associate | 004 | Live. $70.50. 1 hour. Tests Terraform 1.12. 2-year validity. **003 is no longer offered.** | [cert page](https://developer.hashicorp.com/certifications/infrastructure-automation) |
| Apache Airflow 3 Fundamentals | — | Live. **$150, not free.** 75 questions, 60 min, 70% pass. One attempt per purchase. Badge never expires. | [Astronomer](https://www.astronomer.io/certification/) |
| Apache Airflow 3 DAG Authoring | — | Live. $150. Same format. | [Astronomer](https://www.astronomer.io/certification/) |
| dbt Analytics Engineering Certification | — | Live. $200. 2-year validity. | [dbt Labs](https://www.getdbt.com/dbt-certification) |
| dbt Architect Certification | — | Live. $200. There is no "dbt Developer" certification. | [dbt Labs](https://www.getdbt.com/dbt-certification) |
| SnowPro Core | **COF-C03** | Live. $175. Note the code — not C02. | [Snowflake](https://learn.snowflake.com/en/certifications/snowpro-core-c03/) |
| SnowPro Advanced: Data Engineer | **DEA-C02** | Live. $375. Note the code — not C01. | [Snowflake](https://learn.snowflake.com/en/certifications/snowpro-advanced-dataengineer-C02/) |
| Confluent CCDAK / CCAAK / CCAC | — | Live. 2-year validity. Prices not published. | [Confluent](https://www.confluent.io/certification/) |
| Apache Iceberg, Delta Lake | — | **No official certification exists** for either. Apache issues none; Delta Lake is Linux Foundation-hosted with none. | — |

Renewal policy matters more than most people notice. Microsoft: annual, free, unproctored,
open-book, six-month window; fundamentals never expire
([renewal page](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification)).
Databricks: "A Databricks Certification is valid for two years from the date it is awarded"
and "To recertify, you will need to take the full current live exam"
([FAQ](https://www.databricks.com/learn/certification/faq)) — at $200 a time. Astronomer never
expires. That asymmetry should shape which ones are worth sitting.

### Corrections to widely repeated beliefs

- **The Databricks Spark exam was not retired and not renamed.** The page title still reads
  "Databricks Certified Associate Developer for Apache Spark". What changed is that the Spark
  version suffix was dropped entirely — there is no "3.0" any more — and Spark Connect and the
  Pandas API were added to the content. The exam guide states: "This version covers the
  currently live version as of Oct 30, 2025."
- **There is no Databricks Platform Administrator *certification*.** It is a free
  *accreditation*, valid one year, unproctored
  ([page](https://www.databricks.com/learn/certification/platform-administrator-accreditation)).
- **Terraform Associate is on 004, not 003.**
- **SnowPro codes have moved on** to COF-C03 and DEA-C02.

### Which certifications employers actually name

Two separate exercises. A random baseline — 28 data engineer listings pulled by title only, not
by certification keyword, read in full. And a keyword-forced search, which answers "does this
exist at all" rather than "how often".

**The random baseline is the finding.** Of 28 listings read end to end, 6 named any
certification — about 21%. South Africa 6 of 21 (29%), remote-global 0 of 7 (0%). And **all six
SA mentions were generic**: "Certifications, such as: AWS Certification, Microsoft
Certification, Databricks Certification"; "Relevant Microsoft Fabric and/or Azure data
certification."; "Relevant Cloud or Data Engineering certifications advantageous"; "Cloud Data
Certifications"; "Relevant Microsoft certifications in the Fabric, Azure data or Power BI
tracks" (twice). **Not one randomly-sampled listing named a specific exam code.**

The clearest single sentence in the whole certification search is a recruiter telling
candidates not to gate themselves:

> "DP-700 (Fabric Data Engineer Associate) or another relevant Microsoft certification. **These
> are valued rather than required and are achievable after appointment.**"
>
> — Data & AI Engineer (JHB Hybrid), under the heading "ADVANTAGEOUS"
> ([Datafin](https://datafin.com/jobs/data-ai-engineer-jhb-hybrid/))

Where specific exams do appear, they appear as a menu:

> "DP-700 (Fabric Data Engineer)" / "DP-203 / DP-600" — listed under "Advantageous"
>
> — Microsoft Fabric Specialist
> ([Datafin](https://datafin.com/jobs/microsoft-fabric-specialist-data-engineering-governance-dwh-onsite-jhb-contract/))

> "Any of the following certifications: AWS Certified Data Engineer - Associate / … /
> Databricks Certified: Data Engineer Associate / Databricks Certified: Data Engineer
> Professional / … Microsoft Certified: Azure Data Engineer Associate (DP-203) / … Microsoft
> Certified: Fabric Data Engineer Associate (DP-700) / … Microsoft Certified: Azure Solutions
> Architect Expert (AZ-305)" — under "Desired Experience & Qualification"
>
> — Senior Data Engineer, remote SA
> ([PNet](https://www.pnet.co.za/jobs--Senior-Data-Engineer-South-Africa-cloudandthings-io--4089125-inline.html))

Exact-phrase counts across PNet's whole board on 2026-09-23, against a baseline of 3,988 "Data
Engineer" results:

| Phrase | Listings containing it | Note |
|---|---|---|
| "AWS Certified Data Engineer" | 5 | |
| "Databricks Certified" | 5 | of which "Databricks Certified Data Engineer" = 2 |
| DP-203 | 3 | **still named, eighteen months after retirement** |
| DP-700 | 3 | |
| "Azure Data Engineer Associate" | 3 | one of them framed as "required or in progress" |
| DP-600 | 2 | |
| DP-900 | 1 | |
| AI-102 | 7 | only 2 data/AI-engineering relevant |
| AZ-305 | 2 | both solutions-architect roles, zero data engineering |
| AZ-204 | 8 | **zero** data engineering |
| SC-300 | 13 | **zero** data engineering |
| "Terraform Associate" | 12 | essentially all DevOps/SRE; 1 data-adjacent |
| SnowPro | 0 | |
| "dbt certified" | 0 | |
| Airflow / Astronomer certification | 0 | none found anywhere |
| "Microsoft Fabric" | 55 | of which only ~4 name DP-700 |

That last row is the one to keep. **Fifty-five SA listings want Fabric; four want the Fabric
exam.** Employers hire for the product far faster than they name the exam.

Globally, the one credential confirmed in the most distinct listing bodies was SnowPro — which
is noise from a Snowflake-titled search skew, not a signal, and several of those postings were
already removed. The single cleanest global framing was:

> "Hold or are actively pursuing a Databricks certification (Data Engineer Associate or
> Professional, or Apache Spark Developer)" — under the heading "Bonus points if you…"
>
> — Senior Data Engineer (Databricks), remote USA
> ([Greenhouse](https://job-boards.greenhouse.io/livefront/jobs/4395671009))

**DP-750 appeared in zero listings.** It is too new. **Unverified:** whether that changes.

---

## Part 4 — Rising and fading, labelled the `horizon/` way

Three labels, per `horizon/README.md`: **Happening** — in production at companies now.
**Consolidating** — clearly winning, still early. **Noisy** — loud, unproven, might be nothing.

### Open table formats: the war ended in a merge

**Happening.** Delta and Iceberg have converged on each other's feature sets and are now
interoperable through catalogs rather than through file formats.

The Apache Iceberg spec now defines four format versions. Version 3 — "Extended Types and
Capabilities" — adds "New data types: nanosecond timestamp(tz), unknown, variant, geometry,
geography", "Row Lineage tracking" and "Binary deletion vectors"
([Iceberg spec](https://iceberg.apache.org/spec/)). Those are the features Delta shipped first.
Version 4, "Metadata Structure and Representation", restructures metadata for performance —
and Databricks has proposed that "the next version of Delta, Delta 5.0, adopts the adaptive
metadata tree structure" from Iceberg v4
([Databricks blog, 2026-05-28](https://www.databricks.com/blog/unity-catalog-and-next-era-apache-icebergtm)).
The formats are now copying each other in both directions.

On Databricks, Delta remains the default and Iceberg is opt-in: "To create an Apache Iceberg
table, explicitly specify `USING iceberg`. Otherwise, Azure Databricks creates a Delta Lake
table by default."
([Learn](https://learn.microsoft.com/en-us/azure/databricks/tables/managed)). Interop happens
at the catalog: "Iceberg REST Catalog (IRC) has read, write, and create access for Apache
Iceberg clients to managed tables using Apache Iceberg and read-only access to Delta Lake
tables with Apache Iceberg reads enabled."

Delta Lake 4.0 (2025-06-09) introduced "Preview support for catalog-managed tables, a new table
feature that transforms Delta Lake into a catalog-oriented lakehouse table format", Delta
Connect, and the Variant type. It also sunset the old connectors: "Delta Standalone and its
dependent connectors, including Delta Flink and Delta Hive, are no longer under active
development"
([release notes](https://github.com/delta-io/delta/releases/tag/v4.0.0)). Delta 4.4.0 landed
2026-08-20 with Spark 4.2 support
([release notes](https://github.com/delta-io/delta/releases/tag/v4.4.0)).

GitHub stars, 2026-09-23: `apache/iceberg` 9,265; `delta-io/delta` 9,017. Neither is winning.
Latest releases: Iceberg 1.11.0 (2026-05-20), Delta 4.4.0 (2026-08-20).

**What this means for the curriculum:** learning Delta properly and reading Iceberg as the
comparison — which is exactly what Phase 4 already says — is correct. The differentiating
knowledge has moved from "which format" to "what a catalog commit is and why it matters".

### Spark 4: real, and it breaks migrations

**Happening.** Spark 4.0.0 released 2025-05-23; the line is now at 4.2.0 (2026-07-14), with
3.5.9 still shipping as maintenance ([Spark news](https://spark.apache.org/news/)).

Two things matter for a T-SQL replatform. First, **`[SPARK-44444]` Use ANSI SQL mode by
default** ([4.0.0 release notes](https://spark.apache.org/releases/spark-release-4-0-0.html)) —
silent-null-on-overflow behaviour is gone, which changes parity results. Second, Spark Connect
matured: a "New lightweight Python client (`pyspark-client`) at just 1.5 MB", a
`spark.api.mode` configuration, and ML on Spark Connect. Spark Connect is 5% of the Databricks
Spark developer exam.

Spark 4.2.0 adds "Arrow-optimized Python UDFs and Arrow-based PySpark IPC are now enabled by
default", geospatial types, and "a SQL `CHANGES` clause plus DataFrame/PySpark/Connect APIs to
read row-level changes in batch and streaming, and Auto CDC (declarative SCD Type 1) in Spark
Declarative Pipelines"
([4.2.0 release notes](https://spark.apache.org/releases/spark-release-4-2-0.html)).

**The important one:** Databricks donated Delta Live Tables to Apache Spark as **Spark
Declarative Pipelines**, shipped in Spark 4.1
([Databricks press release](https://www.databricks.com/company/newsroom/press-releases/databricks-donates-declarative-pipelines-apache-sparktm-open-source)).
On Databricks it is now called Lakeflow Spark Declarative Pipelines; DLT is gone as a name
([Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture)).
Declarative pipelines are now learnable on open-source Spark, without a Databricks account.

### Orchestration: Airflow absorbed the argument

**Happening — and this changes a `horizon/` prediction.** The 2026-Q3 entry listed "declarative
and asset-based orchestration over imperative DAGs" as Consolidating, with "partitions, lineage
and invalidation as first-class concepts". That was Dagster's differentiator. Airflow has now
taken it.

- Airflow 3.0.0, 2025-04-22.
- Airflow 3.1.0, 2025-09-25: human-in-the-loop tasks that "pause in a deferred state while
  presenting intuitive web forms in the Airflow UI"
  ([blog](https://airflow.apache.org/blog/airflow-3.1.0/)).
- Airflow 3.2.0, 2026-04-07: asset partitioning.
- Airflow 3.3.0, 2026-07-06: "a first-class state store for tasks and assets (AIP-103), a
  Language Task SDK for writing tasks in Java and Go (AIP-108), a major expansion of asset
  partitioning, and pluggable retry policies"
  ([blog](https://airflow.apache.org/blog/airflow-3.3.0/)). New partition mappers —
  `RollupMapper`, `FanOutMapper`, `FixedKeyMapper` with `SegmentWindow` — compose with time
  windows and a `wait_policy`.
- 3.3.2 on 2026-09-17. `apache/airflow` at 46,949 stars.

Dagster is healthy but much smaller (16,193 stars, releasing weekly). Kestra shipped 2.0 on
2026-09-22 — a control-plane/data-plane split, stateless gRPC workers, an MCP server that
"exposes flows as tools AI agents can call", and LTS status
([Kestra](https://kestra.io/blogs/release-2-0)). It is a genuinely interesting product with
28,264 stars and **zero SA job listings**.

**Verdict for the curriculum: Airflow, unchanged.** Phase 4 should learn Airflow 3 assets and
partitions, not Airflow 2 schedules. Dagster and Kestra are worth one paragraph of comparison
and no build time.

### dbt versus SQLMesh: the debate ended when one company bought both

**Happening, and genuinely surprising.** Fivetran acquired Tobiko Data, the company behind
SQLMesh and SQLGlot, on 2025-09-03
([press release](https://www.fivetran.com/press/fivetran-acquires-tobiko-data-to-power-the-next-generation-of-advanced-ai-ready-data-transformation)).
Fivetran then completed its merger with dbt Labs on 2026-06-01
([press release](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents)).
One company now owns both sides of the transformation-framework argument. The GitHub repository
`TobikoData/sqlmesh` now redirects to `SQLMesh/sqlmesh`.

The merger shipped "the open sourcing of the dbt Fusion engine runtime, released as dbt Core
v2.0 under an Apache 2.0 license". dbt's own documentation describes the generations plainly:
"**v1** - The original Python-based generation of dbt, still maintained as dbt v1", while
"Today, the current Rust-based version generation is v2" and "v2 is the default experience when
you install dbt"
([dbt docs](https://docs.getdbt.com/docs/fusion/about-fusion)). No deprecation date is published
for v1.

And on 2026-09-22 — yesterday — "dbt v2, which runs on the new Rust-based Fusion engine, is the
first dbt release that ships with a built-in DuckDB adapter", with "support for DuckLake and
Iceberg catalogs, queryable Parquet-formatted metadata, native SQL comprehension with
column-level lineage"
([DuckDB](https://duckdb.org/2026/09/22/dbt-fusion.html)).

**For the curriculum:** dbt is still the thing to learn, but it is now a Rust binary with
column-level lineage built in, not a Python package. SQLMesh is a comparison, not a fork in the
road. And dbt appeared in exactly 1 of 47 SA listings — so it is a module, not a phase.

### Catalogs: the actual battleground

**Happening.** The horizon entry called this right: "Metadata is the scaling problem, not
data."

- **Unity Catalog** is the governance layer on Databricks and the thing DP-750 spends 15–20% of
  its exam on. Unity Catalog managed tables are "the default and recommended table type"
  ([Learn](https://learn.microsoft.com/en-us/azure/databricks/tables/managed)).
  The open-source `unitycatalog/unitycatalog` is at 3,536 stars, v0.6.0 released 2026-08-20.
- **Apache Polaris** graduated to a Top-Level Project
  ([announcement](https://polaris.apache.org/blog/2026/02/19/apache-polaris-graduates-to-top-level-project/)).
  It is "an open-source, fully-featured catalog for Apache Iceberg" implementing the REST API.
  Latest release 1.7.0, 2026-08-02. 2,064 stars.
- **Hive Metastore is fading on a published timeline.** Databricks: "The per-workspace Hive
  metastore is a legacy feature" and "Databricks recommends that you migrate those tables and
  the workloads that reference them to Unity Catalog and disable direct access to the Hive
  metastore"
  ([Learn](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/hive-metastore)).
  New workspaces stop being provisioned with it from 2026-09-30 — a week from now.
  **Unverified:** I could not find a published end-of-support date for existing workspaces.

The Phase 4 module list already names "catalog concepts — Hive Metastore, Unity Catalog". That
is right, but the weighting should flip: Unity Catalog and the Iceberg REST Catalog are the
live material; Hive Metastore is history you need to recognise in a legacy estate.

### Single-node: DuckDB is no longer the small option

**Happening, and the December check-in question is already answered.** The Q3 horizon asked
"Did single-node processing keep gaining, or did it plateau?" It kept gaining, hard.

`duckdb/duckdb` is at 41,645 stars against `apache/spark`'s 44,030. Latest release tag v1.5.5
(2026-07-22), with v1.4 as LTS and v2.0 in alpha as of 2026-09-02
([DuckDB news](https://duckdb.org/news/)). **DuckLabs, the company behind DuckDB, is joining
AWS as a subsidiary** — announced 2026-08-26, with the nonprofit DuckDB Foundation continuing
to steward the projects and the commitment that "DuckDB, DuckLake, Quack, and all the other
extensions will remain free and open source software under the MIT license"
([announcement](https://duckdb.org/2026/08/26/ducklabs-to-join-aws.html)).

DuckLake — "an integrated data lake and catalog format" that "delivers advanced data lake
features without traditional lakehouse complexity by using Parquet files and a SQL database" —
is at v1.0, described as "a production-ready release with guaranteed backward-compatibility",
and its Parquet files are "compatible with Iceberg"
([ducklake.select](https://ducklake.select/)). **Unverified:** I could not pin the v1.0 release
date to a single consistent primary source; the site and the DuckDB news index disagree.

**Label DuckLake Consolidating, not Happening.** Zero SA listings. But DuckDB itself is now the
default answer to "does this need distribution", and the Phase 4 DuckDB-versus-Spark benchmark
is more defensible than when it was queued.

### Streaming

**Happening.** Kafka 4.0.0 (2025-03-18) removed ZooKeeper entirely: "Apache Kafka 4.0 only
supports KRaft mode - ZooKeeper mode has been removed"
([release announcement](https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/)).
Clusters must migrate to KRaft before upgrading. Kafka is now at 4.3.1 with 4.4.0 in release
candidate. KIP-932 share groups — queue semantics over Kafka topics — arrived in early access.

Flink 2.0.0 released 2025-03-24; the line is at 2.3.0 (2026-06-25)
([Flink downloads](https://flink.apache.org/downloads/)). Redpanda is at v26.2.2 (2026-08-22)
and remains a drop-in Kafka API — which is why Phase 5's choice of Redpanda-in-Docker is still
the cheapest way to learn the Kafka protocol.

Kafka is in 28% of SA listings. Flink is in one. **Learn the Kafka protocol; treat Flink as
reading.**

### LLM and agent tooling in data work

This is where the labelling matters most, because the gap between what shipped and what is
claimed is very wide.

**Happening — agents as governed consumers of data.** Databricks ships managed MCP servers that
"connect your AI agents to data in Unity Catalog, Databricks AI Search indexes, Genie Agents,
and custom functions", with "Unity Catalog enforces permissions, so agents and users access
only the tools and data you grant them"
([Learn](https://learn.microsoft.com/en-us/azure/databricks/agents/mcp-tools/managed-mcp)).
The Genie One MCP server is generally available
([Databricks](https://www.databricks.com/blog/genie-one-mcp-now-generally-available)). Kestra
2.0 exposes flows as agent tools. This pattern — the catalog as the authorization boundary for
an agent — is real, shipped, and is the single most transferable thing to learn.

**Happening — assistants inside the authoring loop.** DuckDB shipped a Claude Code plugin on
2026-09-16 so an agent can "read data files, run queries, convert formats, explore object
storage" with SQL instead of "writing Python scripts to examine files, which was slow and
involved guessing column names and types without verification"
([DuckDB](https://duckdb.org/2026/09/16/duckdb-skills.html)). dbt v2 ships column-level lineage
so a model can reason about a project. And two SA listings now name Claude Code by name.

**Consolidating — LLM steps as ordinary orchestrated tasks.** Airflow's `common-ai` provider
adds "6 operators, 5 toolsets, and 20+ model providers in one package", including
`LLMSQLQueryOperator` and `LLMSchemaCompareOperator`, and "Every LLM task logs token usage and
tool calls to Airflow's metadata DB"
([Airflow](https://airflow.apache.org/blog/common-ai-provider/)). Airflow's own argument for
why this belongs in an orchestrator is worth quoting, because it is the honest version:

> "Each sub-query becomes a named task. The fan-out is Dynamic Task Mapping… Every step is
> observable, independently retryable, and logged." … contrasted with an agent harness, where
> "Each tool call is invisible to any outside observer. If one tool call fails, the loop either
> retries internally or fails entirely."
>
> — [Agentic Workloads on Airflow, 2026-04-15](https://airflow.apache.org/blog/agentic-workloads-airflow-3/)

Airflow keeps DAGs acyclic deliberately: that "prevents generative feedback loops that agent
systems support, but ensures execution is fully auditable and its failure modes predictable."

**Still Noisy — fully autonomous agentic pipelines.** The Q3 horizon called this and nothing has
falsified it. Every shipped primitive above is model-proposes, human-or-orchestrator-disposes:
human-in-the-loop tasks, independent retries, audit logs, permission boundaries. Nobody
credible shipped the loop that runs itself.

---

## The intersection: what all the evidence agrees on

| Question | Microsoft's docs | Apache/OSS release notes | SA job listings | Certification pages |
|---|---|---|---|---|
| Is Spark still the engine? | Yes — Fabric Data Engineering and Azure Databricks both run Spark | Spark 4.2.0, ANSI by default, SDP in 4.1 | 47% of listings | DP-700, DP-750 and the Databricks Spark exam all test it |
| Is Delta still the format? | Yes — Fabric lakehouse "manage it with Delta Lake"; Databricks default | Delta 4.4.0; Iceberg v3 adopted Delta's features | 11% name it explicitly; implied by Databricks/Fabric at 30/32% | Tested inside DP-750 and the Databricks DE exams; no standalone cert exists |
| Databricks or Fabric? | Both, "better together"; Databricks writes, Fabric reads | n/a | Fabric 32%, Databricks 30%, usually together | Microsoft now certifies both (DP-700, DP-750) |
| Is Airflow the orchestrator? | Fabric exam includes "Configure Apache Airflow workspace settings" | Airflow 3.3 took asset partitioning from Dagster | 15% — thin, but 7x Dagster and dbt | Astronomer, $150, never expires, named in zero listings |
| Is Iceberg replacing Delta? | No — Delta is the default, Iceberg is opt-in | Converging in both directions | 1 of 47 listings | No certification for either |
| Do certifications gate hiring? | n/a | n/a | ~21% name any; 0 of 28 random listings named an exam code | Vendors say yes; listings say "advantageous" |

Reduced to a sentence: **the engine, the format and the orchestrator in `CURRICULUM.md` are the
ones the market, the vendors and the Apache projects all still use; the only thing that moved is
which exam attests to them.**

---

## What I could not verify

Recorded honestly, because the rule is that an unreachable source is stated, not guessed.

**Job boards I could not read at all.** Careers24 (HTTP 403), Indeed SA (HTTP 403), OfferZen
(404 on `/job-board` and `/companies/jobs`), GoldmanTech (connection refused), JobMail (search
broken), WeWorkRemotely (403), RemoteOK (no rows returned), Dice (HTTP 410; a reader proxy
returned the title only), Wellfound and Otta (not reached). **LinkedIn returned job titles but
never a job body**, on any attempt, through any route. That is the single biggest hole: the SA
direct-employer market — banking, insurance, FMCG, telco — is visible only as titles and is
absent from every count in this file.

**One SA listing I could see only as a search snippet** claimed to require "Microsoft Certified:
Azure Data Engineer Associate and Databricks Certified Data Engineer". I could not open the
body, so it is excluded from every count. It was the only sighting of "Databricks Certified Data
Engineer" by exact name outside a keyword-forced search.

**Dates vendors do not publish.**

- Exact retirement dates for AZ-204 and AI-102. Both certification pages carry the retirement
  banner and publish no date; the "Learn more" link goes to a Microsoft blog, which this file's
  rules exclude. `/credentials/support/retired-certifications` returns 404.
- DP-700's launch date. Not on the certification page, the study guide, or the change log.
- DP-750's launch date. Not stated anywhere; the page does not even render a "Last Updated"
  value.
- AWS's retirement date for DAS-C01. The page 301-redirects away and the exam is absent from the
  catalogue; the commonly cited date comes only from the AWS blog.
- HashiCorp's retirement date for Terraform Associate 003.
- Microsoft exam prices in USD. Every page says only "Price based on the country or region in
  which the exam is proctored." **This matters for a South African budget and I could not
  resolve it.**

**Facts vendors do not state.**

- Snowflake's certification validity period. The FAQ page is JavaScript-gated and returns
  headings with no answers. The widely repeated "two years" could not be confirmed from a
  Snowflake page.
- Whether Astronomer's Airflow 2 exams are formally retired. `academy.astronomer.io` returns 403
  to automated fetches.
- Whether the SnowPro Associate tier was retired. Observed absent from the index; no statement
  found.
- A Spark version number for the Databricks Spark exam. Databricks publishes none.
- Any Microsoft Fabric customer count from a first-party document.
- DuckLake v1.0's release date, from a source that agrees with the other sources.

**Things I judged rather than measured.** Deduplicating ~60 listing pages to 47 unique roles.
Deciding that a fetcher's hedged "Microsoft Fabric (referenced in similar listings)" was not a
genuine mention. Counting one listing that was marked expired. Each is defensible and each
moves a number by one.

---

## What this changes in `CURRICULUM.md`

Proposed edits. Not applied — this file only argues for them.

### 1. Rewrite "What I am deliberately not taking"

The current paragraph is factually wrong in its premise and should be replaced. Proposed
replacement, in the page's own voice:

> **What moved, and what I am still not taking.** DP-203, the Azure Data Engineer certificate,
> was retired on 31 March 2025. For a while its only successor was DP-700, which examines
> Microsoft Fabric. Microsoft has since shipped **DP-750, Azure Databricks Data Engineer
> Associate**, which examines Unity Catalog, Lakeflow Spark Declarative Pipelines, Auto Loader,
> Delta `OPTIMIZE` and `VACUUM`, and Spark UI debugging — the Phase 4 and Phase 5 projects,
> examined. That is the Microsoft data badge this plan earns. DP-700 stays optional: it is not a
> different engine — Fabric runs Apache Spark over Delta Lake, and DP-700 tests PySpark,
> structured streaming and Airflow configuration — but it is a different product surface, and
> the plan does not build on it.

### 2. Add DP-750 to the certification table, at Phase 4

| Phase | Certification | Why it follows from the work |
|---|---|---|
| 4 | **Azure Databricks Data Engineer Associate (DP-750)** | Unity Catalog, Lakeflow SDP, Auto Loader, Delta optimisation, Spark UI. The replatform is the preparation, and it is the Azure-flavoured version of the Databricks exams already on this page |

### 3. Fix the two retired certifications

- **Phase 8: replace AZ-204.** It is retired. Its functional successor is **AI-200, Azure AI
  Cloud Developer Associate** (containerised solutions on Azure, Azure data management
  services, securing and monitoring). **Unverified** whether AI-200 is out of beta — its own
  page says the practice assessment is "not currently available". Sit nothing here until that
  resolves; Terraform Associate 004 is the certification that Phase 8 actually earns.
- **Phase 6: replace AI-102.** It is retired. Its functional successor is **AI-103, Azure AI
  Apps and Agents Developer Associate**. The Databricks Generative AI Engineer Associate
  remains the better match for the stack, and is the one to prefer.

### 4. Correct three details in the existing table

- Astronomer's Airflow certification is **$150 and gives one attempt per purchase**, not free.
  The badge never expires, which makes it good value per rand but bad value per mistake. It is
  named in **zero** job listings, SA or global. Demote it to optional.
- **HashiCorp Terraform Associate is 004** (tests Terraform 1.12, $70.50, two-year validity).
  003 is no longer offered.
- The **Databricks Spark developer exam no longer carries a version number**, and Spark Connect
  is 5% of it. The Phase 4 line already names Spark Connect, which is right; drop any "Spark
  3.0" phrasing if it appears elsewhere.

### 5. Add a Fabric module to Phase 4 — one module, not a pillar

Phase 4's module list should gain: *Fabric as the serving surface — OneLake, shortcuts,
mirroring a Unity Catalog into Fabric, Direct Lake, and why Microsoft's own architecture keeps
the pipeline in Databricks.* Justification: Fabric is in 32% of the SA listings read, "Azure
Databricks and Fabric are better together" is Microsoft's own sentence, and Microsoft's
reference architecture uses exactly this seam. The plan should be able to explain the seam
without building on it.

### 6. Sharpen the Phase 4 catalog module

Change "catalog concepts — Hive Metastore, Unity Catalog" to *catalogs — Unity Catalog, the
Iceberg REST Catalog, catalog-managed commits, and Hive Metastore as the legacy shape*. The Hive
metastore is a legacy feature; new Databricks workspaces stop being provisioned with it from
2026-09-30. The live skill is the catalog as the transaction and authorization boundary.

### 7. Add ANSI mode to the replatform module

Phase 4's "replatforming T-SQL to Spark SQL with parity evidence" should explicitly name **Spark
4's ANSI SQL mode, on by default**. It is the single most likely cause of a parity report that
disagrees with the shipped warehouse, and it is exactly the sort of thing a reviewer who wants
the report to be wrong will find.

### 8. Rename DLT wherever it appears

Delta Live Tables no longer exists as a name. It is **Spark Declarative Pipelines** in Apache
Spark 4.1 and **Lakeflow Spark Declarative Pipelines** on Databricks. This matters for Phase 4
because SDP is now open source, so declarative pipelines can be built and tested on local Spark
before touching a Databricks account.

### 9. Note the dbt change in the sources table

Phase 4's "dbt Learn for dbt" line should note that **dbt v2 is the Rust-based Fusion engine,
Apache 2.0, and is now the default install**; dbt v1 is "the original Python-based generation of
dbt, still maintained". dbt appeared in 1 of 47 SA listings, so this stays a module, not a
phase. The dbt certification is $200 and named in zero SA listings — move it from the Phase 4
certification row to optional.

### 10. Strengthen the "certifications are not gates" rule with evidence

The page already says certifications are not gates. It can now say so with a number: **of 28
data engineer listings read end to end, 6 named any certification and not one named a specific
exam code.** And it can quote a recruiter saying it outright — "These are valued rather than
required and are achievable after appointment." That sentence belongs on the page.

### 11. Queue one new module

Per `horizon/README.md`, a review with no queue change is entertainment. Proposed addition:
*the catalog as an authorization boundary for agents* — Unity Catalog permissions enforced
through a managed MCP server, and what an agent can and cannot reach. It sits at the exact
overlap of Phase 4 (governance), Phase 6 (agents and tool orchestration) and Phase 7 (policy
layer, audit log), it is shipped and documented rather than speculative, and it is the part of
the LLM-in-data-work story that is Happening rather than Noisy.

---

## Sources

Every URL is inline above. The load-bearing ones, grouped:

- **Fabric and Databricks, first-party:** the Fabric overview, the Fabric lakehouse overview,
  the Fabric Data Engineering overview, the "Microsoft Fabric with Azure Databricks" integration
  page, the "Mirrored catalog from Azure Databricks" page, the Unity Catalog managed tables
  page, and the Azure Architecture Center's "Create a Modern Analytics Architecture by Using
  Azure Databricks" (updated 2026-08-18).
- **Certifications:** each vendor's own certification page, listed in the Part 3 table. No
  summary articles were used.
- **Technology:** `spark.apache.org/news`, `airflow.apache.org/blog`, `iceberg.apache.org/spec`,
  `kafka.apache.org/blog`, `flink.apache.org/downloads`, `polaris.apache.org/blog`,
  `duckdb.org/news`, GitHub release notes for `delta-io/delta`, and the Fivetran and Databricks
  press releases named inline. GitHub star counts and release dates were read from the GitHub
  API on 2026-09-23.
- **Job listings:** the URLs quoted in Part 2 and Part 3. Boards that could not be reached are
  named in "What I could not verify".
