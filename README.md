# Inhibition of SARS-CoV 3CL protease

This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2. It predicts the probability that a small molecule inhibits SARS-3CLpro-mediated peptide cleavage. It was developed using a high-throughput screening against the 3CL protease of SARS-CoV1, as no data was yet available for the new virus (SARS-CoV2) causing the COVID-19 pandemic. 

## Summary
* Predicts **protease inhibitory** activity of small molecules
* The training set includes **>25,000** molecules (406 active hits)
* The **high-throughput assay** measured the inhibitory activity of small molecules against recombinant SARS-3CLpro by using a FRET-quenched fluorescent SARS-3CLpro substrate     that emitted fluorescence when cleaved. 
* The assay is recorded in PubChem [AID1706](https://pubchem.ncbi.nlm.nih.gov/bioassay/1706#section=Protocol)
* Processed **data** can be downloaded [here](https://github.com/yangkevin2/coronavirus_data/blob/master/data/AID1706_binarized_sars.csv)

## Specifications
* Input: SMILES string (also accepts an InChIKey string or a molecule name string, and converts them to SMILES) 
* Endpoint: 3CL protease inhibitory activity (0: inactive -1: active)
* Results interpretation:
    * 70% of the original active compounds in the assay score >0.5 with the SARS-Balanced model
    * 3CL protease retains 96% homology between SARS-CoV1 and SARS-CoV2, so results are highly extrapolable.

## History
1. Model was downloaded on 29.04/2021 from [Chemprop](http://chemprop.csail.mit.edu/checkpoints)
2. We duplicated predict.py and scripts/save_features.py scripts from chemprop GitHub repository.
3. Model was incorporated to Ersilia on 29/04/2021.
