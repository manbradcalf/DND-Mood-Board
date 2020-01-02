from flask import Blueprint, render_template
from flask_socketio import emit

from app import socketio

bp = Blueprint("theater", __name__, url_prefix="/theater")


@bp.route("/")
def get_map():
    return render_template('theater/movie-screen.html')


@socketio.on('change_image')
def change_image(image_path):
    emit('change', image_path)
