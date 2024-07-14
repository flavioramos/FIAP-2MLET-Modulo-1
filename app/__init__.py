from flask import Flask, jsonify
from werkzeug.routing import BaseConverter

from .extensions import db, migrate, jwt
from .models import wine_model
from .routes import register_routes
from .services import cache_service, wine_service, user_service


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.url_map.converters['regex'] = RegexConverter

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    @app.cli.command("clear-cache")
    def clear_cache():
        cache_service.clear_cache()

    @app.cli.command("build-cache")
    def build_cache():
        cache_service.build_cache()

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        user_service.init_db()
        wine_service.load_all()

    return app

