import requests
from bs4 import BeautifulSoup

def get_stock_data(symbol):
    """
    爬取股票数据（示例：使用 Yahoo Finance 获取股票价格）。
    :param symbol: 股票的标识符（如 AAPL）
    :return: 股票价格
    """
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        stock_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
        return stock_price
    except AttributeError:
        raise Exception(f"Failed to retrieve stock price for {symbol}")
