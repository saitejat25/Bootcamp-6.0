import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
## Simple stock prize app
shown are the stock **closing prize** and ***volume*** of google
""")
tickersymbol='GOOGL'
tickerdata=yf.Ticker(tickersymbol)
tickerDf= tickerdata.history(period='1d', start ='2010-05-31',end='2020-05-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
