# Stock Movement Prediction Pipeline (OPPE 1)

Predicts whether a stock's price will be higher five minutes later, using minute-level trading data.

## Why this exists
Submission for OPPE 1 (online proctored exam) of the MLOps course in the IIT Madras BS in Data Science, January 2026 term.

## What it does
- Builds two features per stock: 10-minute rolling average close and 10-minute traded volume
- Labels each row 1 if the price rises after 5 minutes, else 0
- Trains a random forest on data version v0, then on merged v0 + v1
- Serves features through a Feast feature store
- Tracks runs in MLflow and runs tests in GitHub Actions with a CML report

## Project structure
```
23F3004013_IITMBS_MLOPS_OPPE1_JAN_2026/
├── .github/workflows/  CI pipeline and CML report
├── feature_repo/       Feast feature definitions
├── src/                Features, merge and training
├── tests/              Inference test
├── dvc.yaml            Pipeline stages
├── AI_USAGE_DOC.md     How AI tools were used
└── requirements.txt    Python dependencies
```

## Getting started
Requirements: Python 3.10+, DVC, access to the DVC remote on GCS.
```bash
git clone https://github.com/abhijha8287/23F3004013_IITMBS_MLOPS_OPPE1_JAN_2026.git
cd 23F3004013_IITMBS_MLOPS_OPPE1_JAN_2026
pip install -r requirements.txt
dvc pull         # fetch data/v0 and data/v1
dvc repro        # merge data, train model_v0 and model_v1
mlflow ui        # view runs at http://127.0.0.1:5000
```

## Tests
```bash
pytest tests/
```

## Tech stack
Python, scikit-learn, pandas, DVC, Feast, MLflow, GitHub Actions, CML, Google Cloud Storage

## Notes
Data lives in a DVC remote and is not committed. Without remote access, place the raw CSVs in `data/v0` and `data/v1` before running `dvc repro`.
