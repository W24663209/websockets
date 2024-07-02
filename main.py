import asyncio
import websockets
import logging

# 配置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 存储所有连接的客户端
clients = {}
logging.info('开始启动')
async def handle_client(websocket, path):
    name = await websocket.recv()
    logging.info(name)
    clients[websocket] = name
    try:
        async for message in websocket:
            # 解析消息格式为 "to:recipient,message:content"
            recipient, content = message.split(",", 1)
            logging.info(message)
            for client, client_name in clients.items():
                logging.info(client_name)
                if client_name == recipient:
                    await client.send(content)
    finally:
        del clients[websocket]

start_server = websockets.serve(handle_client, "0.0.0.0", 8765)
logging.info('启动成功')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()