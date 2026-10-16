# Marketing Campaign Prediction and Profitability Analysis

## Project Overview

An end-to-end data science project that analyzes marketing campaign performance across three beauty and cosmetics brands: **Nykaa, Purplle, and Tira**.

The project uses data analysis and machine learning to predict campaign revenue and classify campaigns as profitable or loss-making. A Streamlit application provides an interactive interface for generating predictions.

## Business Objectives

- Analyze marketing campaign performance across multiple brands.
- Clean and preprocess campaign datasets.
- Perform exploratory data analysis (EDA).
- Engineer features for machine learning.
- Predict campaign revenue using regression.
- Classify campaign profitability using classification.
- Present model predictions through an interactive Streamlit application.

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

## Dataset Summary

The combined dataset contains approximately **166,665 records** from the three brand datasets before feature engineering.

Campaign-related variables include duration, impressions, clicks, leads, conversions, acquisition cost, engagement metrics, dates, and marketing channels.

The data was used for exploratory analysis, feature engineering, and predictive modeling.

## Project Workflow

1. Combine the three brand datasets.
2. Inspect data quality and handle missing values.
3. Perform exploratory data analysis.
4. Engineer and prepare model features.
5. Train a revenue regression model.
6. Train a profit/loss classification model.
7. Evaluate model performance.
8. Integrate the trained models into a Streamlit application.

## Machine Learning Models and Results

### 1. Revenue Prediction

A Random Forest regression model predicts campaign revenue.

The final model uses 15 features and excludes ROI as an input.

| Evaluation Metric | Final Result |
|---|---:|
| RMSE | 253,269.72 |
| MAE | 164,760.44 |
| R² Score | 0.7169 |

**Interpretation:** The model explains approximately 71.7% of the variance in the evaluation dataset. RMSE and MAE quantify prediction error in the target's units. These results provide a baseline for further model improvement.

The reported results are specific to the evaluation setup and should not be interpreted as guaranteed performance on new campaigns.

### 2. Profit/Loss Classification

A classification model predicts whether a campaign is profitable or loss-making.

| Evaluation Metric | Previously Recorded Result |
|---|---:|
| Accuracy | 85.71% |
| Precision | 86.62% |
| Recall | 88.20% |
| F1 Score | 87.40% |

These are the previously recorded evaluation results for the classification model. Performance should be revalidated on unseen data before business deployment.

## Streamlit Application

The interactive application provides:

- Predicted campaign revenue.
- Predicted profit/loss category.
- A user interface for entering campaign information.

The application loads saved machine learning models and their associated feature lists using Joblib.

## Project Structure

```text
Marketing_Campaign_Prediction/
├── data/
├── notebooks/
│   └── marketing_campaign_analysis.ipynb
├── models/
│   ├── README.md
│   ├── revenue_prediction_model_final.pkl
│   ├── regression_features_final.pkl
│   ├── revenue_prediction_model.pkl
│   ├── regression_features.pkl
│   ├── profit_prediction_model.pkl
│   ├── classification_features.pkl
│   └── classification_scaler.pkl
├── app.py
├── requirements.txt
└── README.md
```

*The structure illustrates the expected project layout. Some files may differ depending on the current repository contents.*

## How to Run the Project

### Prerequisites

- Python installed on your computer.
- The project repository and required model files.

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Marketing_Campaign_Prediction
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

Ensure that the model filenames and paths in `app.py` match the files in the `models/` directory.

## Skills Demonstrated

- Python programming
- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Regression and classification
- Model evaluation
- Machine learning model persistence
- Streamlit application development
- Business-focused data analysis

## Future Improvements

- Compare additional machine learning algorithms.
- Improve validation and model generalization.
- Analyze performance by brand and marketing channel.
- Improve the dashboard with additional visualizations.
- Validate predictions on genuinely unseen campaign data.
- Deploy the application for broader access.

## Conclusion

This project demonstrates an end-to-end machine learning workflow for marketing campaign analysis, revenue prediction, and profitability classification. It combines data preparation, predictive modeling, model evaluation, and interactive application development to explore how machine learning can support marketing decisions.

---

**Author:** Your Name

**Project:** Marketing Campaign Prediction and Profitability Analysis
