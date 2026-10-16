# Marketing Campaign Prediction and Profitability Analysis

## Project Overview

This project uses data analysis and machine learning to evaluate marketing campaign performance across three beauty and cosmetics brands: **Nykaa, Purplle, and Tira**.

The project aims to help businesses understand campaign performance, predict revenue, and classify campaigns according to their expected profitability.

## Business Objectives

- Analyze marketing campaign performance across multiple brands.
- Clean and preprocess campaign datasets.
- Explore relationships between campaign characteristics and business outcomes.
- Predict campaign revenue using a regression model.
- Classify campaigns as profitable or loss-making using a classification model.
- Present predictions through an interactive Streamlit application.

## Brands Covered

- Nykaa
- Purplle
- Tira

## Technologies Used

- **Programming:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model Persistence:** Joblib
- **Application:** Streamlit
- **Development Environment:** Jupyter Notebook

## Project Workflow

1. Collect and combine the three brand datasets.
2. Inspect the data and handle missing values and data-quality issues.
3. Perform exploratory data analysis (EDA).
4. Prepare features for machine learning.
5. Train a regression model for revenue prediction.
6. Train a classification model for profit/loss prediction.
7. Evaluate model performance using appropriate metrics.
8. Integrate the trained models into a Streamlit application.

## Dataset Summary

The combined dataset contains approximately **166,665 records** from the three brand datasets before feature engineering.

The project includes campaign-related information such as:

- Campaign duration
- Impressions and clicks
- Leads and conversions
- Campaign cost
- Engagement metrics
- Campaign dates
- Brand and marketing channel information

The dataset was used for analysis and predictive modeling.

## Machine Learning Models and Results

### 1. Revenue Prediction

A regression model was developed to predict campaign revenue.

| Evaluation Metric | Result |
|---|---:|
| RMSE | 140,260 |
| MAE | 53,995 |
| R² Score | 0.913 |

The model achieved an R² score of 0.913 on the evaluation data. RMSE and MAE measure prediction error; their interpretation depends on the revenue unit and evaluation setup.

### 2. Profit/Loss Classification

A classification model was developed to predict whether a campaign would be profitable or result in a loss.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 85.71% |
| Precision | 86.62% |
| Recall | 88.20% |
| F1 Score | 87.40% |

These results describe the model evaluation previously recorded for this project. Performance on unseen business data may differ.

## Streamlit Application

The application allows users to enter campaign information and obtain:

- Predicted campaign revenue
- Predicted profit/loss category

The application connects the trained machine learning models with a user-friendly interface.

## Project Structure

```text
Marketing_Campaign_Prediction/
├── data/
├── notebooks/
│   └── marketing_campaign_analysis.ipynb
├── models/
│   ├── revenue_prediction_model.pkl
│   ├── profit_prediction_model.pkl
│   ├── regression_features.pkl
│   └── classification_features.pkl
├── app.py
├── requirements.txt
└── README.md
```

*Note: The structure above is illustrative. Adjust it to match the files actually included in the repository.*

## How to Run the Project

### Prerequisites

Install Python and ensure that the required project files are available.

### Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Marketing_Campaign_Prediction
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual URL of your GitHub repository.

Ensure that the trained model files and application paths match the project structure before running the application.

## Skills Demonstrated

- Python programming
- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Regression modeling
- Classification modeling
- Model evaluation
- Model integration
- Interactive dashboard development
- Business-focused data analysis

## Future Improvements

- Compare additional regression and classification algorithms.
- Improve model validation and generalization.
- Add visual campaign performance dashboards.
- Evaluate profitability across brands and marketing channels.
- Deploy the application for public access.

## Conclusion

This project demonstrates an end-to-end machine learning workflow for marketing campaign analysis, revenue prediction, and profitability classification. It combines data preparation, predictive modeling, evaluation, and application development to support data-driven marketing decisions.

---

**Author:** Your Name

**Project:** Marketing Campaign Prediction and Profitability Analysis
