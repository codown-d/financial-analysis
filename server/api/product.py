# api/product.py
from flask import Blueprint, jsonify, request

product_bp = Blueprint('product', __name__)

# 产品相关接口

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Smartphone"}]
    return jsonify(products)

@product_bp.route('/product', methods=['POST'])
def create_product():
    product_data = request.get_json()
    if not product_data or 'name' not in product_data:
        return jsonify({"error": "Name is required"}), 400
    
    product = {"id": 3, "name": product_data['name']}
    return jsonify(product), 201
