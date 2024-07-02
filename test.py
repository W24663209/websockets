import asyncio
import websockets

async def send_name():
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    async with websockets.connect('ws://127.0.0.1:8765') as websocket:
        # await websocket.send("Alice")
        await websocket.send("to:Alice,message:Hello Bob!")

asyncio.get_event_loop().run_until_complete(send_name())