import os

from werkzeug.exceptions import NotFound
from flask import Flask, render_template, url_for, current_app, redirect, Blueprint, request, send_file
import yaml
from icecream import ic


CONTENT_FOLDER = "content"

bp = Blueprint('index', __name__)


@bp.route('/')
def index():

    with open(os.path.join(CONTENT_FOLDER, "posts.yml"), "r") as stream:
        try:
            data = yaml.safe_load(stream)
            posts = data["posts"]
        except yaml.YAMLError as exc:
            print(exc)
            posts = []

    return render_template("index.html", posts=posts)

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

