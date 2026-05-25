#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/aad_acd_selected_results.csv results/expected_aad_acd_selected_results.csv
cp cached/scores/dola_sanity.csv results/expected_dola_sanity.csv
printf 'wrote results/expected_aad_acd_selected_results.csv\n'
printf 'wrote results/expected_dola_sanity.csv\n'
