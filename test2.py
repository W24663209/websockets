import asyncio
import websockets


async def send_name():
    async with websockets.connect('wss://websockets.kingpay.io') as websocket:
        await websocket.send("Alice")

        while True:
            message = await websocket.recv()
            print(message)


asyncio.get_event_loop().run_until_complete(send_name())