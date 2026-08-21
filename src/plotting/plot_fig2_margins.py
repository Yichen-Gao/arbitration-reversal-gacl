#!/usr/bin/env python3
"""Reproduce the margin scatter figure from cached margin rows."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.plotting.style import PALETTE, apply_style

PICKS = [
    ("Qwen2-Audio", "MCR-AQA"),
    ("Qwen2.5-Omni", "MCR-VSC"),
    ("Voxtral", "MCR-SER"),
    ("Qwen3-Omni", "MCR-ALME"),
]
MODEL_LABEL = {
    "Qwen2-Audio": "Qwen2-Audio-Inst.",
    "Qwen2.5-Omni": "Qwen2.5-Omni",
    "Voxtral": "Voxtral-Small-24B",
    "Qwen3-Omni": "Qwen3-Omni",
}
TASK_LABEL = {"MCR-AQA": "AQA", "MCR-VSC": "VSC", "MCR-SER": "SER", "MCR-ALME": "ALME"}


def load_rows(path: Path) -> dict[tuple[str, str], list[dict]]:
    cells = defaultdict(list)
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("M_A") is None or row.get("M_J") is None:
                continue
            key = (str(row.get("model")), str(row.get("task")))
            row["M_A"] = float(row["M_A"])
            row["M_J"] = float(row["M_J"])
            row["repairable"] = row["M_A"] > 0 and row["M_J"] < 0
            cells[key].append(row)
    return cells


def draw(args: argparse.Namespace) -> None:
    apply_style()
    cells = load_rows(args.input)
    fig, axes = plt.subplots(1, 4, figsize=(7.0, 2.1), constrained_layout=True)
    for i, key in enumerate(PICKS):
        ax = axes[i]
        rows = cells[key]
        if not rows:
            raise RuntimeError(f"no rows for {key}")
        repair = [r for r in rows if r["repairable"]]
        other = [r for r in rows if not r["repairable"]]
        ax.axhline(0, color=PALETTE["dark"], linestyle="--", linewidth=0.8)
        ax.axvline(0, color=PALETTE["dark"], linestyle="--", linewidth=0.8)
        ax.scatter([r["M_A"] for r in other], [r["M_J"] for r in other], s=9, color=PALETTE["gray"], alpha=0.45, edgecolors="none", label="Other")
        ax.scatter([r["M_A"] for r in repair], [r["M_J"] for r in repair], s=11, color=PALETTE["orange"], alpha=0.70, edgecolors=PALETTE["dark"], linewidths=0.15, label="Repairable")
        ax.set_xlabel(r"Audio-reference margin $M_A$")
        if i == 0:
            ax.set_ylabel(r"Joint-conflict margin $M_J$")
        pct = 100.0 * len(repair) / len(rows)
        ax.text(0.04, 0.96, f"Repairable: {pct:.1f}%", transform=ax.transAxes, ha="left", va="top", fontsize=7, bbox={"facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.85, "pad": 2})
        ax.set_title(f"({chr(97+i)}) {MODEL_LABEL[key[0]]} x {TASK_LABEL[key[1]]}", fontsize=8)
        ax.grid(alpha=0.12, linewidth=0.4)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", action="store_true", help="Use cached inputs (default).")
    parser.add_argument("--input", type=Path, default=Path("data/cached/scores/margin_rows_r005.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("assets/figures/fig2.pdf"))
    draw(parser.parse_args())


if __name__ == "__main__":
    main()
