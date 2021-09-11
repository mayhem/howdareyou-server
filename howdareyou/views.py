from werkzeug.exceptions import NotFound
from flask import Flask, render_template, url_for, current_app, redirect, Blueprint, request, send_file

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/robots.txt')
def robots():
    return render_template("robots.txt")

@bp.route('/favicon.ico')
def favicon():
    return send_file("../static/img/exclamation-logo.svg")

@bp.route('/make-your-own')
def make_your_own():
    return render_template("make-your-own.html")

@bp.route('/about')
def about():
    return render_template("about.html")

