from flask import render_template
from . import routes

@routes.route('/index/')
def index():
    return render_template('index.html')
