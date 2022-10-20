from flask import Blueprint, render_template

base_app = Blueprint("base_app", __name__)

@base_app.route('/name', methods=['GET', 'POST'])
def namesfunction():
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    name = ''
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
    else:
        message = "No Name given."
    return render_template('name.html', names=name, form=form, message=message)


@server.route("/")
def home():
    return render_template('home.html')

## http://0.0.0.0:5051/

@server.route("/dash")
def my_dash_app():
    return app.index()

## http://0.0.0.0:5051/dash1/

@server.route('/flask')
def index():
    return render_template('index.html')

## http://0.0.0.0:5051/flask

#@base_app.route("/")
#def index():
#    """Landing page."""
#    return render_template("index.html", top_menu_items=get_top_menu_items("/"))