# SARS-CoV inhibition

This model was developed to support the early efforts in the identification of novel drugs against SARS-CoV2. It predicts the probability that a small molecule inhibits SARS-3CLpro-mediated peptide cleavage. It was developed using a high-throughput screening against the 3CL protease of SARS-CoV1, as no data was yet available for the new virus (SARS-CoV2) causing the COVID-19 pandemic. It uses the ChemProp model.

This model was incorporated on 2021-04-29.


## Information
### Identifiers
- **Ersilia Identifier:** `eos9f6t`
- **Slug:** `chemprop-sars-cov-inhibition`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `COVID-19`
- **Target Organism:** `SARS-CoV-2`
- **Tags:** `COVID19`, `Antiviral activity`, `Sars-CoV-2`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of 3CL protease inhibition (%) The classifier was trained using a threshold of 12% of inhibition 

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| activity | float | high | Probability of inhibiting SARS-CoV-1 |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9f6t](https://hub.docker.com/r/ersiliaos/eos9f6t)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f6t.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9f6t.zip)

### Resource Consumption
- **Model Size (Mb):** `9`
- **Environment Size (Mb):** `5852`
- **Image Size (Mb):** `5743.71`

**Computational Performance (seconds):**
- 10 inputs: `55.57`
- 100 inputs: `54.21`
- 10000 inputs: `-1`

### References
- **Source Code**: [http://chemprop.csail.mit.edu/checkpoints](http://chemprop.csail.mit.edu/checkpoints)
- **Publication**: [https://pubmed.ncbi.nlm.nih.gov/32084340/](https://pubmed.ncbi.nlm.nih.gov/32084340/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9f6t
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9f6t
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
