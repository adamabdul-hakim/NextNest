import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")

def get_amadeus_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def search_flights(origin, destination, date):
    token = get_amadeus_token()
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "max": 20
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    carriers_map = data.get("dictionaries", {}).get("carriers", {})

    offers = []
    for offer in data.get("data", []):
        price = float(offer["price"]["total"])
        carrier_code = offer["itineraries"][0]["segments"][0].get("carrierCode")
        airline_name = carriers_map.get(carrier_code, "Unknown airline")
        offers.append({
            "airlineCode": carrier_code,
            "airline": airline_name,
            "price": price
        })

    if not offers:
        return {"message": "No flights found"}

    cheapest = min(offers, key=lambda x: x["price"])
    return cheapest