
import streamlit as st
import pandas as pd
import joblib


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Airbnb Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------

model = joblib.load("airbnb_price_model.pkl")


# ---------------------------------------------------------
# Application Header
# ---------------------------------------------------------

st.title("🏠 Airbnb Price Predictor")

st.write(
    "Enter the details of an Airbnb listing to estimate its "
    "nightly price."
)

st.divider()


# ---------------------------------------------------------
# User Inputs
# ---------------------------------------------------------

st.subheader("Listing Information")

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
)

neighbourhood = st.text_input(
    "Neighbourhood",
    value="Williamsburg"
)

latitude = st.number_input(
    "Latitude",
    min_value=40.4,
    max_value=40.95,
    value=40.718,
    format="%.6f"
)

longitude = st.number_input(
    "Longitude",
    min_value=-74.3,
    max_value=-73.6,
    value=-73.995,
    format="%.6f"
)

room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    max_value=365,
    value=2,
    step=1
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    max_value=1000,
    value=10,
    step=1
)

reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    max_value=100.0,
    value=1.0,
    step=0.1
)

calculated_host_listings_count = st.number_input(
    "Host's Total Listings",
    min_value=1,
    max_value=500,
    value=1,
    step=1
)

availability_365 = st.number_input(
    "Availability (days per year)",
    min_value=0,
    max_value=365,
    value=200,
    step=1
)


# ---------------------------------------------------------
# Review Information
# ---------------------------------------------------------

st.subheader("Review Information")

has_review = st.selectbox(
    "Has the listing received a review?",
    ["Yes", "No"]
)

if has_review == "Yes":

    last_review_year = st.number_input(
        "Last Review Year",
        min_value=2011,
        max_value=2026,
        value=2019,
        step=1
    )

    last_review_month = st.number_input(
        "Last Review Month",
        min_value=1,
        max_value=12,
        value=6,
        step=1
    )

    has_review_value = 1

else:

    last_review_year = None
    last_review_month = None
    has_review_value = 0


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if st.button("💰 Predict Airbnb Price", use_container_width=True):

    # Create input DataFrame with exactly the same
    # feature names used during model training

    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [
            calculated_host_listings_count
        ],
        "availability_365": [availability_365],
        "last_review_year": [last_review_year],
        "last_review_month": [last_review_month],
        "has_review": [has_review_value]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.success(
        f"Estimated Nightly Price: ${prediction:,.2f}"
    )

    st.info(
        "This prediction is an estimate produced by the trained "
        "Random Forest regression model."
    )
