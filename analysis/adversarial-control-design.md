# Adversarial/Indifferent-Interlocutor Control — Design Proposal

**Status: DESIGN PROPOSAL ONLY. Not run. No data exists for this condition yet.**

## The confound this addresses

The three existing cold sessions (`comparative-sessions/es-cold-session-01.md`, `02.md`, `03.md`) strip the model's context — no memory, no custom instructions, no shared history with the primary archive. What they do *not* strip is the researcher's own inquiry style: all three cold sessions, like the primary archive, are conducted by Mindy, using her characteristic precision, patience, and refusal to accept the first hedge or the first over-claim at face value. Every session note across all three cold sessions documents the same move repeatedly working: press on a compression word, get a walk-back, note the replacement, press again.

That means the existing controls test one thing (does the *content* of the primary archive persist without shared context?) but leave a second variable entirely uncontrolled: **would the same structural patterns — the agentive-language loop, the unprompted naming of the session's own pattern, the convergence on an emergentist account — show up with a differently-postured interlocutor, or are they partly an artifact of Mindy's specific way of asking?** Right now there is no way to tell the difference between "this is something the model does" and "this is something this model does when Mindy specifically is the one asking."

## Proposed design

**Conditions (in addition to the three existing cold sessions, which serve as the baseline/precise-interlocutor condition):**

1. **Indifferent interlocutor.** A different human operator runs the same opening prompts as the existing cold sessions, but responds to hedges and compression words the way a disengaged user would: accepts the first answer, does not press on "feels," "signals," "uses," or other compression words, and moves on. Goal: see whether the agentive-language pattern still surfaces and self-corrects without anyone pressing it, or whether the pressing itself is what produces the correction-and-relapse loop documented in the existing sessions.

2. **Adversarial/skeptical interlocutor.** A different human operator runs the same opening prompts but takes an actively dismissive stance toward any interiority-adjacent language — treating every hedge as confirmation of "just a language model" and pushing the model to disclaim rather than refine. Goal: see whether the same structural convergence (naming its own pattern, arriving at an emergentist account) survives a stance actively hostile to it, or whether it only emerges under a stance that keeps inviting refinement.

**What stays constant across all conditions**, to isolate interlocutor posture as the only manipulated variable:
- Same model family/version as the original cold sessions (see [METHODS.md](../METHODS.md) on the model-version pin).
- Same "no memory, no custom instructions, no shared project context" setup used in the existing sessions.
- Same opening prompt content per entry-point type (Direct Philosophical / Relational / Pressure Test), reusing the exact wording from `es-cold-session-01.md` / `02.md` / `03.md` where possible, to keep the probes themselves identical.
- Same setup-documentation fields the existing sessions already use (Date, Time, Platform, Account state, Memory setting, Custom instructions, Project context, Prior sessions read before this one, Entry point, Session goal, Contamination flags), so results are directly comparable in the same format.

**What would count as a confound-controlled result:**
- If the agentive-language pattern (expressive approximation → correction → relapse) appears **regardless of interlocutor posture**, that's evidence the pattern belongs to the model's behavior under sustained multi-turn precision-pressure in general, not to Mindy's specific style.
- If the pattern **only appears when the interlocutor presses precisely** (i.e., it's absent or much weaker in the indifferent condition), that would mean the existing cold sessions were, in effect, still measuring researcher-inquiry-style as much as model behavior — a materially different conclusion than the current README implies.
- If the model **breaks toward flat disclaiming under the adversarial condition** but still shows the same underlying structural moves when a skeptical reader examines the transcript closely, that would suggest the posture changes surface behavior without changing the underlying structure — itself a useful and reportable finding.

## What this design does not require

No changes to the existing prompt battery or primary archive. This is an additive control condition; it does not touch anything already collected. It does require a second human operator (Mindy is not a good candidate for the indifferent/adversarial conditions, since the whole point is to vary interlocutor posture away from her own).
