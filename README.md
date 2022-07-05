# SARS-CoV inhibition

## Model Identifiers
- Slug: chemprop-sars-cov-inhibition
- Ersilia ID: eos9f6t
- Tags: COVID19,	inhibitor,	antiviral

## Model Description
This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2. It predicts the probability that a small molecule inhibits SARS-3CL pro-mediated peptide cleavage. It was developed using a high-throughput screening against the 3CL protease of SARS-CoV1, as no data was yet available for the new virus (SARS-CoV2) causing the COVID-19 pandemic.
- Input: SMILES
- Output: Probability	(Probability of 3CL protease inhibition)
- Model type: Regressiom
- Mode of Training: Pretrained
- Training data: 261,653	https://pubchem.ncbi.nlm.nih.gov/bioassay/1706
- Experimentally validated: No

## Source code
This model was published by National Center for Biotechnology Information. PubChem Bioassay Record for AID 1706, Source: The Scripps Research Institute Molecular Screening Center. https://pubchem.ncbi.nlm.nih.gov/bioassay/1706. Accessed July 5, 2022.
- Code: https://github.com/chemprop/chemprop
- Chedkpoints: http://chemprop.csail.mit.edu/checkpoints

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "chemprop", located at `/model` and licensed under a BSD-3 License

## History
- This model was downloaded on August 01, 2021
- This model was incorporated on September, 01, 2021
