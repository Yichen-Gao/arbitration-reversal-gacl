#!/usr/bin/env python3
"""Recompute the paper-facing MC2 G2 transfer table from cached summaries."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", action="store_true", help="Use cached fixed-parameter G2 summary (default).")
    parser.add_argument("--input", type=Path, default=Path("cached/scores/mc2_g2/fixed_lam0p5_tau0p5_summary.csv"))
    parser.add_argument("--output", type=Path, default=Path("results/expected_mc2_table.csv"))
    args = parser.parse_args()

    rows = read_rows(args.input)
    joint_by_model = {r["model"]: float(r["conflict_vision_follow"]) for r in rows if r["method"] == "Joint baseline"}
    faithful_by_model = {r["model"]: float(r["consistent_vision_follow"]) for r in rows if r["method"] == "Joint baseline"}

    out = []
    paper_methods = {"Joint baseline", "Vision-priority prompt", "GACL (fixed)"}
    for r in rows:
        if r["method"] not in paper_methods:
            continue
        conflict = float(r["conflict_vision_follow"])
        faithful = float(r["consistent_vision_follow"])
        model = r["model"]
        out.append({
            "model": model,
            "method": r["method"],
            "protocol": r["protocol"],
            "conflict_vision_follow": f"{conflict:.1f}",
            "consistent_vision_follow": f"{faithful:.1f}",
            "adv_gain_vs_joint": "--" if r["method"] == "Joint baseline" else f"{conflict - joint_by_model[model]:+.1f}",
            "faithful_drop_vs_joint": f"{faithful_by_model[model] - faithful:.1f}",
            "conflict_gate": r.get("conflict_gate", ""),
            "consistent_gate": r.get("consistent_gate", ""),
            "parse_rate": r["parse_rate"],
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
