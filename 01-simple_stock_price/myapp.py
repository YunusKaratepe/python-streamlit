import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Simple Stock Price App

* Shown are the stock **closing price** and ***volume*** of Google.

""")

ticker_symbol = "GOOGL"

# get data on ticker
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2010-7-31', end='2020-7-31')

# Open High Low Close Volume Dividends Stock Splists -> ticker_df columns

st.write(
    """
        ### Closing Price
    """
)


st.line_chart(ticker_df["Close"])

st.write(
    """
        ### Volume
    """
)
st.line_chart(ticker_df["Volume"])

