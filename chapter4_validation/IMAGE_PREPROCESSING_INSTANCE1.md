# Instance 1 (Repeat Assessment) Image Preprocessing

## Purpose
To ensure strict preprocessing symmetry between the baseline cohort (Instance 0, 2006–2010) and the Repeat Assessment cohort (Instance 1, 2012–2013) used for temporal validation.

---

## Source Repository

Image preprocessing was performed using the external repository:

OpenBlackBoxAboutCVD  
Path:  
`OpenBlackBoxAboutCVD/Process_UKBiobank_FundusData/Image_Preprocess/`

GitHub repository:  
https://github.com/NatsuGao7/OpenBlackBoxAboutCVD

Commit hash used:
`146cda1818bb866b7e485cce1034af6c2b5dd59d`

(The commit hash ensures full reproducibility.)

---

## Preprocessing Function

The exact same preprocessing function used for baseline model training was applied:

process_without_gb()

Located in:
fundus_prep.py


This function performs:

- Fundus circular mask detection
- Background removal (black borders)
- Cropping to bounding box
- Re-padding to square
- No intensity normalization
- No histogram equalization
- No CLAHE
- No brightness correction

This ensures geometric and masking consistency without altering pixel intensity distributions.

---

## Output Resolution

All processed images were resized to:



800 × 800 pixels


This matches the preprocessing performed for Instance 0 during model training.

---

## NumPy Compatibility Adjustment

The original preprocessing code contained deprecated usage of:



np.int


Due to removal in NumPy ≥ 1.20, this was replaced with:



int


This modification does **not** alter preprocessing behavior and only ensures compatibility with modern NumPy versions.

No other functional changes were made to the preprocessing pipeline.

---

## Dataset Summary

Raw Instance 1 Images:
`19,309`

Successfully Cleaned Images:
`<TO BE FILLED AFTER CLEANING COMPLETES>`

Cleaned images were saved to:



/mnt/d/DATA/NEW DATA MAY 2025/bilateralclean_instance1


---

## Reproducibility Statement

Instance 1 images were processed using the identical geometric preprocessing pipeline as Instance 0 to eliminate preprocessing-induced domain shift. No retraining or tuning was performed prior to temporal validation.

This ensures methodological rigor and prevents data leakage.
