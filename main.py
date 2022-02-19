from lib.websocket import WebSocket, set_timeout, sleep

websocket = WebSocket("ws://lite-ch.net/li-learn-timer/ws/raspberry-pi")


async def on_message(data):
    print("get", data)


async def on_connect():
    print("on connect")
    set_timeout(websocket.close, 10)

    while websocket.ws:
        await websocket.send({"value": "Hello World"})
        await sleep(1)


async def on_close():
    print("on close")


websocket.listen_events(
    on_message=on_message,
    on_connect=on_connect,
    on_close=on_close,
)

websocket.wait_end()
