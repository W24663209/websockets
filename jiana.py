import time

import websocket


def test(device):
    uri = 'wss://websockets.kingpay.io'
    # 创建一个WebSocket连接
    ws = websocket.WebSocket()
    ws.connect(uri)
    try:
        ws.send('set_name:payout')
        ws.send(f"to:{device},message:0598970623-*171#-6-2-2-1122")

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

test('0595828475-0598970623')