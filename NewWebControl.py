

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import math
from multiprocessing import Process, Queue

_debug = False


# TODO: axis-mapping should be OOP and automatic!


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
CORS(app)
socketio = SocketIO(app)


@app.route('/')
def control():
    return render_template("control.html")


@socketio.on_error_default
def default_error_handler(e):
    print ("======================= ERROR")
    # print(request.event["message"])
    # print(request.event["args"])


@socketio.on('control', namespace='/control')
def control(message):
    data = message["data"]
    if "left" in data.keys():
        x = data["left"][0]
        y = data["left"][1]
        if _debug:
            print("[Server] Left: ",x,",",y)

    elif "right" in data.keys():
        x = data["right"][0]
        y = data["right"][1]
        if _debug:
            print("[Server] Right: ",x,",",y)

    elif "A" in data.keys():
        if _debug:
            print("[Server] A")
        # binary.q.put(("A",1,0))
    elif "B" in data.keys():
        if _debug:
            print("[Server] B")
        # binary2.q.put(("B",1,0))

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True, use_reloader=False)