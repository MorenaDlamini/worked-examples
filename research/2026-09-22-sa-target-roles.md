# Target roles — three South African postings, what they actually ask for

Primary-source extraction of three postings, read in full on 2026-09-22. Everything quoted is
the posting's own wording. Where I am inferring rather than quoting, it is marked. Recruiter
contact details are deliberately omitted.

These three replace the OpenAI postings in `2026-09-17-openai-target-roles.md` as the source
of the requirements list in `CURRICULUM.md`. The OpenAI file remains the source for the
interview process and for the "production, not projects" bar, which these three restate.

## Why these three

They are the shape of role I want: Python-first, full-stack, on real cloud services, with AI
integration as a requirement and data as the differentiator. Two are product-engineering roles
with AI attached; one is a data-platform role with AI as a plus. Together they cover all four
pillars, and none of them is a research role.

---

## Role 1 — Python / Spark / AI Developer

[Posting on PNet](https://www.pnet.co.za/jobs--Python-Spark-AI-Developer-Cape-Town-Hire-Resolve--4264563-inline.html) ·
[Mirror on IT-Online](https://it-online.co.za/2026/09/02/python-spark-ai-developer-western-cape-cape-town/)

| Field | Value |
|---|---|
| Exact title | Python / Spark / AI Developer |
| Location | Cape Town, Western Cape |
| Recruiter | Hire Resolve, on behalf of an unnamed client |
| Salary | "highly competitive salary for this role based on experience" — no number |

The posting describes "a growing technology team" and the work as "developing scalable data
pipelines, replatforming legacy SQL workloads onto modern Spark and lakehouse technologies,
and supporting the development of APIs and AI-driven features".

### Key responsibilities (verbatim)

- Build Spark/PySpark data pipelines using Delta Lake.
- Replatform legacy T-SQL logic into Spark SQL.
- Develop modern, type-safe and well-tested Python applications.
- Build REST APIs using FastAPI or equivalent frameworks.
- Implement authentication, idempotency and job-status functionality.
- Validate migrated pipelines against legacy systems and provide parity evidence.
- Work from technical specifications, design documents and ADRs.
- Develop automated tests using pytest.
- Contribute to CI/CD pipelines, code reviews and technical documentation.

### Minimum requirements (verbatim)

- 4+ years of professional Python development experience.
- 2+ years of production experience with Apache Spark / PySpark.
- Strong knowledge of Spark SQL and DataFrame APIs.
- Production experience with Delta Lake or equivalent technologies such as Iceberg or Hudi.
- Strong SQL skills and experience working with legacy T-SQL.
- Experience with pytest and automated testing.
- Experience developing REST APIs, preferably with FastAPI.
- Experience with Docker and containerised development environments.
- Strong Git and CI/CD experience.
- Experience with type-hinted Python and static analysis tools such as Pyright or Mypy.
- Experience with modern Python tooling such as uv or Poetry.
- Ability to work independently from written technical requirements and design documentation.
- Bachelor's degree in Computer Science, Engineering or a related field, or equivalent
  experience.
- Proven track record of delivering production Python/Spark pipelines independently.

### Advantageous skills (verbatim)

- Experience with LLM / AI integration.
- Experience with Ollama, vLLM, LM Studio or hosted AI APIs.
- Knowledge of data governance, privacy engineering and POPIA/GDPR principles.
- Experience with Hive Metastore, Trino or Apache Ranger.
- Azure experience, including ADLS Gen2, Synapse, ADF, Key Vault or Service Bus.
- Experience with structured logging, OpenTelemetry or OpenLineage.
- Data migration and pipeline parity testing experience.
- Databricks Certified Developer for Apache Spark or equivalent certification.

### Named technologies

Python, PySpark, Spark SQL, Delta Lake, Iceberg, Hudi, T-SQL, pytest, FastAPI, Docker, Git,
Pyright, Mypy, uv, Poetry. Advantageous: Ollama, vLLM, LM Studio, Hive Metastore, Trino,
Apache Ranger, ADLS Gen2, Synapse, ADF, Key Vault, Service Bus, OpenTelemetry, OpenLineage,
Databricks.

### Wording strength

The most specific of the three by a wide margin, and the only one that names tooling down to
the package manager. Two hard floors: "4+ years" Python and "2+ years of production
experience" with Spark. The verbs that do the filtering are "replatform", "validate ... against
legacy systems" and "provide parity evidence" — this is a migration role, and the proof of the
migration is the deliverable. "Work from technical specifications, design documents and ADRs"
and "work independently from written technical requirements" appear twice in different words,
which means it is a real filter. "Proven track record of delivering ... independently" is
employment history, not capability.

The AI content is entirely in the advantageous list. For this role AI is a plus, not a gate.

---

## Role 2 — Full Stack JavaScript Python AI Engineer

[Posting on PNet](https://www.pnet.co.za/jobs--Full-Stack-JavaScript-Python-AI-Engineer-REMOTE-R800K-PA-REMOTE-E-Merge-IT-Recruitment--4272026-inline.html) ·
[Mirror on e-Merge](https://e-merge.co.za/full-stack-javascript-python-ai-engineer-remote-r800k-pa/)

| Field | Value |
|---|---|
| Exact title | Full Stack JavaScript Python AI Engineer |
| Location | Remote |
| Recruiter | e-Merge IT Recruitment, on behalf of an unnamed client |
| Salary | "R800k per annum, negotiable based on experience and ability" |
| Employment | Permanent |

The posting describes "a talented Full Stack Engineer to build modern, AI-powered products
end to end, combining React, TypeScript and Python with cloud technologies and emerging AI
capabilities".

### Responsibilities (verbatim fragments)

- "building modern, AI-powered products from end to end"
- "work across both frontend and backend development"
- "building production-grade applications, designing APIs and database solutions"
- "integrating LLM-powered features, RAG and intelligent search into real-world products"
- working with "Docker, CI/CD and cloud infrastructure"

### Required experience and skills (verbatim)

- 5+ years of professional experience building full-stack web applications in production.
- TypeScript and React for the frontend.
- Python (FastAPI, Django, or similar) for the backend.
- Relational databases (PostgreSQL, MySQL).
- REST APIs.
- Cloud infrastructure (Azure, AWS, or GCP), CI/CD pipelines, and containerization (Docker).
- Experience integrating AI/LLM-powered features into a product — calling LLM APIs, working
  with retrieval-augmented generation (RAG) or vector search.
- Proficiency working with AI coding assistants (e.g., Claude Code, GitHub Copilot, Cursor) to
  accelerate development, while critically reviewing and validating AI-generated code.
- Strong understanding of software engineering fundamentals: testing, version control, code
  review, and system design.

### Nice-to-have (verbatim fragments)

- Terraform and observability tooling
- vector databases or embedding-based search
- startup or cross-functional team experience
- design systems and component libraries

### Named technologies

TypeScript, React, Python, FastAPI, Django, PostgreSQL, MySQL, Docker, Azure, AWS, GCP,
Claude Code, GitHub Copilot, Cursor. Nice to have: Terraform.

### Wording strength

One hard floor, "5+ years ... in production". The AI requirements are stated as things you have
done in a product — "integrating", "calling", "working with" — not as research. The line about
coding assistants is the most unusual sentence across all three postings: it makes both halves
a requirement, using the tools and "critically reviewing and validating" their output. That
is the only place any posting names the review skill rather than the tool.

"Software engineering fundamentals: testing, version control, code review, and system design"
is the sentence to read twice. It says the client has been burned by people who had the stack
and not the fundamentals.

---

## Role 3 — Full Stack Developer (Advanced)

[Posting on PNet](https://www.pnet.co.za/jobs--Full-Stack-Developer-Advanced-Python-3-9-Angular-17-Typescript-JavaScript-AWS-GenAI-RAG-MLOps-Rest-APIs-Midrand-Menlyn-Rosslyn-Home-Office-Rotation-Abalobi-Solutions--4274440-inline.html)

| Field | Value |
|---|---|
| Exact title | Full Stack Developer (Advanced): Python 3.9 + Angular 17+ + Typescript + JavaScript + AWS + GenAI/RAG + MLOps + Rest APIs |
| Location | Midrand / Menlyn / Rosslyn, home office rotation |
| Recruiter | Abalobi Solutions, for a client whose platform is called GAIA |
| Salary | Not stated |
| Years | Not stated; "Advanced" is the client's own level band |

### Responsibilities (verbatim)

- Design, develop and maintain scalable full-stack applications within the GAIA ecosystem
- Develop backend services, APIs and microservices using Python
- Build modern Angular-based front-end solutions
- Integrate AI capabilities and enterprise knowledge services into GAIA applications
- Ensure code quality through unit testing, peer reviews and engineering best practices
- Manage CI/CD pipelines and deployment processes
- Monitor production systems and resolve incidents
- Support and mentor junior developers where appropriate

### Required skills and experience (verbatim)

- GenAI, Agentic AI, RAG, AWS, Python, Angular, and MLOps exposure
- Strong proficiency in Python 3.9+
- Experience developing microservices and event-driven architectures
- Strong Angular (17+), TypeScript and JavaScript skills
- Experience with AWS cloud services
- Experience working in Agile teams
- Strong communication skills

### Advantageous skills (verbatim)

- AWS Lambda, ECS and Fargate experience
- Kubernetes experience
- Experience with authentication technologies: AWS Cognito, OAuth2, OpenID Connect
- Exposure to MLOps concepts
- Mentoring and technical leadership experience

### Named technologies

Python 3.9+, Angular 17+, TypeScript, JavaScript, AWS. Advantageous: Lambda, ECS, Fargate,
Kubernetes, Cognito, OAuth2, OpenID Connect.

### Wording strength

The softest of the three: no years, "exposure" for the AI and MLOps items, "experience" for
everything else. Do not misread that as junior — the level band is the client's "Advanced",
the responsibilities include "monitor production systems and resolve incidents" and "mentor
junior developers", and "microservices and event-driven architectures" is a requirement, not a
plus. This is a role for someone who has run things.

The frontend framework is Angular, not React. That is the only place the three postings
disagree on a named technology. TypeScript is constant.

---

## The intersection

What all three actually agree on. This is the non-negotiable core, and it is the requirements
list in `CURRICULUM.md`.

| Requirement | Role 1 — Python/Spark/AI | Role 2 — Full Stack AI | Role 3 — Full Stack (Advanced) |
|---|---|---|---|
| Production experience, in years | "4+ years", "2+ years of production" | "5+ years ... in production" | Implied: "Advanced", "resolve incidents" |
| Python as the primary backend | Yes, typed, with Pyright and uv | Yes, "FastAPI, Django, or similar" | Yes, "Python 3.9+", microservices |
| REST APIs, designed and operated | Yes, FastAPI, "authentication, idempotency and job-status" | Yes, "designing APIs and database solutions" | Yes, "APIs and microservices" |
| Docker, CI/CD, a cloud | Docker, CI/CD; Azure as a plus | Docker, CI/CD, "Azure, AWS, or GCP" | CI/CD, AWS required |
| LLM integration | Plus: "LLM / AI integration", Ollama, vLLM | Required: "calling LLM APIs, ... RAG or vector search" | Required: "GenAI, Agentic AI, RAG ... exposure" |
| Coding assistants, reviewed critically | Not mentioned | Required, by name | Not mentioned |
| Specs, design docs, ADRs, review | "Work from ... ADRs", "code reviews" | "code review, and system design" | "peer reviews", "mentor" |
| Relational data, Spark, parity | Spark, Delta, T-SQL, "parity evidence" | PostgreSQL, MySQL | Not named |
| Observability, incidents | Plus: OpenTelemetry, structured logging | Plus: "observability tooling" | Required: "monitor production systems and resolve incidents" |
| Security and privacy judgment | "authentication", plus POPIA/GDPR, Key Vault | Not named beyond fundamentals | Plus: Cognito, OAuth2, OpenID Connect |
| Frontend | Not required | TypeScript and React | Angular 17+, TypeScript |
| Testing | pytest, named twice | "testing" as a fundamental | "unit testing" |

Reduced to a sentence: **all three want a Python engineer who has shipped and run production
systems, designs and operates APIs, can integrate a model into a product, and works from
written designs with other people's review.** One adds Spark and parity as the depth. One adds
critical use of coding assistants. One adds event-driven architecture and incident response.

## The divergence

- **Role 1** is a data-platform role with a product-engineering floor. The depth it pays for is
  Spark, Delta, and proving a migration preserved the numbers. AI is a plus.
- **Role 2** is a product-engineering role with AI as a requirement. Frontend is React. It is
  the only posting to require critical use of coding assistants.
- **Role 3** is a product-engineering role inside an enterprise platform. Frontend is Angular.
  Event-driven microservices and incident response are the systems content.

The specialisation choice, stated plainly: the data depth of Role 1 is the differentiator; the
product engineering of Roles 2 and 3 is the floor. The curriculum is built to that shape.

## The honest gap

Set against the intersection and against `NON-CLAIMS.md`:

1. **Years in the named stack.** Production years exist, but not in Python-first, Spark, or
   with LLM features in a product. The postings count years in the stack they name.
2. **A replatform with parity evidence.** Never done end to end against a legacy system with a
   reviewer who wanted it to be wrong. `platform` exists to produce exactly one.
3. **A model integrated into a product with evals.** Never shipped. `product`'s assistant
   exists to produce one.
4. **Event-driven systems on real infrastructure.** Understood in the abstract, not built and
   operated. The ingestion service exists for this.
5. **Incidents on a system strangers use.** The only way to get this is to run one. Phase 9.

What the learning repository supplies, honestly: the vocabulary to read these postings without
bluffing, tested evidence of understanding, and a demonstrable learning rate. The build
repositories supply the rest, slowly.

## What changed in `CURRICULUM.md` because of these

- Applied AI became a pillar. The previous "AI is waived" position came from three postings
  that waived it; two of these three require it.
- Security was scoped down to what these roles name: auth protocols, secrets, privacy law,
  correctness. Detection as code became optional.
- Data became the deep pillar, with a replatform, a parity tool and an ingestion service as the
  proof.
- The cloud emulator was dropped as a spine. These roles build on cloud services, not copies.
- Design docs, ADRs, assistant-PR review and interview rehearsal became practices, because the
  postings name the first two and the interview process needs the last.
