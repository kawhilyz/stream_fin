import akshare as ak

print(ak.__version__)

import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20200301", end_date='20241001', adjust="")
print(stock_zh_a_hist_df)