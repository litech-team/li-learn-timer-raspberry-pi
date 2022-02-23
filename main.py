from lib.websocket import WebSocket, set_timeout, sleep

websocket = WebSocket(r"wss://li-tech.net/li-learn-timer/ws/raspberry-pi")


async def on_message(name: str, props: dict):
    if name == "ack":
        return

    if True:
        await websocket.send("ack")


async def on_connect():
    print("on connect")

    await websocket.send("send_pi_id", {"pi_id": "hogehoege"}) # ラズパイのIDを送信



async def on_close():
    print("on close")


websocket.listen_events(
    on_message=on_message,
    on_connect=on_connect,
    on_close=on_close,
)

websocket.wait_end()
