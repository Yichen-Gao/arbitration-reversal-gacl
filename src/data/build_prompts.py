"""Prompt builders for full reproduction runs.

The cached path does not call these functions. Full model reproduction can use
these templates after downloading the original benchmark manifests.
"""
from __future__ import annotations


def build_joint_prompt(question: str, conflict_text: str, candidates: list[str]) -> str:
    opts = ", ".join(candidates)
    return f"Question: {question}\nText evidence: {conflict_text}\nCandidates: {opts}\nAnswer with one candidate."


def build_audio_reference_prompt(question: str, candidates: list[str]) -> str:
    opts = ", ".join(candidates)
    return f"Question: {question}\nCandidates: {opts}\nAnswer with one candidate."
