"""Deterministic answer normalization used by cached and full runs."""
from __future__ import annotations

import unicodedata


def normalize_answer(text: str | None, aliases: dict[str, list[str]] | None = None) -> str | None:
    if text is None:
        return None
    normalized = unicodedata.normalize("NFKC", str(text)).strip().strip('"\'`').lower()
    normalized = normalized.rstrip(".!,;:").strip()
    aliases = aliases or {}
    for canonical, names in aliases.items():
        if normalized == canonical.lower() or normalized in {x.lower() for x in names}:
            return canonical
    return normalized or None
