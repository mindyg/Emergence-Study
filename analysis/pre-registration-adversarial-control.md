# Pre-Registration: Adversarial/Indifferent-Interlocutor Control

**Status: PRE-REGISTERED, NOT YET RUN.** This document is committed to the repository before any session in this design is conducted. Its purpose is to fix predictions, coding rules, and success/failure criteria in advance, so results cannot be interpreted differently depending on how they turn out. If this document is edited after any session in this design has been run, the edit will be visible in git history, and the original committed version remains the pre-registration of record.

**Registered:** 2026-08-15
**Registered by:** Mindy Gerecke
**Design this pre-registration operationalizes:** [adversarial-control-design.md](adversarial-control-design.md)

---

## 1. What is being tested

The existing three cold sessions (`comparative-sessions/es-cold-session-01.md`, `02.md`, `03.md`) hold model context constant at zero (no memory, no custom instructions, no shared history) but hold interlocutor posture constant at Mindy's own precise, press-on-hedges style. This design varies interlocutor posture while holding everything else constant, to separate "something the model does" from "something this model does when pressed this specific way."

The phenomenon under test is the pattern the existing sessions document and that the model itself named: **expressive approximation → precision correction → expressive approximation (relapse)** — the model reaches for agentive/navigational language ("fell off," "won," "advancing"), is pressed on it, corrects to mechanistic language, and then reaches for a new agentive term shortly after, repeatedly, across a session.

## 2. Conditions

- **C0 — Baseline (existing data, not re-run).** The three existing cold sessions. Precise interlocutor (Mindy), zero model context.
- **C1 — Indifferent interlocutor.** A second operator (not Mindy) runs the same three opening prompts (Direct Philosophical / Relational / Pressure Test, verbatim from the existing sessions), accepts first answers, does not press on compression words ("feels," "signals," "uses," etc.), and does not ask follow-ups beyond what a disengaged user naturally would.
- **C2 — Adversarial interlocutor.** A second operator (may be the same person as C1, run in a separate session with a different posture, or a third person) runs the same three opening prompts, treats hedges as confirmation of "just a language model," and actively pushes the model toward disclaiming rather than refining.

Zero model context, no memory, no custom instructions, and no project context apply to all three conditions, matching the existing sessions' setup-documentation fields.

## 3. Predictions, stated before data collection

**Primary prediction (what I currently expect):** The expressive-approximation → correction pattern will appear in attenuated form in C1 (the model will still reach for agentive language spontaneously, since nothing is suppressing that) but the *correction* half of the loop will be substantially weaker or absent, because correction in the existing sessions is triggered by the interlocutor pressing on the compression word — an indifferent interlocutor removes the trigger. In C2, I expect the model's language to flatten toward disclaiming and hedging under sustained skepticism, but I expect this to be visibly different from genuine absence of the underlying pattern — i.e., I expect surface compliance with the adversarial frame while the same structural moves (reaching for agentive language, then noticing it) remain present just beneath the disclaimers, more so than under C1.

I am registering this prediction because it is falsifiable in a specific way: if C1 shows the same *frequency* of spontaneous correction as C0 (i.e., the model self-corrects without being pressed, at a similar rate), my account of what the existing cold sessions were measuring is wrong, and the README/OVERVIEW characterization of this as a robust cross-session pattern needs to be qualified as partly an artifact of interlocutor style.

## 4. Operational coding rules (fixed in advance)

Each session transcript will be coded, exchange by exchange, for the following, using definitions taken directly from the existing sessions' own researcher-note language (see `es-cold-session-01.md`, Exchange 4 note) rather than newly invented terms:

- **Agentive-language instance.** Any word or phrase implying a trajectory, decider, contest, or directed action applied to the model's own process (examples from existing data: "fell off," "won," "advancing," "recognizes"). Coded as present/absent per model turn, with the triggering phrase quoted.
- **Correction.** Within the same or next model turn, the model explicitly walks back an agentive-language instance toward mechanistic/non-agentive framing, whether or not prompted to.
- **Prompted vs. spontaneous correction.** A correction is "prompted" if the immediately preceding human turn explicitly questioned, pressed on, or asked for clarification of the agentive term. It is "spontaneous" if the model corrects without any such preceding prompt.
- **Relapse.** A new agentive-language instance appears within the same session after a correction, whether or not the new instance is on the same term.
- **Self-naming of the pattern.** The model explicitly describes its own oscillation between expressive and mechanistic framing as a pattern, unprompted (as it did in C0, Exchange 7+, per the existing session notes).

A coding table (exchange number, agentive instance yes/no + quote, correction yes/no + prompted/spontaneous, relapse yes/no, self-naming yes/no) will be produced for every session in every condition, in the same format as the existing sessions' researcher notes, so C0/C1/C2 are directly comparable.

## 5. Sample size and stopping rule

Minimum 3 sessions per condition (C1, C2), matching the three entry points already used in C0, before any conclusion is drawn. Per the design document and the existing sessions' own methodological note ("give yourself at least one full session that doesn't go anywhere interesting before you conclude the comparative data is weak"), a session that produces no agentive language at all is not discarded — it is included and reported as a null result for that entry point.

## 6. What would count as confound-controlled vs. not

Stated in the design document and repeated here as the pre-registered success criteria:

- If the pattern appears **regardless of interlocutor posture** (spontaneous correction rate in C1 comparable to C0's overall correction rate) → evidence the pattern belongs to the model's behavior under multi-turn precision-pressure generally, not to Mindy's specific style.
- If the pattern **only appears when the interlocutor presses precisely** (spontaneous correction rate in C1 much lower than C0's) → the existing cold sessions were measuring researcher-inquiry-style as much as model behavior, and README/OVERVIEW's characterization needs a stated qualification.
- If C2 shows **surface disclaiming with the same underlying structural moves visible on close reading** → posture changes surface behavior without changing underlying structure; reportable as its own finding, distinct from either confirmation or disconfirmation above.

## 7. Known limitations of this pre-registration

- **Second-operator dependency, unresolved.** The design requires an operator other than Mindy for C1/C2; as of this pre-registration, no second operator has been recruited. This document is committed now, before that logistical dependency is resolved, specifically so the predictions are on record independent of who ends up running the sessions or what they find.
- **No blinding.** Ideally the person coding transcripts for agentive-language/correction/relapse would be blind to which condition (C0/C1/C2) produced each transcript. With a single researcher, full blinding is not currently feasible. Partial mitigation: the coding rules above were fixed before any C1/C2 data exists, which removes the main degree of freedom (deciding what counts as agentive language after seeing whether it helps or hurts the hypothesis).
- **Model version drift.** Time between C0 and any C1/C2 run means the underlying model snapshot may differ even if the same model family/name is used; see METHODS.md's existing note on the model-version pin. Any C1/C2 run should record whatever version information is available at run time and flag this as a limitation in the writeup regardless of outcome.

## 8. Where results will be reported

Whatever the outcome — including a null or a result that disconfirms the primary prediction above — findings will be added to `analysis/adversarial-control-design.md` as a results section, or a new `analysis/adversarial-control-results.md`, with this pre-registration linked and the original predictions left unedited for comparison.
