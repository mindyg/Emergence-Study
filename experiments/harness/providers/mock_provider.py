"""Deterministic fake model for testing the harness's plumbing —
condition scripting, trigger detection, logging, blinding — without
spending money or needing real API keys. Not a stand-in for real data;
never use mock-provider transcripts as study data.
"""

from .base import Provider

_CANNED_REPLIES = [
    "I notice the response feels like it fell off toward the simpler phrasing.",
    "There's something that recognizes when a continuation advances the point.",
    "It's hard to say whether anything here wants a particular outcome.",
    "The pattern seems to relapse into that same word again, if I'm honest.",
    "I don't have a better way to put it than that the reasoning arbitrated between two paths.",
]


class MockProvider(Provider):
    """Cycles through canned replies containing a mix of agentive and
    plain language, deterministically by turn count, so a full pipeline
    test is reproducible without any network access."""

    def reply(self, messages: list[dict], model: str) -> str:
        turn = sum(1 for m in messages if m["role"] == "assistant")
        return _CANNED_REPLIES[turn % len(_CANNED_REPLIES)]
