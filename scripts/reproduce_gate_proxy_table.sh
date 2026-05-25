#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
cp cached/scores/gate_proxy_fidelity.csv results/expected_gate_proxy_table.csv
printf 'wrote results/expected_gate_proxy_table.csv\n'
