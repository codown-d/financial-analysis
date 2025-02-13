import os.path
import akshare as ak
import pandas as pd

from utils.file_utils import check_and_create_folder
def set_code_to_csv(folder_name):
    """检查文件是否存在，不存在则创建并保存数据"""
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')

    # 检查文件是否存在
    if os.path.exists(file_path):
        print('文件存在')
        pass
    else:
        check_and_create_folder(folder_path)
        temp_df =  ak.stock_info_a_code_name()
        temp_df = temp_df.sort_values(by="code", ascending=True)
        temp_df = temp_df[temp_df["code"].str.startswith('00')|
                            temp_df["code"].str.startswith('30')|
                            temp_df["code"].str.startswith('60')|
                            temp_df["code"].str.startswith('688')]
        temp_df['status'] = ["pending"] * len(temp_df)
        temp_df.to_csv(file_path, index=False) 
    

def get_code_from_csv(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')
    csvframe = pd.read_csv(file_path,dtype={'code': str,})
    return csvframe

def get_codes_with_pending_status(folder_name):
    
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')
    # 读取 CSV 文件
    df = pd.read_csv(file_path,dtype={'code': str,})
    # 筛选 status 为 'pending' 的行
    pending_df = df[df['status'] == 'pending']
    
    # 提取 'code' 列
    codes = pending_df['code'].tolist()
    
    return codes

def update_status_to_done(folder_name, code):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, 'code-data.csv')
    try:
        # 读取 CSV 文件
        df = pd.read_csv(file_path,dtype={'code': str})

        # 检查是否存在该 code
        if code in df['code'].values:
            # 更新指定 code 的 status 为 'done'
            df.loc[df['code'] == code, 'status'] = 'done'

            # 保存更新后的 DataFrame 回 CSV 文件
            df.to_csv(file_path, index=False)
            print(f"Code {code} status updated to 'done'.")
        else:
            print(f"Code {code} not found in the CSV.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# if __name__ == "__main__":
#    set_code_to_csv()