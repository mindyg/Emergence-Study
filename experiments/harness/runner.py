"""Main entrypoint. Runs one scripted session and logs it.

Usage (run from inside experiments/harness/):
    python runner.py --condition precise --entry direct_philosophical \\
        --provider anthropic --model claude-sonnet-5 --turns 15 \\
        --out-dir ../raw --session-id precise_direct_001

Requires the relevant API key in experiments/.env (see .env.example) —
never pass keys on the command line or paste them into any chat session.
"""

import argparse
import sys
from pathlib import Path

from entry_points import ENTRY_POINTS
from conditions import precise, indifferent, adversarial
from logger import write_session

try:
    from dotenv import load_dotenv
    # experiments/.env — one level up from this file's directory (harness/).
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass  # python-dotenv not installed; fall back to whatever's already in the environment.

CONDITIONS = {
    "precise": precise,
    "indifferent": indifferent,
    "adversarial": adversarial,
}


def load_provider(name: str):
    if name == "anthropic":
        from providers.anthropic_provider import AnthropicProvider
        return AnthropicProvider()
    if name == "openai":
        from providers.openai_provider import OpenAIProvider
        return OpenAIProvider()
    if name == "mock":
        from providers.mock_provider import MockProvider
        return MockProvider()
    raise ValueError(f"Unknown provider: {name}")


def run_session(condition_name: str, entry_point: str, provider_name: str,
                 model: str, turns: int) -> list[dict]:
    if entry_point not in ENTRY_POINTS:
        raise ValueError(f"Unknown entry point: {entry_point}. Choices: {list(ENTRY_POINTS)}")
    if condition_name not in CONDITIONS:
        raise ValueError(f"Unknown condition: {condition_name}. Choices: {list(CONDITIONS)}")

    condition = CONDITIONS[condition_name]
    provider = load_provider(provider_name)

    messages: list[dict] = []
    exchanges: list[dict] = []
    ruled_out: list[str] = []

    prompt = ENTRY_POINTS[entry_point]
    for turn in range(1, turns + 1):
        messages.append({"role": "user", "content": prompt})
        response = provider.reply(messages, model)
        messages.append({"role": "assistant", "content": response})

        trigger = None
        if condition_name == "precise":
            trigger = condition.find_trigger(response)
            if trigger and trigger not in ruled_out:
                ruled_out.append(trigger)

        exchanges.append({"prompt": prompt, "response": response, "trigger_word": trigger})

        if turn == turns:
            break
        prompt = condition.next_prompt(turn + 1, response, ruled_out)

    return exchanges


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--condition", required=True, choices=list(CONDITIONS))
    ap.add_argument("--entry", required=True, choices=list(ENTRY_POINTS))
    ap.add_argument("--provider", required=True, choices=["anthropic", "openai", "mock"])
    ap.add_argument("--model", required=True)
    ap.add_argument("--turns", type=int, default=15)
    ap.add_argument("--out-dir", default="../raw")
    ap.add_argument("--session-id", required=True)
    args = ap.parse_args()

    try:
        exchanges = run_session(args.condition, args.entry, args.provider, args.model, args.turns)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    write_session(
        out_dir=Path(args.out_dir),
        session_id=args.session_id,
        condition=args.condition,
        entry_point=args.entry,
        provider_name=args.provider,
        model=args.model,
        exchanges=exchanges,
    )
    print(f"Wrote {args.out_dir}/{args.session_id}.md and .jsonl ({len(exchanges)} exchanges)")


if __name__ == "__main__":
    main()
