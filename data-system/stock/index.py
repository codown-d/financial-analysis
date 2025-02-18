from concurrent.futures import ThreadPoolExecutor, as_completed
import os.path
import akshare as ak
import pandas as pd
from utils.stock import  get_codes_with_pending_status, set_code_to_csv, update_status_to_done

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

def task_stock(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')
    set_code_to_csv(folder_name)
    code_list = get_codes_with_pending_status(folder_name)
    print(code_list)
    # code_list= code_list["code"].to_list()
    code_list.sort(reverse = False)
    with ThreadPoolExecutor(max_workers=12) as executor:
        # 提交所有任务，并记录每个任务的输入参数与 future 关联
        futures = {
            executor.submit(get_stock_data, get_stock_full(stock_id)): f'sz{stock_id}'
            for stock_id in code_list[:1000]
        }
         # 等待所有任务完成并收集结果
        for future in as_completed(futures):
            try:
                result = future.result()  # 获取任务的执行结果
                code = futures[future]
                result.to_parquet(os.path.join(folder_path, f'{code}.snappy.parquet') , compression='snappy')
                if result.empty:
                    print("Series is empty")
                else:
                    code=code[2:]
                    update_status_to_done(folder_name,code)
                    print(f"Input parameter: {code}, Result: {result}")
               
            except Exception as e:
                print(f"An error occurred: {e}")