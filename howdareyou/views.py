from werkzeug.exceptions import NotFound
from flask import Flask, render_template, url_for, current_app, redirect, Blueprint, request

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/robots.txt')
def robots():
    return render_template("robots.txt")

#@bp.route('/favicon.ico')
#def favicon():
#    return send_file("../static/img/favicon-32x32.png")
