#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-data/raw/mc2}"
mkdir -p "$ROOT"

cat <<MSG
MC2 upstream:
  Hugging Face: https://huggingface.co/datasets/271754echo/MC2

Target directory:
  ${ROOT}
MSG

if command -v huggingface-cli >/dev/null 2>&1; then
  huggingface-cli download 271754echo/MC2 --repo-type dataset --local-dir "$ROOT"
else
  cat <<'MSG'

Install the Hugging Face CLI to download from the command line:
  pip install huggingface_hub
  huggingface-cli download 271754echo/MC2 --repo-type dataset --local-dir data/raw/mc2
MSG
fi
