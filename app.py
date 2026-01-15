import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Credit Card Default Prediction",
    page_icon="💳",
    layout="centered"
    
)

# -----------------------------
# LOAD MODEL & SCALER
# -----------------------------
model = pickle.load(open("model (1).pkl", "rb"))
scaler = pickle.load(open("scaler (2).pkl", "rb"))

# -----------------------------
# BACKGROUND IMAGE
# -----------------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("background.png")

# -----------------------------
# UI CSS (GLASS EFFECT)
# -----------------------------
st.markdown("""
<style>
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.6);
    z-index: -1;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,0.18);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 32px;
    border: 1px solid rgba(255,255,255,0.25);
}

h1, h3, label {
    color: white !important;
    font-weight: 700;
}

input, select {
    background-color: rgba(255,255,255,0.95) !important;
    color: black !important;
    caret-color: black !important;
    font-weight: 600 !important;
}

input::placeholder {
    color: #555 !important;
}

.stButton button {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 0.7rem;
    border-radius: 12px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<h1 style='text-align:center;'>💳 Credit Card Default Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# FORM
# -----------------------------
with st.form("prediction_form"):
    LIMIT_BAL = st.number_input("Credit Limit", 0, 1000000, 200000)
    SEX = st.selectbox("Gender", ["Male", "Female"])
    EDUCATION = st.selectbox("Education", ["Graduate School", "University", "High School", "Others"])
    MARRIAGE = st.selectbox("Marital Status", ["Married", "Single", "Others"])
    AGE = st.number_input("Age", 18, 100, 30)

    PAY_0 = st.number_input("PAY_0", -2, 8, 0)
    PAY_2 = st.number_input("PAY_2", -2, 8, 0)
    PAY_3 = st.number_input("PAY_3", -2, 8, 0)
    PAY_4 = st.number_input("PAY_4", -2, 8, 0)
    PAY_5 = st.number_input("PAY_5", -2, 8, 0)
    PAY_6 = st.number_input("PAY_6", -2, 8, 0)

    BILL_AMT1 = st.number_input("BILL_AMT1", 0)
    BILL_AMT2 = st.number_input("BILL_AMT2", 0)
    BILL_AMT3 = st.number_input("BILL_AMT3", 0)
    BILL_AMT4 = st.number_input("BILL_AMT4", 0)
    BILL_AMT5 = st.number_input("BILL_AMT5", 0)
    BILL_AMT6 = st.number_input("BILL_AMT6", 0)

    PAY_AMT1 = st.number_input("PAY_AMT1", 0)
    PAY_AMT2 = st.number_input("PAY_AMT2", 0)
    PAY_AMT3 = st.number_input("PAY_AMT3", 0)
    PAY_AMT4 = st.number_input("PAY_AMT4", 0)
    PAY_AMT5 = st.number_input("PAY_AMT5", 0)
    PAY_AMT6 = st.number_input("PAY_AMT6", 0)

    submit = st.form_submit_button("🔍 Predict")

# -----------------------------
# PREDICTION
# -----------------------------
if submit:
    sex_val = 1 if SEX == "Male" else 2
    edu_map = {"Graduate School":1,"University":2,"High School":3,"Others":4}
    mar_map = {"Married":1,"Single":2,"Others":3}

    input_data = [[
        LIMIT_BAL, sex_val, edu_map[EDUCATION], mar_map[MARRIAGE], AGE,
        PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
        BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
        PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6
    ]]

    input_df = pd.DataFrame(input_data, columns=[
        'LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE',
        'PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6',
        'BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6',
        'PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'
    ])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Default\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Low Risk of Default\nProbability: {probability:.2%}")
