import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df):
    """绘制相关性热力图"""
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    plt.title("沪深300 PE 与十年期国债收益率相关性")
    return fig