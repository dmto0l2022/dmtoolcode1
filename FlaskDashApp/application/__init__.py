"""Initialize Flask app."""
from flask import Flask
from routes import *

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask app
        
        app.register_blueprint(routes)
        
        #from . import routes

        # Import Dash application
        from .dash.mindash1 import init_dashboard_functions
        app = init_dashboard_functions(app)

        return app
