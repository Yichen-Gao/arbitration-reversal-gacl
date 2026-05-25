#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=. python scripts/mc2_g2_from_cached.py "$@"
