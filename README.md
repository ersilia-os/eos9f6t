# Inhibition of SARS-CoV 3CL protease

The developers of this model used data from a high-throughput screening against the 3CL protease of SARS-CoV1 to predict the probability that a new compound will inhibit the enzyme activity. This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2.

## Summary
* Predicts **protease inhibitory** activity of small molecules
* Trained with _in vitro_ data against SARS-CoV1 3CL protease extract
* Based on **>25,000** datapoints
* The Assay is recorded in PubChem [AID1706](https://pubchem.ncbi.nlm.nih.gov/bioassay/1706#section=Protocol)
* Processed data can be downloaded [here](https://github.com/yangkevin2/coronavirus_data/blob/master/data/AID1706_binarized_sars.csv)

## Specifications
* Input: SMILES string
* Endpoint: probability of 3CL protease inhibitory activity (0-1)

## History
1. We duplicated predict.py and scripts/save_features.py scripts from chemprop GitHub repository.
2. Model was incorporated to Ersilia on 29/04/2021.
