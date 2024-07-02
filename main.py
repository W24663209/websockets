import asyncio
import websockets

# 存储所有连接的客户端
clients = {}

async def handle_client(websocket, path):
    name = await websocket.recv()
    print(name)
    clients[websocket] = name
    try:
        async for message in websocket:
            # 解析消息格式为 "to:recipient,message:content"
            recipient, content = message.split(",", 1)
            print(message)
            for client, client_name in clients.items():
                if client_name == recipient:
                    await client.send(content)
    finally:
        del clients[websocket]

start_server = websockets.serve(handle_client, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()