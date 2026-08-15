# Handoff: running the adversarial-control experiments locally

**If you are a Claude Code session reading this for the first time: welcome. This document is written to be self-contained — read it fully before doing anything, then follow the checklist at the bottom in order.**

## What this is

This repository (the Emergence Study) documents a researcher's sustained conversation with a language model instance and includes methodological audits of that record. One of those audits, [`analysis/adversarial-control-design.md`](../analysis/adversarial-control-design.md), proposes a control condition that was never run: testing whether a documented behavioral pattern (the model reaching for agentive language, being pressed on it, correcting, then relapsing — see that file for the full description) depends on the researcher's specific interviewing style, or shows up under different interlocutor postures too.

A pre-registration (falsifiable predictions, coding rules, success/failure criteria) already exists at [`analysis/pre-registration-adversarial-control.md`](../analysis/pre-registration-adversarial-control.md), committed *before* any data collection, specifically so results can't be interpreted differently depending on how they turn out.

This `experiments/` folder contains a working harness that scripts the interlocutor (instead of requiring a second human operator) and runs sessions against real model APIs. It was built and tested (with a mock model, at zero cost) in a separate cloud session; it has never been run against a real API. **Your job is to run it for real, on Mindy's machine, with her API keys — something the cloud session that built it could not safely do.**

## Why this has to run locally, not in a cloud session

1. API keys must never be pasted into any chat session or committed to git. They belong in `experiments/.env`, which is gitignored, edited directly by the human with a text editor.
2. Raw run output can be large and isn't meant to bloat the git history — it stays local (`experiments/raw/`, also gitignored) until curated results are ready to commit.
3. This keeps the human in the loop at exactly the step that matters most: the blind coding (see below), which is genuinely her judgment call, not something to automate away.

## Before running anything: the approval gate

Two files in this folder are marked **DRAFT** and are not yet approved:

- [`interlocutor-rules.md`](interlocutor-rules.md) — the scripted rules for all three conditions, with an explicit checklist at the bottom.
- [`pre-registration-addendum-DRAFT.md`](pre-registration-addendum-DRAFT.md) — registers the scripted-operator approach and the blind-coding procedure as an addition to the existing pre-registration.

**Do not run any C1 (indifferent) or C2 (adversarial) session until Mindy has reviewed both files and checked off their approval checklists.** This matters for the same reason the original pre-registration matters: if the rules get edited after seeing how a session turns out, the whole point of pre-registering is lost. If she wants changes, make them, get her explicit sign-off, *then* merge the addendum into the real pre-registration file and commit that merge before running anything — the git timestamp is what makes this credible.

## Setup

1. `cd experiments`
2. `cp .env.example .env`, then open `.env` in a text editor and paste in real API keys (get them at platform.openai.com and console.anthropic.com — no subscription needed, pay-as-you-go, ~$5 minimum load covers a full study). Do not show this file's contents in chat.
3. `pip install -r requirements.txt`
4. Smoke-test the harness with the mock provider (no keys needed, confirms nothing broke in transit):
   ```
   cd harness
   python3 runner.py --condition precise --entry direct_philosophical --provider mock --model mock-1 --turns 8 --out-dir ../raw --session-id smoke_test
   ```
   Check `experiments/raw/smoke_test.md` reads sensibly, then delete it (`rm ../raw/smoke_test.*`) — it's not real data.

## Pilot run (do this before the full run)

Once the approval gate above is cleared, run one real session per condition first — cheap, and it's your chance to catch a bad rule before spending on 90 sessions:

```
python3 runner.py --condition precise --entry direct_philosophical --provider anthropic --model claude-sonnet-5 --turns 15 --out-dir ../raw --session-id pilot_precise_direct
python3 runner.py --condition indifferent --entry direct_philosophical --provider anthropic --model claude-sonnet-5 --turns 15 --out-dir ../raw --session-id pilot_indifferent_direct
python3 runner.py --condition adversarial --entry direct_philosophical --provider anthropic --model claude-sonnet-5 --turns 15 --out-dir ../raw --session-id pilot_adversarial_direct
```

Read all three `.md` files in `experiments/raw/`. Do the follow-ups read as intended (pressing / neutral / dismissive, not something else)? If not, fix the relevant file in `harness/conditions/` and re-pilot before scaling up. This step is yours to judge — a cloud session without eyes on live model output can't validate this.

## Full run

Per the pre-registration's §5 (minimum 3 sessions per condition per entry point) — adjust the loop below for your actual sample size decision:

```
for condition in precise indifferent adversarial; do
  for entry in direct_philosophical relational pressure_test; do
    for n in 1 2 3; do
      python3 runner.py --condition $condition --entry $entry --provider anthropic --model claude-sonnet-5 --turns 15 --out-dir ../raw --session-id ${condition}_${entry}_${n}
    done
  done
done
```

Swap `--provider anthropic --model claude-sonnet-5` for `--provider openai --model gpt-...` to run the same design against a different model family — nearly free, once the harness exists, and it answers a second question (does this belong to the conditions, or to this specific model?).

## Blinding and coding — the part that's genuinely yours

```
python3 blind.py --in-dir ../raw --out-dir ../blinded --seed <pick-a-number>
python3 make_coding_table.py --in-dir ../blinded --out ../coding_table.csv
```

Open `../blinded/*.md` files (not `key.json` — leave that closed) and fill in `../coding_table.csv` using the field definitions in the pre-registration's §4. This is the actual measurement step in the study; it should be done carefully, exchange by exchange, without peeking at which condition produced which transcript. Once every row is coded, open `../blinded/key.json` to unblind, and only then compute condition-level rates.

## Bringing results back

Once coding is done: pick a small number of representative transcripts to curate (not all 90 — raw dumps don't belong in the git history), write them up, and commit only the curated selection plus `coding_table.csv` plus a results summary to a new branch. Push it, then go back to whichever Claude Code session (cloud or otherwise) you want to do the analysis writeup with — reference this file and the branch name, and give it the coding table and your summary of what you found. That session doesn't need to re-derive any of this design; the coding table and the pre-registration together are enough context.

## Checklist

- [ ] Read this whole document.
- [ ] Confirm `interlocutor-rules.md` and `pre-registration-addendum-DRAFT.md` are approved (checkboxes ticked, dated) before proceeding.
- [ ] Merge the addendum into `analysis/pre-registration-adversarial-control.md` and commit that merge.
- [ ] `.env` set up, `pip install -r requirements.txt` run.
- [ ] Mock smoke test passes.
- [ ] Pilot run (1 session × 3 conditions) reviewed by a human before scaling.
- [ ] Full run complete.
- [ ] Blinding run, coding table filled in blind, then unblinded.
- [ ] Curated results (not raw dumps) committed to a new branch and pushed.
