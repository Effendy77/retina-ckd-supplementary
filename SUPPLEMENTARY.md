# Supplementary Materials Index

## S1. Cohort Curation and Outcomes
- **S1.1 UK Biobank retina–CKD cohort flow diagram** — `figures/fig_cohort_flow.pdf`; script: `figures/make_fig_cohort_flow.py`.
- **S1.2 ESRD label derivation (time/event)** — pipeline summary `protocols/ukb_esrd_labels.md`.
- **S1.3 Inclusion/Exclusion** — CSV template `tables/cohort_inclusion_exclusion.csv`.

## S2. Model Development
- **S2.1 RETFound encoder & DeepSurv head** — brief schematic `figures/fig_pipeline.pdf`; script: `figures/make_fig_pipeline.py`.
- **S2.2 Hyperparameters & training schedule** — `tables/hyperparams.yaml`.

## S3. Evaluation
- **S3.1 Internal CV metrics (C-index, IBS)** — `tables/cv_metrics.csv` + `tables/cv_metrics.tex`.
- **S3.2 Time-dependent AUC & calibration** — `figures/fig_calibration_2y_5y.pdf` (script: `figures/make_fig_calibration.py`).
- **S3.3 Decision Curve Analysis (2y, 5y)** — `figures/fig_dca.pdf` (script: `figures/make_fig_dca.py`).
- **S3.4 Reclassification vs KFRE (NRI/IDI)** — `tables/reclass_summary.csv` + `figures/fig_reclass.pdf`.

## S4. Comparators
- **S4.1 KFRE 4‑var & 8‑var** — method note `protocols/kfre_methods.md`; config `tables/kfre_config.yaml`.
- **S4.2 KFRE + biomarker change** — summary note `protocols/kfre_biomarker_change_note.md`.

## S5. Interpretability
- **S5.1 Grad‑CAM casebook** — `figures/fig_gradcam_panel.pdf` with legend `figures/gradcam_legend.md`.

## S6. Prospective External Validation (LHCH)
- **S6.1 Protocol synopsis** — `protocols/lhch_synopsis.md`.
- **S6.2 Site checklist** — `protocols/lhch_site_checklist.md`.
- **S6.3 Statistical analysis plan (SAP)** — `protocols/lhch_sap.md`.

## S7. Reporting Checklists
- **TRIPOD‑AI** — `checklists/tripod_ai_checklist.md`
- **STROBE** — `checklists/strobe_checklist.md`

## S8. Reproducibility
- **Manifest of generated figures/tables** — `manifest.json` (hashes & seeds).
- **Environment** — `environment.yml`

## References
- `references/refs.bib` (cite these in LaTeX).
- PDFs to be placed under `references/pdfs/` (do not commit copyrighted files unless licensed).


---

## Cross-links to Main Code Repo Artifacts
This supplement references outputs produced by the training/evaluation code in the main repository:
- **Predictions & metrics CSVs**: `https://github.com/Effendy77/retina-esrd-survival/tree/main/results`
- **Auto-generated figures**: `https://github.com/Effendy77/retina-esrd-survival/tree/main/results/figures`
- **Model checkpoints**: `https://github.com/Effendy77/retina-esrd-survival/tree/main/checkpoints` (hashes recorded in this supplement's `manifest.json`).

> If your repo uses different paths/branch names, update the links above accordingly.
