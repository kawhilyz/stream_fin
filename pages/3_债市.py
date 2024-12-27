import yfinance as yf
import streamlit as st
import pandas as pd
import akshare as ak
from datetime import datetime
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.mandatory_date_range import date_range_picker

option = st.selectbox(
    "选择对应的指数",
    ("大盘成长","沪深300"),
)
#st.write("你选择了:",option)
result = date_range_picker("选择日期范围")
start_date,end_date = date_string = result[0].strftime('%Y%m%d'),result[1].strftime('%Y%m%d')
#st.write("日期范围:",result[0],"——",result[1])
index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol=option, indicator="市盈率")
stock_zh_a_hist_df = ak.stock_zh_a_hist(
    symbol="600900", 
    period="daily", 
    start_date = start_date, 
    end_date = end_date, 
    adjust="hfq"
)
st.dataframe(stock_zh_a_hist_df)
st.divider()
#stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20200301", end_date='20241001', adjust="")
#st.table(index_value_hist_funddb_df.style.highlight_max(axis=0))
st.line_chart(index_value_hist_funddb_df,x='日期',y='市盈率')

datalist = ("", "人口数据", "环境数据", "交易数据")

if "dataset" not in st.session_state:
    option = st.selectbox(
        "请选择数据集",
        datalist,
    )
else:
    option = st.session_state.dataset
    option = st.selectbox(
        "请选择数据集",
        datalist,
        index=datalist.index(option),
    )

if option == "":
    st.write("当前尚未选择数据集")
else:
    st.write("你当前选择的是: 【", option, "】")

import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.write('Hello, *World!* :sunglasses:')