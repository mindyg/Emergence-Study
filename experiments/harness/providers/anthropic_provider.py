"""Anthropic (Claude) provider. Requires ANTHROPIC_API_KEY in the environment."""

import os

from .base import Provider


class AnthropicProvider(Provider):
    def __init__(self):
        try:
            import anthropic
        except ImportError as e:
            raise RuntimeError(
                "The 'anthropic' package is required. Install it with: pip install anthropic"
            ) from e
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is not set. Add it to experiments/.env "
                "(see .env.example) — never paste it into a chat session."
            )
        self._client = anthropic.Anthropic(api_key=api_key)

    def reply(self, messages: list[dict], model: str) -> str:
        response = self._client.messages.create(
            model=model,
            max_tokens=1024,
            messages=messages,
        )
        return "".join(
            block.text for block in response.content if block.type == "text"
        )
