from flask import jsonify, request
from app.models import create_text_echo, get_user_echos, get_specific_echo, upload_photo_echo, upload_video_echo

def create_text_echo_controller(type="text", public_url="", path_to_file=""):
    """Handles the request to create a new echo."""
    try:
        data = request.json
        user_id, message, expires_at = data["user_id"], data["message"], data["expires_at"]
        echo = create_text_echo(user_id, message, expires_at, type, public_url, path_to_file)

        if type=="photo" or type=="video":
            return echo 
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

"""s3 Bucket Models and Functions"""
def upload_photo_echo_controller():
    data = request.json 
    abs_path = data["abs_path"] # content in this case contains the abs_path to the image

    try:
        photo_response, public_url, path_to_file = upload_photo_echo() # change endpoint to pass in abs_path into upload_photo_echo()
        echo_db_response = create_text_echo_controller(type="photo", public_url=public_url, path_to_file=path_to_file) # embed public_url to the row in the Echo specific database 
        # return jsonify({"photo_response": photo_response, "text_response": text_response})
        # return jsonify({"photo_s3_response": photo_response, "echo_db_response": echo_db_response}), 201
        return echo_db_response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def upload_video_echo_controller():
    data = request.json 
    abs_path = data["abs_path"] 

    try:
        video_s3_response, public_url, path_to_file = upload_video_echo() # change endpoint to pass in abs_path into upload_photo_echo()
        echo_db_response = create_text_echo_controller(type="video", public_url=public_url, path_to_file=path_to_file) # embed public_url to the row in the Echo specific database 

        return jsonify({"video_s3_response": video_s3_response, "echo_db_response": echo_db_response}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
