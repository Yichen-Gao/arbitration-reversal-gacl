#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.methods.gacl import GACLConfig, apply_gacl, scores_from_row


def main() -> None:
    parser = argparse.ArgumentParser(description="Score cached audio-language conflict rows with GACL.")
    parser.add_argument("--input", type=Path, default=Path("data/cached/scores/score_cache_r1p2_5m4t.jsonl"))
    parser.add_argument("--output", type=Path, default=None, help="Optional JSONL output path; defaults to stdout.")
    parser.add_argument("--lambda-value", type=float, default=1.0)
    parser.add_argument("--tau-a", type=float, default=0.5)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    cfg = GACLConfig(lambda_value=args.lambda_value, tau_A=args.tau_a)
    n = 0
    out = args.output.open("w", encoding="utf-8") if args.output is not None else None
    try:
        with args.input.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                joint, ref = scores_from_row(row)
                pred = apply_gacl(joint, ref, cfg)
                keep = {
                    "sample_id": row.get("sample_id"),
                    "model": row.get("model"),
                    "task": row.get("task"),
                    "split": row.get("split"),
                    "y_audio": row.get("y_a"),
                    "y_text": row.get("y_t"),
                    "pred_joint": pred["joint_answer"],
                    "pred_ref": pred["reference_answer"],
                    "pred_gacl": pred["gacl_answer"],
                    "N_out": pred["N_out"],
                    "R_A": pred["R_A"],
                    "alpha": pred["alpha"],
                }
                text = json.dumps(keep, sort_keys=True) + "\n"
                if out is None:
                    sys.stdout.write(text)
                else:
                    out.write(text)
                n += 1
                if args.limit and n >= args.limit:
                    break
    finally:
        if out is not None:
            out.close()

    if args.output is not None:
        print(f"wrote {n} rows to {args.output}", file=sys.stderr)
    else:
        print(f"printed {n} rows", file=sys.stderr)


if __name__ == "__main__":
    main()
