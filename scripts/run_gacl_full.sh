#!/usr/bin/env bash
set -euo pipefail
cat <<'MSG'
Full inference requires the original datasets, downloaded HF checkpoints, and a
model adapter in src/models/load_model.py. The anonymous artifact includes the
cached reproduction path by default:

  bash scripts/run_gacl_cached.sh --limit 20
MSG
