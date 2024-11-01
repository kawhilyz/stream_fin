import yfinance as yf
import streamlit as st
import pandas as pd
import akshare as ak
import datetime
# 设置全局属性
st.set_page_config(
    page_title='财经专栏',
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("财经频道")
st.subheader("Money Never Sleeps")
st.divider()

option = st.selectbox(
    "选择对应的指数",
    ("大盘成长","沪深300"),
)
st.write("你选择了:",option)
index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol=option, indicator="市盈率")
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

st.session_state.dataset = option

