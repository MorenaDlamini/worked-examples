# floci — can I build this locally?

Yes, and the repository is real, large and unusually active — 24,420 stars, 2,633 forks, MIT
licensed, with commits landing the same day this was written ([GitHub API, repos/floci-io/floci](https://api.github.com/repos/floci-io/floci)).
The one blocking gap on this machine is Java: the build enforces **exactly JDK 25** via a Maven
enforcer rule, and this machine has JDK 24.0.2, so `./mvnw` will fail at the enforcer step before
it compiles anything ([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)).
Install Temurin 25 and Docker Desktop and the build itself is unremarkable — but the *project* is
a 4,430-file Java emulator of 80-plus AWS services, so building it is easy while contributing to
it is not.

## What floci is

Floci is a local AWS emulator: it runs AWS-shaped service endpoints on your own machine so that
SDKs, the AWS CLI, Terraform and test suites can point at `http://localhost:4566` instead of a
real AWS account. The README states it plainly:

> "Floci is a free, open-source local AWS emulator for development, testing, and CI. It gives you
> AWS-shaped services on your machine without requiring a cloud account, an auth token, or paid
> feature gates."
> — [README.md](https://raw.githubusercontent.com/floci-io/floci/main/README.md)

It positions itself explicitly as a drop-in replacement for LocalStack Community Edition, and the
repository topics include `localstack` alongside `aws`, `docker`, `testcontainers`
([GitHub API](https://api.github.com/repos/floci-io/floci)).

What is proven from primary sources:

- **License**: MIT ([GitHub API](https://api.github.com/repos/floci-io/floci)).
- **Age**: repository created 2026-02-18; the `floci-io` org created 2026-03-27
  ([GitHub API, orgs/floci-io](https://api.github.com/orgs/floci-io)). This is a young project,
  roughly seven months old at time of writing.
- **Activity**: last push 2026-09-17, the same day. The five most recent commits on `main` span
  five different authors — Hector Ventura, Vũ Thế Huy, Kenshin Okinaka, XuJian, Anders Wasen
  ([commits API](https://api.github.com/repos/floci-io/floci/commits?per_page=5)). Recent merged
  PRs come from at least seven distinct accounts, so this is not a one-person repository with a
  star count ([pulls API](https://api.github.com/repos/floci-io/floci/pulls?state=closed)).
- **Releases**: 2.1.0 on 2026-09-15, 2.0.1 and 2.0.0 on 2026-09-01, 1.7.0 on 2026-08-18
  ([releases API](https://api.github.com/repos/floci-io/floci/releases)). CONTRIBUTING describes
  a tag-driven release model with nightly builds from `main`
  ([CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md)).
- **Open issues**: 113 (this figure from the GitHub API includes open pull requests; there was
  1 open PR at the time of checking) ([GitHub API](https://api.github.com/repos/floci-io/floci)).
- **Family**: it is one of four cloud emulators in the org — `floci` (AWS), `floci-az` (Azure,
  621 stars), `floci-gcp` (359), `floci-oci` (74) — plus a CLI, a UI, Testcontainers modules for
  five languages and a Rust DuckDB sidecar
  ([org repos API](https://api.github.com/orgs/floci-io/repos)).

**Production-ready or early?** Early, but not a toy. At version 2.1.0 and seven months old it is
young by any standard, and the current open issue list is dominated by genuine correctness bugs
in emulated behaviour — DynamoDB composite keys colliding, EC2 `DescribeImages` ignoring tag
filters, RDS silently dropping parameter changes
([issues API](https://api.github.com/repos/floci-io/floci/issues?state=open)). That is the normal
condition for an emulator chasing a moving cloud API, not a sign of neglect. Treat it as suitable
for local development and CI, which is what it claims, and **unverified** for anything else.

## Tech stack and build requirements

Read from the manifests, not the README.

**Language and build system.** Java, built with Maven. Project version `2.1.0`
([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)).

**The hard version pin.** Two places in `pom.xml` fix the JDK:

```xml
<maven.compiler.release>25</maven.compiler.release>
```

and, more importantly, a `maven-enforcer-plugin` rule with a closed range:

```xml
<requireJavaVersion>
    <version>[25,26)</version>
    <message>Floci requires JDK 25. Set JAVA_HOME to JDK 25.</message>
</requireJavaVersion>
```

That is `[25,26)` — inclusive of 25, exclusive of 26. Not "25 or later". JDK 24 fails it; a
future JDK 26 would fail it too ([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)).

**Framework**: Quarkus 3.39.2 (`quarkus.platform.version`), with the `quarkus-maven-plugin` and
a `native` profile that requires GraalVM/Mandrel — not needed for a normal build
([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)).

**Maven**: the wrapper pins Apache Maven 3.9.16, `distributionType=only-script`, meaning the
wrapper script downloads Maven itself
([.mvn/wrapper/maven-wrapper.properties](https://raw.githubusercontent.com/floci-io/floci/main/.mvn/wrapper/maven-wrapper.properties)).
A `mvnw.cmd` is present at the repository root alongside `mvnw`, so no POSIX shell is required to
invoke the build ([repo tree API](https://api.github.com/repos/floci-io/floci/git/trees/main)).

**Docker**. `docker-compose.yml` builds from `docker/Dockerfile` and mounts the Docker socket
into the container:

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
```

([docker-compose.yml](https://raw.githubusercontent.com/floci-io/floci/main/docker-compose.yml)).
The Dockerfile is a two-stage Linux build on `eclipse-temurin:25-jdk-noble` → `eclipse-temurin:25-jre-noble`
([docker/Dockerfile](https://raw.githubusercontent.com/floci-io/floci/main/docker/Dockerfile)).
Docker is not incidental: the emulator shells out to real containers for Lambda, RDS and
ElastiCache, and `docker-java` 3.7.1 is a first-class runtime dependency
([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)).

**Test suite**. JUnit 5 with Hamcrest and RestAssured
([CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md)).
Surefire is configured with `-Xmx6g`, with this comment in the POM:

> "The suite's end-of-run live set exceeds the 4g default heap of 16g CI runners; a full GC near
> the end reclaims almost nothing."

([pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml)). GitHub code search
finds `DockerClient` referenced across 45 files under `src/test`, so a meaningful part of the
suite genuinely needs a Docker daemon
([code search API](https://api.github.com/search/code?q=repo:floci-io/floci+DockerClient+path:src/test)).

**Makefile**. Present, but it only covers documentation tooling — `docs-sync`, `docs-check`,
`docs-test` — and drives Python scripts under `tools/docs/` via `PYTHON ?= python3`. It is not
part of the compile path ([Makefile](https://raw.githubusercontent.com/floci-io/floci/main/Makefile)).
Note the `python3` default: on Windows the executable is usually `python`, so these targets would
need `make PYTHON=python ...`, and `make` is not installed on this machine anyway. Only relevant
if you add or change a service handler, which CONTRIBUTING says requires `make docs-sync` and
`make docs-check` ([CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md)).

**CI — the honest statement of how it builds.** `.github/workflows/ci.yml` runs on
`ubuntu-latest` only, across a four-way test shard matrix, with:

```yaml
- uses: actions/setup-java@...
  with:
    java-version: '25'
    distribution: 'temurin'
```

The steps are `./mvnw test-compile -B` then a sharded `./mvnw surefire:test -B`
([ci.yml](https://raw.githubusercontent.com/floci-io/floci/main/.github/workflows/ci.yml)).
**There is no Windows runner in CI.** Sixteen workflow files exist and none of them is a Windows
build ([workflows listing](https://api.github.com/repos/floci-io/floci/contents/.github/workflows)).
Whatever works on Windows works because nothing has broken it yet, not because it is tested.

No `.tool-versions`, no `.nvmrc`, no `mise.toml`, no root `Dockerfile` — all returned 404. There
is no Node, Python or Go component in the build path of this repository.

## Running it on this machine

### What the project actually tells you to do

CONTRIBUTING, verbatim:

> ### Prerequisites
>
> - Java 25+
> - Maven 3.9+
> - Docker (for integration tests that spin up Lambda/RDS/ElastiCache)

> ### Build & Run
>
> ```bash
> git clone https://github.com/floci-io/floci.git
> cd floci
> ./mvnw quarkus:dev     # hot reload on port 4566
> ```

> ### Run Tests
>
> ```bash
> ./mvnw test                                          # all tests
> ./mvnw test -Dtest=SsmIntegrationTest                # single class
> ```

([CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md))

Note the discrepancy worth flagging: CONTRIBUTING says "Java 25+", the enforcer rule says
`[25,26)`. The POM is the one that runs. Trust the POM.

The docs site adds the build-from-source variants:

> **Production JAR:** `mvn clean package -DskipTests` followed by
> `java -jar target/quarkus-app/quarkus-run.jar`

([floci.io installation docs](https://floci.io/floci/getting-started/installation/)), which also
states Docker requirements of "Docker 20.10+" and "docker compose v2+ (plugin syntax, not
standalone docker-compose)".

If you only want to *use* floci rather than build it, the README's first-listed path is the CLI:

> ```bash
> floci start
> ```

([README.md](https://raw.githubusercontent.com/floci-io/floci/main/README.md)).

### Already on this machine

| Requirement | Status |
|---|---|
| git 2.53 | Have it |
| Maven 3.9+ | Covered by `mvnw.cmd`, which fetches Maven 3.9.16 |
| Python 3.13.1 | Have it — only needed for the `tools/docs` Makefile targets |
| Java | **Have 24.0.2 — wrong version, see below** |

`node`, `dotnet`, `gh` are all irrelevant to this build. `go`, `rust`, `pnpm`, `bun`, `kubectl`,
`helm`, `terraform`, `psql`, `gcc` are all irrelevant too.

### Must install

1. **Eclipse Temurin JDK 25.** Official source: [adoptium.net/temurin/releases](https://adoptium.net/temurin/releases/)
   (Adoptium is the project that publishes Temurin; the CI workflow specifies `distribution: 'temurin'`
   at `java-version: '25'`, so this matches CI exactly). Install it alongside JDK 24 and point
   `JAVA_HOME` at it for this project — do not uninstall 24 if something else needs it. The
   enforcer's own message tells you the fix: *"Set JAVA_HOME to JDK 25."* SDKMAN is what
   CONTRIBUTING suggests, but SDKMAN is a POSIX tool and would mean working inside WSL2; on native
   Windows the Adoptium MSI is the straightforward route.
2. **Docker Desktop for Windows.** Official source: [docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/).
   Required for the `docker compose up` path, and for the 45 test files that touch `DockerClient`.
   Docker Desktop uses the WSL2 backend, which this machine already has (WSL2 v2.4.11).

### Docker/WSL2 or native Windows?

Both, in different roles.

- **The Maven build and `quarkus:dev` should run natively on Windows.** `mvnw.cmd` exists,
  nothing in the compile path needs a POSIX shell, and `.gitattributes` handles line endings
  correctly (see below). This is a reasonable expectation rather than a verified fact —
  **unverified**, since CI never builds on Windows.
- **Docker is not optional for the full experience.** The emulator delegates Lambda, RDS and
  ElastiCache to real containers. Docker Desktop on the WSL2 backend satisfies this without you
  needing to work inside WSL2 yourself.
- **WSL2 is not required as a development environment**, but it is the safer fallback if the
  native Windows build misbehaves — it puts you on the same Linux surface CI uses.

The sibling CLI confirms Windows is a supported *usage* platform, with a PowerShell installer and
a Scoop bucket, and it explicitly handles the Docker named pipe on Windows:

> 3. **OS default** — `/var/run/docker.sock` on Linux/macOS, or the Docker named pipe on Windows

([floci-cli README](https://raw.githubusercontent.com/floci-io/floci-cli/main/README.md)).
That is first-party evidence that Windows users are expected, even though CI does not build there.

### Windows-specific risks, checked individually

- **CRLF** — handled properly. `.gitattributes` sets `* text eol=lf` with explicit CRLF overrides
  for `*.cmd`, `*.bat` and `mvnw.cmd`
  ([.gitattributes](https://raw.githubusercontent.com/floci-io/floci/main/.gitattributes)). No action needed.
- **Symlinks** — none. No tree entry has mode `120000`
  ([recursive tree API](https://api.github.com/repos/floci-io/floci/git/trees/main?recursive=1)). No action needed.
- **Case-sensitivity collisions** — none. Lowercasing all 4,430 blob paths produces no duplicates
  (same source). No action needed.
- **Path length** — a real but manageable risk. The longest path in the repository is 134
  characters (`src/test/java/io/github/hectorvent/floci/services/applicationautoscaling/ApplicationAutoScalingDeleteScalingPolicyIntegrationTest.java`),
  and Maven's `target/` output adds more on top (same source). Windows' legacy 260-character
  limit is close enough to matter. Mitigation: clone to a short root such as `C:\src\floci`, and
  run `git config --global core.longpaths true`.
- **POSIX-only scripts** — the Makefile is POSIX and defaults `PYTHON ?= python3`, and `make` is
  not installed here. Only bites if you touch service handlers or docs generation.
- **Spaces in paths** — avoid cloning under a path containing spaces. Not a documented problem,
  but it is a recurring source of breakage in JVM tooling and costs nothing to avoid.
- **Memory** — Surefire is configured with `-Xmx6g` for the test run. Whether this machine has
  enough RAM to run the full suite comfortably is **unverified**; RAM was not in the inventory.
  If it is 16 GB or less, run targeted tests (`-Dtest=SomeTest`) rather than `./mvnw test`.

### Concrete sequence

```powershell
# 1. Install Temurin JDK 25 from adoptium.net, then in a fresh shell:
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-25..."   # exact path from the installer
& "$env:JAVA_HOME\bin\java.exe" -version                          # must report 25

# 2. Install Docker Desktop, start it, confirm:
docker version

# 3. Clone somewhere short, with long paths enabled
git config --global core.longpaths true
git clone https://github.com/floci-io/floci.git C:\src\floci
cd C:\src\floci

# 4. Build only, no tests — the fastest honest check that the toolchain is right
.\mvnw.cmd clean package -DskipTests

# 5. Run in dev mode, then hit http://localhost:4566
.\mvnw.cmd quarkus:dev

# 6. One targeted test rather than the whole suite
.\mvnw.cmd test -Dtest=SsmIntegrationTest
```

Step 4 is the decision point. If the enforcer rejects your JDK, it will say so by name.

## Difficulty for a beginner

Two different questions, two different answers.

**Getting it to build and run: Moderate.** Not Easy, because it needs a specific JDK version that
is not the one installed, plus Docker Desktop, plus an awareness that `JAVA_HOME` is what the
build reads. Not Hard, because once those two installs are done the commands are a three-line
sequence with a Windows batch wrapper provided, no symlinks, no CRLF trap, and no native
toolchain. Expect an evening, most of it waiting on downloads.

**Contributing to it: Hard, and not advisable as a first open-source contribution.**

The reasons are specific, not vibes:

- It is a **4,430-file Java codebase** ([tree API](https://api.github.com/repos/floci-io/floci/git/trees/main?recursive=1))
  whose entire purpose is reproducing the exact observable behaviour of AWS APIs. The hard part
  is never the Java — it is knowing what real AWS does in the edge case, which is domain knowledge
  a beginner does not have yet.
- CONTRIBUTING's instructions for adding a service run to **twelve numbered steps**, and adding a
  CloudFormation resource type runs to nine more, including registering the type in a TSV fixture
  and wiring it into a test fixture in three separate places, with explicit warnings that missing
  any one makes tests silently pass while the code is never exercised
  ([CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md)).
- The testing policy is strict: *"Pull requests that introduce new behavior must include tests
  that validate that behavior"*, and PR titles are CI-validated against Conventional Commits
  (same source).
- The pace is unforgiving. PR numbers are past #3800 in a repository seven months old. A
  newcomer's PR is competing with maintainers who are refactoring the same files daily.

**The realistic first contribution.** It exists, but it is thin:

- `good first issue` and `help wanted` both exist as labels
  ([labels API](https://api.github.com/repos/floci-io/floci/labels)), which is a good sign.
- But there is exactly **one** open `good first issue` — **#2605, "ec2: ten dispatched operations
  undocumented on main (predates feature/ec2)"** — and it already carries the `has-pr` label, so
  someone is on it ([issue #2605](https://api.github.com/repos/floci-io/floci/issues/2605)).
- There are **zero** open `help wanted` issues
  ([issues API, help wanted](https://api.github.com/repos/floci-io/floci/issues?state=open&labels=help+wanted)).

So the honest reading: the maintainers have the labels but are not stocking them, because they
and a core group of regulars are moving too fast to leave easy work lying around. The two
realistic entry points, neither of them an existing issue:

1. **Documentation**, which CONTRIBUTING explicitly invites and which is exempt from the new-test
   requirement: *"Pull requests that do not change observable behavior, such as documentation
   updates … may not require new tests."* The `documentation` label exists.
2. **A `docs`-typed PR against a service you have actually used in AWS** — pick one service page
   under `docs/services/`, compare it against real AWS behaviour you know, and correct it. This
   builds the domain knowledge that the code contributions require, in the right order.

There is also a Slack, linked from both CONTRIBUTING and the docs site, described as *"the fastest
way to reach maintainers"* — worth using before writing code, as they suggest.

What would make this an Easy project instead: already knowing Java and Quarkus, and already
knowing AWS API semantics well enough to say what the correct response body is. Absent the second
of those, the build is the easy part and the contribution is the wall.

## If floci is not the right target

Included because the difficulty verdict above is "Hard for a beginner to contribute to", not
because the repository is fake — it is emphatically real. If the goal is a first open-source
contribution rather than this specific project:

- **[LocalStack](https://github.com/localstack/localstack)** — the incumbent floci is replacing.
  Python rather than Java, which is closer to the Python on this machine, and a far longer history
  of onboarding outside contributors. Same domain, so anything learned transfers.
- **[Testcontainers for Java](https://github.com/testcontainers/testcontainers-java)** — the
  library floci integrates with. Smaller surface, clearer module boundaries, and a long-running
  culture of accepting small module-scoped PRs.
- **[testcontainers-floci](https://github.com/floci-io/testcontainers-floci)** — the same org's
  Testcontainers module, 57 stars against the main repo's 24,420
  ([org repos API](https://api.github.com/orgs/floci-io/repos)). Dramatically smaller, same
  maintainers, same Slack, and a contribution there is a genuine contribution to the floci
  ecosystem. If the attachment is to floci specifically, this is the sane entry point. The same
  argument applies to `testcontainers-floci-python` and `testcontainers-floci-node`, which match
  the languages already installed here.

This section is a judgement call, not a verified claim. The relative newcomer-friendliness of
LocalStack and Testcontainers is **unverified** — I did not audit their issue trackers.

## Sources

Every URL below was fetched directly during this research.

| Source | What it supported |
|---|---|
| [api.github.com/repos/floci-io/floci](https://api.github.com/repos/floci-io/floci) | Stars (24,420), forks (2,633), open issues (113), MIT licence, Java, created 2026-02-18, last push 2026-09-17, not archived, topics |
| [api.github.com/orgs/floci-io](https://api.github.com/orgs/floci-io) | Org created 2026-03-27, 18 public repos, "Any Cloud. Locally." |
| [api.github.com/orgs/floci-io/repos](https://api.github.com/orgs/floci-io/repos) | The emulator family and star counts; `testcontainers-floci` at 57 stars |
| [api.github.com/repos/floci-io/floci/commits](https://api.github.com/repos/floci-io/floci/commits?per_page=5) | Five most recent commits, five distinct authors, same-day activity |
| [api.github.com/repos/floci-io/floci/pulls](https://api.github.com/repos/floci-io/floci/pulls?state=closed) | Merged PRs from multiple distinct contributors; PR numbers past #3800 |
| [api.github.com/repos/floci-io/floci/releases](https://api.github.com/repos/floci-io/floci/releases) | Release cadence, 2.1.0 on 2026-09-15 |
| [api.github.com/repos/floci-io/floci/labels](https://api.github.com/repos/floci-io/floci/labels) | `good first issue`, `help wanted`, `documentation` labels exist |
| [issues?labels=good first issue](https://api.github.com/repos/floci-io/floci/issues?state=open&labels=good+first+issue) | Exactly one open good-first-issue |
| [issues?labels=help wanted](https://api.github.com/repos/floci-io/floci/issues?state=open&labels=help+wanted) | Zero open help-wanted issues |
| [issues/2605](https://api.github.com/repos/floci-io/floci/issues/2605) | Issue #2605 title, labels including `has-pr`, unassigned |
| [issues?state=open](https://api.github.com/repos/floci-io/floci/issues?state=open) | Current open issues are correctness bugs in emulated AWS behaviour |
| [git/trees/main?recursive=1](https://api.github.com/repos/floci-io/floci/git/trees/main?recursive=1) | 4,430 files; longest path 134 chars; no symlinks; no case collisions |
| [git/trees/main](https://api.github.com/repos/floci-io/floci/git/trees/main) | Top-level layout, presence of `mvnw`, `mvnw.cmd`, `Makefile`, `AGENTS.md` |
| [contents/.github/workflows](https://api.github.com/repos/floci-io/floci/contents/.github/workflows) | Sixteen workflows, none Windows |
| [search/code DockerClient in src/test](https://api.github.com/search/code?q=repo:floci-io/floci+DockerClient+path:src/test) | 45 test files reference `DockerClient` |
| [pom.xml](https://raw.githubusercontent.com/floci-io/floci/main/pom.xml) | `maven.compiler.release` 25; enforcer `[25,26)`; Quarkus 3.39.2; docker-java 3.7.1; Surefire `-Xmx6g`; native profile |
| [CONTRIBUTING.md](https://raw.githubusercontent.com/floci-io/floci/main/CONTRIBUTING.md) | Prerequisites, build/run/test commands, twelve-step service checklist, testing policy, Conventional Commits, Slack |
| [README.md](https://raw.githubusercontent.com/floci-io/floci/main/README.md) | What floci is, quick start via CLI and Compose, LocalStack positioning, emulator family |
| [docker-compose.yml](https://raw.githubusercontent.com/floci-io/floci/main/docker-compose.yml) | Docker socket mount, port 4566, build context |
| [docker/Dockerfile](https://raw.githubusercontent.com/floci-io/floci/main/docker/Dockerfile) | `eclipse-temurin:25-jdk-noble` build stage, `25-jre-noble` runtime |
| [Makefile](https://raw.githubusercontent.com/floci-io/floci/main/Makefile) | Docs-only targets, `PYTHON ?= python3` |
| [.gitattributes](https://raw.githubusercontent.com/floci-io/floci/main/.gitattributes) | `* text eol=lf` with CRLF overrides for `.cmd`/`.bat`/`mvnw.cmd` |
| [.mvn/wrapper/maven-wrapper.properties](https://raw.githubusercontent.com/floci-io/floci/main/.mvn/wrapper/maven-wrapper.properties) | Maven 3.9.16 pinned, `only-script` distribution |
| [.github/workflows/ci.yml](https://raw.githubusercontent.com/floci-io/floci/main/.github/workflows/ci.yml) | `ubuntu-latest` only, Temurin 25, four-shard `mvnw test-compile` + `surefire:test` |
| [docs/contributing.md](https://raw.githubusercontent.com/floci-io/floci/main/docs/contributing.md) | Development setup as the docs site states it |
| [floci.io/floci/](https://floci.io/floci/) | Docs landing page; no system requirements stated there |
| [floci.io/floci/getting-started/installation/](https://floci.io/floci/getting-started/installation/) | "Java 25+", "Maven 3.9+", "Docker 20.10+", "docker compose v2+"; JAR and native build commands |
| [floci-cli README](https://raw.githubusercontent.com/floci-io/floci-cli/main/README.md) | Windows PowerShell installer, Scoop bucket, Docker named-pipe handling on Windows |
| [adoptium.net/temurin/releases](https://adoptium.net/temurin/releases/) | Official JDK 25 source (referenced as install target, not fetched for claims) |
| [docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/) | Official Docker Desktop for Windows source (referenced as install target, not fetched for claims) |

Marked **unverified** above and not to be treated as established: that the native Windows Maven
build succeeds (CI never tests it); whether this machine has enough RAM for the full test suite;
the relative newcomer-friendliness of the alternative projects.
