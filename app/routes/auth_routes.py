from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import check_password_hash

from app import jwt
from app.models.user_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

blacklisted_tokens = set()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in blacklisted_tokens


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad email or password"}), 401


@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    blacklisted_tokens.add(get_jwt()['jti'])
    return jsonify(msg='Successfully logged out'), 200
