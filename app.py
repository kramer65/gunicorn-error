#!venv/bin/python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "I got the key, I got the secret!"
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('ping', namespace='/test')
def handle_my_custom_event(the_json):
    print('received json: ' + str(the_json))
    emit('pong', the_json)


if __name__ == '__main__':
    socketio.run(app, port=5000)
