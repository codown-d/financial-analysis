
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

target_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
# 创建目录（如果不存在）
os.makedirs(target_directory, exist_ok=True)
os.chdir(target_directory)
import pandas as pd
import akshare as ak
from utils.stock import  get_code_from_csv, set_code_to_csv
from utils.file_utils import  get_codes_with_pending_status,update_status_to_done
from stock import task_stock

# # 示例用法

def main():
    folder_name = "2024-02-13"
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
    # print(code_list)
     # 创建一个线程池，最多并发执行 3 个任务
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     # 提交所有任务，并记录每个任务的输入参数与 future 关联
    #     futures = {
    #         executor.submit(get_stock_data, get_stock_full(stock_id)): f'sz{stock_id}'
    #         for stock_id in code_list[:2]
    #     }
    #      # 等待所有任务完成并收集结果
    #     for future in as_completed(futures):
    #         try:
    #             result = future.result()  # 获取任务的执行结果
    #             code = futures[future]
    #             result.to_parquet(f'{code}.snappy.parquet', compression='snappy')
    #             print(f"Input parameter: {futures[future]}, Result: {result}")
    #         except Exception as e:
    #             print(f"An error occurred: {e}")
    # read_stock_from_parquet('000001',folder_name)
    task_stock(folder_name)
    # df= get_codes_with_pending_status(folder_name)
    # print(df)
    # update_status_to_done(folder_name,'000001')

    # df = pd.read_parquet(f'{folder_name}\sz000001.snappy.parquet')
    # print(df)

    # stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sz000002")
    # print(stock_zh_a_tick_tx_js_df)
if __name__ == "__main__":
   main()
