# UKB ESRD Label Derivation
- Inputs: baseline date, ESRD codes (dialysis/transplant), censor date, death date.
- Outcome: `time` (days) and `event` (1/0) derived per eid.
- Censor hierarchy: ESRD > death > last follow-up.
