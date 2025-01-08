# 使用官方的 Python 镜像作为基础镜像
FROM python:3.13.1

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY . /app

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 暴露应用运行的端口
EXPOSE 5000

# 运行 Flask 应用
CMD ["python", "app.py"]
