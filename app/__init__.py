from flask import Flask
from app.routes import register_routes

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object("config")

    # Register routes
    register_routes(app)

    return app
