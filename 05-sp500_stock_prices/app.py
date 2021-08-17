from pandas.core.indexes import period
import streamlit as st
import pandas as pd
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


st.title('S&P 500 Stock Prices')

st.markdown(
    """
        Retrieves the list of the **S&P 500** (from wikipedia)
        * **Data Source:** [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)
    """
)

st.sidebar.header('User Inputs')

# web scraping

@st.cache
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html=pd.read_html(url, header=0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# sidebar sector selection
sorted_sectors = sorted(df["GICS Sector"].unique())
selected_sectors = st.sidebar.multiselect('Sector', sorted_sectors, sorted_sectors)

# filter data
df_selected_sector = df[df["GICS Sector"].isin(selected_sectors)]

x, y = df_selected_sector.shape

st.header('Companies in Selected Sector')
st.write(f'Data dimension: {x} rows, {y} columns.')
st.dataframe(df_selected_sector)

# download option
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}' download=SP500.csv>Download CSV File</a>"
    return href

st.markdown(file_download(df_selected_sector), unsafe_allow_html=True)

max_num_companies = 10
num_company = st.sidebar.slider('Numberof Companies', 1, max_num_companies)

data = yf.download(
    tickers=list(df_selected_sector[:max_num_companies]["Symbol"]),
    period='ytd',
    interval='1d',
    group_by='ticker',
    auto_adjust=True,
    prepost=True,
    threads=True,
    proxy=None
)



def plot_price(symbol):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df = pd.DataFrame(data[symbol]["Close"])
    df["Date"] = df.index
    
    plt.fill_between(df["Date"], df["Close"], color='skyblue', alpha=0.3)
    plt.plot(df["Date"], df["Close"], color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    return st.pyplot()


if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for sym, sec in zip(list(df_selected_sector["Symbol"])[:num_company], list(df_selected_sector["Security"])[:num_company]):
        st.write(sec)
        plot_price(sym)


