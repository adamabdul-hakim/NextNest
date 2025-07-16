
# tmdb_api.py - TMDB API

import requests
from dotenv import load_dotenv
import os
from gemini_api import get_lat_lon

load_dotenv()
city = input("Where are you flying to? ")



WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
WEATHER_API_KEY_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_movie_details():
    params = {
        'appid': WEATHER_API_KEY,
        'q': city,
        "limit": 1
    }

    response = requests.get(WEATHER_API_KEY_URL, params=params)

    if response.status_code == 200 and response.json():
        data = response.json()
        return data
    else:
        return {'error': 'Movie not found on TMDB.'}

print(get_movie_details())
