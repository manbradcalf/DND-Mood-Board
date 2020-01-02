from flask_socketio import send

from app import socketio
import pandas


@socketio.on('update')
def send_update(img):
    send(img)


def parse_image_urls():
    with open("static/image_urls.csv") as f:
        reader = csv.reader(f)
        list_of_urls = list(reader)
        return list_of_urls
