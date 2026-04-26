import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🚗 Car Price Prediction App")

# Inputs
Present_Price = st.number_input("Present Price (in lakhs)")
Kms_Driven = st.number_input("Kms Driven")
Owner = st.selectbox("Owner", [0, 1, 2, 3])

Fuel_Type_Petrol = st.selectbox("Fuel Type Petrol", [0, 1])
Seller_Type_Individual = st.selectbox("Seller Type Individual", [0, 1])
Transmission_Manual = st.selectbox("Transmission Manual", [0, 1])

no_year = st.number_input("Car Age (Years)")

# Prediction
if st.button("Predict Price"):
    
    features = np.array([[Present_Price, Kms_Driven, Owner,
                          no_year, Fuel_Type_Petrol,
                          Seller_Type_Individual,
                          Transmission_Manual]])

    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)

    st.success(f"Estimated Selling Price: ₹ {round(prediction[0], 2)} lakhs")