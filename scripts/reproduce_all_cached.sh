#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
bash scripts/reproduce_table1.sh --cached
bash scripts/reproduce_fig2.sh --cached
bash scripts/reproduce_main_nauc_table.sh
bash scripts/reproduce_table3.sh --cached
bash scripts/reproduce_fig5.sh --cached
bash scripts/reproduce_table2.sh --cached
bash scripts/reproduce_fig3.sh --cached
bash scripts/reproduce_component_table.sh
bash scripts/reproduce_sft_table.sh
bash scripts/reproduce_mc2_table.sh
bash scripts/reproduce_gate_proxy_table.sh
bash scripts/reproduce_baselines.sh
