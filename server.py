from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "57dwad86a465d79"
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('message')
def handleMessage(msg):
    print('\nMessage: {}\n'.format(msg))
    emit('message', msg, broadcast=True)

###

@socketio.on('connect')
def connected():
    print("\nClient connected")

@socketio.on('disconnect')
def disconnected():
    print('\nClient disconnected')


@app.route('/')
def index():
    return  render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
    