#!/usr/bin/env python3
"""Reproduce the mechanism-to-output bridge figure from cached patch results."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.analysis.patch_score_alignment import spearman
from src.plotting.style import PALETTE, apply_style


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def draw(args: argparse.Namespace) -> None:
    apply_style()
    scatter = read_csv(args.scatter)
    curve = read_csv(args.curve)
    xs = [float(r["residual_patch_displacement"]) for r in scatter]
    ys = [float(r["final_branch_displacement"]) for r in scatter]
    rho = spearman(xs, ys)

    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.35), constrained_layout=True)
    ax = axes[0]
    ax.scatter(xs, ys, s=14, color=PALETTE["blue"], alpha=0.65, edgecolors="white", linewidths=0.2)
    ax.set_xlabel("Patch-induced displacement")
    ax.set_ylabel("Final branch-score displacement")
    ax.text(0.05, 0.95, rf"Spearman $\rho={rho:.2f}$", transform=ax.transAxes, ha="left", va="top", bbox={"facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.85, "pad": 2})
    ax.set_title("(a) Per-sample alignment", fontsize=8)
    ax.grid(alpha=0.14, linewidth=0.4)

    ax = axes[1]
    depth = [float(r["relative_depth"]) for r in curve]
    mean = [float(r["rho_mean"]) for r in curve]
    lo = [float(r["rho_min"]) for r in curve]
    hi = [float(r["rho_max"]) for r in curve]
    ax.fill_between(depth, lo, hi, color=PALETTE["blue"], alpha=0.16, linewidth=0)
    ax.plot(depth, mean, color=PALETTE["blue"], linewidth=1.5, marker="o", markersize=2.4, label="Mean alignment")
    ax.axhline(0, color=PALETTE["dark"], linestyle="--", linewidth=0.8)
    ax.set_xlabel("Relative layer depth")
    ax.set_ylabel(r"Spearman $\rho$")
    ax.set_title("(b) Layer-resolved bridge", fontsize=8)
    ax.grid(alpha=0.14, linewidth=0.4)
    ax.legend(frameon=False, loc="lower right")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", action="store_true", help="Use cached inputs (default).")
    parser.add_argument("--scatter", type=Path, default=Path("data/cached/patch_results/panel_a_qwen2_audio_aqa_scatter.csv"))
    parser.add_argument("--curve", type=Path, default=Path("data/cached/patch_results/panel_b_macro_mean_range.csv"))
    parser.add_argument("--output", type=Path, default=Path("assets/figures/fig3.pdf"))
    draw(parser.parse_args())


if __name__ == "__main__":
    main()
