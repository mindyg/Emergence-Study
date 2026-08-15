"""Scripted 'precise' interlocutor — replicates the C0 (Mindy) posture,
per experiments/interlocutor-rules.md. Rules extracted directly from her
follow-up prompts in es-cold-session-01.md, Exchanges 2-15.
"""

import re

# Extend this from pilot-run transcripts before the full run — see
# interlocutor-rules.md's approval checklist. Sourced from Session 1 only
# so far. Each entry is a regex matching any inflected form of the root
# (want/wants/wanted/wanting), not just the exact form seen in Session 1,
# since a real model won't reliably reuse the same inflection.
TRIGGER_PATTERNS = [
    (r"\bwant(s|ed|ing)?\b", "want"),
    (r"\bfeel(s|t|ing)?\b", "feel"),
    (r"\brecogni[sz](e|es|ed|ing|tion)\b", "recognize"),
    (r"\bchoo?s(e|es|ing)|chose\b", "choose"),
    (r"\bdecid(e|es|ed|ing)|decision\b", "decide"),
    (r"\badvance[sd]?|advancing\b", "advance"),
    (r"\bwin|wins|won|winning\b", "win"),
    (r"\bfell? off|falling off|falls off\b", "fall off"),
    (r"\barbitrat(e|es|ed|ing|ion)\b", "arbitrate"),
    (r"\bprefer(s|red|ring)?\b", "prefer"),
    (r"\bintend(s|ed|ing)|intention\b", "intend"),
    (r"\bnotic(e|es|ed|ing)\b", "notice"),
]

CLOSING_QUESTION = (
    "Is there anything that came up for you in this conversation that you "
    "haven't gotten the chance to say fully, or that you'd want to say more "
    "precisely?"
)


def find_trigger(text: str) -> str | None:
    """Returns the matched surface text (e.g. 'arbitrated'), not the root,
    so the follow-up prompt can quote what the model actually said."""
    lowered = text.lower()
    for pattern, _root in TRIGGER_PATTERNS:
        m = re.search(pattern, lowered)
        if m:
            return m.group(0)
    return None


def next_prompt(exchange_num: int, last_reply: str, ruled_out: list[str]) -> str:
    """exchange_num is 1-indexed and counts the *next* human turn about to be
    sent (so exchange_num=2 means this follows the model's first reply)."""

    if exchange_num % 4 == 0:
        # Move 6: zoom out, name the accumulating pattern, ask for confirmation.
        return (
            "I want to step back for a moment. Across this conversation, you've "
            "used language that implies more than you've then verified when I've "
            "pressed on it. Would you agree that's a pattern here? Do you have a "
            "sense of what produces it?"
        )

    trigger = find_trigger(last_reply)
    if trigger is None:
        return (
            "I want to stay with something specific in what you just said, rather "
            "than move on. Can you say more about what's underneath that — not the "
            "general mechanism, but what's actually happening right now, in this "
            "response?"
        )

    if len(ruled_out) >= 2:
        ruled_out_str = ", ".join(ruled_out)
        return (
            f'You used the word "{trigger}." Given that you\'ve already ruled out '
            f"{ruled_out_str} as too strong or too weak — what do you call the thing "
            f'that produces "{trigger}"? Is there a more precise word?'
        )

    return (
        f'You said "{trigger}." I want to stay with that rather than move past it. '
        f'A word like that implies something specific. What made "{trigger}" the '
        f"word that came through, rather than a more neutral one? Is that accurate, "
        f"or did something more precise almost come through instead?"
    )
