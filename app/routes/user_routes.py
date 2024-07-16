from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.routes import url_prefix
from app.services.user_service import get_all_users, create_user

user_bp = Blueprint('user', __name__, url_prefix=f'{url_prefix}/user')


@user_bp.route('/list', methods=['GET'])
@jwt_required()
def get_users():
    """
        Returns all registered users.
        ---
        responses:
          200:
            examples:
              application/json: [
                {
                    "email": "admin@example.com",
                    "name": "Admin"
                },
                {
                    "email": "flavio.ramos@gmail.com",
                    "name": "Flavio"
                }
            ]

    """
    users = get_all_users()
    return jsonify([user.to_dict() for user in users])


@user_bp.route('/create', methods=['POST'])
@jwt_required()
def add_user():
    """
        Creates a new user.
        ---
        consumes:
            - application/json
        parameters:
            -   in: body
                schema:
                    type: object
                    required:
                        - email
                        - name
                        - password
                    properties:
                        email:
                            type: string
                        name:
                            type: string
                        password:
                            type: string
        responses:
          200:
            examples:
              application/json: {
                    "email": "user@email.com",
                    "name": "User Name"
                }
    """
    user_data = request.get_json()
    new_user = create_user(user_data)
    return jsonify(new_user.to_dict()), 201
