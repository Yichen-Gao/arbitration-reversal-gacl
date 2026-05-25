"""Minimal paper-facing implementation of GACL.

The functions in this module mirror the equations in the paper: compute the
observable disagreement gate, compute reference reliability, and interpolate
joint scores toward the same-audio reference without extrapolating past it.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class GACLConfig:
    lambda_value: float = 1.0
    tau_A: float = 0.5
    alpha_max: float = 1.0


def clip(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(value)))


def argmax_label(scores: Mapping[str, float]) -> str:
    if not scores:
        raise ValueError("scores must contain at least one candidate")
    return max(scores, key=lambda key: float(scores[key]))


def disagreement_gate(joint_answer: str | None, ref_answer: str | None) -> int:
    """N_out: correction is considered only when the reference is valid and differs."""
    return int(ref_answer is not None and ref_answer != "" and ref_answer != joint_answer)


def reference_reliability(ref_scores: Mapping[str, float], ref_answer: str | None, tau_A: float) -> float:
    """R_A: clipped reference margin between the reference answer and its runner-up."""
    if ref_answer is None or ref_answer not in ref_scores or len(ref_scores) < 2:
        return 0.0
    competitors = [float(v) for k, v in ref_scores.items() if k != ref_answer]
    if not competitors:
        return 0.0
    margin = float(ref_scores[ref_answer]) - max(competitors)
    if tau_A <= 0:
        return float(margin > 0)
    return clip(margin / float(tau_A), 0.0, 1.0)


def gacl_alpha(joint_answer: str | None, ref_answer: str | None, ref_scores: Mapping[str, float], config: GACLConfig) -> float:
    n_out = disagreement_gate(joint_answer, ref_answer)
    r_a = reference_reliability(ref_scores, ref_answer, config.tau_A)
    return clip(config.lambda_value * r_a * n_out, 0.0, config.alpha_max)


def interpolate_scores(joint_scores: Mapping[str, float], ref_scores: Mapping[str, float], alpha: float) -> dict[str, float]:
    """Return s_J + alpha * (s_A - s_J) for the shared candidate set."""
    labels = sorted(set(joint_scores) & set(ref_scores))
    if not labels:
        raise ValueError("joint and reference scores must share candidates")
    return {label: float(joint_scores[label]) + float(alpha) * (float(ref_scores[label]) - float(joint_scores[label])) for label in labels}


def apply_gacl(joint_scores: Mapping[str, float], ref_scores: Mapping[str, float], config: GACLConfig) -> dict[str, object]:
    joint_answer = argmax_label(joint_scores)
    ref_answer = argmax_label(ref_scores)
    n_out = disagreement_gate(joint_answer, ref_answer)
    r_a = reference_reliability(ref_scores, ref_answer, config.tau_A)
    alpha = clip(config.lambda_value * r_a * n_out, 0.0, config.alpha_max)
    scores = interpolate_scores(joint_scores, ref_scores, alpha)
    return {
        "joint_answer": joint_answer,
        "reference_answer": ref_answer,
        "gacl_answer": argmax_label(scores),
        "N_out": n_out,
        "R_A": r_a,
        "alpha": alpha,
        "scores": scores,
    }


def scores_from_row(row: Mapping[str, object], labels: Sequence[str] | None = None) -> tuple[dict[str, float], dict[str, float]]:
    """Convert a cached candidate-score row into joint/reference score dicts."""
    labels = list(labels or row.get("candidate_labels") or [])
    z_j = row.get("z_J") or row.get("scores_joint")
    z_a = row.get("z_A") or row.get("scores_ref") or row.get("scores_audio_ref")
    if not labels or z_j is None or z_a is None:
        raise ValueError("row must provide candidate_labels plus z_J and z_A scores")
    return {str(k): float(v) for k, v in zip(labels, z_j)}, {str(k): float(v) for k, v in zip(labels, z_a)}
