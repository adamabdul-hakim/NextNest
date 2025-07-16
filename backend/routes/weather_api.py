
# tmdb_api.py - TMDB API

import requests
from dotenv import load_dotenv
import os
from gemini_api import get_lat_lon

load_dotenv()
city = input("Where are you flying to? ")
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']


geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}"
geo_data = requests.get(geo_url).json()

lat = geo_data[0]['lat']
lon = geo_data[0]['lon']


#WEATHER_API_KEY_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY_URL = "https://api.openweathermap.org/data/3.0/onecall"

def get_movie_details():
    params = {
        'appid': WEATHER_API_KEY,
        "limit": 1,
        "lat": lat,
        "lon": lon,
        "units": "imperial"
    }

    response = requests.get(WEATHER_API_KEY_URL, params=params)

    if response.status_code == 200 and response.json():
        data = response.json()
        for day in data['daily']:
            from datetime import datetime
            dt = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
            description = day['weather'][0]['description']
            temp = day['temp']['day']
            print(f"{dt}: {description}, {temp}°F")
    else:
        return {'error': 'Movie not found on TMDB.'}

print(get_movie_details())
