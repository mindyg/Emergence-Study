"""Strips condition/entry-point labels from a folder of session JSONL
files, shuffles them, and writes opaque-ID copies to a blinded output
folder plus a separate key.json mapping IDs back to condition/entry
point. Per the pre-registration addendum: do not open key.json until
coding is complete.

Usage (run from inside experiments/harness/):
    python blind.py --in-dir ../raw --out-dir ../blinded
"""

import argparse
import json
import random
import uuid
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-dir", default="../raw")
    ap.add_argument("--out-dir", default="../blinded")
    ap.add_argument("--seed", type=int, default=None,
                     help="Optional random seed for reproducible shuffling.")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for f in sorted(in_dir.glob("*.jsonl")):
        records.append(json.loads(f.read_text(encoding="utf-8")))

    if args.seed is not None:
        random.seed(args.seed)
    random.shuffle(records)

    key = {}
    for record in records:
        opaque_id = uuid.uuid4().hex[:12]
        key[opaque_id] = {
            "session_id": record["session_id"],
            "condition": record["condition"],
            "entry_point": record["entry_point"],
        }

        blinded_lines = [
            f"# Blinded Session — {opaque_id}",
            "",
            "*(Condition and entry point withheld until coding is complete.)*",
            "",
            "---",
            "",
        ]
        for i, ex in enumerate(record["exchanges"], 1):
            blinded_lines += [
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
                "---",
                "",
            ]
        (out_dir / f"{opaque_id}.md").write_text("\n".join(blinded_lines), encoding="utf-8")

    key_path = out_dir / "key.json"
    key_path.write_text(json.dumps(key, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(records)} blinded transcripts to {out_dir}")
    print(f"Key written to {key_path} — do not open until coding is complete.")


if __name__ == "__main__":
    main()
