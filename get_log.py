import json
import time
from datetime import datetime, timezone

import websocket
from pymongo import MongoClient


# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["certstream_db"]


def save_log(data):
    # 日付決定
    seen_ts = data.get("seen", int(time.time()))
    dt = datetime.fromtimestamp(seen_ts, tz=timezone.utc)
    col_name = f"ctlogs_{dt.year}_{dt.month:02}_{dt.day:02}"

    db[col_name].insert_one(data)


def on_message(ws, message):
    msg = json.loads(message)
    if msg.get("message_type") == "certificate_update":
        save_log(msg["data"])


def on_error(ws, error):
    print("WebSocket Error:", error)


def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed:", close_status_code, close_msg)


while True:
    try:
        print("Connecting with ping support...")
        ws = websocket.WebSocketApp(
            "ws://localhost:4000",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
        ws.run_forever(
            ping_interval=20,  # 20秒ごとに ping
            ping_timeout=10,
        )
    except Exception as e:
        print("Exception:", e)
        print("Retry in 5 seconds...")
        time.sleep(5)
