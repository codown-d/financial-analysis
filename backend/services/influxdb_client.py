from influxdb_client import InfluxDBClient, Point

class InfluxDBClient:
    def __init__(self, url, token, org, bucket):
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.bucket = bucket

    def write_stock_data(self, symbol, price):
        """
        将股票数据写入 InfluxDB 数据库。
        :param symbol: 股票的标识符
        :param price: 股票价格
        """
        point = Point("stocks") \
            .tag("symbol", symbol) \
            .field("price", float(price))
        
        write_api = self.client.write_api()
        write_api.write(bucket=self.bucket, org=self.client.org, record=point)
