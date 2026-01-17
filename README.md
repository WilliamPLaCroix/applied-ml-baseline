End-to-end applied ML baselines (scikit-learn + PyTorch) with reproducible training, evaluation, and CLI inference.

## Scope

This repository provides minimal, production-minded scaffolding for classical and simple deep learning tasks:

- deterministic data handling (seeded splits)
- config-driven training
- metric reporting
- artifactized model saving/loading
- CLI inference
- basic tests

The goal is to demonstrate clean applied ML engineering, not comprehensive MLOps or cloud deployment.

## Structure

```
repo/
├─ README.md
├─ requirements.txt
├─ pyproject.toml   # optional
├─ src/
│  ├─ data/
│  ├─ models/
│  ├─ configs/
│  ├─ training/
│  ├─ evaluation/
│  ├─ tests/
│  └─ cli/
└─ notebooks/
```

Conventions:
- `notebooks/` for EDA and prototyping only  
- `src/` contains reusable training/inference code  
- `configs/` contains YAML/JSON hyperparameter configs  
- `tests/` contains lightweight unit tests  

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
````

## Usage

### Training (example)

```bash
python -m src.training.train \
  --config configs/regression.yaml \
  --output artifacts/regression/
```

### Evaluation (example)

Evaluation artifacts (metrics, plots, confusion matrices) are written to the output directory defined at train time.

### Inference (example)

```bash
python -m src.cli.predict \
  --model artifacts/regression/model.joblib \
  --input samples/input.csv \
  --output predictions.csv
```

## Reproducibility

* seeded splits (NumPy / Torch)
* pinned dependencies
* config-driven hyperparameters
* artifacts stored outside source tree

## Tests

Lightweight tests verify data utilities, model initialization, and CLI inference. Run:

```bash
pytest -q
```

## Status

| Component        | Status    |
| ---------------- | --------- |
| Regression (SKL) | WIP       |
| Classification   | WIP       |
| Torch baseline   | WIP       |
| CLI inference    | WIP       |
| Tests            | WIP       |


## Dataset Policy

No large datasets or sensitive data are committed. Small synthetic or toy CSVs may be used for tests.


## License

MIT

