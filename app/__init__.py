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

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register routes
    register_routes(app)

    @app.cli.command("clear-cache")
    def clear_cache():
        cache_service.clear_cache()

    @app.cli.command("build-cache")
    def build_cache():
        cache_service.build_cache()

    @app.cli.command("init-db")
    def init_db():
        from app.models import user_model, wine_model
        from app.extensions import db

        # Create all tables
        db.create_all()

        # Create new user
        user_service.init_db()
        print("User admin created.")

        # Load Wine CSV data
        wine_service.load_all()
        print("Wine CSV data loaded.")

        print("Done.")

    @app.cli.command("test-db")
    def test_db():
        print(jsonify(wine_service.get_all_years("Producao")).get_json())
        # print(jsonify(wine_service.get_by_year("Producao", 2020)).get_json())

    return app
