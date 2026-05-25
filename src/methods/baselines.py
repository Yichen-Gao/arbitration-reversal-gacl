"""Minimal contrastive-decoding baseline helpers."""
from __future__ import annotations

from typing import Mapping

from .gacl import argmax_label


def joint_prediction(joint_scores: Mapping[str, float]) -> str:
    return argmax_label(joint_scores)


def contrastive_scores(joint_scores: Mapping[str, float], reference_scores: Mapping[str, float], alpha: float) -> dict[str, float]:
    """Generic AAD/ACD-style score adjustment: s_J + alpha * (s_J - s_ref)."""
    labels = sorted(set(joint_scores) & set(reference_scores))
    return {label: float(joint_scores[label]) + float(alpha) * (float(joint_scores[label]) - float(reference_scores[label])) for label in labels}


def aad_prediction(joint_scores: Mapping[str, float], no_audio_scores: Mapping[str, float], alpha: float) -> str:
    return argmax_label(contrastive_scores(joint_scores, no_audio_scores, alpha))


def acd_prediction(joint_scores: Mapping[str, float], perturbed_audio_scores: Mapping[str, float], alpha: float) -> str:
    """ACD scoring with perturbed-audio reference scores."""
    return argmax_label(contrastive_scores(joint_scores, perturbed_audio_scores, alpha))
