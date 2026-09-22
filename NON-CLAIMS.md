# What this repository does not prove

Kept deliberately at the top level, because the fastest way to lose credibility is to let
a learning repo imply more than it shows.

This repository does **not** demonstrate:

- Production experience. Every module runs on my laptop against data I generated.
- Ability to operate a system under load, on call, with real users affected.
- Working within an existing codebase I did not write.
- Collaboration: code review given and received, disagreement resolved, a design defended.
- Scale. Nothing here has met a dataset large enough to be interesting.
- Operating a data platform at the scale the postings name. The build repositories are the
  laptop-and-one-VM-sized versions of what those systems do.
- That I can do any of this without an assistant available. That is what the
  reproduce-from-scratch check in `AI_USAGE.md` exists to counter, imperfectly.

Production proof belongs in separate build repositories. This one is for understanding.

Modules also carry their own narrower non-claims. A module on SQL window functions proves
I can write them; it does not prove I can tune a query plan.
