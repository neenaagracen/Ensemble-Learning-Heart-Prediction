import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Heart Disease Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex (0=Female, 1=Male)", [0,1])
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting Blood Sugar")
restecg = st.number_input("Resting ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.number_input("Exercise Angina")
oldpeak = st.number_input("Oldpeak")
st_slope = st.number_input("ST Slope")

if st.button("Predict"):
    data = np.array([[age, sex, cp, trestbps, chol,
                      fbs, restecg, thalach,
                      exang, oldpeak, st_slope]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease")