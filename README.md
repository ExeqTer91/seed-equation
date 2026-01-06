# The Seed Equation: EEG Alpha/Theta Analysis

Supporting code and data for the manuscript:
**"The Seed Equation: A Unified φ Framework for Neural Frequency Architecture"**

## Overview

This repository contains analysis code for testing whether the golden ratio (φ ≈ 1.618) 
serves as a neural set-point for α/θ EEG power ratios.

## Key Findings

- REST α/θ = 2.19 ± 1.50
- TASK α/θ = 1.13 ± 0.67  
- Midpoint = 1.66 (2.5% from φ)
- State separation: Cohens d = 0.93

## Datasets

- **Primary:** PhysioNet EEGBCI (https://physionet.org/content/eegmmidb/1.0.0/)
- **Cross-validation:** OpenNeuro ds003969 (https://openneuro.org/datasets/ds003969)

## Data Files Description

| File | Contents |
|------|----------|
| findings_complete.npz | All primary results (N=51) |
| finding5_n50.npz | Sensitivity analysis subset |
| findings_n109.npz | Extended sample before exclusions |
| phi_attractor_tests.npz | TOST and Bayesian equivalence results |
| within_subject_results.npz | Paired REST-TASK comparisons |
| zone_transitions.npz | McNemar-Bowker transition matrix |

## Statistical Methods

- Paired t-test + Wilcoxon signed-rank
- TOST equivalence (margin ±0.30)
- Bayesian BF10 (Cauchy prior, scale=0.707)
- RM-ANOVA with Greenhouse-Geisser

## License

MIT License
