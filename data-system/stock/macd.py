import pandas as pd
import os.path

def calculate_macd(data: pd.DataFrame, short_span: int = 12, long_span: int = 26, signal_span: int = 9):
    """
    计算 MACD、DIF 和 DEA 指标
    
    参数:
    - data: 股票数据 (DataFrame)，必须包含 `Close` 列
    - short_span: 短期EMA的周期（默认12）
    - long_span: 长期EMA的周期（默认26）
    - signal_span: 信号线（DEA）的周期（默认9）

    返回:
    - 包含 MACD、DIF 和 DEA 的 DataFrame
    """
    # 计算短期和长期的 EMA
    
    data['Close'] = data['成交价格']
    data['EMA_short'] = data['Close'].ewm(span=short_span, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_span, adjust=False).mean()

    # 计算 DIF = 短期EMA - 长期EMA
    data['DIF'] = data['EMA_short'] - data['EMA_long']

    # 计算 DEA = DIF 的 signal_span 日 EMA
    data['DEA'] = data['DIF'].ewm(span=signal_span, adjust=False).mean()

    # 计算 MACD = 2 * (DIF - DEA)
    data['MACD'] = 2 * (data['DIF'] - data['DEA'])

    return data[['Close', 'EMA_short', 'EMA_long', 'DIF', 'DEA', 'MACD']]

# 示例使用
if __name__ == '__main__':
    # 获取股票数据（例如：平安银行的股票代码 '000001.SZ'）
    folder_name = "2024-02-13"
    folder_path =os.path.join(os.getcwd(), "data-system", "data", folder_name)
    print(folder_path)
    stock_data = pd.read_parquet(os.path.join(folder_path, f'sz000001.snappy.parquet') )
    print(stock_data)
    # 计算 MACD
    # macd_data = calculate_macd(stock_data)

    # # 输出结果
    # print(macd_data.tail())
