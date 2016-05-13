from mcstatus import MinecraftServer
import requests
import time
from config import *

latency = bad_latency_time = last_bad_latency_time = offline_time = last_offline_time = None


def send_telegram_message(text):
        requests.post("https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage", data={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': "[" + COMPUTER_NAME + "] " + text
        })


def check_status():
    global bad_latency_time, last_bad_latency_time, offline_time, last_offline_time, latency

    try:
        server = MinecraftServer.lookup(SERVER_IP)
        status = server.status()
        print("Server Latency: " + str(status.latency))
        latency = status.latency
        offline_time = None
        if latency < MAX_LATENCY:
            bad_latency_time = None
        elif bad_latency_time is None:
            bad_latency_time = int(round(time.time() * 100))
    except Exception:
        print("Server Offline")
        if offline_time is None:
            offline_time = int(round(time.time() * 100))


def send_alerts():
    global bad_latency_time, last_bad_latency_time, offline_time, last_offline_time, latency

    if bad_latency_time is not None and last_bad_latency_time is None:
        send_telegram_message("The server latency is increased (" + str(latency) + "ms) (IP: " + SERVER_IP + ")")
        last_bad_latency_time = int(round(time.time() * 100))
    elif offline_time is not None and last_offline_time is None:
        send_telegram_message("The server is offline (IP: " + SERVER_IP + ")")
        last_offline_time = int(round(time.time() * 100))
    elif last_bad_latency_time is not None and bad_latency_time is None:
        send_telegram_message("The server latency is back to normal (IP: " + SERVER_IP + ")")
        last_bad_latency_time = None
    elif last_offline_time is not None and offline_time is None:
        send_telegram_message("The server is now online (IP: " + SERVER_IP + ")")
        last_offline_time = None

while True:
    check_status()
    send_alerts()
    time.sleep(CHECK_DELAY)
