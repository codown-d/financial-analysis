from datetime import datetime
from influxdb_client import Point

def create_stock_data(symbol, price, volume, date, time):
    timestamp = datetime.strptime(f"{date}T{time}", "%Y-%m-%dT%H:%M:%S")
    point = Point("stock_data") \
        .tag("symbol", symbol) \
        .tag("date", date) \
        .field("price", price) \
        .field("volume", volume) \
        .time(timestamp, write_precision='s')  # 时间戳精度为秒
    return point

