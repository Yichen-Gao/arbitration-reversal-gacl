#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

METHOD_ORDER = ["Joint", "AAD@5pp", "ACD@5pp", "GACL@5pp"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", action="store_true", help="Use cached main-result rows.")
    parser.add_argument("--input", type=Path, default=Path("cached/scores/main_results.csv"))
    parser.add_argument("--output", type=Path, default=Path("results/expected_table3.csv"))
    args = parser.parse_args()
    rows = list(csv.DictReader(args.input.open(encoding="utf-8")))
    grouped = defaultdict(list)
    for row in rows:
        if not row.get("test_conflict_acc"):
            continue
        grouped[row["method"]].append(row)
    out = []
    for method in METHOD_ORDER:
        vals = grouped.get(method, [])
        if not vals:
            continue
        out.append({
            "method": method,
            "evaluated_configurations": len(vals),
            "mean_conflict_acc": f"{100 * sum(float(r['test_conflict_acc']) for r in vals) / len(vals):.1f}",
            "mean_gain_vs_joint": f"{100 * sum(float(r['gain_vs_joint']) for r in vals) / len(vals):.1f}",
            "mean_faithful_acc": f"{100 * sum(float(r['test_aligned_acc']) for r in vals) / len(vals):.1f}",
            "mean_faithful_drop": f"{100 * sum(float(r['aligned_drop']) for r in vals) / len(vals):.1f}",
        })
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader(); writer.writerows(out)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
