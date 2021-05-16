import os
import sys

from flask import Flask, render_template, flash, url_for, current_app, redirect


STATIC_FOLDER = "../static"
TEMPLATE_FOLDER = "../template"

app = Flask(__name__,
            static_folder = STATIC_FOLDER, 
            template_folder = TEMPLATE_FOLDER)

from howdareyou.views import bp as index_bp
app.register_blueprint(index_bp)

@app.errorhandler(404)
def page_not_found(message):
    return render_template('errors/404.html', message=message), 404

@app.errorhandler(401)
def unauthorized(message):
    return render_template('errors/401.html', message=message), 401

@app.errorhandler(403)
def forbidden(message):
    return render_template('errors/401.html', message=message), 403

@app.errorhandler(500)
def internal_server_error(message):
    return render_template('errors/500.html', message=message), 500
