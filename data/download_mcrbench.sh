#!/usr/bin/env bash
set -euo pipefail
cat <<'MSG'
Download MCR-Bench from its official release page, then place or symlink the
manifest/audio tree under data/raw/mcrbench/. This artifact intentionally does
not mirror raw benchmark audio.
MSG
