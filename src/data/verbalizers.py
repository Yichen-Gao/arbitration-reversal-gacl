"""Task candidate sets used in the paper."""
from __future__ import annotations

TASK_CANDIDATES = {
    "aqa": ["yes", "no"],
    "vsc": ["Laughter", "Sigh", "Cough", "Throat clearing", "Sneeze", "Sniff"],
    "ser": ["sad", "happy", "fearful", "angry", "surprised", "disgusted", "neutral"],
    "alme": ["A", "B"],
}


def candidates_for_task(task: str) -> list[str]:
    key = task.lower().replace("mcr-", "").replace("alme-english", "alme")
    if key not in TASK_CANDIDATES:
        raise KeyError(f"unknown task: {task}")
    return TASK_CANDIDATES[key]
