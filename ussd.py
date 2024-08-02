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

def get_phone(device):
    uri = 'wss://websockets.kingpay.io'
    # 创建一个WebSocket连接
    ws = websocket.WebSocket()
    ws.connect(uri)
    try:
        ws.send(f"to:{device},message:{phone()}")
    finally:
        ws.close()

start = time.time()
payOut('a711e39f4df14684', '769121456', '270.000')
payOut('a711e39f4df14684', '722636310', '270.000')
payOut('a711e39f4df14684', '719769001', '270.000')
payOut('a711e39f4df14684', '745935400', '180.000')
payOut('a711e39f4df14684', '799974969', '180.000')
payOut('a711e39f4df14684', '705822756', '270.000')
payOut('a711e39f4df14684', '728177178', '180.000')
payOut('a711e39f4df14684', '741121885', '270.000')
payOut('a711e39f4df14684', '757725906', '180.000')
payOut('a711e39f4df14684', '718759306', '270.000')
payOut('a711e39f4df14684', '111395591', '360.000')
payOut('a711e39f4df14684', '721839554', '180.000')
payOut('a711e39f4df14684', '748615238', '180.000')
payOut('a711e39f4df14684', '703301507', '180.000')
payOut('a711e39f4df14684', '723046432', '990.000')
payOut('a711e39f4df14684', '742693480', '180.000')
payOut('a711e39f4df14684', '759706886', '270.000')
payOut('a711e39f4df14684', '714535280', '360.000')
payOut('a711e39f4df14684', '745782093', '180.000')
payOut('a711e39f4df14684', '742036668', '180.000')
payOut('a711e39f4df14684', '721237753', '270.000')
payOut('a711e39f4df14684', '714265662', '9000.000')
payOut('a711e39f4df14684', '706141133', '10000.000')
payOut('a711e39f4df14684', '714508974', '10000.000')
payOut('a711e39f4df14684', '727756003', '9000.000')
payOut('a711e39f4df14684', '719855131', '5500.000')
payOut('a711e39f4df14684', '987050014', '180.000')
payOut('a711e39f4df14684', '705851443', '9000.000')
payOut('a711e39f4df14684', '728476899', '180.000')
payOut('a711e39f4df14684', '719152166', '270.000')
payOut('a711e39f4df14684', '795651643', '10000.000')
payOut('a711e39f4df14684', '724542618', '180.000')
payOut('a711e39f4df14684', '795942474', '180.000')
payOut('a711e39f4df14684', '794989382', '270.000')
payOut('a711e39f4df14684', '758291632', '280.000')
payOut('a711e39f4df14684', '700646228', '10000.000')
payOut('a711e39f4df14684', '719615444', '270.000')
payOut('a711e39f4df14684', '722845378', '360.000')
payOut('a711e39f4df14684', '113362112', '11000.000')
payOut('a711e39f4df14684', '113362112', '11000.000')
end = time.time()
print(end-start)