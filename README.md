# retina-ckd-supplementary

## Supplementary materials: Retinal vascular feature extraction and selection for kidney outcome prediction

This repository contains the **supplementary methods, figures, and tables** supporting the extraction, exploratory analysis, and **outcome-agnostic selection** of handcrafted retinal vascular features used across kidney-related prediction studies, including:

- **eGFR regression**
- **ESRD risk and survival modelling**

The materials in this repository correspond to **Supplementary Methods S1** and **Supplementary Figures S1–S5** of the associated manuscripts.

---

## Scope and purpose

The purpose of this repository is to provide **transparent and reproducible documentation** of the retinal vascular feature engineering pipeline used prior to predictive modelling.

All analyses presented here were conducted **independently of outcome labels** and **before model training**, and therefore apply equally across downstream tasks.

This repository **does not contain model training, prediction, or performance evaluation code**.

---

## Retinal vascular features

An initial set of handcrafted retinal vascular features was extracted from automated vessel segmentations derived from colour fundus photographs. These features were designed to capture complementary aspects of retinal microvascular architecture, including:

- Global vascular extent  
- Vessel calibre  
- Network complexity  
- Geometric morphology  

A redundancy-aware exploratory data analysis (EDA) was performed to assess feature distributions, multicollinearity, and latent structure.

---

## Outcome-agnostic feature selection

Feature selection was conducted using an **outcome-agnostic strategy**, defined here as selection based exclusively on:

- Distributional properties (e.g. skewness, stability after transformation)  
- Correlation structure and redundancy  
- Biological interpretability of distinct vascular domains  

without incorporating information from kidney outcomes (eGFR, ESRD, or related endpoints).

Highly collinear features representing overlapping constructs (e.g. multiple proxies of vessel size or extent) were not retained simultaneously.

Based on this analysis, a parsimonious subset of **four retinal vascular features** was selected for downstream modelling:

- **Vessel density** – global vascular extent / perfusion  
- **Mean vessel width** – vessel calibre  
- **Fractal dimension** – network complexity  
- **Eccentricity** – global vascular geometry  

These features capture complementary biological dimensions while minimising redundancy and improving interpretability.

---

## Exploratory analyses included

The supplementary materials include the following diagnostic analyses:

- Correlation heatmap of all extracted retinal vascular features  
- Distributional assessment using boxplots and histograms  
- Raw vs log-transformed feature distributions  
- Principal component analysis (PCA), including:
  - Explained variance across components  
  - Two-dimensional projection (PC1 vs PC2)  

PCA was used **solely as a diagnostic tool** to assess latent structure and redundancy and **was not used for feature extraction, transformation, or model training**.

---

## Repository contents
├── figures/
│ ├── Fig_S1_correlation_heatmap.png
│ ├── Fig_S2_boxplots_raw_features.png
│ ├── Fig_S3a_raw_distributions.png
│ ├── Fig_S3b_log_transformed_distributions.png
│ ├── Fig_S4_PCA_explained_variance.png
│ └── Fig_S5_PCA_projection_ESRD.png
│
├── tables/
│ ├── Table_S1_feature_selection_rationale.csv
│ └── Table_S2_retained_features.csv
│
├── Supplementary_Methods_S1.pdf
└── README.md

File names may vary slightly depending on journal formatting requirements.

---

## Relationship to modelling repositories

This repository documents **feature engineering and selection only**.

Model development, training, and evaluation are implemented separately in project-specific repositories (e.g. eGFR regression or ESRD survival modelling pipelines), which reference this repository for feature definitions and selection rationale.

---
### Related repository: feature extraction code

The retinal vascular features documented in this repository were generated using automated pipelines implemented in the companion code repository:

👉 **https://github.com/Effendy77/Retinal-Feature-Extract-CKD**

That repository contains the scripts for vessel segmentation, feature computation, and data preprocessing. The present repository focuses exclusively on **methodological justification, exploratory diagnostics, and outcome-agnostic feature selection**.

## Citation

If you use or reference these materials, please cite the associated manuscript(s) and this repository as supplementary material.

A formal citation entry (DOI or Zenodo record) will be added upon publication.

---

## Notes

- This repository supersedes earlier internal exploratory documents and reflects the **final, submission-ready supplementary methods**.
- Figures showing outcome stratification are presented for **post-hoc interpretability only** and were **not used to inform feature selection**.

---

## Maintainer

**Effendy Bin Hashim**  
Department of Eye and Vision Science  
Institute of Life Course and Medical Sciences  
University of Liverpool

