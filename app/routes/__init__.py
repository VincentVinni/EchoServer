from app.routes.user_routes import user_bp
from app.routes.echo_routes import echo_bp

def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(echo_bp)
