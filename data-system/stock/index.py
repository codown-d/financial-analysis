import os.path
import akshare as ak
import pandas as pd

def get_stock_data(symbol):
    print(symbol)
    temp_df = ak.stock_zh_a_tick_tx_js(symbol)
    print(temp_df)
    return temp_df

def get_stock_full(code):
    stock_id = int(code)  # 将股票ID转换为整数
    result = code
    if 1 <= stock_id <= 199999:  # 深圳股票（000001 ~ 199999）
        result=f"sz{code}"
    elif 600000 <= stock_id <= 699999:  # 上海股票（600000 ~ 699999）
        result=f"sh{code}"
    else:
       pass
    return result

def read_stock_from_parquet(symbol, folder_name):
    folder_path = os.path.join(os.getcwd(),folder_name, f'{symbol}.parquet')
    print(folder_path)
    df = pd.read_parquet(folder_path)
    print(df.head())