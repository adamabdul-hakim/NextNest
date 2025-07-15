import os
import requests
from dotenv import load_dotenv

load_dotenv()

RENTCAST_KEY = os.getenv("RENTCAST_API_KEY")

def get_housing(state):
    url = "https://api.rentcast.io/v1/listings"  # or endpoint for rent data
    params = {
        "state": state,
        "status": "active",
        "limit": 1
    }
    headers = {
        "X-Api-Key": RENTCAST_KEY
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # Process data to get median or example rent
    return data  # adjust based on API docs