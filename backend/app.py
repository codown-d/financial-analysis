from flask import Flask
from api.stock_api import stock_api
from api.error_handlers import register_error_handlers

app = Flask(__name__)

# 注册股票 API 路由
app.register_blueprint(stock_api)

# 注册全局错误处理
register_error_handlers(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
