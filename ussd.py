import asyncio
import time

import websockets
import websocket


def balance():
    return "*334#-x-7-5-2222-1"


def phone():
    return "*100#-x-4-1-1"


def pay_out(phone, amount):
    phone = '0' + phone if len(phone) != 10 else phone
    return f"*334#-x-1-1-{phone}-{int(eval(amount))}-2222-1-1"


# 712166370
# 185235928
# 724100972
# 798276149
# 768798827
# 757106499
def payOut(device, phone, amount):
    uri = 'wss://websockets.kingpay.io'
    # 创建一个WebSocket连接
    ws = websocket.WebSocket()
    ws.connect(uri)
    try:
        ws.send('set_name:payout')
        ws.send(f"to:{device},message:{pay_out(phone, amount)}")

        while True:
            try:
                message = ws.recv()
                print(f"收到消息: {message}")
                if '完成代付' in message:
                    break
                if '代付失败' in message:
                    break
            except websocket.WebSocketConnectionClosedError:
                print("连接已关闭")
                break
            except Exception as e:
                print(f"发生错误: {e}")
            time.sleep(5)  # 使用 time.sleep 进行同步休眠
    finally:
        ws.close()

def bind(device):
    uri = 'wss://websockets.kingpay.io'
    # 创建一个WebSocket连接
    ws = websocket.WebSocket()
    ws.connect(uri)
    try:
        ws.send(f"to:{device},message:{phone()}")
    finally:
        ws.close()

def get_balance(device):
    uri = 'wss://websockets.kingpay.io'
    # 创建一个WebSocket连接
    ws = websocket.WebSocket()
    ws.connect(uri)
    try:
        ws.send(f"to:{device},message:{balance()}")
    finally:
        ws.close()


payOut('ed33cc088d6226ef', '732843251', '180.000')