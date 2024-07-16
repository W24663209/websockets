import asyncio
import websockets
import logging

from fastapi import FastAPI, Request

import ussd

# 配置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 存储所有连接的客户端
logging.info('开始启动')

# 创建 FastAPI 应用实例
app = FastAPI()


@app.get("/payOut")
async def payOut(device, phone, amount):
    ussd.payOut(device, phone, amount)

@app.get("/balance")
async def balance(device):
    ussd.get_balance(device)

@app.get("/bind")
async def bind(device):
    ussd.bind(device)