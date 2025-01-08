import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    INFLUXDB_URL = os.getenv('INFLUXDB_URL', 'http://localhost:8086')
    INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN', 'your_default_token')
    INFLUXDB_ORG = os.getenv('INFLUXDB_ORG', 'your_default_org')
    INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET', 'your_default_bucket')
