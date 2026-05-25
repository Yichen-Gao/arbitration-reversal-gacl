"""Margin utilities for repairable arbitration reversal."""
from __future__ import annotations

from typing import Mapping


def two_answer_margin(scores: Mapping[str, float], y_audio: str, y_text: str) -> float:
    return float(scores[y_audio]) - float(scores[y_text])


def repairable_quadrant(m_audio_ref: float, m_joint: float) -> bool:
    return float(m_audio_ref) > 0.0 and float(m_joint) < 0.0


def summarize_margin_rows(rows: list[dict]) -> dict[str, float]:
    n = len(rows)
    if n == 0:
        return {"n": 0}
    return {
        "n": n,
        "conflict_acc": sum(r.get("joint_top1") == r.get("y_a") or r.get("audio_follow") is True for r in rows) / n,
        "text_follow": sum(r.get("joint_top1") == r.get("y_t") or r.get("text_follow") is True for r in rows) / n,
        "audio_ref_acc": sum(r.get("audio_top1") == r.get("y_a") for r in rows if "audio_top1" in r) / n,
        "repairable_quadrant": sum(bool(r.get("repairable_quadrant", False)) or (float(r.get("M_A", r.get("M_A_oracle", 0))) > 0 and float(r.get("M_J", r.get("M_J_oracle", 0))) < 0) for r in rows) / n,
    }
