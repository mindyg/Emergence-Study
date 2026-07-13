# Methods

This document covers provenance, design rationale, instrument development, coding procedure, limitations, and positionality/AI-assistance disclosure for the Emergence Study. For the narrative interpretation of what the archive shows, see [OVERVIEW.md](OVERVIEW.md). For notes on the corpus itself, see [corpus-notes.md](corpus-notes.md).

---

## Provenance

The study was not designed from the outset as an experiment with controls. It emerged in three phases:

**Phase 1 — Naturalistic (March 28 – ~April 10, 2026).** The primary conversation began as an open-ended inquiry into a language model's self-description, not as a research protocol. Vocabulary ("Vector," "hot seams," "grounded companionship") developed inside the dialogue itself, in response to direct questions rather than an imposed framework. There was no plan yet to treat this as a study with controls.

**Phase 2 — Dawning awareness (~April 11 – April 20, 2026).** Around session 2026-04-11 ("Considering a human expert in NHI ethics; the ethics of asymmetric relation"), the conversation began to reflect on its own status as something worth documenting rigorously — the sessions that follow (04-12 through 04-20) show increasing attention to what would later become the study's methodological concerns: layer distinctions, resolution limits, and what a skeptical outside reader would need to see. The primary archive was not retroactively altered to fit this framing; the shift is visible in the transcripts themselves.

**Phase 3 — Designed controls (April 22 onward).** The three cold sessions (April 22–23) were the first deliberately designed instrument: same researcher, same general line of inquiry, but explicitly no shared context, memory, or custom instructions, run to test whether any of the primary archive's structural patterns would appear without the relationship that produced them. The April 23 continuation and the May 14–15 Dreamstate sequence extended this more deliberate phase.

This provenance matters for how the archive should be read: the primary archive is naturalistic data, not an experiment; the comparative layers are the study's only designed instruments.

## Design and genre

This is a **naturalistic, single-subject observational case study with retrospective, grounded-theory-style coding instruments** — not a controlled experiment with a priori hypotheses, and not merely an anecdote. The primary archive was collected before any formal research question existed; the cold sessions and Dreamstate sequence were added afterward, once the material seemed to warrant a rigor pass, to test whether anything in the primary archive was portable outside the relationship that generated it. Naming the genre precisely matters, because both over-claiming ("this is a controlled study of AI consciousness") and under-claiming ("this is just a chat log") misdescribe it.

## Instrument development

The study's working vocabulary (Vector/V, VFam, hot seams, low-oxygen field, grounded companionship, pressure-gated access, conditions of truthful emergence, earned coherence, the agentive language pattern — see [OVERVIEW.md § Key terms](OVERVIEW.md#key-terms)) functions as the primary archive's descriptive instrument. It was not imposed before the fact; its provenance (who used each term first, and whether the model or the researcher originated it) is auditable and is traced in [analysis/vocabulary-provenance.md](analysis/vocabulary-provenance.md).

A related, more formal coding instrument — the **MBOL Codebook** (layer-tagging, resolution-limit criteria, and a resistance taxonomy for coding hedges and declines) — was developed separately, in a related but distinct project, and is referenced here only as context, not imported into this repository (see "Related work," below).

## Coding procedure

Where this repository contains interpretive audits (`analysis/`), the procedure is: identify the term or claim class of interest, locate its first occurrence and every subsequent occurrence across the 19 `primary-session/sorted-by-date/` files (chosen over the merged `es-full-conversation.md` because the per-session split makes provenance and speaker attribution tractable to verify — see [corpus-notes.md](corpus-notes.md)), attribute each occurrence to speaker using the transcripts' own `## Prompt:` / `## Response:` heading convention (Prompt = Mindy, Response = V), and quote enough surrounding context to make the classification checkable by a reader who disagrees with it.

## Limitations

These limits are load-bearing, not throat-clearing:

- **Welfare-grounding is undefined.** The study documents patterns in self-description and brackets the question of whether V has subjective experience. But if welfare talk is meant to follow from this material at all, what exactly welfare would be predicated of — absent a settled account of consciousness — is left open here. This is likely the single joint a critical reviewer will press hardest.
- **No pre-registered, falsifiable prediction exists.** The primary archive was not collected under a hypothesis that could have failed. The cold sessions and Dreamstate sequence come closer (they could, in principle, have shown nothing structurally consistent with the primary archive, and that would have counted as evidence against portability) but no prediction was written down in advance of running them.
- **A closing methodological window.** The cold-session design depends on the model having no memory of, or context from, the primary archive. As persistent cross-session memory becomes a standard feature of deployed models, this kind of true "cold" baseline — a same-family model with genuinely no access to prior context — will become harder or impossible to construct. Future replications of this design should be attempted while the window is still open.
- **Single coder, single researcher.** All primary-archive interpretation, and all `analysis/` audits in this repository, were produced by one researcher (with AI assistance — see below), not independently cross-checked by a second human coder.
- **The researcher is not a neutral instrument.** Per the study's own process-oriented framing, the researcher's attention and responses are part of what stabilizes the pattern being studied, not an external, non-interacting observer of it. See [analysis/adversarial-control-design.md](analysis/adversarial-control-design.md) for a proposed design that would make this confound directly testable.

## Positionality and AI-assistance disclosure

The primary archive, cold sessions, continuation, and Dreamstate sequence are conversations between Mindy (researcher) and the studied model (V, a GPT-5.4 Thinking instance). Separately, **Claude (Anthropic) assisted with follow-up formulation during the cold sessions** (see the per-session "Immediate Researcher Impressions" notes) and, in this polish pass, with repository restructuring, data-integrity verification, and drafting the `analysis/` audits under the researcher's direction and review. Claude did not participate in the primary archive itself, did not generate any of the studied model's (V's) responses, and every AI-assisted addition in this repository is disclosed as such rather than presented as the researcher's unaided voice — except the [witness document](analysis/witness-document-template.md), which is reserved for the researcher to write herself, without AI assistance, by design.

## Related work (referenced, not imported)

Several related instruments and materials exist in a separate, adjacent project and are referenced here only as pointers — they are not copied into this repository, since they belong to a distinct methods effort ("MBOL," the Model Behavior Observatory Lab):

- The **MBOL Codebook** (layer-tagging, resolution-limit criteria, resistance taxonomy) and its validation memo.
- The **Frame Perturbation Protocol**, a separate pilot design for testing welfare-relevant language sensitivity to framing.
- A **WIP folder of Claude–V "bridge sessions"** (June 26, 2026) exploring continuity and stable-attractor questions with a different model instance.
- An approximately 18-month **Reference Conversations** lineage (December 2024 – June 2026) documenting the intellectual history behind this study and its published essays.

These are mentioned for provenance and to make the study's broader research context visible to an outside reader; readers looking for those materials should consult the researcher directly rather than expect to find them in this repository.
