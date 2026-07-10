import streamlit as st
import requests

st.title("Iris Flower Prediction")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):

    response = requests.post(
        "https://iris-project-1-5rlt.onrender.com//predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
    )
    result = response.json()

    if response.status_code == 200:
        result = response.json()
        st.success(result["prediction"])
    else:
        st.error("Prediction failed!")

    