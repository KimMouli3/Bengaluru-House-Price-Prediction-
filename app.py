
import streamlit as st
import pickle
import json
import numpy as np

with open("bangalore_home_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

locations = sorted(data_columns[3:])

st.title("🏠 Bangalore House Price Prediction")

location = st.selectbox("Location", locations)

sqft = st.number_input("Total Sqft", min_value=300.0, value=1000.0)

bath = st.number_input("Bath", min_value=1, value=2)

bhk = st.number_input("BHK", min_value=1, value=2)

if st.button("Predict Price"):

    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated Price: ₹ {prediction:.2f} Lakhs")
