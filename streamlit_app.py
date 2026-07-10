import streamlit as st
import requests

st.title("Iris Flower Prediction")

sepal_length = st.number_input("Sepal Length")
sepal_width = st.number_input("Sepal Width")
petal_length = st.number_input("Petal Length")
petal_width = st.number_input("Petal Width")

if st.button("Predict"):
    try:
        response = requests.post(
            "https://iris-project-1-5rlt.onrender.com/predict",
            json={
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            },
            timeout=90
        )

        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            st.success(response.json()["prediction"])
        else:
            st.error("Prediction failed!")

    except Exception as e:
        st.error(e)

    