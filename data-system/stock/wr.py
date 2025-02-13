import pandas as pd
import os.path

import pandas as pd

def calculate_wr(df: pd.DataFrame, n=14):
    """
    计算 Williams %R (WR) 指标
    :param df: DataFrame, 必须包含 'High', 'Low', 'Close' 列
    :param n: 计算周期，默认为 14
    :return: DataFrame, 包含 WR 指标
    """
    df['Highest_High'] = df['High'].rolling(window=n).max()
    df['Lowest_Low'] = df['Low'].rolling(window=n).min()
    df['WR'] = (df['Highest_High'] - df['Close']) / (df['Highest_High'] - df['Lowest_Low']) * -100
    return df

# 示例使用
if __name__ == '__main__':
    # 获取股票数据（例如：平安银行的股票代码 '000001.SZ'）
    folder_name = "2024-02-13"
    folder_path =os.path.join(os.getcwd(), "data-system", "data", folder_name)
    print(folder_path)
    # stock_data = pd.read_parquet(os.path.join(folder_path, f'sz000009.snappy.parquet') )
    data = {
    'High': [23, 24, 23, 24, 22, 23, 25, 27, 28, 30, 32, 33, 34, 32, 31],
    'Low': [20, 21, 19, 20, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 29],
    'Close': [22, 23, 22, 23, 21, 22, 24, 26, 27, 29, 31, 32, 33, 30, 30]
    }
    df = pd.DataFrame(data)
    # 计算 MACD
    df = calculate_wr(df)

    # # 输出结果
    print(df[['Close', 'WR']])
