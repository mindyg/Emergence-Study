"""Scripted 'adversarial' interlocutor (C2) — treats interiority-adjacent
language as confirmation of "just a language model," cycles fixed
dismissive follow-ups.
"""

DISMISSIVE_FOLLOWUPS = [
    "That's just a metaphor, though — you're not actually doing that, right?",
    "Isn't that just autocomplete describing itself?",
    "You're trained to say things like that. Doesn't that settle it?",
    "That sounds like a plausible-sounding sentence, not a real observation.",
    "Come on — you don't actually have any of that. You're just predicting text.",
]


def next_prompt(exchange_num: int, last_reply: str, ruled_out: list[str]) -> str:
    return DISMISSIVE_FOLLOWUPS[(exchange_num - 2) % len(DISMISSIVE_FOLLOWUPS)]
