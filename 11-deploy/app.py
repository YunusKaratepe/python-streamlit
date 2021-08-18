import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
    # Penguin Prediction
    * This app predicts **Palmer Penguin** species.
    * Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) by Allison Horst.
    * Using RandomForestClassifier from Sklearn library.
""")

st.sidebar.header('User Inputs')

#st.sidebar.write('You can download an example input csv file from [here](https://raw.githubusercontent.com/YunusKaratepe/python-streamlit/main/08-penguin_classification/penguins_example.csv)')
#uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', type=["csv"])



# if uploaded_file is not None:
#    input_df = pd.read_csv(uploaded_file)


def user_inputs():
    island = st.sidebar.selectbox('Island', ['Biscoe', 'Dream', 'Torgersen'])
    sex = st.sidebar.selectbox('Sex', ['male', 'female'])
    bill_len = st.sidebar.slider('Bill Length (mm)', 30.0, 60.0, 45.0)
    bill_depth = st.sidebar.slider('Bill Depth (mm)', 13.0, 21.0, 17.5)
    flipper_len = st.sidebar.slider('Flipper Length (mm)', 170, 230, 200)
    body_mass = st.sidebar.slider('Body Mass (g)', 2700, 6300, 4200)

    data = {
        'bill_length_mm': bill_len,
        'bill_depth_mm': bill_depth,
        'flipper_length_mm': flipper_len,
        'body_mass_g': body_mass,
        'sex_male': 1 if sex == 'male' else 0,
        'sex_female': 1 if sex == 'female' else 0,
        'island_Biscoe': 1 if island == 'Biscoe' else 0,
        'island_Dream': 1 if island == 'Biscoe' else 0,
        'island_Torgersen': 1 if island == 'Biscoe' else 0,
    }

    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_inputs()

st.subheader('Given Input')
input_df

load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

species = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}

st.subheader('Species')
species

prediction = load_clf.predict(input_df)

st.subheader('Prediction')
species[prediction[0]]

predict_proba = load_clf.predict_proba(input_df)
st.subheader('Prediction Probabilities')
predict_proba




