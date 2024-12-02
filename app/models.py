from app.db import supabase
import json

# Echo Database Models and Functions 
def create_text_echo(user_id, message, expires_at):
    """Insert a new echo into the Supabase database."""
    response = (supabase.table("Echo").insert({"user_id": user_id, "message": message, "expires_at": expires_at}).execute())

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
