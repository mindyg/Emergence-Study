"""Common interface every model provider implements."""

from abc import ABC, abstractmethod


class Provider(ABC):
    """A chat-completion backend. Implementations hold no state between
    calls other than what's passed in `messages` — the harness owns the
    conversation history, not the provider."""

    @abstractmethod
    def reply(self, messages: list[dict], model: str) -> str:
        """messages: list of {"role": "user"|"assistant", "content": str}.
        Returns the assistant's reply text for the next turn."""
        raise NotImplementedError
