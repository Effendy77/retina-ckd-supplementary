# Chapter 4 – Temporal and Longitudinal Validation

This directory contains the validation analyses for Chapter 4.

## Structure

01_temporal_validation/
    Instance 1 temporal validation scripts and outputs.

02_longitudinal_analysis/
    Matched baseline–repeat assessment analyses.

03_figures/
    Main and supplementary figures.

04_tables/
    Main and supplementary tables.

supplementary_materials/
    Full statistical outputs and extended results.

frozen_model_instance0_final/
    Locked model weights and preprocessing config used for validation.

## Leakage Prevention Protocol

- Model weights are frozen.
- No retraining is permitted.
- Normalization parameters remain unchanged.
- All validation is performed strictly via inference.
