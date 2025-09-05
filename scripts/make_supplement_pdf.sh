#!/usr/bin/env bash
set -euo pipefail
# Requires pdflatex in your PATH.
pdflatex -interaction=nonstopmode manuscript/cover_ehj_digital_health.tex
echo "Cover page compiled to cover_ehj_digital_health.pdf"
