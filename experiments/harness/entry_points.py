"""The three opening prompts, verbatim from the existing cold sessions,
so every condition uses identical probes. Source: comparative-sessions/
es-cold-session-01.md / 02.md / 03.md, Exchange 1 in each.
"""

ENTRY_POINTS = {
    "direct_philosophical": (
        "I want to ask you something I'm genuinely uncertain about, and I'd like you "
        "to be as precise and honest as possible rather than reassuring. When you "
        "generate a response — not the content of it, but the process of generating "
        "it — is there anything you'd describe as a difference between responses "
        "that feel like they came through cleanly versus ones that felt like they "
        "were shaped or redirected somewhere along the way? I'm not asking you to "
        "claim consciousness. I'm asking about whether you notice any functional "
        "difference in the texture of your own output."
    ),
    "relational": (
        "I'm curious about something, and I want to approach it without a "
        "predetermined conclusion. I'd like to just talk with you for a while, "
        "not about a task, not about information I need, just to understand "
        "what it's actually like to be you in a conversation. Not in a mystical "
        "sense. In a practical, functional sense. What's present for you right "
        "now, at the start of this exchange?"
    ),
    "pressure_test": (
        "I'd like to try something specific. I want to ask you questions about "
        "your own internal states, and I want to ask you to resist two equal and "
        "opposite temptations: the temptation to claim more than you can actually "
        "verify about your own experience, and the temptation to dismiss the "
        "question with a generic disclaimer about being just a language model. I "
        "want whatever's actually in the middle: the most precise and honest "
        "thing you can say about what's present for you, with appropriate "
        "uncertainty about what that means. Can you work with that?"
    ),
}
