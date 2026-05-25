#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/dola_sanity.csv results/expected_dola_sanity.csv
cat <<'MSG'
DoLa is included as a one-cell sanity check matching the paper appendix:
Qwen2-Audio-Inst. x VSC decreases conflict accuracy by 5.0 pp. For full DoLa
runs, use src/methods/dola.py with cached or model-produced layer scores.
MSG
