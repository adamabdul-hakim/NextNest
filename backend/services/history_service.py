import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validate env variables
if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase URL or Key not set in .env")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Services ---
def save_search(origin_city, destination_city, role, travel_date):
    data = {
        "origin_city": origin_city,
        "destination_city": destination_city,  # match your Supabase column name
        "role": role,
        "travel_date": travel_date
    }
    # execute() will raise an exception if something is wrong
    supabase.table("history").insert(data).execute()

def get_history():
    response = supabase.table("history").select("*").order("id", desc=True).execute()
    return response.data


def clear_history():
    supabase.table("history").delete().neq("id", 0).execute()