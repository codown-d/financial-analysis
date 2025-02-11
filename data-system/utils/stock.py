import os.path
import akshare as ak
import pandas as pd

from utils.file_utils import check_and_create_folder
def set_code_to_csv(folder_name):
    """检查文件是否存在，不存在则创建并保存数据"""
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')

    check_and_create_folder(folder_path)

    temp_df =  ak.stock_zh_a_spot_em()
    temp_df = pd.DataFrame({
        'code':temp_df['代码'],
        'name':temp_df['名称'], 
        "status": ["pending"] * len(temp_df)
        })
    temp_df = temp_df.sort_values(by="code", ascending=True)
    temp_df = temp_df[temp_df["code"].str.startswith('00')|
                        temp_df["code"].str.startswith('30')|
                        temp_df["code"].str.startswith('60')|
                        temp_df["code"].str.startswith('688')]
    temp_df.to_csv(file_path, index=False) 

def get_code_from_csv(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')
    csvframe = pd.read_csv(file_path,dtype={'code': str,})
    return csvframe
folder_path = os.path.join(os.getcwd())
def get_stock_data(symbol, folder_name):
    print(f"{folder_path}/{folder_name}/{symbol}.parquet")
    temp_df = ak.stock_zh_a_tick_tx_js(symbol)
    print(temp_df)
    temp_df.to_parquet(f"{folder_path}/{folder_name}/{symbol}.parquet", compression= 'gzip')

def read_stock_from_parquet(symbol, folder_name):
    folder_path = os.path.join(os.getcwd(),folder_name, f'{symbol}.parquet')
    print(folder_path)
    df = pd.read_parquet(folder_path)
    print(df.head())

   