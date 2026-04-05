# Stock Movement Prediction MLOps Pipeline

## Project Overview

This project implements an end-to-end MLOps pipeline to predict stock price movement (up/down) after 5 minutes using minute-level historical trading data.

The pipeline demonstrates production-style ML workflow including:

• Data Versioning (DVC)  
• Feature Store (Feast)  
• Experiment Tracking (MLflow)  
• Continuous Integration (GitHub Actions + CML)  
• Cloud execution on Google Cloud Platform  

---

## Problem Statement

Predict whether a stock price will increase or decrease after 5 minutes using:

Features:
- Rolling average closing price of last 10 minutes
- Total volume traded in last 10 minutes
- Stock name

Target:
- 1 → price increases after 5 minutes
- 0 → price does not increase

---

## Project Structure

```
.
├── data
│   ├── v0
│   ├── v1
│
├── src
│   ├── features.py
│   ├── merge.py
│   ├── train.py
│
├── feature_repo
│   └── stock_features
│
├── models
│   ├── model_v0.pkl
│   ├── model_v1.pkl
│
├── .github/workflows
│   └── ci.yml
│
├── dvc.yaml
├── dvc.lock
├── requirements.txt
├── README.md
└── AI_USAGE_DOC.md
```

---

## Pipeline Architecture

Raw Data (v0 & v1)  
↓  
DVC Data Versioning  
↓  
Feature Engineering (Feast)  
↓  
Model Training (2 iterations)  
↓  
MLflow Experiment Tracking  
↓  
Model Registry  
↓  
CI Pipeline + CML Reports  

---

## Technologies Used

Python  
Scikit-learn  
DVC  
Feast  
MLflow  
GitHub Actions  
CML  
Google Cloud Platform  

---

## Setup Instructions

### Clone repository

```
git clone <repo_url>
cd 23F3004013_IITMBS_MLOPS_OPPE1_JAN_2026
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run DVC pipeline

```
dvc repro
```

---

### Push data to remote

```
dvc push
```

---

### Run MLflow UI

```
mlflow ui --backend-store-uri file:./mlruns --port 5001
```

---

### Feast Feature Store

Apply feature definitions:

```
cd feature_repo/stock_features/feature_repo
feast apply
```

---

## Training Iterations

Iteration 1:  
Training using v0 dataset  

Iteration 2:  
Training using merged v0 + v1 datasets  

Models generated:

model_v0.pkl  
model_v1.pkl  

---

## CI Pipeline

GitHub Actions pipeline performs:

• Dependency installation  
• Pipeline sanity check  
• CI report generation  

Workflow triggers on push to master branch.

---

## Results

The pipeline successfully demonstrates:

• Reproducible ML pipeline  
• Feature management  
• Experiment tracking  
• Model registry  
• CI automation  

---

## Challenges Faced

Some issues encountered:

• DVC remote configuration errors  
• MLflow tracking mismatch  
• Feast feature definition issues  
• CI dependency conflicts  

These were resolved through dependency corrections and configuration fixes.

---

## Future Improvements

Possible improvements:

• Hyperparameter optimization  
• More feature engineering  
• Model performance comparison  
• Deployment pipeline  

---

## Author

Abhishek Jha  
Roll Number: 23F3004013  
IIT Madras BS Degree Program  

---

## AI Usage

Details available in:

AI_USAGE_DOC.md
