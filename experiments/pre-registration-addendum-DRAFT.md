# Pre-Registration Addendum — DRAFT, pending approval

**This is a draft. It does not modify [pre-registration-adversarial-control.md](../analysis/pre-registration-adversarial-control.md) until Mindy reviews and approves it. Once approved, its content should be merged into that file (or linked from it) and committed before any C1/C2 session is run — same discipline as the original pre-registration.**

## What this changes from the original design

The original pre-registration (§7, "Known limitations") flagged an unresolved dependency: *"the design requires an operator other than Mindy for C1/C2; as of this pre-registration, no second operator has been recruited."*

This addendum resolves that dependency differently than originally imagined: **the interlocutor is scripted, not a second human.** See [interlocutor-rules.md](interlocutor-rules.md) for the fixed decision rules, derived directly from Mindy's actual C0 transcripts.

This is registered as an *improvement* on the original design, not a workaround, for a specific reason: a scripted interlocutor is perfectly reproducible — the exact same rule set runs identically on every session, which no human operator (however well-briefed) can guarantee. It also removes a confound the original design didn't fully control for: a second human operator's *own* idiosyncratic style would have been a new uncontrolled variable, layered on top of the one being tested.

## Second improvement: blind coding becomes possible

The original pre-registration (§7) also flagged: *"With a single researcher, full blinding is not currently feasible."* A scripted, file-based harness removes that limitation. The runner will:

1. Run all C0/C1/C2 sessions and log them to `experiments/raw/` (gitignored, not committed).
2. A blinding tool strips condition labels and entry-point labels from each transcript, renames files to opaque IDs, and shuffles their order, writing the result to a `blinded/` folder plus a separate `key.json` mapping opaque IDs back to condition/entry-point.
3. Mindy codes the blinded transcripts using the coding table format from the original pre-registration (§4), without knowing which condition produced which transcript.
4. Only after coding is complete does she open `key.json` to unblind and compute condition-level rates.

This addendum registers the blinding procedure now, before any session is run, so the coding rules themselves (§4 of the original pre-registration) are not adjusted after seeing which condition a transcript came from.

**Honest limit on what this blinding actually buys.** Confirmed by a pipeline test run: stripping the condition label from a transcript does not stop a coder from *inferring* the condition — the precise condition's follow-ups obviously press, the adversarial condition's obviously dismiss. This is not a flaw in the tool; it's intrinsic to blinding a behavioral manipulation (unlike a drug trial, where the treatment itself is invisible). What this blinding actually protects against: coding a given exchange's agentive-instance/correction/relapse fields with the hypothesis already in mind, and unconsciously coding more generously for whichever condition is expected to show the effect. It does not protect against a coder guessing the condition from the interlocutor's visible behavior. This should be stated as-is in any results writeup, not implied to be stronger than it is.

## Nothing else in the original pre-registration changes

Predictions (§3), operational coding definitions (§4), sample size and stopping rule (§5), and success/failure criteria (§6) all stand as originally written. This addendum only changes *how* C1/C2 are operationalized (scripted vs. human) and *adds* a blinding step that was previously infeasible.

## Approval checklist

- [ ] Mindy has reviewed `interlocutor-rules.md` and signed off on the trigger words, follow-up lists, and exchange counts.
- [ ] Mindy confirms the blinding procedure above before any session is run.
- [ ] This file (or its content) is merged into `analysis/pre-registration-adversarial-control.md`, and the merge is committed to git *before* the first C1/C2 session is executed — preserving the git-timestamp-as-pre-registration guarantee the original document relies on.
