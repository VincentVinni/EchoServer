from flask import Blueprint, jsonify, request

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def hello_world():
    # Logic to retrieve users
    return jsonify({"message": "Hello Monkey!"})

@user_bp.route("/", methods=["POST"])
def create_user():
    # Logic to create a user
    data = request.json
    return jsonify({"message": "User created", "data": data}), 201
