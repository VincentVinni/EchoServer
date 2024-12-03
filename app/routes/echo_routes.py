from flask import Blueprint, jsonify, request
from app.controllers.echo_controller import create_text_echo_controller, get_user_echos_controller, get_specific_echo_controller, upload_photo_echo_controller, upload_video_echo_controller

echo_bp = Blueprint("echos", __name__, url_prefix="/echos")

@echo_bp.route("/get_all", methods=["POST"])
def get_all():
    # Logic to retrieve users
    return get_user_echos_controller()

@echo_bp.route("/upload_text_echo", methods=["POST"])
def upload_text_echo():
    # Logic to upload a text echo
    return create_text_echo_controller()

@echo_bp.route("/get_specific", methods=["POST"])
def get_specific():
    # Logic to fetch specific echo
    return get_specific_echo_controller()

"""s3 Bucket Photo and Vidoe Echo Routes"""
@echo_bp.route("/upload_photo_echo", methods=["POST"])
def upload_photo_echo():
    # Attempt to upload the photo
    try:
        response = upload_photo_echo_controller() 
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # Handle the error (e.g., log it, return an error response)
    
    return response 


@echo_bp.route("/upload_video_echo", methods=["POST"])
def upload_video_echo():
    # Attempt to upload the photo
    try:
        response = upload_video_echo_controller() 
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # Handle the error (e.g., log it, return an error response)
    
    return response 