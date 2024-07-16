from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.routes import url_prefix
from app.services import wine_service, cache_service

wine_bp = Blueprint('wine', __name__, url_prefix=f'{url_prefix}/wine')


@wine_bp.route('/categories')
@jwt_required()
def categories():
    """
        List available categories.
        ---
        consumes:
            - application/json
        responses:
          200:
            examples:
              application/json: {
                    "categories": []
                }
    """
    result = {
        "categories": []
    }
    for category in cache_service.files:
        result["categories"].append(category["name"])

    return jsonify(result), 200


@wine_bp.route('/<regex("[\w]+"):category>/<regex("[\d]{4}"):year>')
@jwt_required()
def categoryByYear(category, year):
    """
        Get category info by year.
        ---
        consumes:
            - application/json
        parameters:
            - name: category
              in: path
              type: string
              enum: [
                "Comercio",
                "ExpEspumantes",
                "ExpSuco",
                "ExpUva",
                "ExpVinho",
                "ImpEspumantes",
                "ImpFrescas",
                "ImpPassas",
                "ImpSuco",
                "ImpVinhos",
                "ProcessaAmericanas",
                "ProcessaMesa",
                "ProcessaSemclass",
                "ProcessaViniferas",
                "Producao"
              ]
              required: true
            - name: year
              in: path
              type: integer
              minimum: 1970
              maximum: 2023
              required: true
              description: 1970 .. 2023
        responses:
          200:
            examples:
              application/json: {
                    "Data description": "int value"
                }
    """
    return jsonify(wine_service.get_by_year(category, int(year))), 200


@wine_bp.route('/<regex("[\w]+"):category>')
@jwt_required()
def category(category):
    """
        Get category info for all years.
        ---
        consumes:
            - application/json
        parameters:
            - name: category
              in: path
              type: string
              enum: [
                "Comercio",
                "ExpEspumantes",
                "ExpSuco",
                "ExpUva",
                "ExpVinho",
                "ImpEspumantes",
                "ImpFrescas",
                "ImpPassas",
                "ImpSuco",
                "ImpVinhos",
                "ProcessaAmericanas",
                "ProcessaMesa",
                "ProcessaSemclass",
                "ProcessaViniferas",
                "Producao"
              ]
              required: true
        responses:
          200:
            examples:
              application/json: {
                "year1": {
                    "Data description": "int value"
                    },
                "year2": {
                    "Data description": "int value"
                    }

                }
    """
    return jsonify(wine_service.get_all_years(category)), 200
