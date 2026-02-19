# Pre-Specified Statistical Analysis Plan – Chapter 4 Validation

## Temporal Validation (Instance 1)

Inclusion:
- 21015-1.0 (left eye image)
- 30700-1.0 (creatinine)
- Age and sex available

Outcomes:
- R²
- MAE
- RMSE
- Pearson correlation
- Calibration slope and intercept

Stratified analyses:
- Sex
- Diabetes
- Hypertension
- Age (<60 vs ≥60)

No model recalibration will be performed.

---

## Longitudinal Analysis (Matched Cohort)

Inclusion:
- 21015-0.0 and 21015-1.0 present
- 30700-0.0 and 30700-1.0 present
- Follow-up ≥ 2 years

Primary outcome:
Annualized eGFR change

Primary model:
Decline ~ Predicted_eGFR0 + Age + Sex

Adjusted model:
Decline ~ Predicted_eGFR0 + Age + Sex + Diabetes + Hypertension

Rapid decline definition:
Annual decline < -3 ml/min/1.73m²/year

Interaction tests:
Predicted × Diabetes
Predicted × Hypertension

Thresholds and models are fixed prior to analysis.

