from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.user_service import get_all_users, create_user

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/list', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    users = get_all_users()
    return jsonify([user.to_dict() for user in users])


@user_bp.route('/create', methods=['POST'])
@jwt_required()
def add_user():
    user_data = request.get_json()
    new_user = create_user(user_data)
    return jsonify(new_user.to_dict()), 201
