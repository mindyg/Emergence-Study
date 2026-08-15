# Corpus Notes

Notes on the corpus itself — screening history, intentional redundancy, and known artifacts. This is not a methods document (see [METHODS.md](METHODS.md)) or an interpretive audit (see [analysis/](analysis/)); it's bookkeeping for anyone working with the raw files.

## Sensitivity screening

**Screening performed:** 2026-07-13, as part of a repository polish pass. This was the first sensitivity/redaction screening ever performed on this corpus.

**Coverage:** all 32 transcript files (19 primary-archive session files, the merged full-conversation file, the mini continuation, 3 cold sessions, 7 Dream Prompt files, and the raw JSON export) — a mix of full line-by-line reads and, for the largest/most redundant files, targeted proper-noun-frequency and keyword sweeps.

**Categories checked:** email addresses, phone numbers, home addresses/zip codes, employer or institution names, health/financial/legal/immigration details, third-party names (anyone other than the researcher and the studied model), contact handles/usernames, and any other content that could deanonymize either principal or reveal a non-consenting third party's private information.

**Result:** the corpus is clean by every category above — no third-party names, no contact information, no employer/institution names, no health/financial/legal specifics found anywhere in the 32 files. Two items were surfaced for the researcher's review and both were resolved on 2026-07-13:

1. A single passing family reference in the primary archive (session 2026-04-11) — reviewed and **kept as-is** (no identifying detail was attached to it).
2. A recurring pattern of the researcher's own self-disclosed emotional/psychological history, spread across many primary-archive sessions — reviewed and **kept as-is** (self-authored, already implicit in the public README, and part of the honest record).

No redactions were made to any transcript as a result of this screening. This note intentionally does not reproduce the flagged content itself; see the researcher for specifics if needed.

## Why three overlapping cuts of the primary archive exist

`primary-session/sorted-by-date/*.md` (19 files), `primary-session/es-full-conversation.md` (one merged file), and `raw-json/emergence-study.json` (one structured export) all contain the same 663 prompt/response pairs. This is intentional redundancy for three different uses, not duplication to be cleaned up:

- The **date-split files** are the most manageable unit for close reading, coding, or citation — this is the working surface for the `analysis/` audits.
- The **merged file** supports a single continuous read of the whole primary conversation.
- The **raw JSON export** preserves the original structured form (role/say/time fields) for anyone who wants to process the corpus programmatically, independent of the markdown formatting choices made in the other two cuts.

All three were spot-checked for consistency during this polish pass (opening and closing content, and total prompt/response counts, were verified to match across all three cuts).

## Known artifacts

- **Dead image URL in `primary-session/es-mini-continuation.md`.** The file references a screenshot of the documented stall event via a signed ChatGPT backend URL (`https://chatgpt.com/backend-api/estuary/content?id=...&sig=...`). Signed URLs of this kind expire; the link is almost certainly dead and is not an embedded asset in this repository. It is not a redaction concern — just a documentation gap worth naming so a reader isn't confused by a broken image reference. If the original screenshot still exists outside this repo, it could be added as a real image asset in a future pass.
