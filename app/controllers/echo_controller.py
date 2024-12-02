from flask import jsonify, request
from app.models import create_text_echo, get_user_echos, get_specific_echo

def create_text_echo_controller():
    """Handles the request to create a new echo."""
    try:
        data = request.json
        user_id, content, expires_at = data["user_id"], data["content"], data["expires_at"]
        echo = create_text_echo(user_id, content, expires_at)
        return jsonify({"message": "Echo created", "data": echo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_user_echos_controller():
    """Handles the request to retrieve all echoes."""
    data = request.json
    user_id = data["user_id"]
    
    try:
        echoes = get_user_echos(user_id)
        return jsonify({"data": echoes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_specific_echo_controller():
    """Handles the request to retrieve a specific echo."""
    data = request.json
    user_id, echo_id = data["user_id"], data["echo_id"]
    
    try:
        echo = get_specific_echo(user_id, echo_id)
        return jsonify({"data": echo}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
