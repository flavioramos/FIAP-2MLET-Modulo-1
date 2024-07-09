from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services import wine_service, cache_service

wine_bp = Blueprint('wine', __name__, url_prefix='/wine')


@wine_bp.route('/categories')
@jwt_required()
def categories():
    result = []
    for category in cache_service.files:
        result.append(category["name"])

    return jsonify(result), 200


@wine_bp.route('/<regex("[\w]+"):category>/<regex("[\d]{4}"):year>')
@jwt_required()
def categoryByYear(category, year):
    return jsonify(wine_service.get_by_year(category, int(year))), 200


@wine_bp.route('/<regex("[\w]+"):category>')
@jwt_required()
def category(category):
    return jsonify(wine_service.get_all_years(category)), 200
