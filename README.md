# Mammal Diversification
### Refer to biodiversity_analysis_by_epochs.ipynb for comprehensive analyses of causes in change of biodiversity by time periods
### Refer to taxa_analysis.ipynb for analyses of changes in biodiversity over time of various mammalian/reptilian taxa
### Refer to correlation_analysis.ipynb for analyses of correlation measures of mammals/reptiles and mean surface temperature

## Overview

This repository is dedicated to the study of mammal diversification throughout geological periods in the Cenozoic Era (66 MYA to present), with a focus on understanding how climate change has influenced the evolution and diversity of mammal species. It aims to answer the question: "Does temperature fluctuations in the Cenozoic Era affects the growth and diversification of mammals?"

## Structure

The repository is organized into several key directories:

- `correlation/`: Contains Python scripts for calculating correlations between mammal and reptile diversification and climate changes.
- `data/`: This directory is divided into `raw/` for unprocessed data and `processed/` for data that has been cleaned and formatted for analysis. It includes climate data and taxon diversity data for mammals, reptiles, and other animals.
- `interpolation/`: Scripts for interpolating missing data points in the diversity records.
- `model/`: Contains models developed to predict diversification patterns based on various factors.
- `processing/`: Scripts for processing raw data into a format suitable for analysis.
- `visualize/`: Visualization scripts for generating graphs and charts to illustrate the findings.

## Methodology
1. **Data Collection and Processing**: Aggregating and cleaning data from multiple sources to create a unified dataset focusing on mammalian taxa.
2. **Taxonomic Group Analysis**: Separating data into distinct taxonomic groups, such as Artiodactyla, Carnivora, and others, to facilitate detailed analyses.
3. **Time-Series Visualization**: Employing Python’s Matplotlib and Pandas libraries to plot the diversity of these groups across geological epochs.
4. **Environmental Correlation**: Integrating climate data to explore correlations between mammalian diversity and changes in global temperature.

## Data Sources
Our analysis is grounded in data extracted from:
- The Paleobiology Database (PBDB): Provides extensive fossil records that serve as the foundation for our evolutionary timelines.
- CENOGRID (Cenozoic Global Reference Stratigraphic Scale and Time Scale): A comprehensive dataset offering detailed global climate data over the Cenozoic era. It includes information on temperature fluctuations, sea levels, and other climatic factors.
