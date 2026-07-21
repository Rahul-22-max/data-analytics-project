# Day 6 Regression Pipeline

## Objective

Prepare data for machine learning regression.

## Target Variable

LTV

## Numerical Features

- tenure
- MonthlyCharges
- TotalCharges
- SeniorCitizen

## Categorical Features

- gender
- Partner
- Dependents
- PhoneService
- InternetService
- Contract
- Churn

## Preprocessing

Numerical:
- StandardScaler

Categorical:
- OneHotEncoder

## Train-Test Split

80% Training
20% Testing

Random State:
42

## Day 6 Progress

- Created train-test split
- Built preprocessing pipeline
- Encoded categorical features
- Scaled numerical features
- Saved reusable preprocessing object