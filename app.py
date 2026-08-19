import streamlit as st
import joblib
import numpy as np

model=joblib.load("house_price.pkl")

st.set_page_config(
    page_title="House Price prediction",
    page_icon="🤖",
    layout="centered"
)
st.title("House Price Prediction app")
st.write("Enter the detail below for prediction")
st.divider()

income=st.number_input("Avg. Area Income")
house_avg=st.number_input("Avg. Area House Age")
rooms=st.number_input("Avg. Area Number of Rooms")
bedrooms=st.number_input("Avg. Area Number of Bedrooms")
population=st.number_input("Area Population")


if st.button("Predict House Price"):
    feature=np.array([[
        income,
        house_avg,
        rooms,
        bedrooms,
        population
    ]])
    prediction=model.predict(feature)
    st.success(f"Predicted house price :$ {prediction[0][0]:,.2f}")
    if prediction[0]>1000000:
        st.balloons()
