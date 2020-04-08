from flask import Flask, request, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "57dwad86a465d79"
socketio = SocketIO(app)


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
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    socketio.run(app, debug=True)
    