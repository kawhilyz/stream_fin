import streamlit as st 
import akshare as ak
import pandas as pd
import numpy as np


macro_info_ws_df = ak.macro_info_ws(date="20241104")
#st.dataframe(macro_info_ws_df)

import akshare as ak
from datetime import datetime

test_date = datetime.now().date().isoformat().replace("-", "")

import akshare as ak

bond_zh_us_rate_df = ak.bond_zh_us_rate(start_date="20241031")
st.dataframe(bond_zh_us_rate_df)