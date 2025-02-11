
from concurrent.futures import ThreadPoolExecutor
import os
target_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
# 创建目录（如果不存在）
os.makedirs(target_directory, exist_ok=True)
os.chdir(target_directory)
import pandas as pd
import akshare as ak
from utils.file_utils import check_data_exists, save_code_to_file
# # 示例用法

def main():
    folder_name = "2024-02-08"
    file_name = "code-data.csv"
    code_name = "sz000001"
    # 调用检查方法
    # data_exists = check_data_exists(folder_name, file_name, code_name)
    # if not data_exists:
    #     save_code_to_file(folder_name, file_name, code_name)
    #     print(f"数据不存在")
    # else:
    #     print(f"数据 {code_name} 已存在，不需要写入！")
    file_path = os.path.join(os.getcwd(), folder_name,f'{code_name}.parquet')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(code_name)
    stock_zh_a_tick_tx_js_df.to_parquet(f'{code_name}.snappy.parquet', compression='snappy')
    stock_zh_a_tick_tx_js_df.to_parquet(f'{code_name}.Gzip.parquet', compression='Gzip')
    print(stock_zh_a_tick_tx_js_df)
if __name__ == "__main__":
   main()
