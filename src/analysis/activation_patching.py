"""Optional heavy activation-patching entry point.

This file documents the expected interface. Running it requires model internals,
GPU memory, and downloaded checkpoints; cached patch results are enough to
reproduce the paper figure.
"""
from __future__ import annotations


def run_activation_patching(*args, **kwargs):
    raise NotImplementedError(
        "Activation patching is a heavy optional analysis. See cached/patch_results "
        "and scripts/reproduce_fig3.sh --cached for the low-cost reproduction path."
    )
