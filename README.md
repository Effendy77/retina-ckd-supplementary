# Retina–CKD Supplementary Materials

**Target journal:** *EHJ Digital Health*  
**Main code repo:** [retina-esrd-survival](https://github.com/Effendy77/retina-esrd-survival)

---

## Overview
This repository contains **supplementary materials** for the manuscript:

> *Retinal Image–Based Survival Prediction of End-Stage Renal Disease: Development and Validation Using UK Biobank and LHCH Cohorts*  
> Effendy Bin Hashim, et al. (2025)

It is designed as a companion to the main pipeline repo (`retina-esrd-survival`), housing **figures, tables, protocols, reporting checklists, and reproducibility manifests**.

---

## Repository Structure

SUPPLEMENTARY.md # Index of all items S1–S8
manifest.json # File hashes & reproducibility metadata
environment.yml # Minimal environment to regenerate figures

figures/ # Auto-generated figures
make_fig_pipeline.py
make_fig_cohort_flow.py
make_fig_calibration.py
make_fig_dca.py
fig_pipeline.pdf
fig_cohort_flow.pdf
...

tables/ # Key tables in CSV and TeX
cv_metrics.csv
reclass_summary.csv
cohort_inclusion_exclusion.csv
kfre_config.yaml
hyperparams.yaml

protocols/ # Cohort, KFRE, LHCH protocols
ukb_esrd_labels.md
kfre_methods.md
lhch_synopsis.md
lhch_sap.md
lhch_site_checklist.md

checklists/ # Reporting guidelines
tripod_ai_checklist.md
strobe_checklist.md

manuscript/ # LaTeX templates for supplement
cover_ehj_digital_health.tex
main.tex
supplementary.tex

scripts/ # Build scripts
build_all.sh
update_manifest.py
make_supplement_pdf.sh

references/ # BibTeX + PDF placeholders
refs.bib
pdfs/


---

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/Effendy77/retina-ckd-supplementary.git
cd retina-ckd-supplementary


2. Set up environment

conda env create -f environment.yml
conda activate retina-ckd-suppl

3. Rebuild all figures & update manifest

bash scripts/build_all.sh

This regenerates pipeline/cohort flow diagrams and updates manifest.json with SHA256 hashes for all supplementary outputs.

4. Generate cover page PDF (optional)

bash scripts/make_supplement_pdf.sh

Requires pdflatex in your PATH.

Cross-links

Code & model training: retina-esrd-survival

Auto-generated figures and results: results/figures/
 in the main repo

Model checkpoints: checkpoints/

Citation

If you use these supplementary materials, please cite:

@misc{hashim2025retinackdsuppl,
  author       = {Effendy Bin Hashim},
  title        = {Retina–CKD Supplementary Materials},
  year         = {2025},
  howpublished = {GitHub},
  url          = {https://github.com/Effendy77/retina-ckd-supplementary}
}

And also cite the main paper once published.

License

MIT License © 2025 Effendy Bin Hashim

