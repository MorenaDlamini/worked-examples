# Decision records

One file per real decision, numbered. `000-template.md` is the shape.

## Why these exist

Every one of the roles in `CURRICULUM.md` asks for judgment under ambiguity, and judgment is
invisible in a commit history. A repository full of working code shows what I built. It does
not show what I considered and rejected, or what I knew I was trading away. That is the part
an interviewer probes and the part I will not remember in six months.

## Rules

- **Written at the time.** A decision record written afterwards is a justification.
- **At least two options, stated fairly.** If a proponent of the option I rejected would not
  recognise my description of it, I have written a straw man and learned nothing.
- **Consequences include the bad ones.** A decision with no downside is a decision I have not
  understood yet.
- **"What would change my mind" is mandatory.** If nothing would, it was not a decision.
- **Never edited to look right later.** Superseded records get a status line and a pointer to
  the record that replaced them. The wrong ones are the valuable ones.

## The test

Two months later, read an old record and ask: did the consequence I predicted actually
happen? That question is how estimation improves, and there is no other way to get it.
