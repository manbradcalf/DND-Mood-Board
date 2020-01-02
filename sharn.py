from flask import Blueprint, render_template

bp = Blueprint("sharn", __name__, url_prefix="/sharn")


@bp.route("/")
def get_map():
    return render_template('sharn/map.html')
