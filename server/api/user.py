# api/user.py
from flask import Blueprint, jsonify, request
from influxdb_client import InfluxDBClient, Point
from config import INFLUXDB

from utils.index import create_stock_data


user_bp = Blueprint('user', __name__)

# 设置 InfluxDB 客户端
client = InfluxDBClient(url=INFLUXDB["url"], token=INFLUXDB["token"], org=INFLUXDB["org"])
write_api = client.write_api()

# 用户相关接口

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    return jsonify(users)

@user_bp.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()

    print(user_data)
    
    if not user_data or 'name' not in user_data:
        return jsonify({"error": "Name is required"}), 400
    
    point = create_stock_data(symbol='AAPL', price=150.25, volume=1200, date="2024-12-24", time="09:30:00")

    try:
        write_api.write(bucket=INFLUXDB["bucket"], record=point)
    except Exception as e:
        return jsonify({"error": f"Failed to write data to InfluxDB: {str(e)}"}), 500

    user = {"id": 3, "name": 'user_name'}
    return jsonify(user), 201
