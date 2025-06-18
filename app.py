import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd

# Load saved model and columns
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

locations = data_columns[3:]  # Adjust index if needed

# App title
st.title("🏠 Banglore House Price Prediction")

# Inputs
location = st.selectbox("Select Location", sorted(locations))
sqft = st.number_input("Total Square Feet", value=1000)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, step=1)
bath = st.number_input("Number of Bathrooms", min_value=1, step=1)

if st.button("Predict Price"):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    prediction = model.predict([x])[0]
    st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")
