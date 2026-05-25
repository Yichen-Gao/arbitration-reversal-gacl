"""Shared matplotlib style for the reproduction package."""
from __future__ import annotations

import matplotlib.pyplot as plt

PALETTE = {
    "blue": "#0F4D92",
    "orange": "#D55E00",
    "gray": "#C9C9C9",
    "dark": "#333333",
}


def apply_style() -> None:
    plt.rcParams.update({
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 8,
        "axes.labelsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "axes.linewidth": 0.8,
    })
