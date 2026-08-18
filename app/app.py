import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Customer Retention Intelligence",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD MODEL FILES
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
MODEL_DIR = os.path.join(PROJECT_DIR, "models")

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "logistic_regression_model.pkl"
    )
)

scaler = joblib.load(
    os.path.join(
        MODEL_DIR,
        "scaler_ml.pkl"
    )
)

feature_names = joblib.load(
    os.path.join(
        MODEL_DIR,
        "feature_names.pkl"
    )
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Customer Retention & Sales Intelligence")

st.markdown(
    """
    ### Turn customer behavior into actionable business insights

    This platform uses **RFM analysis, customer segmentation, and machine learning**
    to understand customer behavior and predict the likelihood of a repeat purchase
    within the next **90 days**.
    """
)

st.divider()


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📊 Navigation")
st.sidebar.markdown("---")
st.sidebar.caption("Customer Retention Intelligence Platform")


page = st.sidebar.radio(
    "Go to",
    [
        "Project Overview",
        "Customer Segmentation",
        "Repeat Purchase Prediction",
        "Business Recommendations"
    ]
)

# -----------------------------
# PROJECT OVERVIEW
# -----------------------------
if page == "Project Overview":

    st.header("Project Overview")

    st.write("""
    This project analyzes retail customer behavior using RFM analysis
    and K-Means clustering. It also uses Machine Learning to predict
    whether a customer is likely to make another purchase within the
    next 90 days.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🤖 Final Model", "Logistic Regression")

    with col2:
        st.metric("🎯 Model Accuracy", "65.8%")

    with col3:
        st.metric("📅 Prediction Window", "90 Days")

    st.subheader("Key Techniques Used")

    st.write("""
    - Data Cleaning
    - Exploratory Data Analysis
    - Customer-Level Feature Engineering
    - RFM Analysis
    - K-Means Customer Segmentation
    - 90-Day Repeat Purchase Prediction
    - Machine Learning Model Comparison
    """)

# -----------------------------
# CUSTOMER SEGMENTATION
# -----------------------------
elif page == "Customer Segmentation":

    st.header("Customer Segmentation")

    st.write("""
    Customers were divided into four segments based on:
    **Recency, Frequency, and Monetary Value (RFM)**.
    """)

    segment_data = pd.DataFrame({
        "Segment": [
            "Regular Customers",
            "At-Risk Customers",
            "VIP Customers",
            "Loyal High-Value Customers"
        ],
        "Description": [
            "Customers with moderate purchasing activity.",
            "Customers who have not purchased recently.",
            "Extremely valuable and highly active customers.",
            "Frequent customers with high spending."
        ]
    })

    st.dataframe(
        segment_data,
        use_container_width=True
    )

# -----------------------------
# REPEAT PURCHASE PREDICTION
# -----------------------------
elif page == "Repeat Purchase Prediction":

    st.header("90-Day Repeat Purchase Prediction")

    st.write(
        "Enter customer RFM values to predict whether "
        "the customer is likely to make another purchase "
        "within the next 90 days."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency (Days)",
            min_value=0,
            value=30
        )

    with col2:
        frequency = st.number_input(
            "Frequency (Number of Purchases)",
            min_value=1,
            value=5
        )

    with col3:
        monetary = st.number_input(
            "Monetary Value",
            min_value=0.0,
            value=1000.0
        )

    if st.button("Predict Repeat Purchase"):

        input_data = pd.DataFrame(
            [[recency, frequency, monetary]],
            columns=feature_names
        )

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)[0]

        probability = model.predict_proba(
            input_scaled
        )[0][1]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.success(
                "This customer is likely to make a repeat purchase "
                "within the next 90 days."
            )
        else:
            st.warning(
                "This customer may not make a repeat purchase "
                "within the next 90 days."
            )

        st.metric(
    "🎯 Repeat Purchase Probability",
    f"{probability * 100:.2f}%"
)


    
        st.progress(float(probability))

        if probability >= 0.70:
            st.success("🟢 High retention potential")
        elif probability >= 0.40:
            st.warning("🟡 Medium retention potential")
        else:
            st.error("🔴 Low retention potential")
        

# -----------------------------
# BUSINESS RECOMMENDATIONS
# -----------------------------
elif page == "Business Recommendations":

    st.header("Business Recommendations")

    recommendations = {
        "VIP Customers":
            "Provide exclusive rewards and personalized offers.",

        "Loyal High-Value Customers":
            "Use loyalty programs and cross-selling opportunities.",

        "Regular Customers":
            "Encourage repeat purchases with targeted promotions.",

        "At-Risk Customers":
            "Launch win-back campaigns and personalized discount offers."
    }

    col1, col2 = st.columns(2)

    segments = list(recommendations.items())

    with col1:
        st.info(f"⭐ {segments[0][0]}")
        st.write(segments[0][1])

        st.info(f"🟢 {segments[2][0]}")
        st.write(segments[2][1])

    with col2:
        st.info(f"💎 {segments[1][0]}")
        st.write(segments[1][1])

        st.warning(f"⚠️ {segments[3][0]}")
        st.write(segments[3][1])