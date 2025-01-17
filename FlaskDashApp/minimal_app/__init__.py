"""Initialize Flask app."""
from flask import Flask

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    #app.config.from_object('config.Config')

    with app.app_context():
        # Import Dash application
        #from minimal_app.minimal import init_dashboard
        #app = init_dashboard(app)
        from minimal_app.minimal import init_dashboard_functions
        app = init_dashboard_functions(app)
        
        return app
