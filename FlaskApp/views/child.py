from flask import Blueprint, render_template

child_blueprint = Blueprint('child', __name__, url_prefix='/child')

# creating route
@child_blueprint.route("/")
def mail():
    return render_template("child.html")

