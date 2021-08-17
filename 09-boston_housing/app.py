import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import pickle

st.write("""
    # Boston House Price Prediction App
""")

st.write('---')

# load the dataset
boston = datasets.load_boston()

x = pd.DataFrame(boston["data"], columns=boston["feature_names"])
y = pd.DataFrame(boston["target"], columns=["MEDV"])

# sidebar
st.sidebar.header('Specify Parameters')

def input_features():
    
    CRIM = st.sidebar.slider('CRIM', x["CRIM"].min(), x["CRIM"].max(), x["CRIM"].mean())
    ZN = st.sidebar.slider('ZN', x["ZN"].min(), x["ZN"].max(), x["ZN"].mean())
    INDUS = st.sidebar.slider('INDUS', x["INDUS"].min(), x["INDUS"].max(), x["INDUS"].mean())
    CHAS = st.sidebar.slider('CHAS', x["CHAS"].min(), x["CHAS"].max(), x["CHAS"].mean())
    NOX = st.sidebar.slider('NOX', x["NOX"].min(), x["NOX"].max(), x["NOX"].mean())
    RM = st.sidebar.slider('RM', x["RM"].min(), x["RM"].max(), x["RM"].mean())
    AGE = st.sidebar.slider('AGE', x["AGE"].min(), x["AGE"].max(), x["AGE"].mean())
    DIS = st.sidebar.slider('DIS', x["DIS"].min(), x["DIS"].max(), x["DIS"].mean())
    RAD = st.sidebar.slider('RAD', x["RAD"].min(), x["RAD"].max(), x["RAD"].mean())
    TAX = st.sidebar.slider('TAX', x["TAX"].min(), x["TAX"].max(), x["TAX"].mean())
    PTRATIO = st.sidebar.slider('PTRATIO', x["PTRATIO"].min(), x["PTRATIO"].max(), x["PTRATIO"].mean())
    B = st.sidebar.slider('B', x["B"].min(), x["B"].max(), x["B"].mean())
    LSTAT = st.sidebar.slider('LSTAT', x["LSTAT"].min(), x["LSTAT"].max(), x["LSTAT"].mean())
    
    data = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT
    }
    
    return pd.DataFrame(data, index=[0])

df = input_features()

st.subheader('Selected Input Parameters')
st.write(df)
st.write('---')

model = pickle.load(open('model.pkl', 'rb'))
predict = model.predict(df)

st.subheader('Predicted')
predict









