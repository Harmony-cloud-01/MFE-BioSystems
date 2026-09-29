# MFE-BioSystems

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23035214.svg)](https://doi.org/10.5281/zenodo.23035214)

Archival and supporting materials for:

**Magnetic-Field Confinement Regularisation for Biomedical Electromagnetic Systems**

Paul D. Markov  
*Journal of Computer Science and Engineering Research (JCSER)*, Volume 3, Issue 1, pp. 31-37, 2026.  
DOI: [10.64820/AEPJCSER.31.31.37.62026](https://doi.org/10.64820/AEPJCSER.31.31.37.62026)

## Important correction

The article's Data and Code Availability section printed an incorrect, unaffiliated GitHub address:

`https://github.com/Harmony-Research/MFE-BioSystems`

The correct author-controlled repository is:

`https://github.com/Harmony-cloud-01/MFE-BioSystems`

## Archived release

Release `v1.0.0`, containing the supporting materials documented in this repository, is permanently archived on Zenodo:

[https://doi.org/10.5281/zenodo.23035214](https://doi.org/10.5281/zenodo.23035214)

Use this version-specific DOI when citing the exact archive associated with the published paper.

## Repository status

This is an archival recovery, not a complete reproduction package. Review of the surviving project files found three illustrative Python listings embedded in an early manuscript, several final figure images, and the numerical values printed in the article. The original online notebook execution, raw finite-element outputs, COMSOL models, and FEniCSx implementation were not retained in the available archive.

See [docs/PROVENANCE.md](docs/PROVENANCE.md) for the full provenance and reproducibility statement.

## Contents

- `illustrative_models/` - recovered pedagogical Python examples from an early manuscript appendix.
- `data/published_values.csv` - values transcribed from the published text and table; not raw simulation data.
- `published_figures/` - surviving figure files from the manuscript archive.
- `docs/PROVENANCE.md` - what was recovered, what is missing, and how the materials may be interpreted.
- `CITATION.cff` - citation metadata for the archived software and published article.

## Running the illustrative models

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python illustrative_models/mri_field_homogenization.py
python illustrative_models/resonance_harmonics.py
python illustrative_models/biofield_coupling_interface.py
```

The scripts write PNG images to the current working directory. They were recovered from manuscript source and test-run during repository preparation. They do **not** reproduce the article's COMSOL/FEniCSx quantitative analyses.

The standalone `simulate_tmf_efficiency.py` found elsewhere in the archive was excluded because it concerns a different plasma-efficiency study and does not generate this paper's biomedical results.

## Scientific scope

The article considers a phenomenological resonance-confinement regularisation for passive magnetic-field shaping in heterogeneous, lossy biomedical media. The work is computational and does not report clinical testing, physical phantom validation, or a medical-device implementation.

## Citation

For the published paper:

> P. D. Markov, "Magnetic-Field Confinement Regularisation for Biomedical Electromagnetic Systems," *Journal of Computer Science and Engineering Research (JCSER)*, vol. 3, no. 1, pp. 31-37, 2026. https://doi.org/10.64820/AEPJCSER.31.31.37.62026

For the exact archived supporting-materials release:

> P. D. Markov, *MFE-BioSystems: Supporting materials for Magnetic-Field Confinement Regularisation for Biomedical Electromagnetic Systems*, v1.0.0, Zenodo, 2026. https://doi.org/10.5281/zenodo.23035214

## Contact

Paul D. Markov  
Harmony Research Initiative, Adelaide, Australia  
paul@harmonyonline.org

## Licence

The recovered supporting software is released under the [MIT License](LICENSE). The published article remains subject to the publication licence stated by JCSER.
