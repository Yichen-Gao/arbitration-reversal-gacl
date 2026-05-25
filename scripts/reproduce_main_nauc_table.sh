#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/main_nauc_results.csv results/expected_main_nauc_table.csv
printf 'wrote results/expected_main_nauc_table.csv\n'
