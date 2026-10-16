import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Marketing Campaign Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Models
# -----------------------------
model_path = "models"

revenue_model = joblib.load(
    os.path.join(
        model_path,
        "revenue_prediction_model_final.pkl"
    )
)

profit_model = joblib.load(
    os.path.join(
        model_path,
        "profit_prediction_model.pkl"
    )
)

regression_features = joblib.load(
    os.path.join(
        model_path,
        "regression_features_final.pkl"
    )
)

classification_features = joblib.load(
    os.path.join(
        model_path,
        "classification_features.pkl"
    )
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Multi-Brand Marketing Campaign Performance Prediction")

st.write("""
This application predicts:

1. Campaign Revenue using Random Forest Regression
2. Campaign Profit/Loss using Machine Learning
""")

# -----------------------------
# User Input Section
# -----------------------------
st.header("Enter Campaign Details")

duration = st.number_input(
    "Campaign Duration (Days)",
    min_value=1,
    value=30
)

impressions = st.number_input(
    "Impressions",
    min_value=0,
    value=50000
)

clicks = st.number_input(
    "Clicks",
    min_value=0,
    value=5000
)

leads = st.number_input(
    "Leads",
    min_value=0,
    value=1000
)

conversions = st.number_input(
    "Conversions",
    min_value=0,
    value=200
)

acquisition_cost = st.number_input(
    "Acquisition Cost",
    min_value=0,
    value=10000
)

engagement_score = st.number_input(
    "Engagement Score",
    min_value=0,
    max_value=10,
    value=7
)

year = st.number_input(
    "Year",
    min_value=2020,
    max_value=2030,
    value=2025
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

channels = st.multiselect(
    "Select Marketing Channels",
    [
        "Email",
        "Facebook",
        "Google",
        "Instagram",
        "WhatsApp",
        "YouTube"
    ]
)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Campaign Performance"):

    # Channel Encoding
    channel_data = {
        "Email": 0,
        "Facebook": 0,
        "Google": 0,
        "Instagram": 0,
        "WhatsApp": 0,
        "YouTube": 0
    }

    for channel in channels:
        channel_data[channel] = 1

    # Input DataFrame
    input_data = pd.DataFrame({
        "Duration": [duration],
        "Impressions": [impressions],
        "Clicks": [clicks],
        "Leads": [leads],
        "Conversions": [conversions],
        "Acquisition_Cost": [acquisition_cost],
        "ROI": [0],
        "Engagement_Score": [engagement_score],
        "Year": [year],
        "Month": [month],
        "Email": [channel_data["Email"]],
        "Facebook": [channel_data["Facebook"]],
        "Google": [channel_data["Google"]],
        "Instagram": [channel_data["Instagram"]],
        "WhatsApp": [channel_data["WhatsApp"]],
        "YouTube": [channel_data["YouTube"]]
    })

    # -----------------------------
    # Revenue Prediction
    # -----------------------------
    revenue_prediction = revenue_model.predict(
        input_data[regression_features]
    )

    predicted_revenue = revenue_prediction[0]

    # -----------------------------
    # Profit / Loss Calculation
    # -----------------------------
    profit_loss_amount = predicted_revenue - acquisition_cost

    # -----------------------------
    # Display Results
        # -----------------------------
    
    st.subheader("📈 Prediction Results")

    st.success(
        f"Predicted Revenue: ₹ {predicted_revenue:,.2f}"
    )

    st.subheader("💰 Financial Summary")

    # Financial estimate based on predicted revenue minus campaign cost
    if profit_loss_amount > 0:
        st.success("Financial Estimate: PROFIT ✅")
        st.success(
            f"Estimated Profit: ₹ {profit_loss_amount:,.2f}"
        )
    elif profit_loss_amount < 0:
        st.error("Financial Estimate: LOSS ❌")
        st.error(
            f"Estimated Loss: ₹ {abs(profit_loss_amount):,.2f}"
        )
    else:
        st.warning("Financial Estimate: BREAK-EVEN ⚖️")

    # Classifier prediction using the exact training features
    campaign_values = {
        "Duration": duration,
        "Impressions": impressions,
        "Clicks": clicks,
        "Leads": leads,
        "Conversions": conversions,
        "Acquisition_Cost": acquisition_cost,
        "Engagement_Score": engagement_score,
        "Year": year,
        "Month": month,
        "Email": channel_data["Email"],
        "Facebook": channel_data["Facebook"],
        "Google": channel_data["Google"],
        "Instagram": channel_data["Instagram"],
        "WhatsApp": channel_data["WhatsApp"],
        "YouTube": channel_data["YouTube"],
    }

    classifier_input = pd.DataFrame(
        [[campaign_values[feature] for feature in classification_features]],
        columns=classification_features
    )

    predicted_class = int(profit_model.predict(classifier_input)[0])
    class_probabilities = profit_model.predict_proba(classifier_input)[0]
    class_labels = list(profit_model.classes_)
    profit_probability = float(
        class_probabilities[class_labels.index(1)]
    )

    st.subheader("🤖 ML Profitability Classification")

    if predicted_class == 1:
        st.success("Classifier Prediction: PROFITABLE ✅")
    else:
        st.error("Classifier Prediction: NOT PROFITABLE ❌")

    st.caption(
        f"Estimated probability of the model predicting profitable: "
        f"{profit_probability:.1%}"
    )

    # ROI estimate based on predicted revenue
    if acquisition_cost > 0:
        estimated_roi = (
            (predicted_revenue - acquisition_cost)
            / acquisition_cost
        ) * 100

        st.info(f"Estimated ROI: {estimated_roi:.2f}%")
