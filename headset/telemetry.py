import websocket
import json

def on_message(ws, message):
    values = json.loads(message)['values']
    xws = values[0]
    yws = values[1]
    zws = values[2]
    print("x = ", x , "y = ", y , "z = ", z )

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

connect(insert-url)
