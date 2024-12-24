// src/utils/axios.js
import axios from 'axios';

// 创建 axios 实例
const instance = axios.create({
  baseURL: 'https://api.example.com/', // 设置你的 API 基础 URL
  timeout: 5000, // 设置请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
instance.interceptors.request.use(
  (config) => {
    // 在请求发送前可以做一些处理，例如添加 token 等
    const token = localStorage.getItem('token'); // 获取 token
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`; // 添加 token
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
instance.interceptors.response.use(
  (response) => {
    return response.data; // 返回数据部分
  },
  (error) => {
    // 处理错误
    if (error.response) {
      console.error('Error Response:', error.response);
      // 可以根据错误码做不同处理
    } else {
      console.error('Error Message:', error.message);
    }
    return Promise.reject(error);
  }
);

export default instance;
