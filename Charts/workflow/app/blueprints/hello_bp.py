from flask import Blueprint, render_template

hello_bp = Blueprint('hello_bp', __name__)

@hello_bp.route('/', methods=['GET', 'POST'])
def rootofserver():
    return 'root'

@hello_bp.route('/hello')
def home():
    return render_template('hello.html')
