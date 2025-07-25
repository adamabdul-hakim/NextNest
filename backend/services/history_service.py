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
def save_search(origin_city, destination_city, role, travel_date, user_id):
    data = {
        "origin_city": origin_city,
        "destination_city": destination_city,
        "role": role,
        "travel_date": travel_date,
        "user_id": user_id  # ✅ associate record with a user
    }
    supabase.table("history").insert(data).execute()

def get_history(user_id):
    response = (
        supabase.table("history")
        .select("*")
        .eq("user_id", user_id)          # ✅ only fetch this user's history
        .order("id", desc=True)
        .execute()
    )
    return response.data

def clear_history(user_id):
    supabase.table("history").delete().eq("user_id", user_id).execute()  # ✅ only delete this user's history
