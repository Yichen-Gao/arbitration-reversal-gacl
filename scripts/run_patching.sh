#!/usr/bin/env bash
set -euo pipefail
cat <<'MSG'
Activation patching is optional/heavy. Cached patch summaries are provided in
cached/patch_results/ and can redraw the mechanism bridge with:

  bash scripts/reproduce_fig3.sh --cached
MSG
