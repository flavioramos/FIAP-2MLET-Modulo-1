from flasgger import Swagger
from flask import Flask
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
    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "Wine Scrapper API",
            "description": "Wine production statistics extracted from Embrapa's website",
            "version": "1.0.0"
        },
        "basePath": "/api/v1",
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "scheme": "bearer",
                "description": "Format: Bearer <access_token>"
            }
        },
        "security": [
            {
                "BearerAuth": [],
            }
        ]
    })

    app.config.from_object('app.config.Config')
    app.url_map.converters['regex'] = RegexConverter

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    @app.cli.command("clear-cache")
    def clear_cache():
        """
        Deletes all CSV files from /cache directory.
        """
        cache_service.clear_cache()

    @app.cli.command("build-cache")
    def build_cache():
        """
        Download missing CSV files from Embrapa website.
        """
        cache_service.build_cache()

    @app.cli.command("init-db")
    def init_db():
        """
        Create admin user and import CSV data into SQL database
        """
        db.create_all()
        user_service.init_db()
        wine_service.load_all()

    return app
