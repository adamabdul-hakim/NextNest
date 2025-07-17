import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

def get_jobs(field, location):
    url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 3,        # only return 3 jobs
        "what": field,                # job field
        "where": location             # city or state
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    jobs = []
    for job in data.get("results", [])[:3]:  # just in case, slice again
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "redirect_url": job.get("redirect_url")
        })

    return jobs
