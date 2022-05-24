from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__, url_prefix='/home')

## https://realpython.com/flask-blueprint/

@index_blueprint.route("/")
def index():
    return "Hello World!"