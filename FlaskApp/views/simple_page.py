# https://flask.palletsprojects.com/en/2.2.x/blueprints/

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page_blueprint = Blueprint('simple_page_blueprint', __name__,
                        template_folder='templates')

@simple_page_blueprint.route('/', defaults={'page': 'index'})
@simple_page_blueprint.route('/<page>')
def show(page):
    try:
        #return render_template(f'pages/{page}.html')
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)