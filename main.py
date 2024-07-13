import asyncio
import websockets
import logging

from fastapi import FastAPI,Request

# 配置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 存储所有连接的客户端
logging.info('开始启动')

# 创建 FastAPI 应用实例
app = FastAPI()

@app.post("/send")
async def send(request: Request):
    # 获取请求中的所有参数
    request_body = await request.body()
    return "success"
