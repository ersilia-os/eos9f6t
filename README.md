# Inhibition of SARS-CoV 3CL protease

This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2. It predicts the probability that a small molecule inhibits SARS-3CLpro-mediated peptide cleavage. It was developed using a high-throughput screening against the 3CL protease of SARS-CoV1, as no data was yet available for the new virus (SARS-CoV2) causing the COVID-19 pandemic. 

## Summary
* Predicts **protease inhibitory** activity of small molecules
* The training set includes **>25,000** molecules
* The **high-throughput assay** measured the inhibitory activity of small molecules(at 300uM) against recombinant SARS-3CLpro(at 150nM) by using a FRET-quenched fluorescent       SARS-3CLpro substrate (at 2uM) that emitted fluorescence when cleaved by 3CLpro. 
* The assay is recorded in PubChem [AID1706](https://pubchem.ncbi.nlm.nih.gov/bioassay/1706#section=Protocol)
* Processed **data** can be downloaded [here](https://github.com/yangkevin2/coronavirus_data/blob/master/data/AID1706_binarized_sars.csv)

## Specifications
* Input: SMILES string
* Endpoint: 3CL protease inhibitory activity (0-1 score)
* Results interpretation:
    * Active compounds: 0.15 - 1
    * Inactive compounds: 0 - 0.15

## History
1. Model was downloaded on 29.04/2021 from [Chemprop](http://chemprop.csail.mit.edu/checkpoints)
2. We duplicated predict.py and scripts/save_features.py scripts from chemprop GitHub repository.
3. Model was incorporated to Ersilia on 29/04/2021.
