import streamlit as st 
import akshare as ak
import pandas as pd
import numpy as np
# 设置全局属性
st.set_page_config(
    page_title='页面标题',
    page_icon='☆☆☆ ',
    layout='wide'
)

# 正文
st.title('慢慢变富')
st.markdown('投资是一件积累幸福的事')

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')


index_value_hist_funddb_df = ak.index_value_hist_funddb(symbol="大盘成长", indicator="市盈率")
print(index_value_hist_funddb_df)
#stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20200301", end_date='20241001', adjust="")
st.dataframe(index_value_hist_funddb_df.style.highlight_max(axis=0))

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

