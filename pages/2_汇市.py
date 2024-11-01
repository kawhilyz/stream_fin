import streamlit as st 
import akshare as ak
import pandas as pd
import numpy as np


# 正文
st.title('慢慢变富')
st.markdown('投资是一件积累幸福的事')


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


# 这是直接写入主主体。由于表单容器定义在上方，这将出现在表单中写入的所有内容下方。
sound = st.selectbox('选择指标', ['股市','汇市','债市','大宗商品','市场消息'])
animal = st.form('my_animal')


# 这些方法是在表单容器上调用的，所以它们出现在表单内。
submit = animal.form_submit_button(f'用{sound}说！')
sentence = animal.text_input('你的句子:', '金枪鱼在哪里？')
say_it = sentence.rstrip('.,!?') + f', {sound}!'
if submit:
    animal.subheader(say_it)
else:
    animal.subheader('&nbsp;')


col1,col2 = st.columns([1,2])
col1.title('总和：')

with st.form('加法'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('加')

if submit:
    col2.title(f'{a+b:.2f}')

import streamlit as st

st.title("我的超棒应用")

@st.experimental_fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("切换")
    cols[1].text_area("输入文本")

@st.experimental_fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("过滤")
    cols[1].file_uploader("上传图片")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("选择", [1,2,3], None)
cols[1].button("更新")
filter_and_file()




if "dataset" not in st.session_state or st.session_state.dataset == "":
    st.write("当前尚未选择数据集")
else:
    st.write("开始分析数据集: 【", st.session_state.dataset, "】")