import yfinance as yf
import akshare as ak

def get_hs300_pe():
    """获取沪深300市盈率"""
    stock_index = ak.stock_index_pe_lg(symbol= "沪深300")
 #   hs300_data = ak.stock_hs300_spot()
 #   pe_ratio = hs300_data[hs300_data["代码"] == "sh000300"]["市盈率"].values[0]
    return stock_index

def get_cn10y_bond_yield():
    """获取中国十年期国债收益率"""
    bond_data = ak.bond_zh_us_rate()
    return bond_data


kk= get_cn10y_bond_yield()

print(kk)
