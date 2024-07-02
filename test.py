import asyncio
import websockets

async def send_name():
    async with websockets.connect('wss://websockets.kingpay.io') as websocket:
        await websocket.send("Alice")
        await websocket.send("to:Bob,message:Hello Bob!")

asyncio.get_event_loop().run_until_complete(send_name())