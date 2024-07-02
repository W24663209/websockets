import asyncio
import websockets
import logging

# 配置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 存储所有连接的客户端
clients = {}
logging.info('开始启动')


async def handle_client(websocket, path):
    msg = await websocket.recv()  # type:str
    logging.info("收到消息:",msg)
    # 按逗号分割字符串
    parts = msg.split(",")

    # 初始化空字典
    message_dict = {}
    # 遍历分割后的部分，按冒号分割并赋值给字典
    for part in parts:
        key, value = part.split(":")
        message_dict[key] = value
    if msg.startswith('set_name'):
        clients[message_dict['set_name']] = websocket
    elif msg.startswith('to'):
        await clients[message_dict['to']].send(message_dict['message'])
    try:
        async for message in websocket:
            pass
    finally:
        pass


start_server = websockets.serve(handle_client, "0.0.0.0", 8765)
logging.info('启动成功')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
