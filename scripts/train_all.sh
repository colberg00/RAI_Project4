#!/usr/bin/env bash
# Train the CBM with all three regimes using the same config.
set -euo pipefail
CONFIG=${1:-configs/default.yaml}
for regime in independent sequential joint; do
  python -m cbm.train --config "$CONFIG" --regime "$regime"
done
