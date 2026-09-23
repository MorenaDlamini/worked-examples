# The 2026 full-stack tooling landscape, from a Johannesburg seat

Primary-source research, done on 2026-09-23, to answer one question: is `CURRICULUM.md`'s
Phase 3 bet — React, TypeScript, and a Vite-built SPA over a FastAPI and Postgres backend —
the right bet for someone in Johannesburg who wants either a senior South African role or
remote work abroad?

Everything factual here is cited to the page that owns the fact. Official documentation,
release notes, the npm registry API, the Devographics results API that backs the State of JS
site, survey result pages published by the survey itself, and job listing bodies that were
opened and read. A blog post summarising a release is not the source; the release note is.
Where I am inferring rather than quoting, it is marked **Unverified**.

**The job-listing counts are a one-day snapshot and are biased by the search terms used.**
They will go stale. Say so out loud whenever they are quoted. The methodology section below
says exactly how the bias was introduced, because in two places it is large enough to flip a
conclusion.

This file extends `2026-09-23-data-stack-and-certifications.md`, which covered the data half of
the stack on the same day. Its reachability notes are extended here rather than repeated.

---

## The verdict

**React plus FastAPI plus Postgres is the right bet. Do not change it. Three details in
Phase 3 are wrong and are worth fixing.**

Three sub-questions, answered in order of how much they should worry you.

**1. Does the Angular share in South Africa justify learning Angular too? No — but the belief
is true, and that matters.** Across 105 South African listing bodies read on one day, Angular
was named in 50 (48%) and React in 49 (47%). Angular is genuinely co-equal with React in the
South African market, which is not true anywhere else measured here. Across 64 remote-first
listings, React was named 23 times (36%) and Angular 3 times (5%) — a seven-to-one gap the
other way. On the npm registry, `react` was downloaded 132,703,321 times in the week of
2026-09-15 and `@angular/core` 4,960,205 times, a ratio of 26.7 to 1
([npm registry API](https://api.npmjs.org/downloads/point/2026-09-15:2026-09-21/react),
[same for @angular/core](https://api.npmjs.org/downloads/point/2026-09-15:2026-09-21/@angular/core)).
The reason not to learn Angular is not that the SA demand is absent — it is that 14 of the 54
listings in one sample named "Angular **or** React" as interchangeable, that the plan's stated
goal includes remote work abroad where Angular is a rounding error, and that a second framework
costs a whole phase. React is the better single bet because it is the only one that is a strong
answer to both markets.

**2. Is abandoning C# and ASP.NET Core a mistake? It is a real cost, and the file should say
so, but not a mistake.** C#/.NET was the single most-named backend in South Africa — 36 of 105
listings (34%), ahead of Java (30, 29%), Node (27, 26%) and Python (20, 19%). Azure was named
in 36 of 105 (34%). In the remote sample, .NET collapsed to 3 of 64 (5%). So the production
C# and ASP.NET Core experience is the most valuable single asset in the local market and close
to worthless in the remote one. The resolution is not to un-abandon it: it is to stop treating
it as abandoned. It is production experience, and the requirements list's first item is
production experience stated in years. `CURRICULUM.md` currently does not mention it at all.
That is the miss.

**3. Is FastAPI a liability where Django or .NET is expected? In South Africa, marginally yes;
everywhere else, no.** FastAPI was named in 2 of 105 SA listings (1.9%) against Django's 11
(10.5%). But Python of any kind was named in only 20 of 105 (19%), so the entire question
concerns a fifth of the local market. Everywhere else the evidence runs the other way. The
Stack Overflow Developer Survey 2025 puts FastAPI at 14.8% and Django at 12.6% of 23,678
respondents, and the survey's own commentary says "The +5 point increase for FastAPI is one of
the most significant shifts in the web framework space"
([survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology)).
On PyPI, `fastapi` was downloaded 84,728,817 times in the last week against `django`'s
9,445,248 — nine to one
([pypistats.org](https://pypistats.org/api/packages/fastapi/recent)). In the remote sample
Django edged FastAPI 6 to 5, and four of the five FastAPI listings named Django or Flask in
the same body as an alternative. FastAPI is not a liability. Django is the thing to be able to
read, not the thing to build in.

**And the finding that most directly protects the plan.** Next.js has *not* become the default
employer ask. It was named in 1 of 64 remote listings (2%) and 4 of 105 South African listings
(4%). Of the 23 remote listings naming React, 22 named no meta-framework at all; two named
Vite by name and one explicitly ruled Next.js out. React plus Vite is still exactly what
employers write down. `react.dev` recommending a framework and employers asking for one are
two different facts, and the plan is aligned with the second.

**What is wrong in Phase 3.** Three things, all small, all concrete, all in "What this changes
in `CURRICULUM.md`" at the end: the component-library module is aimed at a thing no employer
names; the build and test tooling is unnamed where every other phase names its tools; and the
phase says nothing about the C# experience the plan is standing on. The accessibility and
error-surface exit test is good and should be kept exactly as it is.

---

## Methodology, and where the bias is

### What was read

| Sample | N (bodies read in full) | Boards | Date range |
|---|---|---|---|
| **SA-A** | 54 | PNet (25), ExecutivePlacements (12), CareerJunction (10), Datafin (7) | 52 of 54 posted 2026-08-28 or later; two outliers, 2026-04-29 and 2026-01-19 |
| **SA-B** | 51 | freehire.me (17), IT-Online (14), e-Merge (12), Hire Resolve (8) | majority 2026-08 to 2026-09; three from 2026-01 to 2026-05 |
| **Remote** | 64 | Jobicy (28), WeWorkRemotely (19), Remotive (7), WorkingNomads (7), Himalayas (3) | 58 from 2026-09, 5 from 2026-08, 1 from 2026-07 |

**169 listing bodies read in total.** Nothing was counted from a title, from a board's
metadata, or from a search snippet, with two flagged exceptions noted below.

### The five biases that matter

1. **The search terms manufacture the frontend counts.** SA-A ran `react developer` and
   `angular developer` as separate searches of roughly equal effort; SA-B ran freehire's
   `/collections/react` and `/collections/angular` filters. **The 47%/48% React–Angular split
   is partly an artefact of searching both terms.** What it demonstrates is that both searches
   return plenty of live roles — which is the actual claim being tested. It is not a market
   share.
2. **Recruiter concentration is severe.** In SA-A, five recruiters account for roughly half
   the sample. One near-identical automotive contract spec was posted by three agencies at
   three seniorities; remove that family and Playwright drops from 4 to 1 and Django from 5 to
   2. In SA-B, one agency supplies all four Claude Code mentions and all four Cursor mentions.
   In the remote sample, one staffing marketplace appears 8 times and supplies 3 of the 5
   FastAPI hits, all 3 SQLAlchemy hits and all 3 pytest hits.
3. **SA-A and SA-B were harvested independently and I did not reconcile them.** IT-Online is
   substantially a republisher of the CareerJunction feed — at least 5 of SA-B's 14 IT-Online
   listings carry CareerJunction apply links. **The pooled N of 105 therefore contains an
   unknown number of duplicates, probably in the range 3 to 8.** Every pooled percentage below
   should be read as approximate to within a few points. Where a conclusion depends on the
   pooled number, the two samples are also shown separately so a reader can see the spread.
4. **Silence is not absence.** 94% of remote listings named no build tool, 90% of SA listings
   named no ORM, 89% of SA listings named no testing tool. That is a fact about how job ads are
   written, not about what teams use. The one place the silence *is* evidence is Next.js, where
   it is corroborated by the listings that did specify: they chose Vite.
5. **Aggregator location metadata is wrong often enough to be useless.** Nine listings that
   WeWorkRemotely's feed labelled "Anywhere in the World" turned out, in the body, to require
   US work authorisation, East Coast hours, or a named single country. Every location call in
   this file comes from body text.

### One methodology failure, recorded

On two early fetches in SA-A, the summarising fetch tool emitted a "TECH:" line naming tools
that did not appear anywhere in the verbatim body it reproduced. All auto-generated technology
lists were discarded from that point and coding was done only from verbatim requirement prose.
I cannot rule out that a smaller fabrication survived in a body read only once. Two SA-A
listings were coded from their titles because the body was pure boilerplate, which breaks the
rule; both are flagged, and removing them moves React from 28 to 27 and C# from 18 to 17.

---

## Part 1 — Frontend, South Africa

### The counts

Pooled, N = 105, unreconciled. Both samples shown because the disagreement is itself
information.

| Framework | SA-A (n=54) | SA-B (n=51) | Pooled (n=105) | Pooled share |
|---|---|---|---|---|
| **Angular** | 26 (48%) | 24 (47%) | **50** | **47.6%** |
| **React** | 28 (52%) | 21 (41%) | **49** | **46.7%** |
| **Vue** | 9 (17%) | 12 (24%) | **21** | **20.0%** |
| **Svelte** | 0 | 0 | **0** | **0.0%** |
| Blazor | 5 (9%) | not coded | 5 | 4.8% |
| No frontend framework named at all | 9 (17%) | 17 (33%) | 26 | 24.8% |
| Next.js | 3 | 1 | 4 | 3.8% |
| Nuxt / Remix / SvelteKit / Astro | 1 Remix, 1 Astro | 0 | 2 | 1.9% |

### Testing the belief

**The belief that Angular is unusually strong in South African enterprise is true.** It is the
only market measured in this file where Angular and React are within one percentage point of
each other. But three qualifications change what you should do about it.

**Most listings do not choose.** In SA-A, 14 of 54 named both React and Angular, nearly always
as "Angular **or** React". Counting only where one framework is the stated primary technology
gives React-primary ≈ 17 and Angular-primary ≈ 14. The market is framework-agnostic at the job
description level far more often than the headline split suggests.

> "Solid front-end development experience with Angular or React."
>
> — Senior C# Full Stack Developer (Azure), Sandton, ~2026-09-22, via IQbusiness
> ([PNet](https://www.pnet.co.za/jobs--Senior-C-Full-Stack-Developer-Azure-Sandton-IQbusiness--4200242-inline.html))

> "Strong experience with UI frameworks, e.g. Angular, React, Vue." … "Strong experience with
> .Net Core preferable, including C#, ASP.NET Core, etc."
>
> — Development Lead (C#, ASP.NET Core, Azure), Cape Town, 2026-09-22, via Datafin
> ([CareerJunction](https://www.careerjunction.co.za/development-lead-c%23-aspnet-core-azure-cpt-job-2645036.aspx))

> "Experience with front-end frameworks such as Angular, React, or Vue.js."
>
> — .Net Core Fullstack Developer, Cape Town, via Hire Resolve
> ([Hire Resolve](https://hireresolve.co.za/job/net-core-fullstack-developer/))

**Where Angular is named alone, it is the banking and enterprise-platform segment — and the
version asked for is old.** The banking pattern is much stronger in this sample than the
automotive one.

> "Support delivery across multiple initiatives within the banking Rewards portfolio when
> required" … "Become productive within the team's Angular codebase and delivery practices"
>
> — Senior Angular Developer – Banking Rewards Portfolio, Johannesburg, ~2026-09-17, via
> Sabenza IT Recruitment
> ([PNet](https://www.pnet.co.za/jobs--Senior-Angular-Developer-Banking-Rewards-Portfolio-Johannesburg-Sabenza-IT-Recruitment--4262055-inline.html))

> "Lead the upgrade and migration of Angular applications from Angular 14 to Angular 21." …
> "Integrate applications with Ping Identity, Single Sign-On (SSO), and related identity
> management solutions."
>
> — Senior Software Developer (Angular & Java), 6-month contract, Johannesburg, ~2026-09-18,
> via Swan iT Recruitment
> ([PNet](https://www.pnet.co.za/jobs--Senior-Software-Developer-Angular-Java-6-Month-Contract-Johannesburg-Swan-iT-Recruitment-Ltd--4265283-inline.html))

> "Mandatory: Angular 17 experience" … "TypeScript / JavaScript / Playwright / HTML/CSS /
> Node.js / PostgreSQL / Azure / Git/GitHub / Docker / DevOps" … "Insurance industry experience"
> [advantageous]
>
> — Angular 17 Developer, Johannesburg, ~2026-09-22, via Teqleader Consulting
> ([PNet](https://www.pnet.co.za/jobs--Angular-17-Developer-Johannesburg-Teqleader-Consulting-Pty-Ltd--4276536-inline.html))

> "Front-End Technologies – Angular (v16 preferred), TypeScript, JavaScript (ES6+), HTML5,
> CSS3, SCSS/SASS, Bootstrap, Angular Material" … "Testing – Jasmine, Karma, Unit Testing,
> End-to-End Testing (Cypress or Selenium advantageous)"
>
> — Angular Developer, Johannesburg, 2026-08-06, via Sabenza IT & Recruitment
> ([IT-Online](https://it-online.co.za/2026/08/06/angular-developer-at-sabenza-it-recruitment-2/))

> "Thorough mastery of Angular (Version 9+) or React" … "3+ years automated testing using
> Playwright, Cypress, or Selenium."
>
> — Expert Front-End Developer (Angular & Cloud), contract, Midrand, 2026-09-23, via iSanqa
> ([PNet](https://www.pnet.co.za/jobs--Expert-Front-End-Developer-Angular-Cloud-Contract-Gauteng-Hybrid-ISB802692-Midrand-iSanqa--4259167-inline.html))

**Wording strength.** Of the 50 Angular mentions, only 11 stated a version. The versions stated
were v9+, v11+, v15+, v16, v17, "17+", "latest versions", and one migration from v14 to v21.
Angular's own support policy says "All major releases are typically supported for 24 months" —
12 months active, 12 months LTS — and that "Angular versions v2 to v19 are no longer supported"
([angular.dev/reference/releases](https://angular.dev/reference/releases)). Angular 22 was
released 2026-06-03, Angular 21 on 2025-11-19, Angular 20 on 2025-05-28 (dates from the
[npm registry](https://registry.npmjs.org/@angular%2Fcore)). **A posting that says "Angular
17+" in September 2026 is asking for a version that went out of support, and is five majors
behind current.** The target Role 3 in `2026-09-22-sa-target-roles.md` is one of these. That
is a fact about the codebase you would be joining, not about the framework.

The one listing in the corpus that named a framework version *and* was current was the Angular
14-to-21 migration contract. That is the shape of the Angular work in this market: maintenance
and upgrade of long-lived enterprise applications.

**Svelte is zero.** Zero in SA-A, zero in SA-B, zero in the remote sample. 0 of 169 bodies.
This is the most reliable number in the file, because nothing in the search strategy suppressed
it.

---

## Part 2 — Frontend, global and remote

### The counts

N = 64. **Of the 64, 22 (34%) are plausibly open to an applicant in Johannesburg, and the
confident floor is closer to 8 (13%).** The 34% counts timezone bands — "CET ±3 hours", "UTC-4
to UTC+4", "EMEA" — that include Johannesburg on the clock but are plausibly meant as European.
The 13% is the listings that say "worldwide" or name South Africa. Treat 34% as the optimistic
ceiling.

| Framework | Count | Share of 64 |
|---|---|---|
| **React** | 23 | 36% |
| **Angular** | 3 | 5% |
| **Vue** | 3 | 5% |
| **Svelte** | 0 | 0% |
| No frontend framework named | 38 | 59% |

The 59% is mostly backend, platform and SRE roles, but it also includes full-stack posts that
describe the work in outcomes without naming a library.

The only listing in the entire 169 to name South Africa explicitly:

> "We work with developers from 75+ countries across Europe, Latin America, North America (the
> U.S. and Canada), selected countries in Asia […], Oceania […], and Africa (including Morocco
> and South Africa)."
>
> — Senior .NET Full-stack Developer, remote, 2026-09-17, via Lemon.io
> ([Remotive](https://remotive.com/remote-jobs/software-development/senior-net-full-stack-developer-2091130))

### What developers use, from the surveys themselves

**Stack Overflow Developer Survey 2025**, web frameworks and technologies, all respondents,
n = 23,678 (48.3% of survey)
([survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology)).
A 2026 edition does not exist yet: `survey.stackoverflow.co/2026/` returns HTTP 404.

| Framework | "Have used" |
|---|---|
| Node.js | 48.7% |
| React | 44.7% |
| jQuery | 23.4% |
| Next.js | 20.8% |
| Express | 19.9% |
| ASP.NET Core | 19.7% |
| Angular | 18.2% |
| Vue.js | 17.6% |
| **FastAPI** | **14.8%** |
| Spring Boot | 14.7% |
| Flask | 14.4% |
| ASP.NET | 14.2% |
| **Django** | **12.6%** |
| Laravel | 8.9% |
| AngularJS | 7.2% |
| Svelte | 7.2% |
| Blazor | 7.0% |
| NestJS | 6.7% |
| Ruby on Rails | 5.9% |
| Astro | 4.5% |

Languages, all respondents, n = 31,771: JavaScript 66%, Python 57.9%, TypeScript 43.6%, Java
29.4%, C# 27.8%, PHP 18.9%, Go 16.4%. Databases, n = 26,083: PostgreSQL 55.6%, MySQL 40.5%,
SQLite 37.5%, SQL Server 30.1%, Redis 28%, MongoDB 24%.

**State of JS 2025**, front-end frameworks, "have used" — figures pulled from the
[Devographics GraphQL API](https://api.devographics.com/graphql) that backs
[2025.stateofjs.com](https://2025.stateofjs.com/en-US/libraries/front-end-frameworks/), because
the published page renders its charts client-side and serves no numbers to a fetcher. A 2026
edition does not exist: the API's schema contains `Js2025Edition` and no `Js2026Edition`.

| Framework | Have used | Heard, not used | Never heard | n |
|---|---|---|---|---|
| React | 84.81% | 14.85% | 0.35% | 12,130 |
| Vue | 52.79% | 46.48% | 0.73% | 12,098 |
| Angular | 48.35% | 50.53% | 1.12% | 12,093 |
| Svelte | 27.53% | 68.69% | 3.78% | 12,065 |
| Preact | 15.38% | 67.02% | 17.59% | 12,045 |
| Solid | 10.55% | 67.52% | 21.93% | 12,030 |
| htmx | 9.10% | 69.14% | 21.77% | 12,005 |
| Qwik | 3.51% | 56.14% | 40.34% | 12,012 |

Year over year, from the same API: React 82.45% → 84.81%, Angular 50.42% → 48.35%, Svelte
26.31% → 27.53%. Nothing is moving fast. Overall happiness with front-end frameworks was 3.7
out of 5 across 11,952 responses.

**A caveat on the State of JS numbers that the survey does not shout about.** The 2025 question
has three options only — never heard, heard, used. It is lifetime exposure, not current usage,
and it does not measure whether anyone liked it. The retention and positivity ratios that
earlier editions reported are not computable from the 2025 data: the API returns `null` for
`ratios` on every 2025 item. **Any claim of the form "Svelte has 91% retention in State of JS
2025" cannot be sourced to the survey's own data.** Several summary articles make that claim.
None of them is this file's source, and I could not reproduce the figure.

### What gets installed, from the npm registry API

Week of 2026-09-15 to 2026-09-21, [api.npmjs.org](https://api.npmjs.org/downloads/point/2026-09-15:2026-09-21/react).

| Package | Downloads that week | Same week 2025 | Ratio |
|---|---|---|---|
| `typescript` | 209,215,221 | — | — |
| `react` | 132,703,321 | 44,392,172 | 2.99× |
| `vite` | 131,207,416 | 36,497,095 | 3.60× |
| `react-dom` | 125,272,754 | — | — |
| `tailwindcss` | 95,576,864 | 23,191,190 | 4.12× |
| `vitest` | 73,825,000 | 15,614,815 | 4.73× |
| `playwright` | 69,104,951 | 20,624,801 | 3.35× |
| `@vitejs/plugin-react` | 67,276,507 | — | — |
| `@tanstack/react-query` | 48,009,546 | 12,991,605 | 3.70× |
| `next` | 42,734,285 | 12,913,617 | 3.31× |
| `webpack` | 43,367,999 | — | — |
| `zustand` | 39,781,458 | 11,260,878 | 3.53× |
| `jest` | 35,427,628 | 32,102,994 | 1.10× |
| `react-router-dom` | 32,965,386 | — | — |
| `redux` | 32,075,292 | — | — |
| `@tanstack/react-router` | 16,989,243 | — | — |
| `vue` | 12,038,101 | 7,010,314 | 1.72× |
| `@angular/core` | 4,960,205 | 4,146,125 | 1.20× |
| `cypress` | 4,649,846 | 6,284,219 | 0.74× |
| `svelte` | 4,236,198 | 1,859,042 | 2.28× |

**Read the ratios within a week, not across years.** Everything in the React and Vite cluster
roughly tripled year over year, which is implausible as real adoption growth and is more likely
CI volume, container rebuilds and agent-driven installs. **Unverified: I could not establish
what drove the ecosystem-wide inflation.** What survives the caveat is the comparison inside a
single week, and two year-over-year numbers that move against the tide: `@angular/core` grew
1.20× while the ecosystem tripled, and `cypress` **fell** 26% in absolute terms.

Major-version shares, computed from
[api.npmjs.org/versions/react/last-week](https://api.npmjs.org/versions/react/last-week) and
the equivalents:

| Package | Top version shares |
|---|---|
| `react` | 19.x — 69.6%; 18.x — 25.2%; 16.x — 2.4%; 17.x — 2.3% |
| `next` | 16.x — 66.8%; 15.x — 22.3%; 14.x — 7.9% |
| `vite` | 8.x — 43.9%; 7.x — 22.6%; 6.x — 16.0%; 5.x — 15.5% |
| `vue` | 3.x — 86.7%; 2.x — 13.2% |
| `svelte` | 5.x — 75.1%; 4.x — 18.3% |
| `@angular/core` | 21.x — 24.3%; 22.x — 18.7%; 20.x — 12.7%; 19.x — 6.9%; **9.x — 6.5%** |

Angular's version distribution is the flattest of the six and the only one with a
nine-major-versions-old release in its top five. **Unverified, but the natural reading: Angular
installs are weighted toward maintenance of long-lived applications rather than new
greenfield.** That is consistent with what the SA listings describe.

### "What developers like" versus "what employers hire for"

The gap is the point, and it runs in both directions.

| Technology | Developers (SoJS 2025 have-used) | Installs, last week | SA employers (n=105) | Remote employers (n=64) |
|---|---|---|---|---|
| React | 84.8% | 132.7M | 47% | 36% |
| Angular | 48.4% | 5.0M | 48% | 5% |
| Vue | 52.8% | 12.0M | 20% | 5% |
| Svelte | 27.5% | 4.2M | 0% | 0% |
| Next.js | 59.3% | 42.7M | 4% | 2% |
| Vite | 84.6% | 131.2M | 0% | 5% |
| Playwright | 50.3% | 69.1M | 4% | 3% |
| Cypress | 47.4% | 4.6M | 5% | 2% |
| Tailwind | — | 95.6M | 6% | 5% |
| shadcn/ui | — | — | 0% | 0% |
| FastAPI | — | 84.7M (PyPI) | 2% | 8% |
| Django | — | 9.4M (PyPI) | 11% | 9% |

Four readings, each of which changes a decision:

1. **Where developer usage and employer demand disagree most, employer demand lags by years,
   not by fashion.** Vite is used by 84.6% of State of JS respondents and named by 0 of 105 SA
   listings. Playwright outdownloads Cypress 14.9 to 1, and SA listings name Cypress slightly
   more often than Playwright. Job ads describe the last stack the hiring manager wrote, not
   the current one.
2. **Angular is the one place where employer demand exceeds developer enthusiasm, and only
   locally.** 48% of SA listings, 5% of remote listings, 1.20× year-over-year npm growth.
3. **The high developer-usage number for Next.js (59.3%) against the near-zero employer numbers
   (2–4%) is the widest gap in the table.** Developers have used Next.js. Employers are not
   asking for it. Both facts are true and the second one is the one that pays.
4. **Absence of a name is not absence of the tool.** 0% Vite in SA listings does not mean SA
   teams build with Webpack; it means SA job ads do not descend to the bundler. The only
   conclusion the silence supports is that you will not be screened out on it.

---

## Part 3 — Meta-frameworks and the React ecosystem

### Is plain React plus Vite still a normal employer ask?

**Yes, and it is the *normal* one.**

- Next.js named in **1 of 64** remote listings (2%), and even there as one of three options for
  headless commerce.
- Of the **23** remote listings naming React, **22** named no meta-framework at all. Two named
  Vite explicitly. One ruled Next.js out in the body.
- Next.js named in **4 of 105** SA listings (3.8%). Nuxt 0, SvelteKit 0, Remix 1, Astro 1.
- **React Server Components, or "RSC", or "server components", appears in 0 of 169 bodies.**

> "Our frontend is a single-page TypeScript web app built in React. We bundle with Vite and
> target modern browsers only. We test with Vitest, React Testing Library, Playwright, and
> Chromatic for visual regression. […] is styled via CSS modules, and is performance-tuned with
> route-based code splitting and skeleton UI. We've built our own design system, documented in
> an extensive Storybook. […] Our frontend is built on top of our REST API and GraphQL
> endpoints, backed by a Python/Flask/FastAPI, MongoDB, Postgres and Elasticsearch stack running
> on AWS."
>
> — Senior Frontend Engineer, Growth, 2026-09-21, **US only**
> ([Jobicy](https://jobicy.com/jobs/151313-senior-frontend-engineer-growth-usa-only-100-remote))

That is the single most informative stack paragraph in the corpus, and it is almost exactly
`CURRICULUM.md`'s Phase 3 stack with the backend swapped for the same Python one.

> "Frontend: Server-rendered Laravel Blade with Alpine.js, Livewire (admin), Tailwind CSS, and
> Vite — no React/Next.js"
>
> — Product Lead (Strategy + Full Stack), 2026-09-12, worldwide except US
> ([WorkingNomads](https://www.workingnomads.com/job/go/1857010/))

**The npm data agrees.** `@vitejs/plugin-react` was downloaded 67,276,507 times in the week of
2026-09-15 against `next`'s 42,734,285 — 1.58 to 1. `vite` as a whole outdownloaded `next` 3.07
to 1. `react-server-dom-webpack`, the RSC bundler integration, was downloaded 1,386,122 times
against `react-dom`'s 125,272,754 — about 1.1%. **Unverified, and this one needs a caveat: Next
vendors its own RSC implementation, so `react-server-dom-webpack` undercounts real RSC usage by
an unknown amount.** It is a floor, not a measurement.

### What react.dev actually says

This is the part where the documentation and the market genuinely disagree, and you should know
both.

> "If you want to build a new app or website with React, we recommend starting with a
> framework."
>
> — [react.dev/learn/creating-a-react-app](https://react.dev/learn/creating-a-react-app)

The page names, in order: **Next.js (App Router)**, **React Router (v7)**, **Expo** for native.
Under "Other frameworks" it lists **TanStack Start (Beta)** and **RedwoodSDK**. It then offers
the escape hatch:

> "If your app has constraints not well-served by existing frameworks, you prefer to build your
> own framework, or you just want to learn the basics of a React app, there are other options
> available for starting a React project from scratch."

And the from-scratch page is blunt about the cost:

> "Starting from scratch is an easy way to get started using React, but a major tradeoff to be
> aware of is that going this route is often the same as building your own adhoc framework. As
> your requirements evolve, you may need to solve more framework-like problems that our
> recommended frameworks already have well developed and supported solutions for."
>
> "For example, if in the future your app needs support for server-side rendering (SSR), static
> site generation (SSG), and/or React Server Components (RSC), you will have to implement those
> on your own."
>
> "The build tools listed above start off with a client-only, single-page app (SPA), but don't
> include any further solutions for common functionality like routing, data fetching, or
> styling."
>
> — [react.dev/learn/build-a-react-app-from-scratch](https://react.dev/learn/build-a-react-app-from-scratch)

That page names Vite first: "Vite is a build tool that aims to provide a faster and leaner
development experience for modern web projects. […] Vite is opinionated and comes with sensible
defaults out of the box."

**So: react.dev recommends a framework, and employers do not ask for one.** The resolution for
this plan is that the Phase 3 project is a data explorer — an authenticated, interactive,
client-heavy application over an API. It is the case where a SPA is the right answer and
react.dev's warning list (SSR, SSG, RSC) does not apply. Build it with React plus Vite, and be
able to say in an interview, in one sentence, why you did not use Next.js and what you gave up.
That sentence is worth more than the framework would have been.

Note a small inconsistency worth knowing: react.dev names "React Router (v7)" while
`react-router` on npm is at **8.4.0**, released 2026-09-15
([registry](https://registry.npmjs.org/react-router)). **Unverified: the docs page appears not
to have been updated for the v8 release.**

### React 19 and the React Compiler

- **React 19.3** is current, released **2026-09-09**, adding "View Transitions, Fragment Refs,
  `browser()`, Trusted Types, and more" ([react.dev/blog](https://react.dev/blog),
  [react.dev/versions](https://react.dev/versions)). React 19.0 shipped December 2024.
- **React 19 is 69.6% of all `react` installs**, React 18 is 25.2%. The migration is largely
  done.
- **React Compiler reached v1.0 on 2025-10-07** — "We're releasing the compiler's first stable
  release today, plus linting and tooling improvements to make adoption easier"
  ([react.dev/blog](https://react.dev/blog)). `babel-plugin-react-compiler` is at 1.0.0 on npm.
  Next.js 16 lists "React Compiler Support (stable)" as a headline feature.
- **React moved to the Linux Foundation.** "Introducing the React Foundation", 2025-10-07, and
  "The React Foundation: A New Home for React Hosted by the Linux Foundation", 2026-02-24
  ([react.dev/blog](https://react.dev/blog)).
- **RSC had two security incidents in December 2025.** "There is an unauthenticated remote code
  execution vulnerability in React Server Components. A fix has been published in versions
  19.0.1, 19.1.2, and 19.2.1. We recommend upgrading immediately." (2025-12-03), followed by two
  further disclosed vulnerabilities on 2025-12-11 ([react.dev/blog](https://react.dev/blog)).
  **Unverified, but worth saying: an unauthenticated RCE in the flagship new architecture, twice
  in nine days, is a reason employers are not in a hurry.**

### Next.js, for completeness

**Next.js 16** released 2025-10-21; current is **16.3.6**, 2026-09-22
([nextjs.org/blog](https://nextjs.org/blog), [registry](https://registry.npmjs.org/next)).
Headline features, verbatim: "Cache Components: A new programming model leveraging Partial
Pre-Rendering (PPR) and `use cache` for instant navigation"; "Turbopack (stable): Default
bundler for all apps"; "React Compiler Support (stable)". 16.x is 66.8% of `next` installs.

**Turbopack is now the default bundler in Next.js, and is essentially invisible outside it.**
The standalone `turbopack` npm package had 293 downloads in the sample week. State of JS 2025
puts Turbopack at 28.94% have-used against Vite's 84.61%.

### Vite, and the bundler that replaced its bundler

**Vite 8** released **2026-03-12**; current is **8.3.0**, 2026-09-10
([vite.dev/blog](https://vite.dev/blog), [registry](https://registry.npmjs.org/vite)). The
headline is a bundler swap:

> "Vite 8 ships with Rolldown as its single, unified, Rust-based bundler, delivering up to
> 10-30x faster builds while maintaining full plugin compatibility."
>
> "Vite becomes the entry point to an end-to-end toolchain with closely collaborating teams:
> the build tool (Vite), the bundler (Rolldown), and the compiler (Oxc)."
>
> — [vite.dev/blog/announcing-vite8](https://vite.dev/blog/announcing-vite8)

Vite 8 is 43.9% of `vite` installs six months after release; 5.x through 7.x together are 54%.
**Unverified: the slow-ish uptake is consistent with the install-size note in the announcement
(about 15 MB larger) and with Vite 8 being a bundler replacement rather than an API change.**
Standalone `rolldown` is at 10.67% have-used in State of JS 2025, `rspack` 7.47%.

### TanStack, state, and styling

**TanStack Query** is at **5.103.2** (2026-09-21) and describes itself as "the missing
data-fetching library for web applications", which "makes fetching, caching, synchronizing and
updating server state in your web applications a breeze"
([tanstack.com](https://tanstack.com/query/latest/docs/framework/react/overview)). It was
downloaded 48,009,546 times in the sample week — **more than `next`, more than `redux`, more
than `zustand`**. **TanStack Router** is at 1.170.38 with 16,989,243 weekly downloads;
**TanStack Start** is at 1.168.57 and react.dev still labels it "Beta".

Weekly downloads, same week: `@tanstack/react-query` 48.0M, `zustand` 39.8M, `react-router-dom`
33.0M, `redux` 32.1M, `jotai` 4.2M.

**The state-management question is settled in a way that is easy to miss: it split in two.**
Server state goes to TanStack Query, client state goes to Zustand or `useState`, and Redux is
now the third-largest of the three and shrinking relative to both. **Unverified — the npm
numbers support the ranking, not the causal story.** No listing in 169 explained it either way:
TanStack was named once in SA (as "React Query") and once remote ("Experience with TanStack is
a bonus"); Zustand twice remote, zero in SA; Redux four times in SA, four times remote.

**Tailwind CSS** is at **4.3.3** (2026-07-16), 95,576,864 weekly downloads, more than `react`.
v4.0 shipped 2025-01-22 — "an all-new version of the framework optimized for performance and
flexibility, with a reimagined configuration and customization experience"
([tailwindcss.com/blog](https://tailwindcss.com/blog)). v4.3 shipped 2026-05-08. On 2026-09-09
the blog announced "Tailwind Labs is joining Shopify". **Unverified: no statement found about
what that means for the project's governance or licence.** That is worth a `horizon/` line.

**shadcn/ui** describes itself in one sentence that explains why it never appears in a job ad:

> "This is not a component library. It is how you build your component library."
>
> — [ui.shadcn.com/docs](https://ui.shadcn.com/docs)

The `shadcn` CLI is at 4.21.0 (2026-09-04). It was named in **0 of 169 listings**.

### Are component libraries named in listings at all?

Barely. Across all 169 bodies: Tailwind 9, Storybook 3, Material UI 2, Bootstrap 2, Angular
Material 1, Vuetify 1, Ant Design 1, AG Grid 1, Chakra 0, PrimeNG 0, shadcn/ui 0,
styled-components 0. 89% of SA listings and 94% of remote listings named no styling or component
library at all.

The two that did name one, named it as a bonus:

> "Exposure to Material UI, Tailwind CSS, and CSS Grid advantageous"
>
> — Intermediate React Developer, Cape Town, ~2026-09-09, via Communicate IT
> ([PNet](https://www.pnet.co.za/jobs--Intermediate-React-Developer-Cape-Town-Northern-Suburbs-Communicate-IT--4268147-inline.html))

> "Hands-on experience with modern CSS frameworks, specifically Tailwind CSS and/or Vuetify"
>
> — Frontend Developer, Cape Town, ~2026-09-21
> ([PNet](https://www.pnet.co.za/jobs--Frontend-Developer-Cape-Town-TooMuchWifi--4211457-inline.html))

**What *is* named, twice, is a design system rather than a library** — "We've built our own
design system, documented in an extensive Storybook", and "design systems and component
libraries" as a nice-to-have in Role 2 of `2026-09-22-sa-target-roles.md`. That is a different
skill from consuming someone else's components, and it is the one the curriculum should aim at.

---

## Part 4 — Backend

### South Africa

| Backend | SA-A (n=54) | SA-B (n=51) | Pooled (n=105) | Pooled share |
|---|---|---|---|---|
| **C# / .NET** | 18 (33%) | 18 (35%) | **36** | **34.3%** |
| **Java** | 14 (26%) | 16 (31%) | **30** | **28.6%** |
| — Spring / Spring Boot named | 7 | 5 | 12 | 11.4% |
| **Node** | 12 (22%) | 15 (29%) | **27** | **25.7%** |
| — NestJS | 3 | 1 | 4 | 3.8% |
| — Express | 2 | 4 | 6 | 5.7% |
| **Python** | 8 (15%) | 12 (24%) | **20** | **19.0%** |
| — **Django** | 5 | 6 | **11** | **10.5%** |
| — **Flask** | 3 | 0 | **3** | **2.9%** |
| — **FastAPI** | **0** | **2** | **2** | **1.9%** |
| **PHP** | 5 (9%) | 2 (4%) | **7** | **6.7%** |
| — Laravel | 4 | 1 | 5 | 4.8% |
| **Go** | 1 | 2 | **3** | **2.9%** |
| **Ruby / Rails** | 0 | 1 | **1** | **1.0%** |

**C#/.NET is the largest single backend ask in South Africa, and it is not close to being
displaced.** Java is second. Python is fourth, and within Python, Django outnumbers FastAPI
five and a half to one.

The two FastAPI sightings in 105 SA listings, both of them naming Django in the same breath:

> "Python, Django, FastAPI, and modern application frameworks"
>
> — Senior Application Engineer (Python Django FastAPI), 2026-05-08
> ([IT-Online](https://it-online.co.za/2026/05/08/senior-application-engineer-python-django-fastapi/))

> "Python (FastAPI, Django, or similar)" … "TypeScript and React" … "relational databases
> (PostgreSQL, MySQL)"
>
> — Full Stack Engineer (Python), remote, 2026-09-21, via e-Merge IT Recruitment
> ([e-Merge](https://e-merge.co.za/full-stack-engineer-python-remote-up-to-r800k-per-annum/))

The second of these is the same role as Role 2 in `2026-09-22-sa-target-roles.md`, reposted
under a different title and salary. Worth noting: it is still live nine days later.

Django, where it is named, is named as production infrastructure:

> "Extensive experience with Django and Django REST Framework" … "Strong testing practices
> using PyTest, Unit Testing, and Integration Testing"
>
> — Lead Full Stack AI, Python Developer, Johannesburg, ~2026-09-23
> ([freehire](https://freehire.me/jobs/lead-full-stack-ai-python-developer-dvtcareers-3vp76lcl))

> "Django experience is preferred." … "Ability to use AI-assisted development tools responsibly
> while maintaining code quality, security and review standards."
>
> — Senior Python (Django) Developer, Johannesburg, hybrid, 2026-09-16
> ([IT-Online](https://it-online.co.za/2026/09/16/senior-python-django-developer-johannesburg-hybrid/))

### Remote and global

| Backend | Count (n=64) | Share |
|---|---|---|
| **Python, any** | 18 | 28% |
| — Django | 6 | 9% |
| — FastAPI | 5 | 8% |
| — Flask | 3 | 5% |
| — Python, no framework named | 9 | 14% |
| **Go** | 14 | 22% |
| **Node, any** | 14 | 22% |
| **Java, any** | 5 | 8% |
| **C# / .NET** | 3 | 5% |
| Ruby / Rails | 3 | 5% |
| Rust | 3 | 5% |
| PHP / Laravel | 3 | 5% |
| C++ | 2 | 3% |
| No backend language stated | 15 | 23% |

**Go at 22% is the biggest difference between the two markets** — 14 of 64 remote against 3 of
105 in South Africa. **Unverified: the remote sample skews to funded infrastructure and
developer-tools companies, which is where Go concentrates.**

FastAPI as a sole stack, from a listing whose timezone band includes Johannesburg:

> "3+ years of dedicated, hands-on production experience building high-performance asynchronous
> web services with FastAPI and modern Python (3.10+). Deep mastery of Python's asyncio
> ecosystem, dependency injection, and Pydantic v2 data validation."
>
> "Solid proficiency with relational databases (PostgreSQL), writing optimized raw SQL or
> leveraging ORMs like SQLAlchemy and Alembic for schema migrations and query tuning."
>
> "Located in the CET timezone (+/- 3 hours), we are unable to consider applications from
> candidates in other time zones."
>
> — Senior Python Developer (FastAPI), 2026-09-07
> ([WorkingNomads](https://www.workingnomads.com/job/go/1843235/))

And the clearest statement anywhere in 169 listings of what the two frameworks are *for*:

> "Mastery of FastAPI for high-performance microservices or Django (including Django REST
> Framework) for robust, feature-rich monolithic web applications."
>
> "Deep knowledge of relational databases (PostgreSQL preferred) including query profiling,
> optimization, indexing, and object-relational mapping (SQLAlchemy or Django ORM)."
>
> — Senior Python Developer (Fullstack, BE-Heavy), 2026-09-07
> ([WorkingNomads](https://www.workingnomads.com/job/go/1843246/))

That sentence is the answer to question 3. FastAPI is the microservices-and-APIs answer; Django
is the batteries-included monolith answer. `product` is an API with a separate SPA in front of
it. FastAPI is the correct choice for the thing being built, and the listings agree on what
each is for.

### FastAPI and Django, from their own documentation

**FastAPI** is at **0.141.1**, released **2026-07-29**
([release notes](https://fastapi.tiangolo.com/release-notes/)). **There is still no 1.0.** The
version history runs from 0.1.19 in February 2019 to 0.141.1 with no 1.0 milestone.

The notable 2026 change is **0.137.0, 2026-06-14**, which carries a breaking change
([GitHub release](https://github.com/fastapi/fastapi/releases/tag/0.137.0)):

> "♻️ Refactor internals to preserve `APIRouter` and `APIRoute` instances."
>
> "Now `router.routes` is no longer a plain list of `APIRoute` objects, it can contain these
> intermediate objects that can contain additional routers, forming a tree. Any logic that
> depended on iterating on the `router.routes` directly would be affected […] `router.routes`
> should be considered an internal implementation detail."
>
> "Future Features Enabled: Custom `APIRoute` subclasses […] Custom `APIRouter` subclasses […]
> Dependencies per router, Exception handlers per router, Middleware per router"

Also worth knowing: 0.141.0 added `app.frontend(check_dir="auto")` "to make local development
more convenient with `fastapi dev`"
([GitHub release](https://github.com/fastapi/fastapi/releases/tag/0.141.0)), and the docs now
carry "FastAPI Cloud deployment instructions". **Unverified: I did not evaluate what FastAPI
Cloud is or what it costs, and the plan does not need it.**

**Django** is at **6.1.1**, and the current LTS is **5.2 LTS**, supported to **April 2028**
([djangoproject.com/download](https://www.djangoproject.com/download/)). The supported series
are 5.2 LTS (extended support to April 2028), 6.0 (to April 2027) and 6.1 (to December 2027).
The page states that "Django 6.2 is the final release under the previous versioning and support
policy". **Unverified: the new policy is not described on the download page and I did not find
a first-party page that states it.**

**On PyPI**, last week ([pypistats.org](https://pypistats.org/api/packages/fastapi/recent), an
aggregator over PyPI's own published download dataset — flagged because it is one step removed
from the registry itself):

| Package | Last week |
|---|---|
| `uvicorn` | 113,791,906 |
| `starlette` | 110,976,233 |
| **`fastapi`** | **84,728,817** |
| `sqlalchemy` | 75,201,378 |
| `psycopg2-binary` | 47,736,589 |
| `alembic` | 40,303,391 |
| **`flask`** | **29,563,517** |
| `uv` | 28,269,229 |
| **`django`** | **9,445,248** |
| `poetry` | 9,285,297 |

**FastAPI outdownloads Django nine to one and Flask nearly three to one.** The same caveat
applies as for npm — CI and container builds dominate — but the ranking is stable and it
matches the Stack Overflow figure. `uv` outdownloads `poetry` 3.0 to 1, which supports the
curriculum's existing choice.

### .NET, since the question is whether abandoning it is a mistake

**.NET 10 is the current LTS**, released **2025-11-11**, supported to **2028-11-14**. .NET 8
(LTS) and .NET 9 (STS) both end support **2026-11-10**
([Microsoft support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)).
ASP.NET Core sits at 19.7% in the Stack Overflow 2025 survey, ahead of Angular and Vue.

SA listings pair .NET with a frontend framework routinely:

> "3+ years of experience in full-stack development, with a strong focus on Angular for the
> front-end" · "Proficiency in C# and ASP.NET MVC for back-end development" · "A good
> understanding of SQL databases (MSSQL preferred), with experience in writing T-SQL queries" ·
> "Familiarity with Object-Relational Mapping (ORM) technologies (Entity Framework a plus)"
>
> — Intermediate C# Full Stack Software Developer, Centurion, hybrid, 2026-09-21, via e-Merge
> ([e-Merge](https://e-merge.co.za/intermediate-c-full-stack-software-developer-centurion-hybrid-up-to-r800k-per-annum/))

> "C#.Net Core, ASP.Net, React, JavaScript, TypeScript, Redux, HTML, CSS, REST, JSON, SQL
> server/ PostgreSQL, Docker/Kubernetes, CI/CD, Agile, Azure."
>
> — Senior C# React Developer, KwaZulu-Natal, 2026-07-06
> ([IT-Online](https://it-online.co.za/2026/07/06/senior-c-react-developer-2/))

**The second quote is the important one.** C# plus React plus Postgres plus Docker plus Azure is
a live South African job description. The curriculum's Phase 3 produces every element of it
except the C#, which is already there. **The plan does not need to add .NET. It needs to stop
pretending the .NET is not there.**

---

## Part 5 — The rest of the stack

### Databases

| Database | SA pooled (n=105) | Remote (n=64) | Stack Overflow 2025 |
|---|---|---|---|
| SQL Server | 19 (18%) | 1 (2%) | 30.1% |
| **PostgreSQL** | **18 (17%)** | **17 (27%)** | **55.6%** |
| MySQL | 13 (12%) | 8 (12%) | 40.5% |
| Oracle | 8 (8%) | 1 (2%) | — |
| Redis | 5 (5%) | — | 28% |
| MongoDB | 4 (4%) | 6 (9%) | 24% |
| "SQL" or "NoSQL", no product named | 21 (20%) | 6 (9%) | — |
| No database named at all | ~26 | 34 (53%) | — |

**Postgres is the right database.** It is first in the remote sample, first in the Stack
Overflow survey by a wide margin, and effectively tied with SQL Server in South Africa. The SQL
Server share is the .NET and banking share; the curriculum already covers SQL Server in Phase
4 for the replatform, which happens to double as local-market coverage.

**PostgreSQL 18** is current, released 2025-09-25; 14 through 18 are supported, with 14 ending
2026-11-12 ([postgresql.org/support/versioning](https://www.postgresql.org/support/versioning/)).

### ORMs

**Nobody names them.** No ORM was named in 95 of 105 SA listings (90%) and 60 of 64 remote
listings (94%). Across all 169: Entity Framework 4, SQLAlchemy 4, Hibernate 3, Prisma 2,
Django ORM 1, Drizzle 0, TypeORM 0. Notably, Django was named 17 times across all samples and
"Django ORM" once.

`sqlalchemy` had 75.2M PyPI downloads last week and `alembic` 40.3M, so the tool is universal
and simply not worth a line in a job ad. `drizzle-orm` (16.3M/week on npm) now outdownloads
`prisma` (12.2M/week), which is the only interesting movement here and is **Unverified** as a
trend from a single week.

### Auth

**Nobody names an identity provider either.** Across 105 SA listings: Cognito 1, Ping Identity 1,
Active Directory 1, generic OAuth2/OIDC/JWT 5, and **zero** Entra, Auth0, Keycloak or
IdentityServer. Across 64 remote: Okta 1, Entra 1, generic OAuth2/OIDC 6, and zero Auth0,
Cognito, Clerk, Keycloak or Supabase Auth. 94% of SA listings and 89% of remote listings named
no auth technology at all.

The one SA listing that named a full auth stack is the same contract spec that is Role 3 in the
target-roles file:

> "Experience with authentication technologies: AWS Cognito, OAuth2, OpenID Connect, Active
> Directory integration"
>
> — Full Stack Developer (Advanced), Midrand / Menlyn / Rosslyn, ~2026-09-18, via Abalobi
> Solutions
> ([PNet](https://www.pnet.co.za/jobs--Full-Stack-Developer-Advanced-Python-3-9-Angular-17-Typescript-JavaScript-AWS-GenAI-RAG-MLOps-Rest-APIs-Midrand-Menlyn-Rosslyn-Home-Office-Rotation-Abalobi-Solutions--4274440-inline.html))

Interestingly, the same body names **"ORM frameworks such as SQLAlchemy / SQLModel"** — one of
only four SQLAlchemy sightings in the whole corpus, and it is in the Angular posting.

**Implication for Phase 7: the protocol is the asset, not the product.** Learn OAuth2 and OIDC
properly; treat Entra, Cognito, Auth0 and Keycloak as interchangeable implementations of it.
That is already what `CURRICULUM.md` says. No change needed.

### Testing

| Tool | SA pooled | Remote | SoJS 2025 have-used | npm last week |
|---|---|---|---|---|
| **Playwright** | 4 (4%) | 2 (3%) | 50.29% | **69,104,951** |
| **Cypress** | 5 (5%) | 1 (2%) | 47.37% | **4,649,846** |
| Selenium | 4 (4%) | 0 | 37.74% | — |
| **Vitest** | **0** | 1 (2%) | 54.00% | **73,825,000** |
| **Jest** | 2 (2%) | 2 (3%) | 75.19% | **35,427,628** |
| pytest | 1 (1%) | 3 (5%) | — | — |
| Storybook | 2 (2%) | 1 (2%) | 56.47% | — |
| No testing tool named | 89% | 91% | — | — |

**Playwright has won and the market has not noticed.** `playwright` outdownloads `cypress` 14.9
to 1, and `cypress` **fell** from 6,284,219 to 4,649,846 weekly downloads year over year while
everything else in the ecosystem tripled. Cypress is the only package measured in this file
whose absolute download count went down. Yet SA listings name Cypress slightly more often than
Playwright, and always in a list — "Playwright, Cypress, or Selenium".

`vitest` outdownloads `jest` 2.08 to 1 and passed it during the last year (15.6M against 32.1M
a year ago). **Vitest is now the default test runner for a Vite project and Jest is the
legacy.** Zero SA listings named either. `@playwright/test` alone had 44,409,707 weekly
downloads.

### Build tooling and package managers

Named in listings: **Vite 0 of 105 in SA**, 3 of 64 remote. Webpack 2 SA, 1 remote. Bun 0
everywhere. Turbopack 0 everywhere. 98% of SA listings and 94% of remote listings named no
build tool.

The reality underneath, from npm, same week: `esbuild` 201,162,613 (it is a dependency of
almost everything), `vite` 131,207,416, `webpack` 43,367,999, `turbopack` 293. State of JS 2025
have-used: Webpack 87.18%, Vite 84.61%, esbuild 54.33%, Turbopack 28.94%, Bun 25.95%, Rolldown
10.67%, Rspack 7.47%.

**Bun** is at 1.4.2 (2026-09-05) and 25.95% have-used. It appears in **0 of 169 listings** as a
requirement. It is a real tool and not yet a hiring signal.

Package managers, npm weekly: `pnpm` 128,881,068, `npm` (the CLI package) 12,032,977, `yarn`
6,769,120, `corepack` 3,430,944. **The `npm` figure understates reality badly, because the CLI
ships with Node and most users never install the package.** `pnpm` outdownloading `yarn` 19 to
1 is the reliable comparison. **Unverified: I could not find a first-party source that measures
package-manager share rather than download volume.**

On the Python side: `uv` 28,269,229 last week against `poetry` 9,285,297. The curriculum's `uv`
choice is correct and matches Role 1's "modern Python tooling such as uv or Poetry".

### Deployment

| Target | SA pooled (n=105) | Remote (n=64) |
|---|---|---|
| Azure, any | 36 (34%) | 10 (16%) |
| Docker | 31 (30%) | 12 (19%) |
| AWS, any | 27 (26%) | 24 (38%) |
| Kubernetes | 25 (24%) | 19 (30%) |
| GCP | 11 (10%) | 14 (22%) |
| Azure App Service | 5 (5%) | — |
| Terraform | 4 (4%) | — |
| Azure Container Apps | 2 (2%) | — |
| AWS ECS / Fargate | 2 (2%) | — |
| Cloudflare | 1 (1%) | 4 (6%) |
| **Vercel** | **0** | **1 (2%)** |
| **Netlify** | **0** | **1 (2%)** |

**Azure leads in South Africa; AWS leads remote.** The curriculum's "Azure first, AWS
equivalents documented" is exactly right for someone in Johannesburg who also wants remote work,
and the ratio is close enough that the AWS half must not be skipped.

**Vercel and Netlify are 1 each out of 169.** Deployment, as employers write it, means
containers and a hyperscaler. Container Apps appears twice, App Service five times — which
supports the Phase 8 choice of Container Apps but says nobody will screen you on it.

### AI coding assistants in listing requirements

This is the fastest-moving item in the corpus.

| | SA pooled (n=105) | Remote (n=64) |
|---|---|---|
| Any AI-assistance expectation | **21 (20%)** | **22 (34%)** |
| A specific product named | 9 (9%) | 8 (13%) |
| — Claude Code | 6 | 7 |
| — Cursor | 4 | 6 |
| — GitHub Copilot | 4 | 3 |
| — Codex | 2 | 2 |
| — Gemini / Amazon Q | 2 | 0 |
| Generic only ("AI coding assistants", "AI tools") | 12 | 14 |

**Caveat, and it is a big one.** In SA-B all four Claude Code mentions and all four Cursor
mentions come from a single agency; in SA-A both Claude Code mentions come from a single
agency. This is agency house style as much as market signal. The generic mentions are spread
more widely and are the sturdier number.

**Claude Code is the assistant most often named by product name in South African listings, and
GitHub Copilot is named less often than it.** That is the opposite of what the market share of
the tools would predict, and it is the single most surprising line in the local data.

> "Understand agentic development workflows, including using AI coding agents for tasks such as
> code generation, investigation, refactoring, testing, documentation and development
> automation. Critically evaluate AI-generated code and solutions rather than relying on
> generated output without appropriate Engineering review."
>
> — Senior Full Stack Software Developer (C#, Python, Node.js, JavaScript/TypeScript &
> React/Vue.js), Irene, ~2026-09-16, via Datafin
> ([PNet](https://www.pnet.co.za/jobs--Senior-Full-Stack-Software-Developer-C-Python-Node-js-JavaScript-TypeScript-React-Vue-js-Ir-Irene-Datafin-IT-Recruitment--4260401-inline.html))

> "Use AI tools such as Gemini and Claude Code responsibly to improve productivity while
> maintaining full ownership of every technical decision and every line of code you commit."
>
> — Full Stack Java Developer, Stellenbosch, hybrid, 2026-09-16, via Datafin
> ([Datafin](https://datafin.com/jobs/full-stack-java-developer-stellenbosch-hybrid/))

> "Exposure to or willingness to build strong proficiency in AI-assisted coding tools,
> particularly Claude Code."
>
> — Intermediate Fullstack Developer, remote (C#, Blazor, Entity Framework Core with SQLite),
> 2026-08-31, via Datafin
> ([Datafin](https://datafin.com/jobs/intermediate-fullstack-developer-remote-c-blazor-entity-framework-core-with-sqlite/))

> "Experience directing AI coding agents (e.g. Claude Code, Codex, Cursor)" — listed under
> **Must-Have**
>
> — Senior Java AI Software Engineer, Pretoria, hybrid, 2026-09-14, via e-Merge
> ([e-Merge](https://e-merge.co.za/senior-java-ai-software-engineer-pretoria-hybrid-r1-08m-pa/))

> "Using AI coding assistants as part of modern software development practices." — listed as a
> day-to-day duty for an **entry-level** role
>
> — Entry Full Stack Developer, Pretoria, 2026-09-21, via Sabenza IT & Recruitment
> ([CareerJunction](https://www.careerjunction.co.za/entry-full-stack-developer-at-sabenza-it-%26-recruitment-job-2645343.aspx))

And the remote end of the range:

> "Hands-on, day-to-day experience with AI-assisted development tools (e.g., GitHub Copilot,
> Cursor, Claude Code, Zed's Agentic editing, or similar) for coding, debugging, and code
> review; comfort with prompt/context engineering and sound judgment about validating
> AI-generated output"
>
> — Senior Software Engineer (Full-stack Node + React), 2026-09-20, **LATAM only**
> ([Jobicy](https://jobicy.com/jobs/153741-senior-software-enginner-full-stack-node-react))

> "AI agents produce most of our code."
>
> — Senior Software Engineer, remote, 2026-08-17
> ([WeWorkRemotely](https://weworkremotely.com/remote-jobs/edfinity-senior-software-engineer-remote))

**Wording strength.** In September 2026 the requirement has two halves everywhere it appears —
use the tool, and review its output. "Critically evaluate AI-generated code […] rather than
relying on generated output", "while maintaining full ownership of every technical decision and
every line of code you commit", "sound judgment about validating AI-generated output".
`2026-09-22-sa-target-roles.md` called that sentence "the most unusual sentence across all three
postings". It is no longer unusual. It is a fifth of the local market and a third of the remote
one, and it has reached entry-level postings.

`AI_USAGE.md` and the Friday reproduce-from-scratch check are, on this evidence, the most
directly employable practice in the whole repository. That is worth saying out loud in
`CURRICULUM.md`.

---

## The intersection: what all the evidence agrees on

| Question | Official docs | npm / PyPI | Surveys | SA listings | Remote listings |
|---|---|---|---|---|---|
| Is React the frontend to learn? | react.dev is React's own docs | 26.7× Angular | SoJS 84.8% used; SO 44.7% | 47%, tied with Angular | 36%, 7× Angular |
| Is Angular worth learning too? | v22 current; v2–v19 unsupported | 1.20× YoY against a 3× ecosystem | SoJS 48.4% used | **48% — yes, locally** | 5% — no |
| Is Next.js the default ask? | react.dev recommends a framework | `next` 42.7M vs `@vitejs/plugin-react` 67.3M | SoJS 59.3% used | 4% | **2%** |
| Is Vite the build tool? | react.dev names it first for from-scratch | 131.2M/wk; Vite 8 ships Rolldown | SoJS 84.6% used | 0% named | 5% named |
| Is FastAPI the Python backend? | 0.141.1, still pre-1.0 | 9× Django on PyPI | SO 14.8% vs Django 12.6% | **2% — Django wins locally** | 8% vs Django 9% |
| Is Postgres the database? | PG 18 current, 5-year support | — | SO 55.6%, first | 17%, tied with SQL Server | 27%, first |
| Playwright or Cypress? | — | **14.9× Cypress; Cypress fell 26%** | SoJS 50.3% vs 47.4% | Cypress 5, Playwright 4 | Playwright 2, Cypress 1 |
| Vitest or Jest? | — | 2.08× Jest | SoJS Jest 75.2% vs Vitest 54.0% | both ~0 | both ~0 |
| Is .NET dead in SA? | .NET 10 LTS to 2028 | — | SO ASP.NET Core 19.7% | **34% — the largest backend** | 5% |
| Are AI assistants a requirement? | — | — | — | 20% | 34% |

Reduced to a sentence: **every layer `CURRICULUM.md` picked is either the leader or tied for
the lead in the market the plan is aiming at, and the only two places the local market disagrees
are Angular, which the plan should decline on purpose, and .NET, which the plan already has and
does not count.**

---

## Happening / Consolidating / Noisy

Per `horizon/README.md`. Most career mistakes come from treating the third category as the
first.

### Happening — in production at companies now

- **React 19.** 69.6% of all `react` installs. 19.3 released 2026-09-09. The migration from 18
  is largely done.
- **TypeScript everywhere.** 209M weekly npm downloads, more than `react`. Constant across all
  three target postings and both listing samples.
- **Vite as the build tool.** 84.6% have-used, 131M weekly downloads, named first by react.dev's
  own from-scratch page.
- **Playwright.** 69.1M weekly downloads against Cypress's 4.6M, and Cypress declining in
  absolute terms. Already named in the Phase 3 exit test.
- **Tailwind v4.** 95.6M weekly downloads, more than React. Named more than any other styling
  choice in listings, which is a low bar but a real one.
- **TanStack Query.** 48.0M weekly, more than `next`, more than `redux`.
- **Postgres.** First in the remote sample, first in Stack Overflow, tied first locally.
- **Docker plus a hyperscaler as the deployment story.** 30% of SA listings, Kubernetes 24%.
- **AI coding assistants as a stated requirement.** 20% of SA listings, 34% of remote, including
  entry-level. With "critically review the output" attached every time.
- **Angular, in South African enterprise.** 48% of listings. This is happening whether or not
  the plan engages with it.
- **C#/.NET in South Africa.** 34% of listings, the largest single backend, with .NET 10 LTS
  supported to 2028.

### Consolidating — clearly winning, still early

- **Vitest over Jest.** 2.08× on npm and it overtook during the past year, but Jest is still at
  75.2% lifetime have-used against Vitest's 54.0%. It will win; it has not finished winning.
- **React Compiler.** v1.0 on 2025-10-07, stable integration in Next.js 16. Not yet visible in
  any listing.
- **Rolldown inside Vite.** Default in Vite 8 since 2026-03-12, and Vite 8 is 43.9% of installs
  six months on. The migration is under way and is invisible to users, which is the point.
- **TanStack Router.** 17.0M weekly downloads and growing; `react-router` is at 33.0M. Two
  routers, both real.
- **pnpm.** 19× yarn. **Unverified as a share measurement** for the reason given above.
- **Zustand as the client-state default.** 39.8M weekly, above `redux` at 32.1M.
- **Drizzle over Prisma.** 16.3M against 12.2M. One week of data. Watch it, do not act on it.

### Noisy — loud, unproven, might be nothing, *for a person being hired*

- **React Server Components.** Zero mentions in 169 listings. `react-server-dom-webpack` at
  about 1.1% of `react-dom`. Two unauthenticated-RCE security advisories in December 2025.
  Understand what it is; do not build the curriculum around it.
- **Next.js as a requirement.** 1 of 64 remote, 4 of 105 SA. The discourse and the hiring market
  are not the same market. Know the difference between App Router and Pages Router well enough
  to answer a question; do not spend a module on it.
- **Bun.** 25.95% have-used, 0 of 169 listings. A good tool, not a hiring signal.
- **Turbopack outside Next.js.** 293 weekly downloads as a standalone package.
- **shadcn/ui.** 0 of 169 listings. Useful; not a credential.
- **Svelte and SvelteKit.** 0 of 169 listings against 27.5% have-used. The gap between how much
  developers like it and how much anyone hires for it is the widest in the file.
- **Vercel and Netlify as deployment targets.** 1 each of 169.
- **Rolldown, Rspack and Bun as standalone bundler choices.** 10.7%, 7.5% and 26.0% have-used,
  and nobody is hiring on them.

### One thing to stop tracking

**"Is Next.js the default?"** It has been asked and answered on three independent sources that
disagree with each other in the right way: the docs say yes, the installs say no, the job ads
say emphatically no. Revisit at the next `horizon/` entry only if the remote listing count moves
above 10%.

---

## What I could not verify

Recorded honestly, because the rule is that an unreachable source is stated, not guessed.

**Survey data I could not get from the publisher.**

- **State of JS retention, interest and positivity ratios for 2025 do not exist in the
  publisher's own data.** The Devographics GraphQL API returns `null` for `ratios` on every 2025
  and 2024 item, and the 2025 question offers only three options — `never_heard`, `heard`,
  `used`. Widely repeated figures such as "Svelte 91% retention in State of JS 2025" could not
  be reproduced from the survey's own API and are not used in this file.
- **Stack Overflow's 2025 "Admired and Desired" figures for web frameworks.** The section exists
  in the page's navigation; the numbers are rendered client-side and did not come through any
  fetch route tried.
- **The Stack Overflow 2025 percentage table could not be read through a reader proxy.**
  `r.jina.ai` returned the narrative text and the response counts but rendered every chart row
  as 0%. The percentages in this file come from two independent fetches of the same page that
  agreed with each other. **Unverified to the extent that both fetches used the same rendering
  path.**
- **There is no 2026 Stack Overflow Developer Survey.** `survey.stackoverflow.co/2026/` and
  `/2026/technology` both return HTTP 404. There is no State of JS 2026: `2026.stateofjs.com`
  does not resolve, and the Devographics schema contains `Js2025Edition` with no 2026 successor.
  Every survey figure in this file is from 2025.

**Facts the vendors do not publish.**

- **What drove the roughly 3× year-over-year inflation in npm download counts across the React
  and Vite cluster.** It is not plausible as adoption growth. npm publishes no breakdown of CI
  versus human installs.
- **What "Tailwind Labs is joining Shopify" (2026-09-09) means for Tailwind's governance,
  licence or release cadence.** The blog post is the only first-party statement and it does not
  say.
- **Whether react.dev's "React Router (v7)" recommendation is deliberate or stale**, given
  `react-router` shipped 8.4.0 on 2026-09-15.
- **Django's post-6.2 versioning and support policy.** The download page says "Django 6.2 is the
  final release under the previous versioning and support policy" and does not describe the new
  one; I found no first-party page that does.
- **Real React Server Components adoption.** `react-server-dom-webpack` is a floor, not a
  measurement, because Next vendors its own implementation.
- **Package-manager share as opposed to download volume.** The `npm` CLI ships with Node, so its
  package download count is meaningless; no first-party share measurement was found.
- **What FastAPI Cloud is, costs, or implies for the framework's governance.** The docs link to
  it; I did not evaluate it.

**Job-listing holes.**

- **The pooled SA figure of 105 contains an unreconciled overlap.** IT-Online republishes the
  CareerJunction feed; at least 5 IT-Online listings in SA-B carried CareerJunction apply links,
  and SA-A read CareerJunction directly. The true unique count is probably 97 to 102.
- **LinkedIn again returned titles and never a body**, so the SA direct-employer segment —
  banking, insurance, telco, FMCG hiring without an agency — is absent from every count here as
  it was from the data file. This is the largest single hole and it is the segment most likely
  to be Angular-and-.NET heavy, which means **the Angular and .NET shares in this file are more
  likely to be understated than overstated.**
- **Two SA-A listings were coded from their titles** because the bodies were pure boilerplate.
  That breaks the file's own rule. Removing them moves React from 28 to 27, Node from 12 to 11,
  C# from 18 to 17 and Java from 14 to 13.
- **One SA-B listing titled "React Developer" never names React in its body** — the skills
  section lists only Java, Agile and teamwork. It was coded as no-framework. A title-based crawl
  would have scored it as React. This is the clearest evidence in the harvest that title
  inference is unsafe.
- **One SA-B listing names Redux, Apollo and Material-UI and never the word React.** Coded as
  no-framework-named. It is almost certainly a React job. Counting it moves React from 21 to 22
  in that sample.
- **A summarising fetch tool fabricated a technology list on at least one SA-A page.** All
  auto-generated lists were discarded thereafter. A smaller fabrication in a body read once
  cannot be ruled out.
- **The remote sample's Python-framework breakdown is substantially one staffing marketplace's
  templated copy.** Strip it and FastAPI drops from 5 to 2 and Django from 6 to 4.
- **I did not count Blazor as a frontend framework.** Five SA-A listings use it as their
  frontend. If Blazor counts, the SA-A no-framework bucket drops from 9 to 7. It is a
  definitional choice and it is arguable.
- **"AI coding assistant as a requirement" is the softest column in the file.** Listings naming
  Claude or GPT as *product* dependencies were excluded; listings saying only "AI-savvy" were
  included. A different coder would land anywhere between 14 and 45 across the two samples.

**Reachability notes — extending the list in `2026-09-23-data-stack-and-certifications.md`.**

Two corrections to yesterday's list, from today's attempts:

- **RemoteOK was reachable today.** `https://remoteok.com/api` returned HTTP 200, 625 KB, 100
  rows with full `description`, `location`, `tags` and `date` fields. Yesterday's file records
  it as returning no rows. It should not be skipped next time.
- **Dice returned 200 on its homepage** rather than yesterday's 410. Not harvested; noted.

New results:

| Host | Result today |
|---|---|
| PNet, CareerJunction, Datafin, ExecutivePlacements | 200 on every page, no rate limiting, no proxy needed |
| IT-Online, e-Merge, freehire.me, Hire Resolve | 200 on every page, no proxy needed |
| **Remotive API** (`/api/remote-jobs?category=software-dev`) | 200, full HTML descriptions, **but caps at 18 jobs for this category regardless of `limit`** |
| **Jobicy API** (`/api/v2/remote-jobs?count=50&industry=dev`) | 200, 50 jobs, full `jobDescription`. Best single remote source by volume |
| **WeWorkRemotely RSS** | 200. Full-stack 40 items, devops 22, backend 6. **The frontend category returns an empty 460-byte feed.** The HTML site is still 403 |
| **Himalayas** (`/jobs/api?limit=50&offset=N`) | 200, paginates, useful `locationRestrictions` and `timezoneRestrictions` fields, but mostly non-dev rows |
| **WorkingNomads** (`/api/exposed_jobs/`) | 200, 56 jobs, full descriptions, filterable by `category_name` |
| **Devographics GraphQL** (`api.devographics.com/graphql`) | 200 on POST, introspectable. **This is how to get State of JS numbers**; the rendered site serves none |
| **npm registry and downloads API** | 200. `api.npmjs.org/downloads/point/<range>/<pkg>` and `api.npmjs.org/versions/<pkg>/last-week` both work and are the right tools |
| **pypistats.org API** | 200 but **rate-limits aggressively** — roughly one request per three seconds. Pace it |
| Y Combinator `workatastartup.com` | **HTTP 406** |
| `survey.stackoverflow.co/2026/` | **HTTP 404** — no 2026 survey |
| `2026.stateofjs.com` | **does not resolve** — no 2026 edition |
| `executiveplacements.com/Jobs/Search?q=` and `/Jobs/1/IT-Jobs.htm` | **404**; the working path is `/JobList.asp?kwds=` |
| `hireresolve.co.za/jobs/` | **404**; working paths are `/find-a-career/it/` and `/job/<slug>/` |
| `hireresolve.co.za/career-search/?keyword=` | 200 but the `keyword` parameter is silently ignored |
| `it-online.co.za/<yyyy>/<mm>/<dd>/` | 200, but it is a **news** archive, not a job archive. Jobs are at `/category/jobs/` and `/<yyyy>/<mm>/<dd>/<job-slug>/`, and `/category/jobs/page/3/` and `/page/4/` return byte-identical results — pagination is broken |
| `e-merge.co.za/web-mobile-jobs/` | 200 but stale; newest item September 2023. `/c-net-jobs/` and `/java-jobs/` are current |

**Two structural warnings for anyone repeating this.** IT-Online double-publishes every listing
under a bare slug and a `– Province City` slug with identical bodies; a naive crawl doubles
every count. And several staffing marketplaces append a boilerplate catalogue of every stack
they place into — one such catalogue would have inflated Next.js from 1 to 4 in the remote
sample and invented Svelte hits from nothing.

---

## What this changes in `CURRICULUM.md`

Proposed edits. **Not applied — this file only argues for them.** They are small, because the
evidence says the plan is right. The three that matter are 1, 2 and 4.

### 1. Name the C# and ASP.NET Core experience, in "The requirements"

The plan "abandoned" C# and the page never mentions it. That is the largest single asset in the
local market — 34% of 105 SA listings, the biggest backend ask — and the requirements list's
first item is production experience in years. Proposed addition after the requirements list, in
the page's own voice:

> **What the plan is standing on.** The production experience is C# and ASP.NET Core, and this
> plan does not build on it. That is deliberate — the roles in `research/` are Python-first, and
> a second backend is a whole phase — but it is not a reason to leave it off the page. C#/.NET
> is named in 34% of South African listings read on 2026-09-23, more than any other backend, and
> ASP.NET Core sits at 19.7% in the Stack Overflow 2025 survey, ahead of Angular and Vue. Those
> years count toward requirement 1 wherever they were earned. The move is not to re-learn .NET;
> it is to be able to say, in an interview, what transfers — HTTP semantics, dependency
> injection, ORMs, migrations, auth middleware, CI — and to have Phase 2 and Phase 3 prove the
> Python and React halves that do not. See `research/2026-09-23-full-stack-tooling.md`.

### 2. Change the Phase 3 component-library module

"A small component library" is aimed at a thing that appears in **0 of 169 listing bodies** for
shadcn/ui, 2 for Material UI, and 0 for every other named library. What *is* named, twice, is a
**design system** — "We've built our own design system, documented in an extensive Storybook",
and "design systems and component libraries" as a nice-to-have in Role 2. Proposed edit to the
Phase 3 modules cell:

- Replace `a small component library` with `a small design system — tokens, a handful of
  accessible primitives, and Storybook as its documentation`
- Add `Tailwind CSS v4` to the same cell. It is 95.6M weekly npm downloads, more than React, and
  the most-named styling choice in listings even at 6%.
- Add `Storybook` to the Phase 3 project cell.

The reason is not that Storybook is fashionable. It is that a documented design system is
demonstrable to a stranger and a copy of someone else's components is not.

### 3. Name the build and test tooling in Phase 3

The phase says "build tooling" and "end-to-end testing" without naming anything. Every other
phase in the file names its tools. Proposed edit to the Phase 3 modules cell:

- `build tooling` → `build tooling — Vite 8, and what Rolldown replaced`
- `end-to-end testing` → `component and unit testing with Vitest; end-to-end testing with
  Playwright`

Evidence: Vite 131.2M weekly against Webpack's 43.4M; Vite 8 ships Rolldown as default since
2026-03-12; Vitest 73.8M against Jest's 35.4M and rising; Playwright 69.1M against Cypress's
4.6M, with Cypress the only package measured here whose absolute downloads fell year over year.
Playwright is already in the Phase 3 project cell — this makes the module match the project.

### 4. Add one sentence to Phase 3 on the framework decision, and make it a decision record

Phase 3 builds a SPA. react.dev says "we recommend starting with a framework". Those two facts
need reconciling once, in writing, because it is an interview question. Proposed addition below
the Phase 3 table:

> **Why React and Vite rather than Next.js.** `react.dev` recommends starting with a framework;
> employers do not ask for one. Next.js was named in 1 of 64 remote listings and 4 of 105 South
> African listings read on 2026-09-23, and 22 of the 23 remote listings naming React named no
> meta-framework at all. The explorer is an authenticated, interactive client over an API — the
> case where react.dev's own warnings about SSR, SSG and RSC do not bite. This goes in
> `decisions/` with what it costs: no server rendering, no React Server Components, and routing,
> data fetching and code splitting assembled by hand. See
> `research/2026-09-23-full-stack-tooling.md`.

That is a decision record with two fairly-stated options, which is exactly what the
`decisions/` practice exists for. Write it during Phase 3, not after.

### 5. Add TanStack Query to Phase 3's data-fetching module

The module is currently `data fetching`. TanStack Query at 48.0M weekly downloads is larger than
`next`, larger than `redux` and larger than `zustand`, and server-state caching is where the
interesting failure modes live — stale reads, refetch storms, cache invalidation after a
mutation. Proposed: `data fetching, and server state as its own problem — TanStack Query`.
Add to the same cell: `client state with Zustand, and why it is a different problem`.

### 6. Do not add Angular. Say why, on the page

The Angular share is 48% locally and the plan should still decline. But an unexplained absence
reads as an oversight to a reviewer, and one of the three target postings names Angular 17+.
Proposed addition below the Phase 3 table, or in "When to reassess":

> **Angular is deliberately not here.** It was named in 48% of South African listings read on
> 2026-09-23 — genuinely co-equal with React locally — and in 5% of remote ones. A second
> framework costs a phase and buys only the local half of the target. React is the answer that
> works in both markets. The trigger to revisit: if the search narrows to South African
> enterprise, or if an offer conversation reaches a technical round on an Angular codebase, then
> Angular becomes a two-week reading task and not a phase, because the TypeScript, the
> component tree and the reactivity concepts already transfer. Note also what the listings
> actually ask for: of 50 Angular mentions only 11 named a version, and those ran v9 to v17 —
> versions Angular itself no longer supports, since "Angular versions v2 to v19 are no longer
> supported". The Angular work in this market is maintenance of long-lived applications.

### 7. Strengthen the `AI_USAGE.md` line in the requirements list

Requirement 6 says "Using coding assistants, and critically reviewing what they produce",
sourced to one posting. It is now 20% of South African listings and 34% of remote ones, it has
reached entry-level postings, and the review half is attached every single time. Proposed: add
one sentence to requirement 6 or to the note beneath the list:

> Measured again on 2026-09-23: named in 20% of 105 South African listings and 34% of 64 remote
> ones, including an entry-level posting, and never without the review clause — "critically
> evaluate AI-generated code […] rather than relying on generated output". Claude Code is the
> assistant most often named by product name in South African listings, ahead of GitHub Copilot.
> `AI_USAGE.md` and the Friday reproduce-from-scratch check are the practice that answers this.

### 8. Correct one detail in the Phase 2 sources row

The Phase 2 row lists "FastAPI documentation" as the free source, which is right. Add a line to
the paragraph below the table:

> FastAPI is still pre-1.0 — 0.141.1 as of 2026-07-29 — and 0.137.0 on 2026-06-14 carried a
> breaking change to router internals: `router.routes` is now a tree rather than a flat list and
> "should be considered an internal implementation detail". Pin the version in `product` and
> read the release notes on every bump. Pre-1.0 is not a reason to avoid it: 84.7M weekly PyPI
> downloads against Django's 9.4M, and 14.8% against Django's 12.6% in the Stack Overflow 2025
> survey.

### 9. One line for the Phase 3 sources row

The row currently reads "react.dev, including its interactive tutorial". Add: `the Vite
documentation, and Playwright's own docs`. Both are first-party, both are free, and both are
named in the module changes above.

### 10. Queue one `horizon/` item

**"Tailwind Labs is joining Shopify" (2026-09-09).** Tailwind is 95.6M weekly downloads and is
about to be a proposed Phase 3 module. There is no first-party statement on what the acquisition
means for governance, licence or cadence. Track it; do not act on it yet.

---

## Sources

Every URL is inline above. The load-bearing ones, grouped:

- **React, first-party:** `react.dev/learn/creating-a-react-app`,
  `react.dev/learn/build-a-react-app-from-scratch`, `react.dev/versions`, `react.dev/blog`.
- **Other official docs and release notes:** `nextjs.org/blog`, `vite.dev/blog` and
  `vite.dev/blog/announcing-vite8`, `angular.dev/reference/releases`,
  `fastapi.tiangolo.com/release-notes` and the GitHub release pages for FastAPI 0.137.0 and
  0.141.0, `djangoproject.com/download`, `postgresql.org/support/versioning`,
  `dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core`, `tailwindcss.com/blog`,
  `ui.shadcn.com/docs`, `tanstack.com/query/latest/docs/framework/react/overview`.
- **Registries, read directly on 2026-09-23:** `api.npmjs.org/downloads/point/<range>/<pkg>` for
  weekly download counts, `api.npmjs.org/versions/<pkg>/last-week` for major-version shares,
  `registry.npmjs.org/<pkg>` for `dist-tags` and release dates, and `pypistats.org/api` for
  PyPI counts — the last flagged as one step removed from PyPI's own dataset.
- **Surveys, from the publisher:** `survey.stackoverflow.co/2025/technology`, and the State of
  JS 2025 figures pulled from `api.devographics.com/graphql`, which is the API behind
  `2025.stateofjs.com`. No 2026 edition of either exists.
- **Job listings:** the URLs quoted in Parts 1 through 5. Boards, APIs and failures are recorded
  in the reachability table under "What I could not verify".
- **Companion file:** `research/2026-09-23-data-stack-and-certifications.md`, same date, the
  data half of the stack, and the origin of the reachability notes this file extends.
