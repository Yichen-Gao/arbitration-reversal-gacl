#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/sft_comparison.csv results/expected_sft_table.csv
printf 'wrote results/expected_sft_table.csv\n'
