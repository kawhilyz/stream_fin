import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import akshare as ak
from datetime import datetime
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.mandatory_date_range import date_range_picker
from utils.data_loader import get_cn10y_bond_yield, get_hs300_pe
from utils.plot_utils import plot_correlation_heatmap
import plotly.graph_objects as go


# 设置全局字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # Linux
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False
# 设置全局属性
st.set_page_config(
    page_title='财经专栏',
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# 页面标题
st.title("资产配置观测指标")
st.divider()
# 获取数据
bond_yield = get_cn10y_bond_yield().sort_values(by='日期', ascending=False)['中国国债收益率10年'].head(1).iloc[0]
hs300_pe = get_hs300_pe().sort_values(by='日期', ascending=False)['滚动市盈率'].head(1).iloc[0]
hs300_yl = (1 / hs300_pe) * 100

# 展示指标
st.subheader("当前观测指标")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("沪深300市盈率", f"{hs300_pe:.2f}")
with col2:
    st.metric("中国十年期国债收益率", f"{bond_yield:.2f}%")
with col3:
    st.metric("沪深300盈利收益率", f"{hs300_yl:.2f}%")

# 资产配置建议
st.subheader("资产配置建议")
if hs300_pe < 15 and bond_yield > 3.5:
    st.success("当前股市估值较低，债市收益率较高，建议增加股市配置，减少债市配置。")
elif hs300_pe > 20 and bond_yield < 2.5:
    st.warning("当前股市估值较高，债市收益率较低，建议减少股市配置，增加债市配置。")
else:
    st.info("当前市场估值和收益率处于中性水平，建议保持均衡配置。")

# 添加说明
st.markdown("""
**说明**：
- 沪深300市盈率：衡量股市估值水平,越低表示股市越便宜。
- 中国十年期国债收益率：衡量债市收益率水平，越高表示债市吸引力越大。
""")

# 展示指标
st.divider()
st.subheader("沪深300盈利收益率 与十年期国债收益率走势")

hs300_data = get_hs300_pe()[['日期','静态市盈率']]
bond_data = get_cn10y_bond_yield()[['日期','中国国债收益率10年']]

# 合并数据
df = pd.merge(hs300_data, bond_data, on="日期")
df.columns = ['日期', '沪深300 PE','十年期国债收益率']
# 计算盈利收益率
df["沪深300盈利收益率"] = (1 / df["沪深300 PE"]) * 100
# 沪深300 ERP
df["沪深300 ERP"] = df["沪深300盈利收益率"] - df["十年期国债收益率"]


# 添加滑动条选择时间范围
# 计算默认日期
max_date = df["日期"].max()  # 当前最大日期
default_start_date = max_date - pd.DateOffset(years=3)  # 三年前的日期

# 将两个日期筛选器放在同一行
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("开始日期", default_start_date)
with col2:
    end_date = st.date_input("结束日期", df["日期"].max())

# 过滤数据
filtered_df = df[(df["日期"] >= start_date) & (df["日期"] <= end_date)]

# 创建 Plotly 图表
fig = go.Figure()

# 添加沪深300 PE 折线
fig.add_trace(
    go.Scatter(
        x=filtered_df["日期"],
        y=filtered_df["沪深300盈利收益率"],
        name="沪深300盈利收益率",
        line=dict(color="blue"),
        yaxis="y1"  # 绑定到左侧 y 轴
    )
)

# 添加十年期国债收益率折线
fig.add_trace(
    go.Scatter(
        x=filtered_df["日期"],
        y=filtered_df["十年期国债收益率"],
        name="十年期国债收益率",
        line=dict(color="red"),
        yaxis="y2"  # 绑定到右侧 y 轴
    )
)



# 设置布局
fig.update_layout(
    title="沪深300 盈利收益率 与十年期国债收益率走势",
    xaxis=dict(title="日期"),
    yaxis=dict(title="沪深300 盈利收益率", titlefont=dict(color="blue"), tickfont=dict(color="blue")),
    yaxis2=dict(title="十年期国债收益率 (%)", titlefont=dict(color="red"), tickfont=dict(color="red"), overlaying="y", side="right"),
    legend=dict(x=0.1, y=1.1),
    hovermode="x unified"
)

# 在 Streamlit 中显示
st.plotly_chart(fig, use_container_width=True)

# 显示过滤后的数据
st.subheader("过滤后的数据")
st.write(filtered_df)


# 展示原始数据
st.subheader("原始数据")
st.write(df)
