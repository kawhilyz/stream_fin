import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import akshare as ak

symbol = "000001"
df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date="20200301", end_date='20241001', adjust="")
st.write("股票代码:",symbol)
fig = go.Figure(data=go.Ohlc(x=df['日期'],
                    open=df['开盘'],
                    high=df['最高'],
                    low=df['最低'],
                    close=df['收盘']))
st.plotly_chart(fig, use_container_width=True)

