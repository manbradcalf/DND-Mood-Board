from threading import Lock

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

async_mode = None
app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def dashboard():
    return render_template("dashboard/dashboard.html")


@app.route('/sharn')
def hello_sharn():
    return render_template("sharn/map.html")


@app.route('/khorvair')
def hello_khorvair():
    return render_template("khorvair/map.html")


@app.route('/theater')
def show_movie_screen():
    return render_template("theater/movie-screen.html")


@socketio.on('request_image_update')
def update(image_path):
    emit('change_image', image_path, broadcast=True)


@socketio.on('request_audio_update')
def update(audio_path):
    emit('change_audio', audio_path, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='192.168.0.11', debug=True, port=5001)
