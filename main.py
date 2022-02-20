from lib.websocket import WebSocket, set_timeout, sleep

websocket = WebSocket(r"wss://li-tech.net/li-learn-timer/ws/raspberry-pi")


async def on_message(data):
    print("get", data)

    if data["name"] != "ack":
        await websocket.send({"name": "ack"})


async def on_connect():
    print("on connect")

    await websocket.send({
        "name": "message",
        "props": {"text": "Hello!"},
    })


async def on_close():
    print("on close")


websocket.listen_events(
    on_message=on_message,
    on_connect=on_connect,
    on_close=on_close,
)

websocket.wait_end()
