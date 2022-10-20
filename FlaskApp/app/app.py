from flask import Flask

from app.views import base_app

def create_app(test_config=None):
    """Create and configure Flask app"""

    app = Flask(__name__)

    app.register_blueprint(base_app)

    return app