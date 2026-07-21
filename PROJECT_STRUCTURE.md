# Project Structure

## Root Directory

```
data-analytics-project/
```

---

## Folder Structure

### api/

Contains the Flask REST API.

Files:
- app.py

---

### data/

Stores the project dataset.

Subfolders:

- raw/
- processed/

---

### docs/

Contains all project documentation.

Files include:

- dataset_description.md
- team_progress_report.md
- day8_model_training.md
- day9_model_comparison.md
- day10_random_forest.md
- day11_model_selection.md
- day12_prediction_pipeline.md
- day14_api_prediction.md

---

### eda/

Contains Exploratory Data Analysis scripts.

Files:

- feature_engineering.py
- churn_analysis.py
- churn_visualization.py
- correlation_analysis.py
- correlation_visualization.py

---

### models/

Contains Machine Learning scripts.

Files:

- logistic_regression_model.py
- decision_tree_model.py
- random_forest_model.py
- model_comparison.py
- save_model.py
- predict.py

---

### saved_models/

Stores trained models.

Files:

- churn_prediction_model.pkl
- model_columns.pkl

---

## Root Files

- README.md
- CHANGELOG.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- SUPPORT.md
- ROADMAP.md
- RELEASE_NOTES.md
- LICENSE
- requirements.txt
- .gitignore

---

## Summary

The project follows a modular folder structure to separate data, machine learning models, API development, and documentation for better readability and maintainability.