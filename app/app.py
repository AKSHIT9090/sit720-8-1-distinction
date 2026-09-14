import streamlit as st
import pandas as pd
import joblib
from datetime import date
from pathlib import Path

# Load the trained model
MODEL_PATH = Path(__file__).resolve().parent / "housing_price_model.pkl"
model = joblib.load(MODEL_PATH)


# Page configuration
st.set_page_config(
    page_title="Sydney Housing Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# Application title
st.title("🏠 Sydney Housing Price Predictor")

st.write(
    "Enter the property details below to estimate the "
    "likely sale price using the trained Gradient Boosting model."
)


# Property details
st.subheader("Property Details")


suburb = st.selectbox(
    "Suburb",
    [
        "Bondi",
        "Campbelltown",
        "Parramatta"
    ]
)


property_type = st.selectbox(
    "Property Type",
    [
        "Apartment",
        "Block of units",
        "Duplex/semi-detached",
        "House",
        "Studio",
        "Townhouse",
        "Unit",
        "Villa"
    ]
)


bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=0.0,
    max_value=20.0,
    value=2.0,
    step=1.0
)


bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1.0,
    max_value=10.0,
    value=1.0,
    step=1.0
)


parking_spaces = st.number_input(
    "Number of Parking Spaces",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=1.0
)


listed_area_m2 = st.number_input(
    "Listed Area (m²)",
    min_value=0.0,
    max_value=5000.0,
    value=200.0,
    step=10.0
)


sale_date = st.date_input(
    "Sale Date",
    value=date.today()
)


# Prediction button
if st.button("Predict Sale Price"):

    # Extract year and month from sale date
    sale_year = sale_date.year
    sale_month = sale_date.month

    # Create input dataframe with exactly the same
    # feature names used during model training
    input_data = pd.DataFrame({
        "suburb": [suburb],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "parking_spaces": [parking_spaces],
        "listed_area_m2": [listed_area_m2],
        "sale_year": [sale_year],
        "sale_month": [sale_month]
    })

    # Generate prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.success(
        f"Estimated Sale Price: AUD ${prediction:,.0f}"
    )

    st.info(
        "This is an estimated sale price based on the "
        "trained machine learning model and the property "
        "characteristics provided."
    )


# Footer
st.markdown("---")

st.caption(
    "SIT720 8.1 Distinction Task | Sydney Housing Price Prediction"
)
