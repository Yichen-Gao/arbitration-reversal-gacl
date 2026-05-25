#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/component_diagnostic.csv results/expected_component_table.csv
printf 'wrote results/expected_component_table.csv\n'
