from flask import Blueprint, jsonify, request
from services.stock_service import fetch_and_store_stock

stock_api = Blueprint('stock_api', __name__)

@stock_api.route('/api/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    """
    获取指定股票的当前价格。
    :param symbol: 股票的标识符（如 AAPL）
    :return: 返回 JSON 格式的股票数据
    """
    try:
        price = fetch_and_store_stock(symbol)
        return jsonify({"symbol": symbol, "price": price}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@stock_api.route('/api/stock/bulk', methods=['POST'])
def get_bulk_stocks():
    """
    获取多个股票的当前价格。
    :return: 返回多个股票的 JSON 数据
    """
    try:
        symbols = request.json.get("symbols")
        if not symbols:
            return jsonify({"error": "Symbols list is required"}), 400

        result = {}
        for symbol in symbols:
            price = fetch_and_store_stock(symbol)
            result[symbol] = price

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
