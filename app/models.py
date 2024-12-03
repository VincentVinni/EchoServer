from app.db import supabase
import json
import os 
import uuid

def upload_photo_to_bucket(file_path):
    """Uploads a photo to the Supabase bucket."""
    unique_filename = f"{uuid.uuid4()}.jpg"  # Generate a unique filename
    bucket_name = "photo-echos"

    with open(file_path, "rb") as file:
        response = supabase.storage.from_(bucket_name).upload(
            unique_filename, file, {"upsert": True}
        )

    if "error" in response:
        raise Exception(f"Error uploading file: {response['error']}")

    # Retrieve the public URL
    public_url = supabase.storage.from_(bucket_name).get_public_url(unique_filename)
    return public_url


"""Echo Database Models and Functions"""
def create_text_echo(user_id, message, expires_at, type="text", public_url=None, path_to_file=None):
    """Insert a new echo into the Supabase database."""
    response = (supabase.table("Echo").insert({"user_id": user_id, "message": message, "expires_at": expires_at, "type": type, "public_url": public_url,"bucket_path": path_to_file}).execute())

    response_data = response.json()
    if isinstance(response_data, str):  # If it's a string, parse it
        response_data = json.loads(response_data)
    
    # Extract the 'data' field and return
    return response_data.get("data", [])
    
def get_user_echos(user_id):
    """Retrieve all echoes for a specific user."""
    response = (supabase.table("Echo").select("*").eq("user_id", user_id).execute())

    response_data = response.json()
    if isinstance(response_data, str):  # If it's a string, parse it
        response_data = json.loads(response_data)

    # Extract the 'data' field and return 
    return response_data.get("data", [])

def get_specific_echo(user_id, echo_id):
    """Retrieve a specific echo for a specific user."""
    response = (supabase.table("Echo").select("*").eq("user_id", user_id).eq("id", echo_id).execute())

    response_data = response.json()
    if isinstance(response_data, str):  # If it's a string, parse it
        response_data = json.loads(response_data)

    # Extract the 'data' field and return 
    return response_data.get("data", [])

"""Echo s3 Storage Models and Functions"""
def upload_photo_echo():
    """Upload a photo to S3."""
    unique_filename = f"{uuid.uuid4()}.jpg"  # Generate a unique filename
    file_path = os.path.join(os.path.dirname(__file__), 'assets/banana.png') # Dynamically construct the full path
    file_path = os.path.abspath(file_path) # Ensure the path is normalized
    
    # Validate that the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, 'rb') as f:
            response = supabase.storage.from_("photo-echos").upload(
                file=f,
                path=f"{unique_filename}",  # Path inside the bucket
                file_options={"cache-control": "3600", "upsert": "false"},
            )
    except Exception as e:
        raise Exception(f"Error uploading photo: {e}")
    
    public_url = supabase.storage.from_("photo-echos").get_public_url(unique_filename)
    return [response, public_url, unique_filename] # return response, public_url, and path_to_file in bucket (for deletion)

def upload_video_echo():
    """Upload a video to S3."""
    unique_filename = f"{uuid.uuid4()}.mp3"  # Generate a unique filename
    file_path = os.path.join(os.path.dirname(__file__), 'assets/test.mp3') # Dynamically construct the full path
    file_path = os.path.abspath(file_path) # Ensure the path is normalized
    
    # Validate that the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, 'rb') as f:
            response = supabase.storage.from_("video-echos").upload(
                file=f,
                path=f"{unique_filename}",  # Path inside the bucket
                file_options={"cache-control": "3600", "upsert": "false"},
            )
    except Exception as e:
        raise Exception(f"Error uploading video: {e}")
    
    public_url = supabase.storage.from_("photo-echos").get_public_url(unique_filename)
    return [response, public_url, unique_filename] # return response, public_url, and path_to_file in bucket (for deletion)

# User Database Models and Functions 
def create_user(data):
    """Insert a new user into the Supabase database."""
    response = supabase.table("users").insert(data).execute()
    if response.status_code != 200:
        raise Exception(f"Error inserting user: {response.json()}")
    return response.json()

def get_user_by_email(email):
    """Retrieve a user by email."""
    response = supabase.table("users").select("*").eq("email", email).execute()
    if response.status_code != 200:
        raise Exception(f"Error fetching user: {response.json()}")
    return response.json()
