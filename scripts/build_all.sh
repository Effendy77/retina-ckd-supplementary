#!/usr/bin/env bash
set -euo pipefail
# 1) Generate figures
python figures/make_fig_pipeline.py
python figures/make_fig_cohort_flow.py
# Placeholders for when you wire in evaluation outputs:
# python figures/make_fig_calibration.py
# python figures/make_fig_dca.py
# 2) Update manifest hashes
python scripts/update_manifest.py
echo "Done. Figures generated and manifest.json updated."
