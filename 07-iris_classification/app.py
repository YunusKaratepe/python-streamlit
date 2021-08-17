import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.markdown(
    """
        # Iris Flower Predicter
        * This app predicts iris flower type by given features.
    """
)

st.sidebar.header("User Inputs")

def user_inputs():
    sepal_length = st.sidebar.slider('sepal_length', 4.0, 8.0, 5.5)
    sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.5, 3.5)
    petal_length = st.sidebar.slider('petal_length', 1.0, 7.0, 2.5)
    petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 0.8)

    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    return pd.DataFrame(data, index=[0])

inputs = user_inputs()

st.subheader('Given Features')
inputs


iris_data = datasets.load_iris()

x, y = iris_data["data"], iris_data["target"]

clf = RandomForestClassifier(n_estimators=100)
clf.fit(x, y)

prediction = clf.predict(inputs)
prediction_proba = clf.predict_proba(inputs)

st.subheader('Class Labels')
st.write(iris_data["target_names"])

st.subheader('Prediction')
st.write(iris_data["target_names"][prediction])

st.subheader('Prediction Probabilities')
prediction_proba = {
    iris_data["target_names"][0]: prediction_proba[0][0],
    iris_data["target_names"][1]: prediction_proba[0][1],
    iris_data["target_names"][2]: prediction_proba[0][2],
}

st.write(prediction_proba)


