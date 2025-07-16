# weather_api.py

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
WEATHER_API_KEY_URL = "https://api.openweathermap.org/data/3.0/onecall"

def get_lat_lon(city):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={WEATHER_API_KEY}"
    geo_data = requests.get(geo_url).json()

    if not geo_data:
        return None, None
    return geo_data[0]['lat'], geo_data[0]['lon']

def get_weather_forecast(lat, lon):
    params = {
        'appid': WEATHER_API_KEY,
        'lat': lat,
        'lon': lon,
        'units': 'imperial',
        'exclude': 'minutely,hourly,alerts,current'
    }

    response = requests.get(WEATHER_API_KEY_URL, params=params)
    if response.status_code != 200:
        return None

    forecast = []
    for day in response.json().get('daily', []):
        dt = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
        description = day['weather'][0]['description']
        temp = day['temp']['day']
        forecast.append({
            "date": dt,
            "description": description,
            "temperature": f"{temp}°F"
        })

    return forecast
