# SARS-CoV inhibition

This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2. It predicts the probability that a small molecule inhibits SARS-3CLpro-mediated peptide cleavage. It was developed using a high-throughput screening against the 3CL protease of SARS-CoV1, as no data was yet available for the new virus (SARS-CoV2) causing the COVID-19 pandemic. It uses the ChemProp model.

## Identifiers

* EOS model ID: `eos9f6t`
* Slug: `chemprop-sars-cov-inhibition`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of 3CL protease inhibition (%) The classifier was trained using a threshold of 12% of inhibition 

## References

* [Publication](https://www.sciencedirect.com/science/article/pii/S0092867420301021)
* [Source Code](http://chemprop.csail.mit.edu/checkpoints)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9f6t)

## Citation

If you use this model, please cite the [original authors](https://www.sciencedirect.com/science/article/pii/S0092867420301021) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!