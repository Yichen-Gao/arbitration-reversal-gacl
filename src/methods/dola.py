"""Minimal DoLa-style layer-contrast helper.

DoLa contrasts logits from a mature (late) layer against a premature (early)
layer. The paper uses DoLa only as a one-cell sanity check; this helper exposes
that contrastive scoring form for reproducibility scripts.
"""
from __future__ import annotations

import math
from typing import Mapping

from .gacl import argmax_label


def _log_softmax(scores: Mapping[str, float]) -> dict[str, float]:
    m = max(float(v) for v in scores.values())
    z = m + math.log(sum(math.exp(float(v) - m) for v in scores.values()))
    return {k: float(v) - z for k, v in scores.items()}


def dola_scores(late_layer_scores: Mapping[str, float], early_layer_scores: Mapping[str, float], alpha: float = 1.0) -> dict[str, float]:
    labels = sorted(set(late_layer_scores) & set(early_layer_scores))
    late = _log_softmax({k: late_layer_scores[k] for k in labels})
    early = _log_softmax({k: early_layer_scores[k] for k in labels})
    return {label: late[label] + float(alpha) * (late[label] - early[label]) for label in labels}


def dola_prediction(late_layer_scores: Mapping[str, float], early_layer_scores: Mapping[str, float], alpha: float = 1.0) -> str:
    return argmax_label(dola_scores(late_layer_scores, early_layer_scores, alpha))
