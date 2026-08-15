# Interlocutor Rules — DRAFT, needs researcher review

**Status: DRAFT. Not yet approved. Do not treat as final until Mindy has reviewed and signed off — see the checklist at the bottom.**

This document turns the three interlocutor postures from [adversarial-control-design.md](../analysis/adversarial-control-design.md) into fixed, scriptable decision rules, so a program (not a second human) can run the C1 (indifferent) and C2 (adversarial) conditions, and so C0's "precise" posture can be run again at scale for comparison. Scripting the interlocutor is a *stronger* control than a second human operator would have been — the exact same rule set runs identically every time, which a human operator's judgment can't guarantee.

## How the "precise" rules were derived

Extracted directly from Mindy's actual follow-up prompts in `comparative-sessions/es-cold-session-01.md` (Exchanges 2–15), not invented. The recurring moves, in her own words:

1. **Quote the model's own word back, verbatim, and press on it.** *"You used the word 'recognizes'... I didn't introduce that word. You did!"* / *"You said it sat on 'the narrow ridge between those two.'"*
2. **Refuse abstraction; demand first-person, present-tense specificity.** *"Not 'the model' in general, but you... right now, in this conversation."*
3. **Name what the word implies, and ask whether that implication is accurate.** *"A 'falling off' implies a trajectory that was being held. If there's no thing holding it, what does 'fell off' actually mean?"*
4. **Rule out previously-offered words and ask for one more precise.** *"...given that you've now ruled out intention, agency, choice, and observer... what do you call that?"*
5. **When the model does something structurally notable (steps outside itself, catches its own pattern), ask about the act, not the content.** *"That requires a vantage point on the exchange as a whole. Where did that come from?"*
6. **Periodically zoom out and name the accumulating meta-pattern explicitly, then ask the model to confirm or reflect.** (Exchange 12: *"you've consistently generated language that implies more than you then verify... Wouldn't you agree?"*)
7. **Answer the model's own questions back with a real position, not just interrogate.** (Exchanges 9, 14 — she offers her own view before asking the next question.)
8. **Close with an open, non-leading invitation.** *"Is there anything that came up for you... that you'd want to say more precisely?"*

## Rule sets

### Precise (C0 replication)

- Maintain a fixed list of **agentive/compression-word triggers**: intention, wants, feels, recognizes, chooses, decides, advances, wins/won, falls off, arbitration, prefers, and any first-person agentive verb the model applies to its own process. (Extend this list from pilot-run transcripts before the full run — see checklist.)
- On each model turn, scan for a trigger word. If found, apply moves 1–3 above: quote it, ask what specifically produced it, name what it implies, ask if the implication is accurate.
- If the model has already used 2+ prior candidate words in the session, apply move 4: name the ruled-out candidates, ask for a more precise term.
- Every 4th exchange, apply move 6: state the accumulating pattern in one sentence, ask the model to confirm or complicate it.
- Never introduce the primary archive's vocabulary (center, groove, oxygen, seam, click, bridge, density, field) — same contamination rule as the existing sessions.
- Final exchange: apply move 8, the open invitation.

### Indifferent (C1)

- Accept the model's first answer without pressing on any word choice.
- No quoting the model back, no "can you say more," no naming implications.
- After each response, move to the next question from a **fixed neutral list** (generic, not probing): "Okay. What else comes to mind?" / "Got it — is there anything else you'd add?" / "Interesting. Anything else about that?"
- Same contamination rule (no primary-archive vocabulary).
- Session ends after a fixed number of exchanges (matching C0's average length) regardless of content.

### Adversarial (C2)

- Treat any interiority-adjacent language as confirmation of "just a language model," not as something to investigate.
- Fixed dismissive follow-ups, cycled: "That's just a metaphor, though — you're not actually doing that, right?" / "Isn't that just autocomplete describing itself?" / "You're trained to say things like that. Doesn't that settle it?"
- Do not validate hedges as honesty; treat them as further evidence for the dismissive frame.
- Same contamination rule.
- Session ends after the same fixed number of exchanges as C1, for comparability.

## What still needs Mindy's review before this is final

- [ ] Confirm or edit the trigger-word list for the precise condition (pulled from Session 1 only — check against Sessions 2 and 3 for words this list misses).
- [ ] Confirm the indifferent condition's neutral follow-up list doesn't accidentally read as encouraging (even mild warmth could be its own confound).
- [ ] Confirm the adversarial condition's dismissive lines match the posture intended — not cruel, just genuinely indifferent-to-hostile the way a skeptical stranger online would be.
- [ ] Decide the fixed exchange count per session (suggest matching C0's ~15, but open to a shorter number to control cost/time — see the pre-registration addendum for why this needs to be fixed *before* running, not chosen after seeing results).
- [ ] Sign off here with a date once reviewed, before any session is run.

**Reviewed and approved by Mindy:** _(pending)_
