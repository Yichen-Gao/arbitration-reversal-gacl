#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/aad_acd_selected_results.csv results/expected_aad_acd_selected_results.csv
printf 'wrote results/expected_aad_acd_selected_results.csv\n'
cat <<'MSG'
AAD and ACD selected operating points are reproduced from cached rows. Full
inference uses the same candidate-scoring interface with no-audio (AAD) and
perturbed-audio (ACD) references; see src/methods/baselines.py.
MSG
