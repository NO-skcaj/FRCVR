import websocket
import json
import threading
import numpy

from test import send, init
x = 0
y = 0
z = 0

def on_message(ws, message):
    values = json.loads(message)['values']
    
    
    global x
    global y
    global z
    dead = 0.1
    
    x = values[0]
    if abs(values[1]) > dead:
        y += values[1]
    z = values[2]
    
    send([x,y,z])


def on_error(ws, error):
    print("error occurred ", error)
    
def on_close(ws, close_code, reason):
    print("connection closed : ", reason)
    
def on_open(ws):
    print("connected")
    

def connect(url):
    ws = websocket.WebSocketApp(url,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.run_forever()
 
init()
connect("ws://localhost:8080/sensor/connect?type=com.samsung.sensor.super_steady_gyro")