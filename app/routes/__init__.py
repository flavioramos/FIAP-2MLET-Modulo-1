def register_routes(app):
    from .user_routes import user_bp
    from .auth_routes import auth_bp
    from .wine_routes import wine_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(wine_bp)
