from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.blueprints.hello_bp import hello_bp
    app.register_blueprint(hello_bp)
        
    return app
