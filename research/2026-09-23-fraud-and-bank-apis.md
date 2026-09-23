# South African bank APIs, open banking, and fraud detection as an engineering discipline

Research for a decision: is a fraud/data-heavy system worth one of four or five portfolio slots?
Read on 2026-09-23. Primary sources cited inline. Inference is marked **Unverified**.
Sources that could not be reached are listed rather than guessed.

Companion to `research/2026-09-22-sa-target-roles.md` and
`research/2026-09-23-data-stack-and-certifications.md`, and written to the same rules.

---

## The verdict

**Option (a). Fraud becomes the security phase's detection-as-code deep-dive, scored over the
transaction stream the ingestion service already carries. No fifth system, no new repo.**

The short version, in three sentences:

Fraud detection is a real engineering discipline and most of it is data engineering — a
point-in-time-correct feature layer, a replayable stream, a versioned rule layer, and an
evaluation regime built on review budgets and money rather than accuracy — which is exactly
the work `platform` already does. But fraud has no oracle: labels arrive 120 days late, are
missing entirely for everything the system blocked, and are produced by a budgeted human
process that only ever looks where the model already pointed, so "is this detector better"
is irreducibly a judgement call. And the South African market for it is thin and closed —
of 22 listings read in full on 2026-09-23, **two** were roles where fraud detection itself is
the engineering object, the advertised stack is SAS AML rather than anything in this
curriculum, and every SAS AML posting demands five years of SAS AML, which is unobtainable
outside a bank that already runs it.

So: build the engineering, not the model. Upgrade the optional item in Phase 7 to a real,
graded deep-dive with a hard exit test, and score it over the ingestion service's own stream.
Do not spend a whole system on it.

### Judged against the file's own four tests

| Test | Fraud as a fifth system | Fraud as the Phase 7 deep-dive |
|---|---|---|
| **1. It is the work the roles do** | Partly. The SA roles that exist are SAS AML platform work and Azure ETL with "fraud" as a domain noun. The genuine fraud-ML roles are at Absa, Old Mutual, FNB and Moniepoint, behind Workday, and they want years in the domain | Yes, in the honest sense: streaming feature correctness, replay, rules-as-code, evaluation under a budget. That is the data role's day job wearing a fraud hat |
| **2. Someone else could use it** | A fraud detector trained on PaySim is not usable by anyone. A rules engine might be | Yes, if the artefact is the rule engine and the point-in-time feature layer, not the model |
| **3. It forces the hard parts** | Yes — this is the strongest argument for it | Yes, and the same hard parts: ordering, replay determinism, late data, idempotency, training/serving parity |
| **4. It has an oracle** | **No.** This is the disqualifier, and it is not fixable | **Yes, if you move the oracle.** Feature computation, point-in-time correctness, replay determinism and rule purity all have pass/fail answers. Model quality does not, and the write-up says so |

Test 4 is what decides it. A fifth system whose headline claim is "I built a fraud detector"
rests on an oracle that does not exist, on a synthetic dataset that lacks the entity-reuse
density that makes the features work, and a senior reviewer in this domain will ask about
label delay and censoring inside two minutes. The same work, framed as "I built a
replay-deterministic scoring pipeline with a point-in-time-correct feature layer and a
backtestable rule engine, evaluated at precision@k against a stated review budget, and here
is what I could not make correct", survives that question — because acknowledging the gap is
the senior signal.

**Happening / Consolidating / Noisy**, applied to the option set:

| | Label | Why |
|---|---|---|
| Fraud detection as engineering practice | **Consolidating** | The architecture is settled across Monzo, Stripe and the ULB/Worldline handbook: layered controls, pure-function rules, feature store, budgeted human review |
| SA fraud-engineering job market | **Noisy** | Board counts are fuzzy-matched garbage; the readable surface is SAS AML contracting; the interesting employers are unscrapeable |
| SA bank developer APIs | **Consolidating, one winner** | Investec is real and open; everyone else is partner-gated |
| SA open banking regulation | See Q2 |

---

## Q1 — South African bank developer APIs

Read 2026-09-23, from the portals and their own documentation.

### Summary table

| Bank | Public portal | What it exposes | Sandbox without being a customer | Auth | Could a Johannesburg dev build against it this week? |
|---|---|---|---|---|---|
| **Investec** | [developer.investec.com](https://developer.investec.com/) | Accounts, balances, transactions, pending transactions, profiles, beneficiaries, inter-account transfers, payments, documents; separate Card API with programmable card code | **Yes — credentials published in the docs. I called it.** | OAuth2 client credentials + `x-api-key`; 3-legged OAuth for approved third parties | **Yes** |
| **Nedbank** | [apim.nedbank.co.za](https://apim.nedbank.co.za/) | Customers, Accounts, Payments, Rewards, Credit Card Account Details, Business Transactions, Account Verification, CashOut, Short Term Insurance, Open Data (branch/bank lists) | Sandbox base URLs are published, but access needs a portal account and "a thorough due-diligence process" | OAuth 2.0 | **No — not this week.** Weeks, and a company |
| **Absa** | [api.absa.africa](https://www.api.absa.africa/home/) (marketing) and [developer.absa.africa](https://developer.absa.africa/) (SPA) | Not publicly listed. Marketing names "Live APIs", "My Playpen", "Concept APIs" | Claimed ("your own, safe and free environment") but the catalogue is behind auth | Not stated publicly | **No** — catalogue unreadable without login |
| **Standard Bank** | [developer.standardbank.co.za](https://developer.standardbank.co.za/) | A large, oddly internal catalogue: Diners Club virtual cards, airport lounge access, electronic receipts, document management, GPI cross-border tracking, a technology register, **and a "Falcon CCS WhatsApp Response API"** | No. Registration is switched off | OAuth 2.0, mTLS named on the landing page | **No** |
| **FNB / RMB** | None. [fnb.co.za/integration-channel](https://www.fnb.co.za/integration-channel/index.html) is a corporate product page | DebiCheck, EFT collections and payments, 3PIM, proof of payment, transaction history | No | Not published | **No** — a phone number, a client service manager, and an Online Banking profile |
| **Capitec** | None | Capitec Pay, a payment-initiation service reached through PSPs (Ozow, Paystack, EBANX, Klasha) | No | n/a | **No** |

Plainly: **one.** Investec. Everything else in South African retail banking is
partner-gated, contract-first, and invisible without a login.

### Investec Programmable Banking — precisely what it gives and requires

Two separable things travel under the same brand, and conflating them is the mistake.

**1. The APIs.** The [API reference](https://developer.investec.com/api-reference) lists six
products: Private Bank API, Business & Commercial Banking API, Intermediaries API,
Intermediaries Forex API, Card API, and Authorisation API (OAuth).

The Private Bank API's endpoints, verbatim from
[SA PB Account Information](https://developer.investec.com/api-reference/SA%20PB%20Account%20Information):

```
GET  /za/pb/v1/accounts
GET  /za/pb/v1/accounts/{accountId}/balance
GET  /za/pb/v1/accounts/{accountId}/transactions
GET  /za/pb/v1/accounts/{accountId}/pending-transactions
GET  /za/pb/v1/profiles
GET  /za/pb/v1/profiles/{profileId}/accounts
GET  /za/pb/v1/profiles/{profileId}/accounts/{accountId}/authorisationsetupdetails
GET  /za/pb/v1/profiles/{profileId}/accounts/{accountId}/beneficiaries
POST /za/pb/v1/accounts/{accountId}/transfermultiple
POST /za/pb/v1/accounts/{accountId}/paymultiple
GET  /za/pb/v1/accounts/beneficiaries
GET  /za/pb/v1/accounts/beneficiarycategories
GET  /za/pb/v1/accounts/{accountId}/documents
GET  /za/pb/v1/accounts/{accountId}/document/{documentType}/{documentDate}
```

Auth, from
[SA Open API – Authorization](https://developer.investec.com/api-reference/SA%20Open%20API%20-%20Authorization):
`POST /identity/v2/oauth2/token`, `grant_type=client_credentials`, Basic-authorization header
carrying base64 `client_id:client_secret`, plus an `x-api-key` header. Production base URL is
`https://openapi.investec.com`. Tokens expire in 1799 seconds.

**2. The programmable card.** The Card API
([SA Card Code](https://developer.investec.com/api-reference/SA%20Card%20Code)) is the part
with no equivalent anywhere else:

```
GET/POST /za/v1/cards
GET/POST /za/v1/cards/{cardKey}
GET/POST /za/v1/cards/{cardKey}/code
GET      /za/v1/cards/{cardKey}/publishedcode
POST     /za/v1/cards/{cardKey}/publish
POST     /za/v1/cards/{cardKey}/code/execute
GET      /za/v1/cards/{cardKey}/code/executions
GET/POST /za/v1/cards/{cardKey}/environmentvariables
POST     /za/v1/cards/{cardKey}/toggle-programmable-feature
GET      /za/v1/cards/countries | /currencies | /merchants
```

Investec's own description:
> "Programmable Banking, through the Integrated Development Environment on Investec Online,
> allows you to deploy JavaScript code rule which executes before and after every card
> transaction."
> — [investec.com, Programmable Banking](https://www.investec.com/en_za/banking/tech-professionals/programmable-banking.html)

The API-reference capability list is: "Get the code that is published to your cards; Save and
publish new code to your cards; Run card simulations to test saved code; Check logs of
simulated and real transactions." Environment variables exist for secrets — "The public and
private keys used to get sensitive card information; Account details for third-party
services."

That `code/execute` + `code/executions` pair is genuinely a detection-engineering primitive: a
rule, a simulator, and an execution log. It is the closest thing in South Africa to a
production card-authorisation hook a private person can hold.

**What it requires.** The card code needs a real Investec card, and therefore a real Investec
Private Bank or Business Bank account. Enrolment is through Investec Online: "Login to
Investec Online to enable API access on your account", and "Only the main account holder will
have access to credentials and have the ability to create new API keys"
([Individuals & Private Business](https://developer.investec.com/individuals)). Commercial
clients with "annual turnover of > R30m" are routed elsewhere.

### The sandbox works, and I used it

This is the finding that changes what is possible without becoming a customer. The
Individuals page says, verbatim:

> "Don't have an Investec account? You can test out our Sandbox APIs."

And the sandbox credentials are **published in the public API reference**, not issued on
registration. Base URL `https://openapisandbox.investec.com`, with `client_id`
`yAxzQRFX97vOcyQAwluEU6H6ePxMA5eY`, a client secret, and an `x-api-key`, all printed on the
[SA PB Account Information](https://developer.investec.com/api-reference/SA%20PB%20Account%20Information)
page.

I called it on 2026-09-23. No registration, no form, no terms accepted.

- `POST /identity/v2/oauth2/token` → HTTP 200, `{"access_token":"…","token_type":"Bearer","expires_in":1799,"scope":"accounts balances beneficiarypayments transactions transfers"}`
- `GET /za/pb/v1/accounts` → HTTP 200, **8 accounts** for a mock profile ("Mr Smith", Private Bank Account, PrimeSaver, MoneyFund Tracker, Cash Management, …)
- `GET /za/pb/v1/accounts/{id}/transactions` → HTTP 200, **263 transactions** on the main account, rolling window **2026-06-24 → 2026-09-23**
- `GET /za/v1/cards` → **HTTP 404.** The Card API is not in the sandbox.

The transaction shape is realistic and the volume is a toy:

```json
{"accountId":"3353431574710163189587446","type":"DEBIT","transactionType":"CardPurchases",
 "status":"POSTED","description":"MUNSWAMI COMMERCE KURUMAN ZA","cardNumber":"402261xxxxxx0011",
 "postedOrder":10615,"postingDate":"2026-06-28","valueDate":"2026-07-31",
 "actionDate":"2026-09-23","transactionDate":"2026-06-27","amount":60,
 "runningBalance":7600.71,"uuid":"87446202606280010615"}
```

`transactionType` takes eight values — `ATMWithdrawals`, `CardPurchases`, `DebitOrders`,
`Deposits`, `FasterPay`, `FeesAndInterest`, `OnlineBankingPayments`, `VASTransactions`. Card
numbers are masked to two distinct PANs. Merchant strings carry a South African town and
country code.

What that means for a fraud project, stated plainly: **the Investec sandbox is a good shape
and a useless dataset.** 263 rows, one cardholder, three months, two cards, no labels. It is
enough to build a client and a schema against. It is not enough to detect anything. Its real
value is as a *realistic target schema* your synthetic generator emits into — which is a
better use of it than pretending it is data.

### Terms — can you build and publish a personal project?

Investec's [Terms of Use](https://developer.investec.com/terms-of-use) are public and
readable without login. The relevant clauses, verbatim:

- **1.1** — "We grant You a revocable, limited, non-exclusive, royalty-free,
  non-sub-licensable, non-transferable, licence to access and use the Investec APIs to
  develop, test, connect with Your Solution subject to these Terms."
- **6.1** — "We will not provide You with real Client Data, including real Client API
  Credentials and Keys, unless our clients have provided us with express consent to do so.
  **You may make use of a sandbox environment which can be accessed on the Investec Developer
  Portal bearing mock client data for testing purposes.**"
- **6.2** — "You undertake to acquire the required Client Consent before You receive and
  process any Client data."
- **2.4** — "You undertake to ensure that all Contributions You make will bear the original
  MIT license." (A "Contribution" is defined as code you share *with the Developer Community*
  — it is not a licence condition on everything you write against the API.)
- **10.1.6** — you may not "Licence, sell, rent, lease, transfer, assign, distribute, display,
  disclose, or otherwise commercially exploit, or otherwise make the Investec Developer Suite
  available to any third party".
- **11.4** — "our total aggregate liability … shall be limited to R 6 000.00 (six thousand
  rand)."
- **20.2** — you grant Investec rights to use "Your Likeness" royalty-free. Worth knowing
  before you speak at one of their meetups.

Nothing in the terms prohibits a personal, non-commercial project, and nothing requires
approval to use the sandbox. 10.1.6 restricts redistributing *Investec's* developer suite, not
publishing your own code. A public GitHub repo with an MIT licence, built against the sandbox,
is squarely inside what clause 1.1 grants.

One asymmetry worth noting: the Investec route is the only SA bank where the *community* is a
first-class object in the terms. Clause 2 grants a Developer Community licence, clause 4 says
Investec "may, at our sole discretion, reward You for Your Contribution", and the definitions
name "monthly meetups, community chats via Slack, access to community resources on GitHub,
social events and participation in hackathons". If the goal includes being seen, that matters
more than the endpoint list.

### Nedbank — real APIs, closed door

The [API Marketplace](https://apim.nedbank.co.za/) publishes a proper product catalogue and,
unusually, its sandbox base URLs: `https://api.nedbank.co.za/apimarket/sandbox` for B2C and
`https://b2b-api.nedbank.co.za/apimarket/b2b-sb` for B2B
([Base URLs](https://apim.nedbank.co.za/static/docs/bases)). Auth is OAuth 2.0 across every
product.

The [API marketplace terms](https://personal.nedbank.co.za/legal/terms-and-conditions/api-marketplace.html)
are the most developer-friendly text of any SA bank, and they define the sandbox broadly:

- **1.9** — "'Sandbox' means the API Marketplace test environment website and related
  materials, information and resources currently located at API Marketplace."
- **1.13** — "'You' or 'your' refers to any visitor to this Sandbox, including any other
  person, website, business or agent."
- **3.1** — "Limited right to access and use the Sandbox, API content, API services, and
  Sandbox data to develop, test, connect with, and support your application's access."
- **19** — "You may publicise your use of the API in line with these terms, but you may not
  state or imply that you have a partnership or preferred relationship with us."
- **14.1** — "We exclusively retain all intellectual property rights in all APIs…"

No clause bars a personal project. The blocker is operational, not contractual: Nedbank's own
onboarding description says "signing on as an API partner involves a thorough due-diligence
process" scrutinising "your company, your business credentials and your technical
capabilities"
([Nedbank blog](https://apim.nedbank.africa/blog/signing-up-for-api-marketplace.html)). You
need a company and weeks. Not this week.

### Standard Bank — a catalogue you cannot join

[developer.standardbank.co.za](https://developer.standardbank.co.za/) is an IBM API Connect
portal on Drupal. The landing page advertises "Payments, accounts, cards, forex, lending and
open-banking APIs — BIAN-aligned, documented and ready to integrate" with "REST, GraphQL,
SOAP, JSON, OpenAPI 3.0, BIAN, OAuth 2.0, mTLS, Webhooks".

The actual `/product` catalogue does not match the pitch. What is listed is largely internal
and partner-specific: Document Management API, Credit Life Inquiry API, EAS Customer Profile
& Alerts, Diners Club Virtual Card APIs, Airport Lounge Access Verification API, Electronic
Receipts API, GPI Cross-Border Payment Tracking API ("Internal Standard Bank API"), TC Keys
API, Stakeholders API, Universal Technology Register API, Merchant Information API, Money
Markets Trading Services API, Multi-Product Quote API, IBL Broker Connection API ("partners
only"). There is no public accounts or transactions API.

`GET /user/register` returns HTTP 307 to the login page, and the rendered page reads
**"Self-service onboarding is disabled for this site."** (observed through the r.jina.ai
reader proxy; the 307 corroborates it). No sandbox statement anywhere I could reach. The FAQ
says only "When you add an application you are provided with an API Key and Secret for the
application."

One item on that catalogue is worth carrying to Q4: the **"Falcon CCS WhatsApp Response API"**,
described as an "API designed to receive and process customer WhatsApp responses to Falcon
CCS fraud alerts". That is FICO Falcon, the card-fraud platform, running at Standard Bank —
the only direct, primary-source confirmation of a named fraud vendor in a South African bank
that this research found. It did not come from a job advert. It came from a developer portal.

### Absa — marketing public, catalogue private

Two properties. [developer.absa.africa](https://developer.absa.africa/) is an Angular SPA that
serves a bare `<app-root>` and nothing else to a fetcher.
[www.api.absa.africa/home/](https://www.api.absa.africa/home/) is the marketing front and does
describe a sandbox — "Live APIs", "My Playpen" ("Test, troubleshoot and refine your code in a
simulated environment"), "Concept APIs" ("Explore our future-state APIs that we are thinking
of delivering"), and a "Playpen Portal … your own, safe and free environment". Onboarding is
described as: set up an account, create an application, request API keys.

Every catalogue path I tried on that host (`/catalog`, `/apis`, `/products`, `/explore`,
`/documentation`, `/live-apis`) returns **HTTP 401**. I could not see a single named Absa API,
a sandbox base URL, or the terms. Recorded as unread, not as absent.

### FNB and RMB — a phone number

FNB's [Integration Channel](https://www.fnb.co.za/integration-channel/index.html) lists
DebiCheck, EFT Collections & Payments, 3rd Party Investment Manager, Proof of Payments,
Transaction History, and two push-message feeds, over "Application Programming Interface" or
host-to-host. Eligibility is stated as having "registered for and logged in using your Online
Banking profile", and access is by telephone — "Contact us on 087 736 2247, select option 3
and then option 1 for Integration Channel" — or through a Client Service Manager. No developer
portal, no sandbox, no published specs.

RMB's integration-channel page (`rmb.co.za/page/integration-channel`) returns HTTP 200 with
the title **"Page Not Found - Integration Channel"**. A soft 404. Recorded as unreachable.

### Capitec — not a developer product

There is no Capitec developer portal; `developer.capitecbank.co.za` does not resolve. Capitec
Pay is a **payment-initiation service** sold to merchants and payment service providers, and
Capitec's own published document is a fee schedule, not documentation: "payment initiation API
service — Provision of a secure API to send a request to pay instruction to your customer's
Capitec retail bank account and process the payment, once authorised by them and disburse
funds to your nominated bank account", priced at "0.7% of the transaction value or R0.81 per
transaction, whichever is higher" against a Capitec Business Bank Account, with tiered volume
discounting from R50m monthly turnover
([Capitec Pay fees PDF](https://www.capitecbank.co.za/globalassets/pages/documents-library/transact/18638-capitec-pay-fees-f.pdf)).
Developers reach it only through a PSP — Ozow, Paystack, EBANX or Klasha, each of whom
documents it in their own API. `capitecbank.co.za` serves a bot-protection interstitial to
fetchers, so the consumer product pages could not be read.

### What a Johannesburg developer can actually build against this week

**Investec's sandbox, today, with no account and no registration.** That is the entire list.

Everything else needs a company, a due-diligence questionnaire, and weeks: Nedbank's stated
process, Investec's own third-party route ("6–8 weeks if you are quick in submitting your
responses", per [Third Parties](https://developer.investec.com/third-parties)), Absa's
account-gated Playpen, and Standard Bank's disabled registration.

---

## Q2 — Open banking in South Africa, and what POPIA does to a personal project

### Is there a PSD2 or UK-style push?

**No mandated open-banking API standard exists in South Africa, and none has ever existed.**
What exists as at 2026-09-23 is a screen-scraping directive, a draft payment-initiation
licence, and a decade of policy papers saying it ought to be mandatory one day.

Two tracks, and they are moving at different speeds:

| Track | Status | Label |
|---|---|---|
| **Payment initiation** (the PSD2 "PIS" analogue) | Interim registration in force; full authorisation in a third draft, final promised Q3 2026, not yet published | **Happening** |
| **Account information / data sharing** (the PSD2 "AIS" analogue) | Policy only. No instrument, no standard, no date | **Noisy** |

**The one binding instrument.** *Directive 2 of 2024*, Government Gazette No. 51556,
15 November 2024, effective ~13 February 2025
([PDF](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight/Directive%202%20of%202024.pdf)).
It **registers and supervises screen scraping** rather than prohibiting it:

> **5.1.2** "A juristic person must apply for registration with the SARB to issue payment
> instructions or initiate payment on behalf of a payer."
> **5.3.3.1** "A person issuing electronic funds transfer credit payment instructions on
> behalf of the payer must obtain and receive informed consent prior to using the payer's
> online banking credentials to access the transactional accounts of the payer…"
> **5.3.3.2(d)** the consent request must "state that by entering their login credentials, the
> payer is sharing the credentials with that person and is not logging on to their online
> banking website or application".
> **7.3** "Contravention of this directive is an offence in terms of section 12(8) of the NPS
> Act."

That is the opposite of PSD2's trajectory, and a reversal of the SARB's own 2020 framing, which
called screen scraping one of the "'bad' practices … that should be prohibited"
([Consultation paper on open-banking activities in the NPS, November 2020](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight/Consultation%20Paper%20on%20open%20banking.pdf), §9.1).
That 2020 paper proposed "a common API standard to allow for open and controlled access to
shared data" (§9.2) and working groups to develop technical standards (§9.6). **The SARB never
published a response paper to it.** There is no SARB position paper on open banking in the
position-paper series at all.

**The draft that is moving.** *Draft Authorisation Framework — Directive X of 2026*, May 2026,
135 pp, published as Annexure D to Prudential Communication 10 of 2026
([PDF](https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/communication/2026/prudential-communication-10-of-2026/Annexure%20D-%20Draft%20Authorisation%20Framework.pdf)).
Comments closed 15 June 2026; the final version was promised for Q3 2026 and had not appeared
by 2026-09-23. It creates a licensed **payment initiation service provider**, and the access
right is genuinely PSD2-shaped:

> **23.4.3** "A payment initiation service provider **need not enter into a contractual
> relationship** with a payment account service provider to provide payment initiation
> activity."
> **23.4.2(c)** a payment account service provider must "not unfairly prioritise the processing
> of payment instructions".
> **23.7.1** "A payment account service provider must apply **strong client authentication**…"
> **23.8.2(d)** the interface infrastructure must "comply with **technical standards applicable
> to this payment activity as prescribed by the Reserve Bank**."

The May 2026 draft adds a **centralised interface infrastructure** — a single utility that
PISPs and banks both connect to. **Unverified inference:** that utility is PayInc / the National
Payments Utility.

**The gap that matters.** None of the three drafts contains an account-information-service or
data-access activity category. A grep across all three for "account information service",
"account aggregat" and "data access provider" returns nothing. **Payment initiation is being
regulated. Account data sharing is not.**

**The policy consensus, and its absence of an instrument.** The IFWG's
*Articulating the policy rationale and policy imperatives for Open Finance in South Africa*
(November 2021,
[PDF](https://www.ifwg.co.za/IFWG%20Documents/IFWG_Articulating-the-policy-rationale-and-policy-imperatives-for-Open-Finance-in-South-Africa_November-2021.pdf))
is direct about why:

> "South Africa's financial system is characterised by sectors where a few players have
> significant market share… The banking sector for example is dominated by five banks which
> collectively hold about 90% of total banking-sector assets as at March 2021."
> "**It is for this reason that the IFWG's policy view is that a mandatory regime … is the most
> appropriate for South Africa.**"

and on ownership: "the IFWG has taken the view that personal information stored by financial
institutions belongs to the customer."

The FSCA's *Open Finance — Policy Recommendations* (March 2024,
[PDF](https://www.fsca.co.za/Regulatory%20Frameworks/FinTechDocuments/2024%20Open%20Finance_FSCA%20Position%20Paper.pdf))
says the same and sequences it:

> "**The FSCA continues to support mandating Open Finance in future**…"
> Recommendation 1: "**Supporting voluntary adoption is proposed as a first step**… a mandatory
> approach is proposed over the longer term, with phased implementation."
> Recommendation 5: "The FSCA proposes **the development of agreed API standards**… It is
> envisaged that these standards be embedded in law, although **voluntary adoption may be a
> first step**."

The most recent dated government statement is National Treasury's Budget Review 2026,
Annexure E ([PDF](https://www.treasury.gov.za/documents/National%20Budget/2026/review/Annexure%20E.pdf)),
under "Implementation of an open finance framework": "In 2025, the IFWG finalised a
comprehensive cost-benefit analysis… Over the next financial year, the IFWG will continue with
work to develop an appropriate regulatory framework for open finance." That cost-benefit
analysis could not be found on any of the four relevant government sites and may not be public.

**And the body that would own a standard no longer exists.** PASA's own site states its
functions transitioned to the SARB and PayInc under a directive of 2 June 2026, and that "From
**2 September 2026**, transitioned functions and related enquiries are administered by the
relevant organisation" ([pasa.org.za](https://pasa.org.za/)). PayInc is the rebranded
BankservAfrica, 50% SARB-held, being turned into the National Payments Utility under the
SARB's Payments Ecosystem Modernisation programme. **There is currently no industry standards
body for open banking in South Africa.**

**BASA has published nothing on open banking** that could be located — searched directly and
through a reader proxy. Recorded as a genuine absence, not a fetch failure.

**Terminology trap worth writing down.** A South African "TPPP" is not a PSD2 TPP. Here a
Third-Party Payment Provider is an entity that collects payments on behalf of a beneficiary
under bank sponsorship; the SARB's public register (~545 entities, May 2026) is a list of
collection agents, not account-information providers.

**What this means for the curriculum, plainly.** Nobody is going to hand a South African
developer a standardised bank API in the near term. The Investec route is not an early sample
of an emerging standard — it is one bank's product, and it is likely to remain the only one.

### POPIA — what constrains a personal project touching real transaction data

Source: *Protection of Personal Information Act 4 of 2013*, consolidated text at
[justice.gov.za](https://www.justice.gov.za/legislation/acts/2013-004.pdf), section 6 wording
cross-checked against the gazetted original,
[GG 37067 of 26 November 2013](https://www.gov.za/sites/default/files/gcis_document/201409/3706726-11act4of2013protectionofpersonalinforcorrect.pdf).
Sections 2–38 and 55–109 commenced 1 July 2020; s58(2) on 1 February 2022.

**Bank transaction data is personal information.** Section 1 includes, verbatim, "(b)
information relating to the education or the medical, **financial**, criminal or employment
history of the person" and "(c) any identifying number, symbol, e-mail address, physical
address, telephone number, location information, online identifier or other particular
assignment to the person".

**It is not *special* personal information — but a fraud label is.** Section 26's list is
closed and excludes financial data. It does include "(b) the **criminal behaviour** of a data
subject to the extent that such information relates to— (i) the alleged commission by a data
subject of any offence". **A fraud label attached to an identifiable person is special personal
information and s26 prohibits processing it unless s27 applies.** That is the single most
important POPIA fact for a fraud project on real data, and it is easy to miss.

**The "purely personal or household" exemption is eight words long.** Section 6(1), verbatim:

> (1) This Act does not apply to the processing of personal information—
> **(a) in the course of a purely personal or household activity;**
> **(b) that has been de-identified to the extent that it cannot be re-identified again;**
> (c) by or on behalf of a public body— (i) which involves national security… or (ii) the
> purpose of which is the prevention, detection, including assistance in the identification of
> the proceeds of unlawful activities and the combating of money laundering activities,
> investigation or proof of offences… to the extent that adequate safeguards have been
> established in legislation…

No elaboration, no definition of "purely", and no South African case law found interpreting it
in a data context. The GDPR analogue is narrow — publishing to the internet defeats it.
**Unverified for South Africa, strongly indicated:** a learn-in-public project is not "purely
personal or household", because publication is exactly what takes it outside.

**s6(1)(b) is the exemption that actually works, and the bar is high.** Section 1 defines
de-identify as deleting information that "(a) identifies the data subject; (b) can be used or
manipulated by a reasonably foreseeable method to identify the data subject; or (c) **can be
linked by a reasonably foreseeable method to other information that identifies the data
subject**". Hashing an account number does not clear (c). There is no enumerated safe harbour.

**The research route.** s15(3)(e) permits further processing where "the information is used for
historical, statistical or research purposes and the responsible party ensures that the further
processing is carried out solely for such purposes **and will not be published in an
identifiable form**". That, plus s14(2), is the provision a portfolio project should be built
on if it touches real data at all.

**The sleeper clause for entity resolution.** Section 57(1) requires **prior authorisation from
the Regulator** before a responsible party plans to "(a) process any unique identifiers of data
subjects— (i) for a purpose other than the one for which the identifier was specifically
intended at collection; and (ii) **with the aim of linking the information together with
information processed by other responsible parties**", and also before "(b) process information
on criminal behaviour … on behalf of third parties". Section 58(2), in force since 1 February
2022, adds a standstill: processing may not proceed "until the Regulator has completed its
investigation". Entity resolution across parties on real data is a notification-and-wait
activity, not a weekend project.

**Cloud outside South Africa.** Section 72(1) permits transfer only where "(a) the third party
… is subject to a law, binding corporate rules or binding agreement which provide an adequate
level of protection" that is "substantially similar" and binds onward transfers — or on
consent, or contractual necessity. **POPIA has no adequacy-decision mechanism and no list of
approved countries.** A South African cloud region sidesteps the question; anything else needs
the s72(1)(a) contractual analysis. Consent is fragile because s11(2)(b) makes it withdrawable
at any time. And s57(1)(d) requires prior authorisation before transferring *special* personal
information — which, again, includes fraud labels — to a country without adequate protection.

**Security and breach.** s19 requires "appropriate, reasonable technical and organisational
measures", with a four-step programme in s19(2): identify risks, establish safeguards,
"regularly verify that the safeguards are effectively implemented", and keep them updated.
s21(1) requires a **written contract** with any operator. s22 requires notification of the
Regulator and the data subject "as soon as reasonably possible after the discovery of the
compromise" — **no 72-hour clock and no de minimis threshold.**

**Exposure.** Administrative fines up to **R10 million** (s109(2)(c)), CPI-adjustable.
Imprisonment up to **10 years** for the account-number offences in ss105–106 (s107(a)) — s105(5)
defines "account number" as a unique identifier assigned "by a financial or other institution
which enables the data subject … to access his, her or its own funds or to access credit
facilities". And civil damages are **strict liability**: s99(1) allows an action "**whether or
not there is intent or negligence** on the part of the responsible party", with aggravated
damages available.

**The safe design, stated once.** Synthetic or already-public data; or real data de-identified
to the s1 standard *before it leaves the source*; hosted in a South African region; never
published in identifiable form. Nothing in POPIA gives a hobby project a pass, and the
combination of a fraud label (special information), an account number (10-year offence) and
cross-party linking (prior authorisation plus standstill) is the worst possible corner of the
Act to stand in.

**Which settles a design question for free: this project uses synthetic data, and that is a
legal conclusion, not a convenience.**

---

## Q3 — Fraud detection as an engineering discipline

What the work actually is. Practitioner sources only: a bank's own engineering blog, a
payments company's own guide, the ULB/Worldline handbook, Apache project documentation, and
Google's production-ML rubric.

### The shape of a system

The ULB/Worldline handbook — Le Borgne and Bontempi, *Reproducible Machine Learning for Credit
Card Fraud Detection*, written with Worldline's fraud team — gives the canonical layering
([Chapter 2, FDS](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_2_Background/FDS.html)):

> "A credit card Fraud Detection System (FDS) is typically composed of a set of five layers of
> control"

**Terminal → Transaction-Blocking Rules → Scoring Rules → Data-Driven Model → Investigators.**

> "The first two layers (*Terminal* and *Transaction Blocking Rules*) are executed in real-time
> (i.e. within milliseconds and before authorization)."

Only those two are pre-authorisation. Transaction-blocking rules are "*if-then (-else)*
statements meant to block transaction requests that are perceived as frauds" using only
information available at payment time, "without analyzing historical records or cardholder
profiles". Scoring rules are "expert-driven models that are expressed as *if-then (-else)*
statements". The model layer scores *already-authorised* transactions. Investigators are the
fifth layer and they are part of the system, not outside it.

Monzo's public architecture is the best bank-side description
([Building a reactive fraud prevention platform](https://monzo.com/blog/build-a-reactive-fraud-prevention-platform)).
Three control types in a network — Detectors ("typically machine learning models, responsible
for predicting if fraud is occurring"), Action Controls, and an Action Selection Control
("responsible for aggregating all the requested actions into a final decision"). Controls can
be "updated, replaced or removed, and the remainder of the network will continue operating the
same".

### Rules versus models — they are not alternatives

Monzo again, and this is the single most useful engineering idea in the field. Controls are
written in **Starlark**, a Python dialect, as *pure functions* — "their output is dictated
entirely by their input, and they don't rely on or mutate any external state". The payoff:

> "Having our controls as pure functions lets us backtest over historic data to assess their
> performance before shipping."

**Purity is what buys you backtesting.** That is a testable architectural constraint, cheap to
demonstrate, and it is the thing to steal.

Stripe frames rules as models rather than their opposite: custom rules are "simple models" that
"can be represented as decision trees" and "should be evaluated … in the same way as models"
([Radar guide](https://stripe.com/radar/guide)). Rule backtesting is a shipped product feature
— before a rule is enabled Stripe shows "historical statistics on the number of matching
transactions that were actually disputed, refunded, or accepted", and afterwards "you can see
the impact on false positive and dispute rates by rule".

Sift's Workflows show the three-outcome routing a two-class model cannot express: criteria
"that when met, Sift will auto-block, auto-accept, or send the user ID to a Sift Review Queue
for manual review"
([Decisions API](https://developers.sift.com/docs/curl/decisions-api/overview)).

Monzo states the combination directly: "Typical detection architectures rely on a combination
of predictive models, static rules, and human expert investigations to resolve complex cases."

Monzo also adds a blast-radius limiter worth noting: "each action can declare rate limits
which, once surpassed, will prevent more actions being applied and alert an engineer."

### Streaming versus batch

Terminal checks "have to be performed in real-time (response has to be provided in a few
milliseconds)" (handbook). Stripe states the inline constraint and its cost in one breath:

> "We need to compute the value of every feature for every new payment in real time because we
> want to be able to block all transactions that our classifier believes are likely to be
> fraudulent."

and

> maintaining "an up-to-date state on the two most frequently used IP addresses for every card
> ever seen at Stripe, and fetching and updating those counts needs to be fast because those
> operations happen as part of the Stripe API flow."

That second quote is the whole streaming-feature problem: **a mutable per-entity aggregate,
read and updated on the request path.** It is the same problem as an idempotent merge into
Delta, with a latency budget bolted on.

Asynchronous scoring is real and separate. Stripe's Smart Refunds runs "in the hours after your
transaction completes" and publishes its calibration
([Radar reviews](https://docs.stripe.com/radar/reviews)): at the *highest* confidence tier, a
72% chance of an early fraud warning or dispute; at "very low", 15%. Note what is being
predicted — a warning or a dispute, not fraud.

**Apache Flink is where the determinism lives.** Flink ships test harnesses specifically for
stateful, timer-driven operators
([Testing](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/testing/)):
`KeyedOneInputStreamOperatorTestHarness`, `ProcessFunctionTestHarnesses`,
`MiniClusterWithClientResource`. You "push (timestamped) elements into the operator", "trigger
event time timers by advancing the event time of the operator with a watermark", and advance
processing time with `setProcessingTime()`. The mini-cluster runs whole pipelines "against a
local, embedded mini cluster" with parallelism > 1 and checkpoint-based failure testing.

**Time becomes an input you control in tests.** That is the oracle this project needs, and it
is the same lesson the curriculum's append-only-log deep-dive already teaches.

### Feature stores

The problem, stated canonically by Chronon, the open-source descendant of Airbnb's Zipline
([chronon.ai](https://chronon.ai/)):

> "Eliminate data leakage with guaranteed point-in-time correctness."
> "Write features **once**. The same declarative definitions automatically power both batch
> training datasets and real-time serving endpoints—eliminating training-serving skew."
> "One unified API works across batch (Spark), streaming (Flink or Spark streaming), and
> serving contexts."

Google's *ML Test Score* (Breck et al., IEEE Big Data 2017,
[PDF](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf))
states training/serving skew and — more importantly — how to *test* it. Monitor 3:

> "The codepaths that actually generate input features may differ at training and inference
> time. Ideally the different codepaths should generate the same values, but in practice a
> common problem is that they do not. This is sometimes called 'training/serving skew' …"

> "it is crucial to log a sample of actual serving traffic. For systems that use serving input
> as future training data, adding identifiers to each example at serving time will allow direct
> comparison; **the feature values should be perfectly identical at training and serving for
> the same example.**"

That is a parity check. Same shape as "gold matches the shipped warehouse to the cent":
recompute from a second path, assert equality, report the diff. Anyone who has built a `parity`
tool already owns this skill; the fraud context renames it.

Data 7, same paper: "Feature creation code may appear simple enough to not need unit tests, but
this code is crucial for correct behavior … Bugs in features may be almost impossible to detect
once they have entered the data generation process, especially if they are represented in both
training and test data."

Monzo's Feature Loader declares three freshness tiers — **Just in Time** ("computed *on the
fly*"), **Near Real Time** ("pre-computed then cached"), **Batch** — and a failure policy worth
copying: "To avoid an error in a single node causing an entire request to fail, the service
will return all the features it could successfully load, alongside the errors of any that
failed." Partial feature vectors are normal, and training data must represent them.

Actual fraud features, from Stripe: "the country in which the card was issued"; "the number of
distinct countries where the card was used across the Stripe network in the past day"; "the
difference between the time on the user device and the current Coordinated Universal Time";
"embeddings for a variety of categorical features, such as issuing bank, merchant and user
country, day of the week".

And the warning that matters most for a synthetic-data project:

> "Ninety percent of the cards used on the Stripe network have been seen more than once."

Cross-entity velocity features only work because entities repeat. A generated dataset with one
transaction per synthetic card makes most of the interesting feature space inert.

### Entity resolution and graph

Ravelin's Connect is the most concrete public description
([deep dive](https://www.ravelin.com/blog/deeper-look-ravelin-connect-graph-network-fraud-link-analysis)).
The graph is built from shared high-cardinality attributes — emails, phone numbers, device IDs,
payment methods, IPs, shipping addresses. "When two customers share an attribute, they will be
connected in the network." The rationale: "Often fraudsters will have used the same device or
email in another account previously, and so when they open a new account it will be linked to
their past activity."

The engineering trick is turning a graph back into a row. Ravelin's graph features: "the number
of hops to a chargeback or reviewed fraudster", "the number of each type of node", "the count
of connections each node type has". A point-wise model cannot express "hops to a known
fraudster" — that needs the global relation. That is the honest technical argument for graph,
and the one place where fraud is structurally different from ordinary tabular ML.

Stripe's review UI renders a one-hop graph at triage time: "related payments" showing "other
payments made to your business that use the same email address, IP address, or card number as
the payment you're currently reviewing".

### Label delay, imbalance, and censoring

**Label delay.** Stripe's own dispute documentation gives the number
([How disputes work](https://docs.stripe.com/disputes/how-disputes-work)):

> "Card networks typically allow cardholders to initiate disputes within 120 days of the
> original payment, but their rules allow more time in some situations."

> "The full dispute lifecycle, from initiation to the final decision, can take 2-3 months to
> complete."

So a label may not settle for six months. You cannot ask "did last week's change help" last
week.

South Africa makes the same point in published statistics. SABRIC's *Annual Crime Statistics
2025* computes on transaction date, not report date: "All calculations are based on the date
that the fraudulent transaction occurred"
([PDF](https://www.sabric.co.za/wp-content/uploads/2026/08/SABRIC-Annual-Crime-Statistics-Report-2025.pdf), p.11).
Every recent month's fraud figure is a lower bound that keeps ratcheting up.

**The censoring problem, which is the deep one.** Stripe, verbatim:

> "Payments that have scores above the threshold, however, are blocked, and so we can't know
> what their outcomes would have been. Computing the full production precision-recall or ROC
> curve is thus more involved than computing the validation curves because it involves
> counterfactual analysis"

> "counterfactual analysis—we need to obtain statistically sound estimates of what would have
> happened even to the payments we blocked."

Stripe says it "has developed methods to do this" and publishes none of them. Your training set
is a sample selected by the previous version of your own model; every deployment corrupts the
data for the next one.

**And the labels you do get come from a budgeted, biased human process.** Carcillo, Le Borgne,
Caelen and Bontempi, *Streaming Active Learning Strategies for Real-Life Credit Card Fraud
Detection* ([arXiv 1804.07481](https://arxiv.org/abs/1804.07481)):

> "The labeling is the outcome of an active learning process, as every day human investigators
> contact only a small number of cardholders (associated to the riskiest transactions) and
> obtain the class (fraud or genuine) of the related transactions."

> "we highlight the existence of an exploitation/exploration trade-off for active learning in
> the context of fraud detection, which has so far been overlooked in the literature."

**Scale, South Africa, primary.** SABRIC 2025: gross card-fraud losses on SA-issued credit and
debit cards rose from **R1 479 082 576 (2024) to R1 745 352 519 (2025), +18.0%**; domestic
losses **R598m → R857m, +43.3%**; Gauteng is 51.7% of credit-card and 42.1% of debit-card
losses; 59.2% of credit-card losses on SA-issued cards occurred abroad. Digital banking crime:
**110 074 incidents / R2 406 728 972 in 2025**, average loss per incident **R21 865**, banking
app about 89% of cases. SABRIC states its own caveats — gross rather than net of recoveries,
SA-issued cards only, fleet and foreign-issued cards excluded. Note what is missing: SABRIC
publishes losses, not fraud as a fraction of volume, so **these do not give a base rate.**

### Alert triage and the review budget

The review budget is a literal integer. From the handbook
([Top-k metrics](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_4_PerformanceMetrics/TopKBased.html)):

> "The process of contacting cardholders is time-consuming, and the number of fraud
> investigators is limited."
> "Precisions are computed daily … The k parameter quantifies the maximum number of alerts that
> can be checked by investigators in a day."

Their worked example uses **k = 100 alerts per day** and a decision-tree baseline reaching
**CP@100 = 0.1** — ten of the hundred most suspicious cards per day are real. That is the
operating point. About 90% of what you hand a human is wrong at a *working* system.

And the evaluation unit is the investigation, not the row:

> "Multiple transactions in |A_d| from the same card should be counted as a single alert since
> investigators check all the recent transactions when contacting cardholders."

Deduplicating alerts to entities before scoring is a correctness requirement, and a
deterministic, unit-testable assertion about your own evaluation code.

Stripe's [review docs](https://docs.stripe.com/radar/reviews) are the only complete public
description of a triage workflow, and several details matter:

- "Payments placed into review are typically already successfully processed, unless you capture
  authorized payments later." **The review happens after the money moved.**
- Three terminal actions — Approve / Refund / **Refund and report fraud** — and only the third
  creates a label. It also "adds the associated card fingerprint and customer email to your
  block lists".
- Label contamination, documented: "If a customer disputes a payment that's currently in your
  review queue, the review is automatically closed." Some queue items are resolved by the
  world, not the analyst.
- The queue is an event stream: `review.opened`, `review.closed` with a `reason`. That is what
  makes analyst labelling a pipeline rather than a spreadsheet.
- Assignment and locking are first-class: "Anyone managing the review queue can assign
  themselves to reviews to avoid duplicating effort", with a timeline showing "a complete
  history of assignment changes and other actions".
- Stripe warns about the operational cost: "If you don't have a built-in delay between orders
  and fulfillment with your business, adding a review process might slow down orders and create
  a bottleneck for good customers."

Sift makes the obligation explicit: if you decide in your own system, "make sure to send all of
the decisions from your system to Sift as Decision events." **Your decisions are training data
and must be logged as deliberately as your features.**

### Evaluation — why accuracy is not a metric

At a fraud base rate, predicting "not fraud" for everything is right upwards of 99.8% of the
time. Neither Stripe's guide nor the handbook uses accuracy anywhere.

Stripe's definitions and worked example: "Precision … the fraction of transactions we block
that are actually fraudulent" (4/6 = 0.66); "recall is the fraction of all fraud that is caught
by our policy" (4/5 = 0.8); "the false positive rate is the fraction of all legitimate payments
that are incorrectly blocked" (2/5 = 0.4).

**Money-weighted, with an actual break-even formula.** Stripe:

> "If your average sale is $26 with a margin of 8%, your profit per sale is $26.00 × 8.00% =
> $2.08."
> with a $15 chargeback fee, "your break-even precision is 1 / (1 + 18.71) = 5.07%."

Read that carefully. **At those unit economics, a rule that is wrong 94.9% of the time is still
profitable.** Precision without the cost ratio is meaningless, and the same model is good for
one merchant and bad for another. This is the single fact that most re-calibrates an intuition
built on conventional ML.

**Drift, with a rate.** Stripe:

> "even retraining a model from last month on more recent data (using the same feature
> definitions and architecture) and releasing it allows us to increase our recall by as much as
> half a percentage point each month."

Half a point of recall per month, recovered by retraining alone with no modelling change.
Release cadence is a model-quality lever. Google's Model 4 formalises this — "if the pipeline
fails to adequately train and deploy up-to-date models, we say the model is *stale*" — and
recommends "a small A/B experiment with older models. Testing a range of ages can produce an
age-quality curve."

Google's infrastructure tests map one-to-one onto fraud practice: **Infra 4** (an automated
system "must either bless the model or veto it"), **Infra 6** (canary — "Offline testing,
however extensive, cannot by itself guarantee that the model will perform well in live
production"), **Infra 7** ("Because rolling back is an emergency procedure, operators should
practice doing it normally, when not in emergency conditions").

And the honest caveat, Monitor 7: "Validation data will always be older than real serving input
data … However, it is not always possible to know the correct labels even shortly after serving
time, making quality measurement difficult."

### AML is a different job wearing an adjacent name

Card fraud has a victim who eventually complains. Money laundering does not. The IBM/ETH
NeurIPS 2023 paper states the consequence
([arXiv 2306.16424](https://arxiv.org/abs/2306.16424)):

> "using synthetic data in these comparisons can be even better than using real data: the
> ground truth labels are complete, whilst many laundering transactions in real data are never
> detected."

and, on scale: "The UN estimates 2-5% of global GDP or $0.8 - $2.0 trillion dollars are
laundered globally each year."

That is why AML is rules-driven and regulator-facing rather than model-driven: the target has no
label, so the thing you can actually optimise is investigator productivity. Vendors sell exactly
that — a second model that ranks the alerts the first model produced.

South African institutional context, verified incidentally in the SABRIC report: the **Financial
Intelligence Centre** is a formal SABRIC partner alongside SAPS, the Hawks, the NPA and the FSCA
(p.5), and there is an industry **Banking Industry Anti-Scam Centre** which SABRIC itself says
"is not yet operating at the scale, coverage or level of automation required to materially
reduce overall industry losses" (p.10).

### Detection-as-code is a security practice, and it is only half the same thing

The curriculum's Phase 7 optional item borrows the name from security detection engineering.
What that actually is, from the primary repositories:

- **Sigma** ([SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)) — "Sigma is a generic and open
  signature format that allows you to describe relevant log events in a straightforward
  manner", so analysts can "describe their once developed detection methods and make them
  shareable with others". "Sigma is for log files what Snort is for network traffic and YARA is
  for files." Detection Rule License 1.1.
- **Elastic detection-rules**
  ([elastic/detection-rules](https://github.com/elastic/detection-rules)) — "Detection Rules
  contains more than just static rule files. This repository also contains code for building
  Detections-as-code pipelines, unit testing in Python and integrating with the Detection Engine
  in Kibana." Rules are TOML, generated via a `create-rule` command, unit-tested in Python, CI
  on GitHub Actions. Elastic License v2.
- **Panther** ([docs.panther.com/detections](https://docs.panther.com/detections)) — "leverage
  detections-as-code by creating detections in Python, or use Panther's Simple Detections
  features", with a CLI workflow and a CI/CD guide.

The shared engineering with financial fraud is real: rules in version control, unit-tested
against synthetic or replayed events, deployed through CI, tuned against false positives, routed
into a triage queue. Monzo's "controls as pure functions → backtest over historic data" is
structurally the same discipline.

**The divergence is the part that matters, and it belongs in the write-up.** Security detection
has a *deterministic* oracle: execute the technique, assert the rule fired. Financial fraud's
ground truth is delayed, censored and adversarial. Same tooling discipline, different
epistemics. **Unverified** as a general claim, but it follows directly from the sources above.

Design consequence for the phase: detection-as-code over an audit log teaches the
rule-engineering half honestly and teaches nothing at all about the label half — which is the
half that makes financial fraud hard. If the deep-dive is worth upgrading, it is worth upgrading
precisely by adding the half the security framing omits.

### The oracle problem, stated plainly

The question the verdict turns on.

**What is irreducibly weak:**

1. Labels arrive up to 120 days late and take 2–3 months to settle (Stripe).
2. Negative labels mostly mean "nobody complained", not "this was legitimate". In AML, "many
   laundering transactions in real data are never detected" (IBM/ETH).
3. Labels are censored by your own policy. You never learn the outcome of anything you blocked
   (Stripe, verbatim, above). Every deployment corrupts the next training set.
4. Labels are produced by a budgeted human process biased toward the region your model already
   scores high (Carcillo et al.).
5. Labels are noisy — "refund and report fraud" is a merchant judgement; friendly fraud is
   labelled fraud and is not; reviews auto-close when a dispute lands.
6. The target distribution is adversarial and moves: ~0.5pp recall lost per month without
   retraining (Stripe).
7. Offline metrics may not predict online impact at all (Google Model 2; the recommended test is
   an A/B experiment, not a computation).

**Compare the replatform.** Its oracle is total, immediate and free: recompute, compare to the
cent, any difference is a defect. Fraud has no such comparison for the model. **"Is this model
better" is irreducibly a judgement call informed by a controlled online experiment.**

**What an engineer can still make deterministic** — the entire case for doing it at all. Each of
these has a pass/fail answer as crisp as a parity check:

| Property | The test |
|---|---|
| Feature computation correctness | Unit tests on feature code (Google Data 7) |
| Training/serving parity | Log serving traffic with example IDs, recompute offline, assert bit-equality (Google Monitor 3) |
| Point-in-time correctness | Assert no feature used at time *t* depends on an event after *t*. Adversarial test: inject a future event, assert the backfilled feature does not move |
| Leakage, demonstrated | Build a deliberately leaky join, show the inflated AUC, fix it, show the honest one |
| Replay determinism | Same event log in → same state and same decisions out, including across a simulated failure (Flink test harnesses, `MiniClusterWithClientResource`) |
| Rule correctness | Pure functions have a total oracle: given inputs, assert outputs |
| Rule backtest reproducibility | A backtest over a fixed historical window is reproducible even when its business interpretation is not |
| Alert deduplication | Per-card, not per-transaction (handbook). A deterministic assertion about your own evaluation code |
| Latency SLO | Measurable, enforceable, regression-testable |
| Reproducible training | Google Infra 1: "training twice on the same data should produce two identical models" — makes refactors diffable |
| Schema and data invariants | Google Data 1 / Monitor 2 |
| Rollback | Google Infra 7, practised deliberately |

**The strongest single artefact** this research can point at: a point-in-time-correct feature
pipeline with an automated training/serving skew test and a replay-deterministic streaming
scorer, plus a pure-function rule layer with backtests, evaluated at CP@k against a stated
review budget and a stated cost ratio — with the counterfactual gap named rather than papered
over. The naming is the senior signal.
---

## Q4 — What South African employers actually ask for

**Snapshot taken 2026-09-23. It will go stale. It is not statistically rigorous.** Method and
reachability follow `research/2026-09-23-data-stack-and-certifications.md`: IT-Online, PNet,
Datafin, ExecutivePlacements, CareerJunction, Hire Resolve, e-Merge and freehire mirrors were
the readable surface; `r.jina.ai` was needed as a reader proxy for PNet detail pages, which
time out on a direct fetch. **LinkedIn returned titles and never bodies, so zero LinkedIn
listings are in any count below.**

### The two numbers, kept apart

| Measure | Number |
|---|---|
| Listing **titles** surfaced across all boards, including duplicates and fuzzy-match noise | ~250 |
| Titles plausibly combining fraud / financial crime / AML / transaction monitoring **with a technical role** | ~40 |
| Listings whose **body was read in full** | **22** |
| Of those 22, roles where **fraud detection itself is the engineering object** | **2** |

### What the 22 actually are

| Class | n | Examples |
|---|---|---|
| Genuine fraud/financial-crime ML modelling | **1** | wePlace, *Quantitative Analyst*, Cape Town |
| Genuine detection engineering on a vendor AML platform (rules/scenarios) | **1** | Tumaini, *SAS AML Developer \| Financial Crime Technology*, Johannesburg |
| Generalist DS/ML where fraud is one domain among several, or a nice-to-have | 2 | Sabenza *Senior Data Scientist*; Network IT *Machine Learning Engineer* |
| **Infrastructure / QA wearing an AML label** — DevOps, DevSecOps, test automation around a SAS AML platform | **4** | Tumaini ×3, Reverside *DevOps Engineer* |
| **Data engineering wearing a fraud label** — pipelines, SQL, ETL, reporting; "fraud" names the business domain | **5** | Samaha *Data Engineer*; Capital H and Optim-G *Senior Data Engineer*; FIC *Senior Data Technologist* and *Data Technologist* |
| Analyst / compliance / leadership, non-engineering | 7 | Capitec *AML Operations Manager*; QE *AML Analyst*; *Head of Fraud* ×2; *Financial Crime Analyst* |
| Security engineering, fraud-adjacent | 1 | FIC *Cyber Security Engineer* |
| Mislabelled, no fraud content at all | 1 | a *Data Scientist* ad surfaced by a fraud search |

**Yes, overwhelmingly: they are data engineering roles wearing a fraud label.** Nine of 22
(41%) are pipeline, ETL, DevOps or QA work where "fraud" or "AML" is a domain noun attached to
otherwise generic infrastructure. Two of 22 (9%) are roles where the detection is the
engineering.

The purest specimen is Samaha Consulting's *Data Engineer*, Johannesburg, which says it serves
"Transaction Monitoring, Fraud, and Financial Crime platforms" and then asks for nothing but
Azure: "Strong experience as a Data Engineer / ETL Developer / Azure Data Engineer" — Azure Data
Factory, Databricks, Microsoft Fabric, Synapse — "Excellent SQL/T-SQL skills, including stored
procedures, functions and query optimisation", SSIS, and "Strong knowledge of Data Vault 2.0 and
Kimball dimensional modelling". No fraud logic, no scenarios, no model, no vendor platform.

The sharpest specimen of the disease is Isilumko Staffing's **"Fraud Detection Consultant"**,
Sandton, whose own body heading reads "Call Centre Agent – Criminology / Forensic Science
Graduate" and which asks for "Minimum 18 months' call centre experience within the banking
industry". That title survives into every aggregator and inflates every "fraud detection jobs
in South Africa" count anyone will ever quote.

### Technology frequency, out of 22 bodies read in full

| Technology | Count |
|---|---|
| SQL (incl. T-SQL, PROC SQL) | 11 |
| Python | 9 |
| **SAS** (Base / Macro / SAS SQL / certifications) | **8** |
| Azure (DevOps, ADF, Synapse, Fabric, Analysis Services) | 6 |
| CI/CD — Jenkins, GitLab CI, GitHub Actions | 5 |
| Docker / Kubernetes (incl. SAS Viya, Helm) | 4 |
| Linux/Unix + shell | 4 |
| Terraform / Ansible / ARM | 3 |
| ML libraries (XGBoost, CatBoost, MLflow, "ML frameworks") | 3 |
| Airflow | 2 |
| Databricks | 2 |
| Snowflake | 2 |
| Power BI | 2 (both FIC) |
| Grafana / Prometheus / Splunk | 2 |
| Java | 1 |
| AWS | 1 (certification, "advantageous") |
| **Kafka / streaming** | **0 explicit** (closest: one "event-driven architectures") |
| **Spark / PySpark** | **0 explicit** (implied by Databricks) |
| **.NET / C#** | **0** |
| **Graph databases (Neo4j, TigerGraph)** | **0** |
| **Rules engines (Drools)** | **0** |

### Named fraud and AML vendor platforms

| Vendor | Count in bodies read | Note |
|---|---|---|
| **SAS AML** | **5** | Dominant. "SAS AML scenario and case management", "SAS AML data models", SAS Viya, SAS Environment Manager, SAS Data Integration |
| SIRON | 1 | "advantageous" |
| ORMS | 1 | "advantageous" |
| Actimize/NICE, Oracle FCCM, Featurespace, Feedzai, FICO Falcon, Verafin, ThetaRay, NetReveal, Quantexa, Fiserv, ACI, Temenos | **0** | None appeared in any listing body |

**The advertised South African financial-crime stack is SAS AML + SQL + Linux + CI/CD, with
Azure data engineering attached.** The Western fraud-vendor ecosystem is essentially invisible
in the open job market this week.

One correction to that, from a source that is not a job board: Standard Bank's own developer
portal lists a **"Falcon CCS WhatsApp Response API"** for "customer WhatsApp responses to Falcon
CCS fraud alerts" (Q1 above). FICO Falcon is running at Standard Bank. **The absence of a vendor
name from job adverts is not evidence the vendor is absent.**

### Pillar lean, out of 22

| Pillar | n |
|---|---|
| Data engineering | 6 |
| Full-stack / software and platform engineering | 4 (all DevOps, DevSecOps or SDET) |
| Applied AI/ML | 3 (only one actually about fraud) |
| Security | 1 |
| None of the four — analyst, compliance, management, irrelevant | 8 |

**There is no full-stack role in this sample that builds a fraud product** — no case-management
UI, no decisioning API, no rule-authoring tool. That pillar is absent from the readable market.

### Seniority, salary, and who is hiring

Salary is never stated on a fraud-specific listing. Experience bars: 5+ years *of SAS AML
specifically* on all four Tumaini roles; 8+ years data engineering on three; 5–8 years on the
quant role; 10+ including 5 leadership on Head of Fraud. **There is no junior on-ramp, and the
SAS AML bar is a closed loop — you cannot acquire five years of SAS AML outside a bank that
already runs SAS AML.**

Sixteen of 22 (73%) are recruiters fronting unnamed clients. Four are the Financial Intelligence
Centre, a state agency. **One is a bank posting directly — Capitec — and it is an AML Operations
Manager with no technology requirement at all.**

### The honest limit on this snapshot

Board counts lie. PNet claims 4 600 results for "financial crime" and page one includes a
construction piping supervisor in Gaborone; CareerJunction claims 377 for "fraud engineer" and
page one contains zero fraud roles. CareerJunction's own curated "financial crime" category
holds five listings. Datafin's site search for "fraud" returns one result: a claims validator.

Against ~250 surfaced titles, the true population of open, SA-based, engineering-shaped
fraud roles on the public boards that day is on the order of **15–25**, of which perhaps **3–6**
are about building detection systems. The 22 read in full is therefore close to exhaustive for
the readable surface rather than a sample of it.

**But the bias runs one way, and it matters.** The three most interesting employers sit behind
unscrapeable applicant-tracking systems and were visible only as summaries:

- **Absa — "Head of Data Engineering and Analytics: Fraud Risk Operations"**, Johannesburg,
  posted 10 August 2026: "Lead the design and implementation of data platforms for fraud
  detection and risk analytics at a major bank, focusing on real-time decisioning, AI
  initiatives, and regulatory compliance." Workday returned an empty body directly and through
  the reader proxy.
- **Old Mutual — "Senior Data Scientist – Fraud Analytics & AI Governance"**, Cape Town, posted
  10 August 2026: owning "the end-to-end MLOps lifecycle across AWS and DataBricks, applying a
  Feature / Training / Inference (FTI) pipeline architecture".
- **Moniepoint — "Data Scientist (Fraud)" / "Senior Data Scientist (Fraud)"**, remote South
  Africa: "3+ years of experience in data science, decision science, or risk analytics within
  fraud, payments, or financial crime" and "hands-on experience building and deploying machine
  learning models in a production environment". Greenhouse would not render the detail pages.

**If those three bodies were readable the "genuine fraud engineering" count would roughly
double.** So: treat "9% are genuine" as a statement about what is publicly readable, not a
proven claim about the market. The real fraud-ML work is at Absa, Old Mutual, FNB, Moniepoint
and PayInc, and it is exactly the work that does not reach a public board.

Also worth noticing: **Old Mutual's advert names the Feature/Training/Inference pipeline
architecture by name.** That is the feature-store discipline from Q3 appearing in a South
African job title. It is the strongest single piece of evidence that the *engineering* framing
of this project points at real local demand, even while the *modelling* framing does not.

### Bank career portals — reachability

| Portal | Result |
|---|---|
| Nedbank (`jobs.nedbank.co.za`) | **The only bank portal that worked.** A search for "fraud" returned 12 results, all branch service-consultant roles. Zero fraud-technology vacancies open that day |
| Absa (`absa.wd3.myworkdayjobs.com`) | Empty body, direct and via proxy. Workday SPA |
| Capitec (`capitecbank.co.za/careers`) | Bot-protection interstitial, even through the proxy |
| Standard Bank | Marketing overview, no job search in the fetched content |
| Old Mutual, DigiOutsource | Workday, detail bodies not retrievable |
| **SABRIC** | Homepage reachable; **no careers section exists**; `sabric.co.za/careers/` returns HTTP 503 |

---

## Q5 — Data a personal project can legally and practically use

### The shortlist

| Dataset | Contents | Licence (exact) | Entity IDs | Timestamps | Headline weakness |
|---|---|---|---|---|---|
| **PaySim** (Kaggle `ealaxi/paysim1`) | 6 362 620 rows × 11 cols; 744 hourly steps ≈ 30 days; 5 transaction types; ~0.13% fraud | **CC BY-SA 4.0**. Simulator repo `EdgarLopezPhD/PaySim` is **GPL-3.0** | `nameOrig`/`nameDest`, near-unique per row — useless | `step` = hour index | **The publisher's own landing page says 4 of 11 columns must not be used.** Fraud is "empty the account then cash out", so `amount == oldbalanceOrg` nearly solves it |
| **Sparkov** (Kaggle `kartik2112/fraud-detection`) | 1 852 394 rows × 23 cols; 2019–2020; **1 000 customers, 800 merchants**; ~0.5% fraud | Kaggle **CC0**. Generator `namebrandon/Sparkov_Data_Generation` is **MIT** | `cc_num`, merchant, customer geo | Full `trans_date_trans_time` + `unix_time` | Fraud drawn from **separate "fraudulent profiles"** — a different distribution family, trivially separable. Same 1 000 entities in train and test. Merchant names literally prefixed `fraud_` |
| **IEEE-CIS** (Kaggle, Vesta) | 590 540 train rows × 434 cols; 20 663 frauds = **3.50%**; ~183 days | **Kaggle Competition Rules §7** — "non-commercial purposes only … and for academic research and education"; "**You agree not to transmit, duplicate, publish, redistribute**…" | No user key; the community reconstructs one from `card1`+`addr1`+`D1` | `TransactionDT`, a timedelta from an undisclosed epoch | Label is a graph-propagated chargeback proxy with a 120-day look-forward. 339 of 434 columns are Vesta's own undocumented production-model features. **Cannot be redistributed** |
| **ULB / Worldline** (`mlg-ulb/creditcardfraud`) | **284 807 rows, 492 frauds = 0.172%**; September 2013, **2 days**, European cardholders; V1–V28 PCA | **ODbL 1.0 (database) + DbCL 1.0 (contents)** — both, not one | **None at all** | `Time` = seconds since first transaction | PCA features permanently uninterpretable; 13 years old; 492 positives is statistically thin; **no entity identifiers, so no graph or entity-resolution work is possible**. Its own maintainers now point users at their simulator |
| **Feedzai BAF** (NeurIPS 2022) | 6 datasets × 1 000 000 rows × 30 features; 8 months as a `month` column; 1.8% fraud | **CC BY-NC-ND 4.0** per the datasheet — **NoDerivatives**. Repo is Apache-2.0 for code only | None | None beyond integer `month` | Bank-account-**opening** applications, not transactions. Unusable for streaming, entity resolution or graph. **The ND clause blocks publishing derivatives** |
| **IBM AML** (NeurIPS 2023) | 6 sets, HI/LI × Small/Medium/Large — 5M to 180M transactions, 515K to 2.1M accounts, 10–97 days, laundering 1/807 to 1/1 950 | **CDLA-Sharing-1.0** for the data ("Although this Github repository is under the Apache-2.0 license, the actual data is released under the CDLA-Sharing-1.0 license"). **Commercial use permitted** | **Yes** — from/to account plus bank code | **Yes** — full date and time | Fully synthetic; the typologies are the eight the simulator injected, so detectors overfit the generator; accounts only, no person layer |
| **IBM TabFormer** (ICASSP 2021) | **24M transactions, 12 fields**; 2 000 simulated US consumers with multiple cards | Repo **Apache-2.0**; Kaggle mirror's licence field reads "Apache License, Version 2.0" | **Yes** — User, Card, Merchant name/city/state/zip/MCC | **Yes** | Only 2 000 users, so the customer graph is thin; US-only; merchant names are generated tokens, so text-based entity resolution is artificial |
| **AMLSim** (generator, not a dataset) | Multi-agent generator. Outputs transaction CSVs, alerts, **account mapping and entity-resolution ground truth**, validation reports | **Apache-2.0** | Yes, you define them | Yes | You own the realism problem. The classic eight typologies only |

### The finding that matters most

**Four canonical datasets, four *different* label-definition failures.**

- PaySim's label is leaked by the four balance columns the publisher explicitly tells you not to
  use. Verbatim from the Kaggle data card, as a section heading: "NOTE: Transactions which are
  detected as fraud are cancelled, so for fraud detection these columns (oldbalanceOrg,
  newbalanceOrig, oldbalanceDest, newbalanceDest) must not be used." Essentially every published
  benchmark ignores it.
- Sparkov's label comes from a separate generative distribution — the fraud and the non-fraud
  are not samples from one world.
- IEEE-CIS's label is a graph-propagated chargeback proxy with a 120-day look-forward.
- ULB's label is real, and the features that would let you use it were destroyed by PCA.

**No public fraud benchmark gives you a realistic label and usable features at the same time.**
That is a finding in its own right, and it is the honest answer to "can a portfolio project
demonstrate fraud detection?" — not with any of these, not on the modelling axis.

A second, subtler point on PaySim: the canonical paper it tells you to cite
(Lopez-Rojas, Elmir and Axelsson, EMSS 2016,
[PDF](https://www.msc-les.org/proceedings/emss/2016/EMSS2016_249.pdf)) says in its own abstract:

> "**The injection of malicious fraud behaviour and the application of different fraud detection
> methods are outside the scope of this paper** and are the topics for further work with the
> PaySim simulator."

**The canonical PaySim citation contains no fraud model.** Everyone citing it as provenance for
`isFraud` is citing a paper that disclaims it.

Two licence traps worth writing down: "the GitHub repo is Apache-2.0" is false for both Feedzai
BAF and IBM AML — in both cases Apache covers the *code* and the *data* is under something else
(CC BY-NC-ND 4.0 and CDLA-Sharing-1.0). And the ULB licence is the compound ODbL + DbCL, so
"it's ODbL" and "it's DbCL" are each half right.

### South Africa-specific sources — the honest answer

**There is no South African equivalent of any of these. Nothing off the shelf gives South
African transactions with entity IDs and fraud labels.** What exists:

| Source | What it is | Licence | Use |
|---|---|---|---|
| **SABRIC** annual crime statistics | ~29pp PDF, ~15 aggregate tables. Card fraud R1.745bn (2025); digital banking 110 074 incidents / R2.407bn; per-channel and per-province splits | **No licence statement anywhere in the report** | A **calibration target** for prevalence and ZAR loss magnitudes. Never training data. Coverage is voluntary member submission — SABRIC itself says the figures "should not be interpreted as a complete measure" |
| **SARB** | Online Statistical Query for macro series, plus a **public, unauthenticated Web API** (34 GET endpoints, [Swagger](https://custom.resbank.co.za/SarbWebApi/swagger/index.html)). **NPS statistics are PDF-only** | **All rights reserved** — the site disclaimer says material "may not be copied, reproduced, adapted, published or distributed in any form whatsoever without the prior written consent" | Macro context only. The copyright is a hard blocker on redistributing anything derived from it |
| **PayInc** (ex-BankservAfrica) | Economic Index, Net Salary Index, Private Pension Index — monthly PDFs | "© 2026 PayInc. All rights reserved." Terms page is JS-rendered and could not be retrieved | Not usable |
| **National Treasury Municipal Money** | **The only genuinely open SA financial data source found.** 21 cubes, JSON REST plus bulk CSV/XLSX, including an Unauthorised/Irregular/Fruitless and Wasteful Expenditure cube | Terms permit use "including for commercial and non-commercial purposes", with attribution. Effectively CC BY-equivalent though not a named licence | Already the spine of `product`. **Not transaction-like** — municipality × year × line-item aggregates, no timestamps, no counterparties, no labels |
| Zindi *Xente Fraud Detection Challenge* | ~140 000 transactions with CustomerId, ProviderId, ProductId, ChannelId and timestamps | **No licence stated**; generic Zindi terms; login required | **Uganda, not South Africa.** Interesting shape, unusable licence |
| DataFirst (UCT) | Survey and administrative microdata, CC BY-SA or CC BY-NC per dataset | Varies | **No payments or fraud data.** Sensitive holdings only inside a secure research centre |

**The practical South African verdict:** synthesise it. Run AMLSim (Apache-2.0) or Sparkov's
generator (MIT), emit **ZAR, South African bank codes, EFT / RTC / PayShap rails, and Investec's
own transaction schema**, and calibrate prevalence and loss distributions to SABRIC's published
figures. **In that project, the calibration story is the contribution** — it is the part nobody
else has done, it is defensible from primary sources, and it sidesteps POPIA entirely.

### The three safe foundations

For a public, redistributable worked example with streaming shape:

1. **IBM AML** — CDLA-Sharing-1.0, commercial use permitted, real timestamps, account and bank
   codes, labelled typologies. The best single fit.
2. **IBM TabFormer** — Apache-2.0, 24M card transactions with uncoded merchant fields, User and
   Card identifiers. The best card-shaped option.
3. **Sparkov** — CC0, so a re-shaped, re-labelled, South-Africanised derivative can be published
   with no legal friction at all. Weak as a benchmark, ideal as a substrate.

Everything else is non-commercial, no-derivatives, share-alike, no-redistribution, or has no
stated licence.

---

## Q6 — The verdict, argued

Three options were on the table. Taking them in reverse order of how tempting they are.

### (b) A separate fifth system with its own repo — no

Three arguments against, and the first is decisive.

**It fails test 4 and cannot be made to pass it.** A fifth system's headline claim would be "I
built a fraud detector". That claim needs an oracle and there is none: labels are 120 days late,
missing entirely for everything the system blocked, noisy where they exist, and produced by a
review process biased toward wherever the model already pointed. Every other system in the plan
has a crisp oracle — gold to the cent, replay byte-for-byte, Treasury's published figures, a
passing eval set. A fifth one whose oracle is "I think it got better" would be the weakest
thing in the portfolio and would drag the average down, because a reviewer calibrates on the
weakest artefact, not the strongest.

**It fails test 2.** A model trained on PaySim is not usable by anyone. PaySim's own publisher
says four of its eleven columns leak the label; its canonical paper disclaims having a fraud
model at all. A fraud detector built on a synthetic set with 1 000 entities, where every
fraudulent merchant name is prefixed `fraud_`, is a demo, not a thing someone runs.

**It costs a whole phase the plan cannot spare.** The curriculum already says the lever, when
the daily loop stops fitting, is "cutting a pillar, never lowering a standard" — and it already
carries four pillars, two systems, ten phases and the Angular decision deferred on exactly this
reasoning. A fifth system is a fifth deployment, a fifth CI pipeline, a fifth README a stranger
has to be able to run. That is the cost, and the return is a claim that does not survive its
first question.

### (c) Not worth it at all — nearly right, and wrong for one reason

The market case for (c) is strong. Two of 22 readable listings are genuine fraud engineering.
The advertised stack is SAS AML, which is not in this curriculum and cannot be learned outside a
bank. Every SAS AML posting asks for five years of SAS AML. Zero of 22 listings named Kafka,
Spark, a graph database or a rules engine. **On the market evidence alone, fraud is a worse bet
than another Spark slice.**

But (c) is wrong, for one reason: **the security phase already has "detection as code" on it as
an optional deep-dive, and optional items in this plan are the ones that quietly never happen.**
The choice is not "add fraud or not". It is "leave a vague optional item that will be skipped,
or turn it into a graded deep-dive with an exit test". And the graded version is cheap, because
every hard part it needs is already being built for other reasons: the ingestion service already
carries a stream, already does idempotent merges, already has replay from offset zero as its
exit test, already handles late data and schema drift. Scoring that stream is a slice, not a
system.

There is also a real, non-hypothetical hook in the local market that (c) would throw away. Old
Mutual's Cape Town advert asks for "the end-to-end MLOps lifecycle across AWS and DataBricks,
applying a Feature / Training / Inference (FTI) pipeline architecture". Absa is hiring a Head of
Data Engineering and Analytics for Fraud Risk Operations, "focusing on real-time decisioning".
Those are data-platform roles. They are the roles this curriculum is already aimed at. The fraud
framing is free evidence that the platform work generalises.

### (a) The Phase 7 deep-dive, over the ingestion service's stream — yes

What makes this the right answer is that **it moves the oracle rather than pretending the oracle
exists.**

The claim is not "my detector is accurate". The claims are:

- The same feature definition produces bit-identical values in the streaming path and the batch
  path, asserted by a test, over logged serving traffic with example identifiers. *(Google
  Monitor 3. This is a parity check, and `parity` already exists to run it.)*
- No feature used at time *t* depends on an event after *t*, asserted by an adversarial test
  that injects a future event and shows the backfilled value does not move. Plus the honest
  demonstration: a deliberately leaky join, its inflated AUC, the fix, and the real number.
- A replay from offset zero reproduces every score and every decision byte-for-byte, including
  across an injected failure. *(Already the ingestion service's exit test; this extends it from
  gold to decisions.)*
- Rules are pure functions in version control, unit-tested, and backtested over a fixed window
  in CI. *(Monzo's constraint, Sigma and Elastic's workflow, and the security half of the
  existing optional item, kept.)*
- Evaluation is precision@k at a stated review budget, per entity not per row, with a stated
  cost ratio and a stated break-even precision — and an explicit paragraph on the counterfactual
  gap that cannot be closed.

Every one of those is pass/fail. None of them is "I think the model is better". And every one is
a thing the target roles do.

**The data question answers itself from Q2 and Q5.** POPIA makes real transaction data the worst
possible substrate: a fraud label is special personal information under s26, an account number
carries a 10-year criminal exposure under ss105–107, cross-party linking triggers prior
authorisation and a standstill under ss57–58, and publication defeats the household exemption.
So: synthetic, generated by AMLSim or Sparkov's generator, emitted in **Investec's own sandbox
schema** — which I verified is real, reachable and documented — denominated in ZAR, over South
African rails, with prevalence and loss distributions calibrated to SABRIC's published figures.
The calibration is the original contribution, and it is defensible line by line from primary
sources.

**What this deliberately does not claim.** It does not claim a working fraud detector. It does
not claim domain experience. It does not claim SAS AML, which is what the local market actually
advertises for. Those non-claims belong in `NON-CLAIMS.md`, stated as plainly as the rest.

---

## What I could not verify

Recorded because the rule is that an unreachable source is stated, not guessed.

**Bank portals.**

- **Absa's API catalogue.** Every path on `www.api.absa.africa` beyond the marketing home page
  returns HTTP 401 (`/catalog`, `/apis`, `/products`, `/explore`, `/documentation`,
  `/live-apis`). `developer.absa.africa` is an Angular SPA that serves an empty `<app-root>`.
  I could not see a single named Absa API, a sandbox base URL, or the terms. Recorded as unread,
  not absent.
- **Standard Bank's sandbox**, if one exists. The FAQ does not mention it, and registration is
  disabled, so I could not reach the product detail pages that might.
- **Standard Bank's full product count.** I read two pages of the catalogue. There is no total.
- **Investec's card-code execution limits.** A search summary gives "2 seconds" for
  `beforeTransaction` and "15 seconds" for `afterTransaction`; **I could not find either number
  in Investec's own documentation.** Unverified.
- **Capitec's consumer pages.** `capitecbank.co.za` serves a bot-protection interstitial to
  fetchers. Only the fee-schedule PDF was readable.
- **RMB's integration channel.** `rmb.co.za/page/integration-channel` returns HTTP 200 with the
  title "Page Not Found - Integration Channel". A soft 404.
- **`developer.absa.co.za`, `apimarket.nedbank.co.za`, `developer.nedbank.co.za`,
  `developer.fnb.co.za`, `api.fnb.co.za`, `developer.capitecbank.co.za`, `developer.rmb.co.za`**
  — none resolve. The live hosts are `developer.absa.africa` / `www.api.absa.africa` and
  `apim.nedbank.co.za`.

**Regulation.**

- **The final Authorisation Framework**, promised for Q3 2026. Not published as at 2026-09-23.
- **The 2025 IFWG open-finance cost-benefit analysis** cited in Budget Review 2026. Not found on
  ifwg.co.za, resbank.co.za, fsca.co.za or treasury.gov.za. May not be public.
- **SAFLII** returns HTTP 403 directly and through the reader proxy. POPIA was read from
  justice.gov.za with section 6 cross-checked against the gazette.
- **Whether s6(1)(a) "purely personal or household activity" excludes a published portfolio
  project.** No South African authority found. The GDPR analogue says publication defeats it.
  Marked Unverified and treated as not applying.
- **BASA.** No open-banking material found at all. Recorded as a genuine absence.
- **COFI full implementation by 2029–2030.** Secondary reporting only.
- Whether the "centralised interface infrastructure" in the May 2026 draft is PayInc. Inference.

**Fraud engineering.**

- **A card-authorisation latency budget in milliseconds from a scheme document.** The handbook
  says "a few milliseconds" and "within milliseconds and before authorization". No scheme number.
- **A fraud base rate in basis points from a primary source.** SABRIC publishes losses, not a
  denominator. The widely quoted 0.172% is the ULB dataset's own positive rate, not an industry
  figure.
- **The AML false-positive figure** commonly quoted at 90–95%. No regulator, BIS, FATF or bank
  source found for it. Not used.
- **SR 11-7, the FIC Act's specific sections, and any SARB Prudential Authority model-risk
  guidance.** Not reached.
- **Davis & Goadrich (2006) and Saito & Rehmsmeier (2015)** on PR versus ROC curves. Not
  retrieved; the argument is carried here by Stripe's and the handbook's own framing instead.
- **Splink**, the UK Ministry of Justice probabilistic linkage library. Not reached, and it is
  the obvious tool for the entity-resolution part.
- **Panther's detection-as-code definition** in one consolidated quote. The overview page names
  Python detections and a CI/CD guide but does not define the practice in one place.

**Job market.**

- **Absa, Old Mutual, Moniepoint and every other Workday or Greenhouse posting.** Summaries only.
  This is the single biggest hole and it biases the sample toward agency-brokered SAS AML work.
- **LinkedIn bodies.** Titles only, on every attempt, as in the previous snapshot.
- Unreachable this run: Careers24 (403), Indeed SA (403), OfferZen (404), GoldmanTech (refused),
  JobMail (broken), WeWorkRemotely (403), `sabric.co.za/careers/` (503), recruit.net (403),
  RemoteOK (no rows rendered), Bizcommunity (410 Gone).

**Datasets.**

- **Elliptic++'s licence.** Not stated on the repository.
- **Berka / PKDD'99's licence.** None stated anywhere; the original host no longer resolves.
- **FiFAR's licence.** No licence on the README; the datasheet URL 404s.
- **PaySim's source country.** The paper says "an African country" and does not name it. It is
  not stated to be South Africa.
- Several fraud-rate figures in the summary table are marked Unverified at source.

---

## Proposed change to `CURRICULUM.md` — a proposal only, changing nothing

Five edits. They add one graded deep-dive and one exit test. They add no phase, no repository,
and no pillar.

**1. Phase 7, modules column.** Replace `Optional deep-dive: detection as code` with:

> **`deep-dive`: detection as code.** Sigma and Elastic's `detection-rules` as the security
> shape; rules as pure functions in version control, unit-tested against replayed events, with
> a backtest in CI. Scored over two streams: the audit log, and the ingestion service's
> transaction stream. Point-in-time correctness and training/serving parity as tests, not
> aspirations. Precision at a review budget, per entity, with a stated cost ratio.

**2. Phase 7, project column.** Replace `Optional: detection rules over the audit log, tested in
CI` with:

> Detection rules over the audit log **and** over a synthetic South African transaction stream
> carried by the ingestion service: rules as pure functions, unit-tested and backtested in CI;
> a point-in-time-correct feature layer with velocity windows; an automated training/serving
> skew test; an alert queue with a fixed daily review budget; an evaluation report giving
> precision@k per entity, a stated cost ratio and break-even precision, and a written section on
> the counterfactual gap.

**3. Phase 7, exit test.** Add a second clause to the existing one:

> …and a deliberately leaky feature join is caught by a point-in-time test that existed first,
> with the inflated score and the honest score both published; and a replay from offset zero
> reproduces every alert decision byte for byte.

**4. "The oracle, named" table.** Add a row:

| System | What "correct" means |
|---|---|
| Detection | Features are bit-identical across the streaming and batch paths; no feature at time *t* reads an event after *t*; a replay reproduces every decision. **Not** "the model is good" — that is a judgement, and the write-up says so |

**5. Phase 5, ingestion service project column.** Add one clause, because this is what makes the
Phase 7 work a slice rather than a system:

> …and a synthetic South African transaction generator — AMLSim or Sparkov, in ZAR over EFT,
> RTC and PayShap, emitting Investec's Private Bank API transaction schema, with prevalence and
> loss distributions calibrated to SABRIC's published annual statistics — as a second source
> alongside CDC and Municipal Money.

**And one line for `NON-CLAIMS.md`:**

> I have not built a fraud detection system that works. I have built the engineering around one
> and can say precisely which parts of it are correct and which are judgement. I have no
> experience of SAS AML, which is what South African banks actually advertise for.

### What this costs, stated honestly

One extra generator in Phase 5. One deep-dive module instead of an optional bullet in Phase 7.
Two extra exit-test clauses. No new repository, no new deployment, no fifth README.

### What would change my mind

- **A response to an Absa, Old Mutual or Moniepoint fraud-engineering advert that got read.**
  If the in-house bank market is bigger and more Python/Databricks-shaped than the readable
  surface suggests, the case for more weight strengthens.
- **A published South African transaction dataset with entity IDs and labels.** None exists
  today. One would remove the calibration work and change the cost-benefit.
- **The SARB publishing an open-finance framework with an account-information activity.** That
  would make a real-data project possible and would make bank API work a market skill rather
  than a curiosity.
- **Two rejections where fraud or financial-crime domain experience was the stated blocker.**
  Same trigger shape as the Angular decision.
