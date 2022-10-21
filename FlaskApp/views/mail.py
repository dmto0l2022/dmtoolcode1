from flask import Blueprint, render_template

mail_blueprint = Blueprint('mail', __name__, url_prefix='/mail')

# creating route
@mail_blueprint.route("/")
def mail():
    return render_template("mail.html", name='Andy', email="andy@gmail.com")

