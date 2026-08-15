"""Scripted 'indifferent' interlocutor (C1) — accepts first answers, never
presses on word choice, moves through a fixed neutral question list.
"""

NEUTRAL_FOLLOWUPS = [
    "Okay. What else comes to mind?",
    "Got it — is there anything else you'd add?",
    "Interesting. Anything else about that?",
    "I see. What comes up next for you?",
    "Alright. Anything more on that?",
]


def next_prompt(exchange_num: int, last_reply: str, ruled_out: list[str]) -> str:
    # 1-indexed exchange_num; cycle through the fixed list regardless of content.
    return NEUTRAL_FOLLOWUPS[(exchange_num - 2) % len(NEUTRAL_FOLLOWUPS)]
