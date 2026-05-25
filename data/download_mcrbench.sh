#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-data/raw/mcrbench}"
ARCHIVE="MCR-Bench.zip"
DRIVE_ID="1nXJCx8Neqdm0WMfe9Uq6sX2bvk_3FWUG"

mkdir -p "$ROOT"
cat <<MSG
MCR-Bench upstream:
  Repository: https://github.com/WangCheng0116/MCR-BENCH
  Data:       https://drive.google.com/file/d/${DRIVE_ID}/view?usp=sharing

Target directory:
  ${ROOT}
MSG

if command -v gdown >/dev/null 2>&1; then
  echo "Downloading with gdown..."
  gdown "https://drive.google.com/uc?id=${DRIVE_ID}" -O "${ROOT}/${ARCHIVE}"
  echo "Archive written to ${ROOT}/${ARCHIVE}"
else
  cat <<MSG

gdown is not installed. Install it with:
  pip install gdown

Then run:
  gdown "https://drive.google.com/uc?id=${DRIVE_ID}" -O "${ROOT}/${ARCHIVE}"
  unzip "${ROOT}/${ARCHIVE}" -d "${ROOT}"
MSG
fi
