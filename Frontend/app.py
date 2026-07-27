import streamlit as st
import pandas as pd
import os
import joblib
# Load the trained model and scaler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, 'heart_disease_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
expected_columns = joblib.load(os.path.join(BASE_DIR, 'columns.pkl'))

st.title("Heart Stroke Prediction App")
st.markdown("Enter the details below to predict the likelihood of a heart stroke.")
age = st.slider("Age", 18, 100, 40)
gender = st.selectbox("Gender", ["Male", "Female"])
chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "TA", "NAP", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
rest_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])



if st.button("Predict"):

    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": 1 if fasting_bs == "Yes" else 0,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        "Sex_M": 1 if gender == "Male" else 0,

        "ChestPainType_ATA": 1 if chest_pain_type == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain_type == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain_type == "TA" else 0,

        "RestingECG_Normal": 1 if rest_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if rest_ecg == "ST" else 0,

        "ExerciseAngina_Y": 1 if exercise_angina == "Yes" else 0,

        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("High risk of heart disease.")
    else:
        st.success("Low risk of heart disease.")