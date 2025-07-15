import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


def get_jobs(field, state):
    url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": field,
        "where": state
    }
    response = requests.get(url, params=params)
    data = response.json()
    # Return the total job count
    return data.get("count", 0)