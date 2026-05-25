#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/patch_results/table2_site_localization.csv results/expected_table2.csv
printf 'wrote results/expected_table2.csv\n'
