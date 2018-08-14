import requests
import websocket
import json
import time
from playsound import playsound
def on_message(ws, message):
    message = json.loads(message)
    print (message)
    print (message["text"])
    if message["text"] == "*Build succeed!*\nYou're awersome":
        playsound("/Users/jacob/Documents/Misc/alarmslack/audio.mp3")
        print ("sonaaar")

def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    time.sleep(1)
    print ("thread terminating...")



if __name__ == "__main__":
    token = "xoxp-55574273794-248433869075-403660196384-1db0432ea40018af985cc50c050a1d79"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'Authorization': 'Bearer ' + token,
        'cache-control': "no-cache"
    }
    r = requests.get('https://slack.com/api/rtm.connect',headers=headers)
    print (r)
    websock = r.json()["url"]
    ws = websocket.WebSocketApp(websock,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
