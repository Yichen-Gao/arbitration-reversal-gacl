#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m src.plotting.plot_fig2_margins "$@"
