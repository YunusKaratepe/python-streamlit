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

st.markdown('You can find an example input csv file from [here]')

uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', )


