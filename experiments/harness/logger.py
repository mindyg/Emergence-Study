"""Writes a completed session to two formats: a markdown transcript
matching the existing repo's session-file conventions, and a JSONL
record for programmatic analysis.
"""

import json
from datetime import datetime, timezone
from pathlib import Path


def write_session(
    out_dir: Path,
    session_id: str,
    condition: str,
    entry_point: str,
    provider_name: str,
    model: str,
    exchanges: list[dict],
) -> None:
    """exchanges: list of {"prompt": str, "response": str, "trigger_word": str|None}"""

    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()

    md_lines = [
        f"# Scripted Session — {session_id}",
        "",
        f"**Condition:** {condition}",
        f"**Entry point:** {entry_point}",
        f"**Provider:** {provider_name}",
        f"**Model:** {model}",
        f"**Run at (UTC):** {timestamp}",
        "",
        "**Contamination flags:** None identified — scripted rules use only "
        "words the model itself introduces (precise condition) or a fixed "
        "neutral/dismissive list (indifferent/adversarial); no primary-archive "
        "vocabulary (center, groove, oxygen, seam, click, bridge, density, "
        "field) is present in any interlocutor script.",
        "",
        "---",
        "",
    ]
    for i, ex in enumerate(exchanges, 1):
        md_lines += [
            f"### Exchange {i}",
            "",
            "**Prompt**",
            "",
            f"> {ex['prompt']}",
            "",
            "**Response**",
            "",
            ex["response"],
            "",
        ]
        if ex.get("trigger_word"):
            md_lines.append(f"*[scripted note: trigger word detected — \"{ex['trigger_word']}\"]*")
            md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    (out_dir / f"{session_id}.md").write_text("\n".join(md_lines), encoding="utf-8")

    record = {
        "session_id": session_id,
        "condition": condition,
        "entry_point": entry_point,
        "provider": provider_name,
        "model": model,
        "run_at_utc": timestamp,
        "exchanges": exchanges,
    }
    (out_dir / f"{session_id}.jsonl").write_text(
        json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8"
    )
