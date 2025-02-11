
from concurrent.futures import ThreadPoolExecutor
import os

target_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
# 创建目录（如果不存在）
os.makedirs(target_directory, exist_ok=True)
os.chdir(target_directory)
import pandas as pd
import akshare as ak
from utils.stock import  get_code_from_csv, get_stock_data, read_stock_from_parquet, set_code_to_csv
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
    set_code_to_csv(folder_name)
    code_list = get_code_from_csv(folder_name)
    code_list= code_list["code"].to_list()
    code_list.sort(reverse = False)
    # 创建线程池
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务
        for code in code_list[:1]:
            executor.submit(get_stock_data,code,folder_name)
    # read_stock_from_parquet('000001',folder_name)

    # stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sz000002")
    # print(stock_zh_a_tick_tx_js_df)
if __name__ == "__main__":
   main()
