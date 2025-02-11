import os
import pandas as pd
import akshare as ak

def check_folder_exists(folder_path):
    """
    检查指定的文件夹是否存在。如果不存在，则创建该文件夹。

    :param folder_path: 文件夹路径
    :return: 如果文件夹存在则返回 True，否则创建并返回 True
    """
    if os.path.exists(folder_path):
        return True
    else:
        # 文件夹不存在，创建文件夹
        return False

def check_data_exists(folder_name, file_name, code_name="000001"):
    """
    检查指定文件夹中是否有包含特定 code（如 "000001"）的数据。
    
    :param folder_name: 文件夹名称
    :param file_name: 文件名
    :param code_name: 需要检查的 code，默认为 "000001"
    :return: 如果数据存在返回 True，否则返回 False
    """
    # 构建文件路径
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, file_name)
    
    # 检查文件夹是否存在
    if not check_folder_exists(folder_path):
        return False

    # 检查文件是否存在
    if os.path.exists(file_path):
        # 如果文件存在，读取 CSV 数据
        df = pd.read_csv(file_path,dtype={'code': str})

        # 检查是否包含 code_name
        if 'code' in df.columns and (df['code'] == code_name).any():
            return True
        else:
            return False
    else:
        return False

def check_and_create_folder(folder_path):
    """检查文件夹是否存在，如果不存在则创建"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# def check_data_exists(file_path, code):
#     """检查 CSV 文件中是否存在指定的股票代码数据"""
#     if os.path.exists(file_path):
#         df = pd.read_csv(file_path,dtype={'code': str})
#         if 'code' in df.columns and (df['code'] == code).any():
#             return True
#     return False

def add_data_to_csv(file_path, data):
    """将数据添加到 CSV 文件中"""
    if os.path.exists(file_path):
        df = pd.read_csv(file_path,dtype={'code': str})
        df = pd.concat([df, data], ignore_index=True)
        df.to_csv(file_path, index=False)
    else:
        data.to_csv(file_path, index=False)

def save_code_to_file(folder_name,file_name, code_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, file_name)
    check_and_create_folder(folder_path)
    # 检查是否需要添加数据
    if check_data_exists(folder_name,file_name, code_name):
        pass  
    else:
        # 创建新数据并添加到 CSV 文件中
        new_data = pd.DataFrame({"code": [code_name]})
        add_data_to_csv(file_path, new_data)


# 示例用法
if __name__ == "__main__":
    check_data_exists("2024-02-07", "code-data.csv", "000001")
