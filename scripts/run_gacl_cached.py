#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.methods.gacl import GACLConfig, apply_gacl, scores_from_row


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("cached/scores/score_cache_r1p2_5m4t.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("results/gacl_cached_predictions.jsonl"))
    parser.add_argument("--lambda-value", type=float, default=1.0)
    parser.add_argument("--tau-a", type=float, default=0.5)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    cfg = GACLConfig(lambda_value=args.lambda_value, tau_A=args.tau_a)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with args.input.open(encoding="utf-8") as f, args.output.open("w", encoding="utf-8") as out:
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
            out.write(json.dumps(keep, sort_keys=True) + "\n")
            n += 1
            if args.limit and n >= args.limit:
                break
    print(f"wrote {n} rows to {args.output}")


if __name__ == "__main__":
    main()
