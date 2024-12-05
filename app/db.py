from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables (make sure to set these in your .env or environment)
SUPABASE_URL = "https://foweikjmjpvxscdguhby.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZvd2Vpa2ptanB2eHNjZGd1aGJ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzMxMTUyODMsImV4cCI6MjA0ODY5MTI4M30.Tgsd34-cDkFdI2dGmlVPaw7I_wXu5w_07rtLaX61nBM"

# Initialize Supabase client
def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase URL and Key must be set in environment variables.")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = get_supabase_client()
