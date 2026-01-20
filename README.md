# Network Biology Analysis

This repository contains tools for analyzing biological networks, focusing on interactions between entities in the Hetionet graph.

## 📁 Repository Contents

- **💻 Source Code** (`src/`)
  - `src/data_loader.py`: Graph loading from SIF/TSV files.
  - `src/analysis.py`: General graph metrics (entity counts, degrees, similarity).
  - `src/disease_case_study.py`: Specific analysis for disease-symptom relationships and case studies.

- **📊 Notebooks** (`notebooks/`)
  - `NetworkBiology final.ipynb`: Original analysis notebook.

- **🚀 Main Script**
  - `main.py`: Executable script running the full analysis pipeline.

## ⚠️ Data Requirements
This project requires the Hetionet data files in the root directory:
- `hetionet-v1.0-nodes.tsv`
- `hetionet-v1.0-edges.sif`

## Usage
To run the analysis:
```bash
python main.py
```

