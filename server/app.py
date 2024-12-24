# app.py
from flask import Flask
from api.user import user_bp
from api.product import product_bp
from influxdb_service.influxdb import InfluxDBService
from config import INFLUXDB  # 引入配置

app = Flask(__name__)

# 从配置文件中提取 InfluxDB 相关配置
INFLUXDB_URL = INFLUXDB["url"]
INFLUXDB_TOKEN = INFLUXDB["token"]
INFLUXDB_ORG = INFLUXDB["org"]
INFLUXDB_BUCKET = INFLUXDB["bucket"]

# 创建 InfluxDB 服务实例
influxdb_service = InfluxDBService(INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET)

# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to Flask API!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
