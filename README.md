# Effects of Non-Invasive Neuromodulation on Brain-Body Synchronicity in Basketball Athletes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15282796.svg)](https://doi.org/10.5281/zenodo.15282796)

## Author
Danilo Cavalcante Brambila de Barros

## Institution
Universidade Federal do ABC (UFABC)

## Program
Programa de Pós-Graduação em Neurociência e Cognição

## Advisors
- Prof. Dr. Alexandre Hideki Okano (Advisor)
- Prof. Dr. Edgard Morya (Co-Advisor)

## Location
São Bernardo do Campo - SP, Brazil

## Year
2025

## Abstract
This project investigates the effects of non-invasive neuromodulation on brain-body synchrony in basketball athletes. The study employs multiple connectivity metrics to analyze phase synchronization between EEG and ECG signals, with comprehensive statistical analysis and network-based approaches to understand the impact of neuromodulation on neural and physiological processes.

## Keywords
Neuromodulation, EEG-ECG Synchronization, Phase Locking Value (PLV), Phase Lag Index (PLI), Complex Frequency-Phase Locking Metric (CF-PLM), Network Analysis, Graph Theory, Non-parametric Statistics

## Structure
The dissertation is structured into the following chapters:

- **Introduction and Theoretical Foundation**
  - Introduction
  - Objectives
  - Hypotheses
- **Methodology and Processing**
  - Methodology
  - Data Preprocessing
  - Phase Synchronization Analysis Methods
- **Analysis Approaches**
  - Normality Distribution Analysis
  - Non-parametric Statistical Analysis
  - Network Analysis
  - Graph Centrality Analysis
- **Results and Conclusions**
  - Results and Discussions
  - Conclusions and Future Work

## Analysis Methods
This research utilizes three main connectivity metrics to assess brain-body synchronization:

1. **Phase Locking Value (PLV)**: Measures the consistency of phase differences between signals
2. **Phase Lag Index (PLI)**: Quantifies asymmetry in phase difference distribution, robust against volume conduction
3. **Complex Frequency-Phase Locking Metric (CF-PLM)**: A novel approach combining frequency and phase synchronization

Analyses are conducted across multiple frequency bands (Delta, Theta, Alpha, Beta, Gamma) with both EEG-EEG (brain-brain) and EEG-ECG (brain-heart) synchronization evaluated.

## Data Visualization
The project includes extensive visualization outputs organized in the `figs/` directory:
- Connectivity metrics distributions
- Temporal evolution of synchronization 
- Individual athlete analyses
- Network graphs with and without outliers
- Centrality measures (Degree, Betweenness, Eigenvector)

## Code and Reproducibility
This repository contains all materials necessary to reproduce the dissertation:

### Jupyter Notebooks
Three main analysis notebooks are provided in the `codes/` directory:
- `EEG preprocessing and plot examples for synchronicity.ipynb`: Signal preprocessing and visualization
- `EMG processing and EEG-EEG EEG-ECG synchronicity.ipynb`: Connectivity analysis
- `Testing normality and Non-parametrical Synchronicity Statistics.ipynb`: Statistical testing

### Statistical Results
Complete statistical results are available in the `tabelas/` directory, including:
- Descriptive statistics
- Normality tests (Shapiro-Wilk, D'Agostino, Jarque-Bera, Kolmogorov-Smirnov, Lilliefors)
- Non-parametric test results
- Bootstrap analysis results

## How to Compile
To compile the LaTeX document, you can either:

1. Use the provided batch file:
```sh
./compiler.bat
```

2. Or compile manually with:
```sh
pdflatex dissertacao.tex
bibtex dissertacao
pdflatex dissertacao.tex
pdflatex dissertacao.tex
```

## How to Cite
If you use any part of this work, please cite:

Barros, D. C. B. (2025). Effects of Non-Invasive Neuromodulation on Brain-Body Synchronicity in Basketball Athletes. (Master's Thesis). Federal University of ABC, São Bernardo do Campo, SP, Brazil. https://doi.org/10.5281/zenodo.15282796

## Contributions
This research contributes to the understanding of:
- Effects of non-invasive neuromodulation on neural and physiological synchronization
- Methodological approaches for quantifying brain-body connectivity
- Application of network theory to neurophysiological data
- Potential interventions for enhancing athletic performance through neuromodulation

## License
This project is licensed under the MIT License.
