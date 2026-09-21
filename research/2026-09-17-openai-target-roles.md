# Target roles — what they actually ask for

Primary-source extraction of three OpenAI engineering postings, checked on 2026-09-17.
Everything quoted below is OpenAI's own wording. Where I am inferring rather than quoting,
it is marked.

## Verdict on the entry bar, first

None of the three is accessible without professional software engineering experience.
That is not a judgement call — two of them state a years-of-experience floor in writing
(4+ and 5+), and the third describes itself entirely in terms of production shipping
history. There is no version of these postings where a self-taught candidate with a
learning repository and no employment history is in scope.

The relevant number: across the 818 jobs OpenAI had listed on 2026-09-17, exactly one
engineering posting stated a bar below two years — `Software Engineer, Applied Emerging
Talent (2027)`, at 0–1 years and $180K. That is the actual door. The three roles in this
document are two to three promotions past it.

This is worth writing down rather than skirting, because the failure mode is spending a
year building toward a posting that was never going to read the application.

---

## Role 1 — Software Engineer, Data Infrastructure

[Posting](https://openai.com/careers/software-engineer-data-infrastructure-san-francisco/) ·
[ATS record](https://jobs.ashbyhq.com/openai/f763c6b3-5167-4a67-b691-4c3fa2c44156)

| Field | Value |
|---|---|
| Exact title | Software Engineer, Data Infrastructure |
| Department / team | Scaling |
| Primary location | San Francisco |
| Salary | $266K – $445K, "Offers Equity" |
| Employment | Full time, hybrid, 3 days per week in office, relocation assistance |
| First published | 2024-06-27 |

Two caveats on location. The posting body says both "This role is based in San Francisco, CA"
and, at the end, "This role is exclusively based in our San Francisco HQ." The structured
record behind the posting nevertheless carries New York City, Seattle and Mountain View as
secondary locations. The prose is the safer reading. Second: this posting has been live since
June 2024. A req that has been open for over two years is either a standing pipeline or a very
high bar, and I cannot tell which from the outside. **Unverified either way.**

### In this role, you will

- Design, build, and maintain data infrastructure systems such as distributed compute, data orchestration, distributed storage, streaming infrastructure, machine learning infrastructure while ensuring scalability, reliability, and security
- Ensure our data platform can scale by orders of magnitude while remaining reliable and efficient
- Accelerate company productivity by empowering your fellow engineers & teammates with excellent data tooling and systems
- Collaborate with product, research and analytics teams to build the technical foundations capabilities that unlock new features and experiences
- Own the reliability of the systems you build, including participation in an on-call rotation for critical incidents

### You might thrive in this role if you (verbatim)

> - Have 4+ years in data infrastructure engineering OR
> - Have 4+ years in infrastructure engineering with a strong interest in data
> - Take pride in building and operating scalable, reliable, secure systems
> - Are comfortable with ambiguity and rapid change
> - Have an intrinsic desire to learn and fill in missing skills, and an equally strong talent for sharing learnings clearly and concisely with others

That bullet list is strikingly short on technology names. The stack is instead stated in the
*About the Role* prose, which is where the real filter sits:

> You've supported Spark, Kafka, Flink, Airflow, Trino, or Iceberg **as platforms**. You're
> well-versed in infrastructure tooling like Terraform, experienced in debugging large-scale
> distributed systems, and excited about solving data infrastructure problems in the AI space.

"As platforms" is the load-bearing phrase. Using Spark is not the ask; running Spark for other
people is.

### Named technologies

Spark, Kafka, Flink, Airflow, Trino, Iceberg, Delta, Chronon, Terraform.

From *About the Team*: "some of the largest Spark compute fleets in production"; "data lakes
and metadata systems on Iceberg and Delta with a vision toward exabyte-scale architecture";
"high throughput streaming platforms on Kafka and Flink"; "orchestration with Airflow";
"ML feature engineering tooling such as Chronon".

No cloud provider is named. No programming language is named — not Python, not Scala, not Java,
not Go. That absence is itself a signal: the role is defined by systems operated, not languages
written.

### Wording strength

"Have 4+ years" — a hard floor, stated twice. "Supported ... as platforms" — operational
ownership, not usage. "Well-versed in" for Terraform — the strongest phrasing in the posting,
but still short of "deep expertise". "Experienced in debugging large-scale distributed systems"
— experience-level, but the qualifier *large-scale* does the filtering. The posting nowhere
uses "deep expertise" or "expert".

The hardest requirement is not in the qualifications list at all. It is in the responsibilities:
"participation in an on-call rotation for critical incidents". That cannot be acquired outside
employment, which `NON-CLAIMS.md` in this repository already says plainly.

---

## Role 2 — Full Stack Software Engineer, API Experience

[Posting](https://openai.com/careers/full-stack-software-engineer-api-experience-new-york-city/) ·
[ATS record](https://jobs.ashbyhq.com/openai/66288824-8b77-4774-bc57-6825d3e6221e)

| Field | Value |
|---|---|
| Exact title | Full Stack Software Engineer, API Experience |
| Department / team | Core Product & Platform / API |
| Location | New York City |
| Salary | $266K – $385K, "Offers Equity" |
| Employment | Full time; the structured record flags hybrid, the body does not mention it |
| First published | 2026-06-25 |

Note the salary ceiling is $60K lower than the other two. Same floor, lower top. I read that as
a narrower level band rather than a cheaper role, but that is inference. **Unverified.**

This posting does **not** use the "You might thrive in this role if" heading. It uses
**"Your background might look something like:"** — softer framing, but with the hardest numeric
requirement of the three.

### In this role, you will

- Build and scale developer-facing products including the OpenAI API Playground, documentation experiences, onboarding flows, examples, and API workflow tools.
- Own full stack projects end to end, from product definition and UX collaboration through backend implementation, launch, measurement, and iteration.
- Improve the systems that generate, maintain, and publish SDKs, API references, docs, guides, and developer examples.
- Partner with API, research, design, and infrastructure teams to bring new model capabilities and API primitives to developers in a clear, usable way.
- Use developer feedback, product analytics, and direct customer insight to identify friction and improve the API experience.
- Help set technical and product direction for a new NYC-based team with broad ownership over OpenAI's developer experience.

### Your background might look something like (verbatim)

> - 5+ years of professional engineering experience, excluding internships, in product-driven engineering teams.
> - Strong experience with TypeScript, React, and modern web application development.
> - Proficiency in one or more backend languages such as Python, Go, Rust, TypeScript, or similar.
> - Experience designing, building, and operating production APIs, services, databases, or developer tooling.
> - Strong product judgment and a track record of turning ambiguous developer problems into simple, high-quality product experiences.
> - Experience with documentation systems, SDKs, API design, developer tools, or technical content pipelines is a strong plus.
> - Comfort working across product, design, engineering, research, and external developer feedback loops.
> - Care for reliability, performance, accessibility, and maintainability in production systems.
> - Interest in AI and developer platforms; direct ML experience is helpful but not required.
> - Ability to thrive in a fast-moving environment with loosely defined problems and competing priorities.

### Named technologies

TypeScript, React, Python, Go, Rust. Plus non-branded categories: SDKs, APIs, databases,
documentation systems, developer tooling, the OpenAI API Playground.

### Wording strength

This is the most explicit of the three, and the most exclusionary.

- **"5+ years of professional engineering experience, excluding internships"** — the phrase
  *excluding internships* is deliberate and closes the obvious workaround. It is also the only
  one of the three postings to define what counts.
- **"Strong experience with TypeScript, React"** — elevated above plain "experience". Not
  "deep expertise", but the only place any of the three roles escalates a specific named
  technology.
- **"Proficiency in one or more backend languages"** — deliberately loose; the language does
  not matter, the backend competence does.
- **"a track record of"** — again, employment history, not capability.
- **"is a strong plus"** applies only to documentation systems and SDK work. Everything above
  it is a requirement.
- **"direct ML experience is helpful but not required"** — the AI part is explicitly *not* the
  barrier. The engineering seniority is.

---

## Role 3 — Full Stack Software Engineer, Cybersecurity Products

[Posting](https://openai.com/careers/full-stack-software-engineer-cybersecurity-products-san-francisco/) ·
[ATS record](https://jobs.ashbyhq.com/openai/88654e7f-4e23-4e75-8e54-18c10d09b093)

| Field | Value |
|---|---|
| Exact title | Full Stack Software Engineer, Cybersecurity Products |
| Department / team | Applied AI / Codex - Engineering |
| Location | San Francisco |
| Salary | $266K – $445K, "Offers Equity" |
| Employment | Full time, hybrid, 3 days per week in office, relocation assistance |
| First published | 2026-06-04 |

Worth registering that this sits under **Codex - Engineering**, not under a security
organisation. The product is described as "Codex Security and related cyber products".

### In this role, you will

- Build end-to-end workflows for vulnerability discovery, security scanning, red teaming, findings review, remediation, and reruns.
- Design and operate backend services for long-running security work, including APIs, asynchronous orchestration, durable state, and integrations with developer workflows.
- Make complex security results actionable through clear product surfaces, strong evidence, thoughtful prioritization, and reliable reporting.
- Partner with security researchers, product teams, and users to evaluate quality, reduce noise, improve coverage, and ship safely.

### You might thrive in this role if you (verbatim)

> - Have experience shipping production full-stack products across modern web frontends and backend services.
> - Can design clear APIs and data models, reason about asynchronous systems, and diagnose reliability or performance problems.
> - Care about building products that experts trust while making sophisticated workflows usable for a broader set of engineers.
> - Bring strong judgment around privacy, security, and correctness. Application-security or cybersecurity experience is helpful, but not required.

### Named technologies

**None.** Zero. Not one language, framework, database, protocol or vendor product appears
anywhere in the posting. The only proper noun in the whole description is Codex.

The requirements are stated entirely as capabilities: "modern web frontends", "backend
services", "APIs and data models", "asynchronous systems", "asynchronous orchestration",
"durable state".

### Stated years of experience

None given. This is the only one of the three with no numeric floor.

### Wording strength

Softest language of the three, and it is easy to misread as the most accessible. It is not.

- **"Have experience shipping production full-stack products"** — plain "experience", but the
  gate is the word *shipping* and the word *production*. Together they mean employment.
- No "deep expertise" or "expert" anywhere. No "strong experience". No years.
- **"Application-security or cybersecurity experience is helpful, but not required."** This is
  the single most useful sentence across all three postings for anyone weighing a security
  specialisation: OpenAI is explicitly saying the security domain knowledge is *not* the gate
  on this team. The gate is production full-stack engineering.
- The genuinely hard bit is buried in *About the Role*: "long-running workflows, large
  repositories, sensitive data, reliability, observability, and a high bar for earning user
  trust". That is a distributed-systems posting wearing a product-engineering label.

---

## The intersection

What all three actually agree on. This is the non-negotiable core.

| Skill | Data Infrastructure | API Experience | Cybersecurity Products |
|---|---|---|---|
| Production experience, not project experience | Yes — "4+ years" | Yes — "5+ years ... excluding internships" | Yes — "shipping production full-stack products" |
| Designing and operating APIs / services | Implied (platform services) | Yes — "designing, building, and operating production APIs" | Yes — "Design and operate backend services ... including APIs" |
| Reliability as an owned responsibility | Yes — on-call rotation named | Yes — "Care for reliability, performance ... in production systems" | Yes — "diagnose reliability or performance problems" |
| Data modelling / storage | Yes — distributed storage, lakehouse | Yes — "databases" | Yes — "clear APIs and data models" |
| Distributed / asynchronous systems reasoning | Yes — "debugging large-scale distributed systems" | Implied (scale, "millions of developers") | Yes — "reason about asynchronous systems" |
| Cross-functional collaboration with research and product | Yes | Yes | Yes |
| Tolerance for ambiguity and rapid change | Yes — "comfortable with ambiguity and rapid change" | Yes — "loosely defined problems and competing priorities" | Yes — "fast-moving product development" |
| Clear written and spoken communication | Yes — "sharing learnings clearly and concisely" | Yes — cross-functional loops | Yes — "Make complex security results actionable" |
| Security and correctness judgment | Yes — "reliable, secure systems" | Partially — via "maintainability", "accessibility" | Yes — "strong judgment around privacy, security, and correctness" |
| Named ML/AI expertise | Not required | Explicitly not required | Not mentioned |
| A specific named language | No language named | TypeScript, React required; backend language flexible | No language named |

Reduced to a sentence: **all three want someone who has operated something in production for
other people, can design an API and a data model, can reason about asynchronous behaviour, and
can explain themselves.** None of them wants AI/ML expertise. Only one insists on a named
language.

The consistent absence of "deep expertise" phrasing across all three is worth noting. OpenAI's
escalation is not in adjectives — it is in verbs. "Supported as platforms", "operating",
"shipping", "own the reliability". The bar is expressed as things you have been responsible for.

## The divergence

- **Data Infrastructure** is the only one asking for a *named operational stack* — Spark,
  Kafka, Flink, Airflow, Trino, Iceberg, Terraform — and the only one that names on-call in
  the responsibilities. It is a platform-operations role.
- **API Experience** is the only one asking for *frontend craft by name* (TypeScript, React)
  and the only one asking for product judgment and developer empathy as first-class skills.
  It is also the only one with an explicit "excluding internships" clause. It is a
  product-engineering role.
- **Cybersecurity Products** is the only one with *no technology names and no years*, and the
  only one that explicitly waives domain expertise. It is the most stack-agnostic and the most
  seniority-implicit. It is a product-engineering role with a systems problem underneath.

The specialisation choice, stated plainly: infrastructure operations, frontend-weighted product
engineering, or backend-weighted product engineering. The security branding on the third role
is a product domain, not a skill requirement.

## The honest gap

### What a beginner does not have

Set against the intersection table above, and against this repository's own `NON-CLAIMS.md`,
which already lists most of this:

1. **Years.** Two of three state a number. No portfolio substitutes for a date range on a CV.
   "Excluding internships" tells you OpenAI has already thought about the workaround.
2. **Production operation.** Every one of the three is built on the verb *operate*. Running a
   system that other people depend on, that breaks at inconvenient hours, is the shared core.
   A laptop-scale module cannot produce it.
3. **On-call.** Named explicitly in the Data Infrastructure responsibilities. Unobtainable
   outside employment.
4. **Scale.** "Large-scale distributed systems", "exabyte-scale", "millions of developers",
   "large repositories". Nothing in a learning repository has met a dataset large enough to be
   interesting.
5. **Working in a codebase you did not write**, and the collaboration that comes with it —
   review given and received, a design defended. All three postings assume it; none of them
   say it, because it is assumed.
6. **A track record of product judgment.** API Experience asks for it by name. It is formed
   by having shipped things that were used and sometimes were wrong.

What a learning repository *does* supply, honestly: the vocabulary to read these postings
without bluffing, the ability to reason about the systems in question, and a demonstrable
learning rate. The fifth bullet on the Data Infrastructure list — "intrinsic desire to learn and
fill in missing skills, and an equally strong talent for sharing learnings clearly and
concisely" — is the one requirement across all three postings that a public learning repository
speaks to directly. One bullet out of nineteen.

### The realistic path in

**OpenAI's own stated entry point.** The Emerging Talent page says OpenAI offers "full time
roles in research, applied engineering, and product, designed for people with 0–3 years of
experience", and specifically names "a recent graduate **or a self-taught learner just
beginning your career**"
([source](https://openai.com/careers/emerging-talent/)). That page describes three programmes:
early-career full-time roles, internships ("open to undergraduate and master's students"),
and the Research Residency ("a six-month program that helps researchers and engineers
transition into AI. It can also lead to a full-time role").

The concrete posting behind it, as of 2026-09-17:

**`Software Engineer, Applied Emerging Talent (2027)`** — Applied AI, San Francisco, $180K plus
equity. Stated background:

> - Bachelor's or Master's degree in Computer Science, Computer Engineering, relevant technical field, **or equivalent practical experience**
> - 0-1 years of experience in software engineering or a relevant field
> - Proficiency with JavaScript, React, and some backend languages (we use Python)
> - Some experience with relational databases like Postgres/MySQL
> - Interest in AI/ML (direct experience not required)
> - Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

([ATS record](https://jobs.ashbyhq.com/openai/55150071-fce8-48f5-aea4-14ed78b83511))

Three things to take from it. The degree requirement carries "or equivalent practical
experience", which is the only crack in the wall any of these postings offers. The stack is
concrete and small — JavaScript, React, Python, Postgres or MySQL — and is a realistic
self-study target in a way that operating a Spark fleet is not. And it maps most directly onto
the **API Experience** role of the three, not the data infrastructure one, which means the
frontend-and-Python path is the shorter ladder even for someone whose interest is data.

**Caveat on availability.** Of the 818 roles OpenAI had listed on 2026-09-17, this was the only
engineering posting with a stated bar below two years, and there were no postings with "Intern"
or "New Grad" in the title. The emerging-talent door exists but it is one door, and the 2027 in
the title suggests a cohort intake rather than a rolling req. **This is a snapshot; re-check
rather than trust it.**

**Adjacent roles as stepping stones.** The following is my judgement, not sourced from OpenAI,
and should be treated as such. **Unverified.** The pattern that gets someone from zero to a
posting like these is: any role where you carry a pager for a real system. Concretely, the
adjacent titles that hire on potential rather than track record are data engineer or analytics
engineer at a mid-size company, platform or internal-tools engineer, support engineer or
solutions engineer at an infrastructure vendor with a documented path into engineering, and
security operations analyst for the security branch. OpenAI itself lists several of these
families — `Forward Deployed Engineer`, `Support Engineer`, `Applied AI Engineer`, `Data
Engineer` — but their stated floors on the current board run from 3+ to 8+ years, so they are
not shortcuts at OpenAI. They are shortcuts elsewhere, and OpenAI is the destination rather
than the first stop.

The unpleasant but accurate summary: these three postings are a target to aim the *curriculum*
at, not a target to aim *applications* at. They tell you what to learn. They do not tell you
where to apply.

## The hiring process, from OpenAI's own pages

A first-party description does exist, at **[openai.com/interview-guide](https://openai.com/interview-guide/)**.
Note the URL — it is not under `/careers/`. `openai.com/careers/interviewing-at-openai/` is not
listed in OpenAI's sitemap and did not resolve; I could not confirm whether it ever existed, so
I will not claim it 404s. The canonical page is the one above, and it is linked from the
Emerging Talent page as "The OpenAI Interview Guide".

### Stated hiring philosophy

> **Hiring values.** We want to ensure all candidates go through a consistent interview process
> and have the opportunity to showcase their variety of strengths. **We are not
> credential-driven** — rather, we want to understand your unique background and what you can
> contribute to our team.

> **What we look for.** We're excited about people who are already experts in their fields as
> well as people who are not yet specialized but show high potential. By "high potential" we
> mean people who have demonstrated the ability to ramp up quickly in a new domain and produce
> results.

"Not credential-driven" is genuinely encouraging and should be read precisely: it rules out
*degree* gatekeeping, not *experience* gatekeeping. The 5+ years clause in the API Experience
posting sits alongside this statement without contradiction.

### The stated stages

1. **Application and résumé review.** "It typically takes the recruiting team one week to
   review your résumé and email you back."
2. **Introductory calls.** With hiring manager or recruiter. "Be prepared to discuss your work
   and academic experience, motivations and goals." They recommend familiarising yourself with
   recent OpenAI work, "especially those related to the team you are interviewing for".
3. **Skills-based assessment.** "Formats vary by team and may include: pair coding interviews,
   take-home projects, technical tests, etc. We may ask you to complete more than one
   assessment depending on the role. The recruiting team will provide prep to set you up for
   success."
4. **Final interviews.** "By default, our interviews will continue to take place virtually,
   though you may choose to interview onsite at our office in San Francisco. Typically, our
   candidates go through **4–6 hours of final interviews with 4–6 people over 1–2 days**."
   And: "For engineering interviews, we generally look for **well-designed solutions to the
   challenge, high-quality code, optimal performance, and good test coverage**."
5. **Decision.** "You should expect to hear from us within one week of your final interviews."

That fourth-stage sentence is the most actionable line on the page. Test coverage is named as a
graded criterion, which is unusual to state openly and happens to be the one thing this
repository's structure already trains.

### Recommended preparation, as stated

> Recommended general reading includes the OpenAI Charter, research publications, and blog
> posts that you find interesting. Recommended technical reading includes Deep Learning Book
> and Spinning Up in Deep RL.

Worth registering that both named technical texts are ML texts, despite none of the three
target roles requiring ML.

### AI-assisted coding during interviews

There **is** a first-party policy, and it is a policy of "it depends", stated verbatim on the
interview guide:

> **We want to understand how you think.** Our interviews are designed to help us understand
> how you approach problems, make decisions, and communicate your reasoning. **Expectations for
> AI and other tools vary by interview: some formats intentionally allow them, while others are
> designed to assess your independent problem-solving without AI tools.** We'll explain what is
> allowed in your interview preparation materials. If you're unsure, please ask your recruiter
> before the interview.

Three things follow. There is no blanket ban and no blanket permission. The unassisted format
is explicitly retained — "independent problem-solving without AI tools" — so the ability to
work without an assistant is still directly assessed. And the burden of clarification is placed
on the candidate: "please ask your recruiter before the interview".

This is close to the position `AI_USAGE.md` in this repository already takes, and it is the
clearest external justification for keeping the reproduce-from-scratch check.

### OpenAI's engineering blog

The engineering blog index lists 22 posts as of 2026-09-17. **None of them describes how OpenAI
hires.** The blog is engineering write-ups only. Several are directly relevant as *reading* for
the data infrastructure role — `scaling-postgresql`, `scaling-storage-one-billion-users-part-one`,
`core-dump-epidemiology-data-infrastructure-bug` — which lines up with the interview guide's
advice to read recent work from the team you are interviewing for.

## Sources

**Method note.** The three `openai.com/careers/...` URLs returned **HTTP 403** to every
automated fetch attempted, from both the built-in fetcher and curl with browser headers. This
is bot protection, **not** a 404 — the pages are live. I confirmed all three slugs are present
in the HTML of `openai.com/careers/`, and took the posting text from OpenAI's own applicant
tracking feed at `api.ashbyhq.com/posting-api/job-board/openai`, which is the source that
populates the careers site. Titles, locations, departments, salary bands, publication dates and
full body text all come from that feed. Nothing below is reconstructed from memory.

- [Software Engineer, Data Infrastructure — careers page](https://openai.com/careers/software-engineer-data-infrastructure-san-francisco/) (403 to automated fetch; slug confirmed live on the careers index)
- [Full Stack Software Engineer, API Experience — careers page](https://openai.com/careers/full-stack-software-engineer-api-experience-new-york-city/) (403 to automated fetch; slug confirmed live)
- [Full Stack Software Engineer, Cybersecurity Products — careers page](https://openai.com/careers/full-stack-software-engineer-cybersecurity-products-san-francisco/) (403 to automated fetch; slug confirmed live)
- [OpenAI job board feed (Ashby, OpenAI's ATS)](https://api.ashbyhq.com/posting-api/job-board/openai?includeCompensation=true) — 818 jobs, retrieved 2026-09-17
- [Data Infrastructure — ATS record](https://jobs.ashbyhq.com/openai/f763c6b3-5167-4a67-b691-4c3fa2c44156)
- [API Experience — ATS record](https://jobs.ashbyhq.com/openai/66288824-8b77-4774-bc57-6825d3e6221e)
- [Cybersecurity Products — ATS record](https://jobs.ashbyhq.com/openai/88654e7f-4e23-4e75-8e54-18c10d09b093)
- [Software Engineer, Applied Emerging Talent (2027) — ATS record](https://jobs.ashbyhq.com/openai/55150071-fce8-48f5-aea4-14ed78b83511)
- [OpenAI Interview Guide](https://openai.com/interview-guide/) — hiring philosophy, five stages, AI-tools policy
- [OpenAI Emerging Talent](https://openai.com/careers/emerging-talent/) — 0–3 years framing, internships, residency
- [OpenAI careers index](https://openai.com/careers/) — slug confirmation (403 to the fetcher, retrieved via curl)
- [OpenAI engineering blog index](https://openai.com/news/engineering/) — checked for hiring content; none found
- Not found: `openai.com/careers/interviewing-at-openai/` is absent from OpenAI's sitemap and did not resolve. I cannot confirm it ever existed and have not reconstructed it.

**Re-check date.** All job-board figures are a snapshot taken 2026-09-17. Postings close,
salary bands move and the emerging-talent req is cohort-dated. Anything in this document that
depends on "currently listed" should be re-run rather than trusted after about a month.
