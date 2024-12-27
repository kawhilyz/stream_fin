import pandas as pd
import akshare as ak
from datetime import datetime


import pandas as pd
def resample_k_lines(data, resample_config=None):
    """
    resample the k-lines by the given freq
    :param data:
    :param resample_config:
    :return:
    """
    if resample_config is None:
        resample_config = {
            'rule': '1W',
        }
    resampled_data = pd.DataFrame()
    resampled_data['open'] = data['open'].resample(**resample_config).first()
    resampled_data['close'] = data['close'].resample(**resample_config).last()
    resampled_data['low'] = data['low'].resample(**resample_config).min()
    resampled_data['high'] = data['high'].resample(**resample_config).max()
    resampled_data['vol'] = data['vol'].resample(**resample_config).sum()
    resampled_data['color'] = 'red'
    resampled_data.loc[resampled_data['close'] < resampled_data['open'], 'color'] = 'green'
    return resampled_data

hkmi = ak.fund_etf_hist_sina(symbol="sh510060")

macro_info_ws_df = ak.macro_info_ws(date="20241104")
print(macro_info_ws_df)