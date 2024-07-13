import asyncio
import time

import websockets


def balance():
    return "*334#-x-7-5-2222-1"


def phone():
    return "*100#-x-4-1-1"


def pay_out(phone, amount):
    phone = '0' + phone if len(phone) != 10 else phone
    return f"*334#-x-1-1-{phone}-{amount}-2222-1-1"


async def send_name():
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    #     await websocket.send("to:e134da9178c00f6f,message:*334#-x-7-5-2222-1")
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    #     await websocket.send("to:32ebb76a252c7c5a,message:*334#-x-7-5-2222-1")
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    #     await websocket.send("to:d6deeabf93340f98,message:*334#-x-7-5-2222-1")
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    #     await websocket.send("to:98f7b72c4fc0d268,message:*334#-x-7-5-2222-1")
    # async with websockets.connect('wss://websockets.kingpay.io') as websocket:
    # await websocket.send("to:fc48abda8a661ee9,message:*100#-x-4-1-1")
    async with websockets.connect('wss://websockets.kingpay.io') as websocket:
        await websocket.send('set_name:payout')
    async with websockets.connect('wss://websockets.kingpay.io') as websocket:
        await websocket.send(f"to:6876e02ecbb56ec1,message:{pay_out('115271477', '180')}")
        # await websocket.send("to:6876e02ecbb56ec1,message:*100#-x-4-1-1")
        # await websocket.send("to:ed33cc088d6226ef,message:*334#-x-7-5-2222-1")


    while True:
        time.sleep(1)
        try:
            message = await websocket.recv()
            print(message)
        except:
            pass


asyncio.get_event_loop().run_until_complete(send_name())
