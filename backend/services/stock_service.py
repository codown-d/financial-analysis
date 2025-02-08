import os
from dotenv import load_dotenv
from services.stock_crawler import get_stock_data
from services.influxdb_client import InfluxDBClient
from config import Config

# 加载环境变量
load_dotenv()

def fetch_and_store_stock(symbol):
    """
    获取股票数据并存储到数据库。
    :param symbol: 股票的标识符
    :return: 返回股票的当前价格
    """
    price = get_stock_data(symbol)
    
    return price
    # 使用环境变量中的配置项来连接 InfluxDB
    influx_client = InfluxDBClient(
        url=Config.INFLUXDB_URL, 
        token=Config.INFLUXDB_TOKEN, 
        org=Config.INFLUXDB_ORG, 
        bucket=Config.INFLUXDB_BUCKET
    )
    
    influx_client.write_stock_data(symbol, price)
    
    return price
