import os
from collections import defaultdict

from werkzeug.exceptions import NotFound
from flask import Flask, render_template, url_for, current_app, redirect, Blueprint, request, send_file
import yaml
from icecream import ic


CONTENT_FOLDER = "content"
SUPPORTED_LANGUAGES = ['en', 'fr', 'es', 'ca']
DEFAULT_LANGUAGE = "en"


bp = Blueprint('index', __name__)


def parse_posts(sort=DEFAULT_LANGUAGE):

    with open(os.path.join(CONTENT_FOLDER, "posts.yml"), "r") as stream:
        try:
            data = yaml.safe_load(stream)
            posts = data["posts"]
        except yaml.YAMLError as exc:
            print(exc)
            posts = []


    lang_posts = []
    other_posts = []
    for post in posts:
        if post["lang"] == sort:
            lang_posts.append(post)
        else:
            other_posts.append(post)

    lang_posts.extend(other_posts)

    return lang_posts


@bp.route('/')
def index():

    lang = request.accept_languages.best_match(SUPPORTED_LANGUAGES)
    posts = parse_posts(sort=lang)

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

@bp.route('/tags')
def tags():

    class reversor:
        def __init__(self, obj):
            self.obj = obj

        def __eq__(self, other):
            return other.obj == self.obj

        def __lt__(self, other):
            return other.obj < self.obj

    posts = parse_posts()

    tags = defaultdict(int)
    for post in posts:
        tags[post['tag']] += 1

    # Sort tags in descending order of count
    tags = {k: v for k, v in sorted(tags.items(), key=lambda item: (reversor(item[1]), item[0])) } 

    return render_template("tags.html", tags=tags)

@bp.route('/tag/<tg>')
def tag(tg):

    if tg.startswith("#"):
        tg = tg[1:-1]

    posts = parse_posts()
    filtered = []
    for post in posts:
        if tg.lower() == post["tag"].lower().strip():
            filtered.append(post)

    return render_template("tag.html", posts=filtered)
