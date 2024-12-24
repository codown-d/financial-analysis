# influxdb_service/influxdb.py
from influxdb_client import InfluxDBClient, Point
from datetime import datetime

class InfluxDBService:
    def __init__(self, url, token, org, bucket):
        self.client = InfluxDBClient(url=url, token=token)
        self.write_api = self.client.write_api()
        self.query_api = self.client.query_api()
        self.bucket = bucket
        self.org = org

    def write_data(self, measurement: str, location: str, temperature: float):
        """
        向 InfluxDB 写入数据
        """
        point = Point(measurement).tag("location", location).field("value", temperature).time(datetime.utcnow())
        self.write_api.write(self.bucket, self.org, point)

    def query_data(self, query: str):
        """
        查询 InfluxDB 数据
        """
        result = self.query_api.query(query, org=self.org)
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "measurement": record["_measurement"],
                    "field": record["_field"],
                    "value": record["_value"],
                    "time": record["_time"]
                })
        return data

    def close(self):
        """关闭连接"""
        self.client.close()
