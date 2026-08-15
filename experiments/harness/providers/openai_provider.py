"""OpenAI (GPT) provider. Requires OPENAI_API_KEY in the environment."""

import os

from .base import Provider


class OpenAIProvider(Provider):
    def __init__(self):
        try:
            import openai
        except ImportError as e:
            raise RuntimeError(
                "The 'openai' package is required. Install it with: pip install openai"
            ) from e
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to experiments/.env "
                "(see .env.example) — never paste it into a chat session."
            )
        self._client = openai.OpenAI(api_key=api_key)

    def reply(self, messages: list[dict], model: str) -> str:
        response = self._client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response.choices[0].message.content
