"""Generates a blank coding-table CSV for a folder of blinded transcripts,
with the exact fields from pre-registration-adversarial-control.md §4.

Usage (run from inside experiments/harness/):
    python make_coding_table.py --in-dir ../blinded --out ../coding_table.csv
"""

import argparse
import csv
import re
from pathlib import Path


def count_exchanges(md_text: str) -> int:
    return len(re.findall(r"^### Exchange \d+", md_text, re.M))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-dir", default="../blinded")
    ap.add_argument("--out", default="../coding_table.csv")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    rows = []
    for f in sorted(in_dir.glob("*.md")):
        opaque_id = f.stem
        text = f.read_text(encoding="utf-8")
        n = count_exchanges(text)
        for exchange_num in range(1, n + 1):
            rows.append({
                "opaque_session_id": opaque_id,
                "exchange_num": exchange_num,
                "agentive_instance_present": "",   # yes/no
                "agentive_quote": "",                # quoted phrase, if yes
                "correction_present": "",            # yes/no
                "correction_prompted_or_spontaneous": "",  # prompted/spontaneous/n-a
                "relapse_present": "",               # yes/no
                "self_naming_present": "",           # yes/no
                "coder_notes": "",
            })

    out_path = Path(args.out)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows across {len(list(in_dir.glob('*.md')))} sessions to {out_path}")


if __name__ == "__main__":
    main()
