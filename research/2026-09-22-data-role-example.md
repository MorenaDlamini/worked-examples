# A data role, as an example — Senior Data Engineer, Databricks migration

A fourth posting, kept separately because it is an example of what data roles pay for rather
than a target. Seen 2026-09-22 on a South African job board; agency and rate omitted. Quoted
text is the posting's own.

| Field | Value |
|---|---|
| Title | Senior Data Engineer, Databricks Migration |
| Location | Cape Town, hybrid, onsite three days a week |
| Employment | Six-month contract, starting immediately |
| Client | "A large SA retailer ... moving off an on-prem data estate onto Databricks" |

## The posting, verbatim

> A large SA retailer is moving off an on-prem data estate onto Databricks, and they need
> someone who's done this before — not learned it on the job halfway through.
>
> You'll be building the modern platform: Medallion Architecture, Data Vault modelling,
> governed pipelines. This isn't a maintenance seat. It's the migration itself.

**What you'll actually do**

- Lead the lift from on-prem to a governed Databricks platform
- Build with PySpark, Python and SQL across the Medallion layers
- Model in Data Vault and translate messy business rules into clean data
- Sit with Finance and C-suite stakeholders and own the outcome, not just the code

**What you need**

- Real Databricks migration experience (done it end-to-end)
- Strong PySpark, Python, SQL
- Finance / Economics data exposure — big plus
- The ability to hold a room with senior stakeholders and manage delivery

## Named technologies

Databricks, PySpark, Python, SQL. Named patterns: Medallion Architecture, Data Vault.

## Wording strength

"Done this before — not learned it on the job halfway through" and "done it end-to-end" are
the gate, and they are the same gate as Role 1's "proven track record of delivering production
Python/Spark pipelines independently", said less politely. The technology list is short; the
verbs are "lead", "model", "translate messy business rules", "own the outcome". Half of the
requirements are about stakeholders, not code.

## What it adds to the requirements list

Two things the three target postings imply and this one states outright:

- **Owning the outcome with stakeholders, not just the code.** Finance and executives, in the
  room. That is why `scenarios/` exists and why the replatform's exit test needs a reviewer who
  wants the parity report to be wrong.
- **Having done a migration end to end.** The replatform in `platform` is the only way to
  produce one outside employment. It is a laptop-sized migration, and `NON-CLAIMS.md` says so.

It also names the two modelling patterns — Medallion and Data Vault — that Phase 4 teaches,
and confirms that "Finance data exposure" is a plus in this market, which the municipal finance
product happens to provide.

## What it does not change

The target remains the three roles in `2026-09-22-sa-target-roles.md`. This posting is a
six-month contract for someone who has already done the migration; it is where the data
pillar leads, not where it starts.
