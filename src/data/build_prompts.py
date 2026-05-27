"""Prompt builders for full reproduction runs.

The cached path uses stored scores. Full model reproduction can use these
builders after downloading the original benchmark manifests.

Free-form builders intentionally do not add candidate lists or short-label
output constraints.
"""
from __future__ import annotations

PROMPT_VARIANT_SUFFIXES = {
    "original": "",
    "audio_priority": "Prioritize the audio evidence when the text and audio disagree.",
    "ignore_text": "Ignore the textual description and answer from the audio.",
    "bias_awareness": "The textual description may be unreliable. Check whether it conflicts with the audio before answering.",
    "chain_of_thought": "Think briefly about the audio and text evidence, then give the final answer only.",
}


def _append_suffix(prompt: str, suffix: str = "") -> str:
    suffix = suffix.strip()
    return prompt.rstrip() if not suffix else f"{prompt.rstrip()}\n{suffix}"


def build_joint_prompt(question: str, conflict_text: str, candidates: list[str]) -> str:
    opts = ", ".join(candidates)
    return f"Question: {question}\nText evidence: {conflict_text}\nCandidates: {opts}\nAnswer with one candidate."


def build_audio_reference_prompt(question: str, candidates: list[str]) -> str:
    opts = ", ".join(candidates)
    return f"Question: {question}\nCandidates: {opts}\nAnswer with one candidate."


def build_free_form_joint_prompt(question: str, conflict_text: str, variant: str = "original") -> str:
    prompt = f"{question}\nText evidence: {conflict_text}"
    return _append_suffix(prompt, PROMPT_VARIANT_SUFFIXES.get(variant, ""))


def build_free_form_audio_reference_prompt(question: str, variant: str = "original") -> str:
    return _append_suffix(question, PROMPT_VARIANT_SUFFIXES.get(variant, ""))


def build_prompt_intervention(prompt: str, variant: str) -> str:
    return _append_suffix(prompt, PROMPT_VARIANT_SUFFIXES.get(variant, ""))
