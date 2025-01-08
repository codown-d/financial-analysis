# 使用官方 Node.js 镜像作为基础镜像
FROM node:18.20.5

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json（如果有的话）
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制应用程序代码
COPY . .

# 构建应用
RUN npm run build

# 暴露应用运行的端口
EXPOSE 3000

# 运行 Astro 应用
CMD ["npm", "run", "start"]
