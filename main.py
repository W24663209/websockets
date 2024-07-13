import asyncio
import websockets
import logging

# 配置日志输出格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 存储所有连接的客户端
clients = {}
logging.info('开始启动')

async def handle_client(websocket, path):
    try:
        async for msg in websocket:
            logging.info("收到消息:" + msg)
            # 按逗号分割字符串
            parts = msg.split(",")
            message_dict = {}
            for part in parts:
                key, value = part.split(":")
                message_dict[key] = value.strip()

            if 'set_name' in message_dict:
                clients[message_dict['set_name']] = websocket
                logging.info(f"用户 {message_dict['set_name']} 已连接.")
            elif 'to' in message_dict and 'message' in message_dict:
                to_client = message_dict['to']
                if to_client in clients and clients[to_client].open:
                    await clients[to_client].send(message_dict['message'])
                    logging.info(f"消息已发送到 {to_client}.")
                else:
                    logging.warning(f"无法发送消息到 {to_client}: 连接已关闭或不存在.")
    except websockets.exceptions.ConnectionClosed:
        logging.info("连接关闭")
    except Exception as e:
        logging.error(f"处理消息时发生错误: {e}")
    finally:
        # 清理操作
        clients_to_remove = [name for name, ws in clients.items() if ws == websocket]
        for name in clients_to_remove:
            del clients[name]
            logging.info(f"用户 {name} 已断开连接.")

start_server = websockets.serve(handle_client, "0.0.0.0", 8765)
logging.info('启动成功')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()