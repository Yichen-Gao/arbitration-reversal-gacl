#!/usr/bin/env bash
set -euo pipefail
cat <<'MSG'
Download ALME-English from its official release page, then place or symlink the
processed manifest/audio tree under data/raw/alme/. This artifact intentionally
does not mirror raw benchmark audio.
MSG
