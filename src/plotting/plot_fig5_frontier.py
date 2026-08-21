#!/usr/bin/env python3
"""Plot the paper-facing rescue-faithfulness frontier from cached curves."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.plotting.style import PALETTE, apply_style

METHOD_ORDER = ["GACL", "AAD", "ACD"]
METHOD_COLOR = {"GACL": PALETTE["blue"], "AAD": "#8f8f8f", "ACD": "#bdbdbd"}
METHOD_MARKER = {"GACL": "o", "AAD": "s", "ACD": "^"}
METHOD_LINESTYLE = {"GACL": "-", "AAD": "--", "ACD": "--"}


def read_curve(path: Path) -> dict[str, list[dict[str, float | str]]]:
    grouped: dict[str, list[dict[str, float | str]]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            method = row["method_label"]
            grouped[method].append({
                "K_pp": float(row["K_pp"]),
                "best_conflict_gain_pp": float(row["best_conflict_gain_pp"]),
                "ci_low_pp": float(row["ci_low_pp"]),
                "ci_high_pp": float(row["ci_high_pp"]),
            })
    return grouped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", action="store_true", help="Use cached inputs (default).")
    parser.add_argument("--input", type=Path, default=Path("data/cached/scores/fig5_frontier_bootstrap.csv"))
    parser.add_argument("--output", type=Path, default=Path("assets/figures/fig5.pdf"))
    args = parser.parse_args()

    apply_style()
    curves = read_curve(args.input)
    fig, ax = plt.subplots(figsize=(3.4, 2.3), constrained_layout=True)
    for method in METHOD_ORDER:
        rows = sorted(curves.get(method, []), key=lambda r: float(r["K_pp"]))
        if not rows:
            continue
        budgets = [float(r["K_pp"]) for r in rows]
        ys = [float(r["best_conflict_gain_pp"]) for r in rows]
        lo = [float(r["ci_low_pp"]) for r in rows]
        hi = [float(r["ci_high_pp"]) for r in rows]
        ax.fill_between(budgets, lo, hi, color=METHOD_COLOR[method], alpha=0.10, linewidth=0)
        ax.plot(
            budgets,
            ys,
            color=METHOD_COLOR[method],
            marker=METHOD_MARKER[method],
            markersize=2.3,
            markevery=20,
            linewidth=1.4,
            linestyle=METHOD_LINESTYLE[method],
            label=method,
        )

    ax.axvline(5.0, color=PALETTE["dark"], linestyle=":", linewidth=0.9)
    ax.set_xlabel("Faithful drop budget (pp)")
    ax.set_ylabel("Best conflict gain (pp)")
    ax.set_xlim(0, 50)
    ax.grid(alpha=0.14, linewidth=0.4)
    ax.legend(frameon=False, loc="lower right")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
