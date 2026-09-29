# Provenance and reproducibility status

## What was recovered

The publication archive retained:

- the published article and several manuscript versions;
- three Python toy-model listings embedded in an early LaTeX manuscript;
- final PNG figures used during manuscript preparation; and
- numerical values printed in the article text and table.

The files in `illustrative_models/` are verbatim recoveries of those embedded listings, apart from ordinary file extraction. They were executed successfully during repository preparation using Python 3, NumPy, and Matplotlib.

The file `data/published_values.csv` is a transcription of values printed in the article. It is not raw simulation output and must not be treated as an independently generated dataset.

## What was not recovered

The archive did not contain:

- COMSOL Multiphysics model files;
- FEniCSx source code or meshes;
- Colab notebooks or their execution history;
- raw finite-element output;
- per-seed results for the reported repeated simulations;
- source arrays for the final figures;
- statistical-analysis scripts; or
- a preserved computational environment.

Consequently, this repository cannot presently reproduce or independently verify the article's quantitative finite-element results, confidence intervals, hypothesis tests, or reported cross-platform agreement.

## Interpretation of the illustrative models

The recovered scripts are reduced pedagogical models. They illustrate field shaping, resonator overlap, and a conductive interface. They are not substitutes for the absent COMSOL or FEniCSx analyses and do not establish the article's headline quantitative results.

## Future reconstruction

A future clean-room reconstruction should be versioned separately. It should specify all geometries, material properties, boundary conditions, meshes, solver settings, parameter sweeps, random seeds, raw outputs, and statistical procedures. Any reconstructed result should be compared openly with the published values and identified as a new analysis rather than recovery of the original execution.
