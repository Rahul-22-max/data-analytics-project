Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

«An end-to-end Machine Learning project that predicts customer churn using the Telco Customer Churn dataset and exposes predictions through a Flask REST API.»

Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project analyzes customer behavior, identifies churn patterns, and develops a machine learning solution capable of predicting whether a customer is likely to discontinue the company's services.

The project follows a complete Data Analytics and Machine Learning workflow including:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Development
- Model Comparison
- Model Serialization
- Prediction Pipeline
- Flask REST API Development
- API Testing using Postman

---

Problem Statement

Businesses lose significant revenue when customers leave their services.

This project helps organizations identify customers with a high probability of churn so that proactive customer retention strategies can be implemented.

Objectives:

- Predict customer churn using Machine Learning.
- Generate business insights from customer data.
- Provide real-time churn predictions through a Flask API.
- Build a foundation for future Customer Lifetime Value (LTV) prediction.

---

Dataset Information

Dataset: Telco Customer Churn Dataset

The dataset contains customer information including:

- Customer Demographics
- Contract Details
- Internet Services
- Subscription Services
- Payment Methods
- Monthly Charges
- Total Charges
- Customer Churn Status

Dataset Statistics

Metric| Value
Total Customers| 7043
Customers Stayed| 5174
Customers Churned| 1869
Processed Dataset Shape| (7043, 32)

---

Technology Stack

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Joblib
- Git & GitHub
- VS Code
- Postman

---

Project Architecture

Telco Customer Churn Dataset
            │
            ▼
Data Preprocessing
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Feature Engineering
            │
            ▼
Machine Learning Models
(Logistic Regression, Decision Tree, Random Forest)
            │
            ▼
Model Comparison
            │
            ▼
Best Model Selection
            │
            ▼
Model Saving (Joblib)
            │
            ▼
Prediction Pipeline
            │
            ▼
Flask REST API
            │
            ▼
Postman Testing

---

Project Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Correlation Analysis
- Multiple Machine Learning Models
- Model Comparison
- Best Model Selection
- Model Saving using Joblib
- Prediction Pipeline
- Flask REST API
- API Testing using Postman
- Comprehensive Documentation

---

Installation & Setup

Clone the repository

git clone https://github.com/Rahul-22-max/data-analytics-project.git
cd data-analytics-project

Install dependencies

py -m pip install -r requirements.txt

Run the Flask API

py api/app.py

API URL

http://127.0.0.1:5000

---

Machine Learning Models

Model| Accuracy
Logistic Regression| 80.06%
Decision Tree| 80.62%
Random Forest| 80.41%

Best Model

Decision Tree Classifier

Accuracy: 80.62%

---

Performance Summary

Metric| Value
Features Used| 33
Training Samples| 5634
Testing Samples| 1409
Selected Model| Decision Tree
Best Accuracy| 80.62%

---

API Endpoints

Health Check

GET

/health

Response

{
    "status": "API Running Successfully"
}

---

Predict Churn

POST

/predict

Sample Request

{
    "gender": 0,
    "SeniorCitizen": 0,
    "tenure": 1,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}

Sample Response

{
    "prediction": "Customer is likely to CHURN"
}

---

Key Business Insights

- Gender has minimal impact on customer churn.
- Month-to-month contracts have the highest churn rate.
- Long-term contracts significantly reduce churn.
- New customers are more likely to churn.
- Churn decreases as customer tenure increases.
- Fiber optic customers show higher churn tendencies.
- Electronic check payment users are more likely to churn.

---

Repository Highlights

- End-to-End Machine Learning Project
- Flask REST API
- Prediction Pipeline
- Saved Model using Joblib
- Postman API Testing
- Git Version Control
- Production-ready Project Structure


---


# Project Documentation

The repository contains comprehensive documentation covering every phase of the project.

| Document | Description |
|----------|-------------|
| README.md | Project overview, setup instructions, workflow, and API usage |
| CHANGELOG.md | Records all major project updates and milestones |
| LICENSE | MIT License for project usage and distribution |
| docs/team_progress_report.md | Team progress and daily project updates |
| docs/day8_model_training.md | Logistic Regression model training |
| docs/day9_model_comparison.md | Machine learning model comparison |
| docs/day10_random_forest.md | Random Forest implementation |
| docs/day11_model_selection.md | Best model selection |
| docs/day12_prediction_pipeline.md | Prediction pipeline development |
| docs/day14_api_prediction.md | Flask API implementation and testing |

---

| CONTRIBUTING.md | Guidelines for contributing to the project |

---

| CODE_OF_CONDUCT.md | Community guidelines and expected behavior |

---

| SECURITY.md | Security policy and vulnerability reporting guidelines |

---

| SUPPORT.md | Project support and help information |

---

| ROADMAP.md | Future project roadmap and planned enhancements |

---

| RELEASE_NOTES.md | Version history and release summary |

---

| PROJECT_STRUCTURE.md | Explanation of project folder organization |

---

| KNOWN_ISSUES.md | Current limitations and future improvements |


---

# Repository Maintenance

This repository follows software engineering best practices including:

- Modular project structure
- Git version control
- Comprehensive documentation
- Machine Learning model serialization
- REST API development using Flask
- API testing using Postman
- Project changelog maintenance
- Open-source licensing (MIT)

---

Team Members

Role| Name
Team Lead| B. Rahul Charan Babu
Member 1| S. Mohamed Javeeth
Member 2| B. Rahul Charan Babu
Member 3| Prakalya G B
Member 4| Hariom Pandey
Member 5| Sri Veena Tejaswini

---

Project Status

Module| Status
Data Collection| ✅
Data Preprocessing| ✅
EDA| ✅
Feature Engineering| ✅
Machine Learning| ✅
Model Comparison| ✅
Model Saving| ✅
Prediction Pipeline| ✅
Flask API| ✅
API Testing| ✅
Documentation| ✅

Overall Project Completion: 100%

---

Future Enhancements

- Customer Lifetime Value (LTV) Prediction
- Interactive Dashboard
- Cloud Deployment
- Authentication
- Automated Model Retraining
- Real-Time Customer Monitoring

---

Author

B. Rahul Charan Babu

Team Lead | B.Tech Data Analytics Student

Project Version: 1.0

Status: Completed