#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-data/raw/alme}"
mkdir -p "$ROOT"

cat <<MSG
ALME upstream:
  Repository:       https://github.com/jb1999/alme-benchmark
  Common Voice 22:  https://commonvoice.mozilla.org/en/datasets

Suggested layout:
  ${ROOT}/alme-benchmark/
  data/raw/common_voice/cv-corpus-22.0-2025-06-20/
MSG

if command -v git >/dev/null 2>&1 && [ ! -d "${ROOT}/alme-benchmark/.git" ]; then
  git clone https://github.com/jb1999/alme-benchmark.git "${ROOT}/alme-benchmark"
fi

cat <<'MSG'
Download Common Voice Corpus 22.0 from Mozilla Common Voice and place/extract it under:
  data/raw/common_voice/cv-corpus-22.0-2025-06-20/

MSG
