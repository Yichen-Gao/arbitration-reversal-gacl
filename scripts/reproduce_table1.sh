#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python scripts/table1_from_cached.py "$@"
