import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_access_token(client_id, client_secret):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=payload)
    return response.json()['access_token']

def get_cheapest_destinations(origin, token):
    url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "origin": origin,
        "oneWay": "true",
        "currencyCode": "USD",
    }
    res = requests.get(url, headers=headers, params=params)
    return res.json().get("data", [])

def get_flight_offer(origin, destination, date, token):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "currencyCode": "USD",
        "max": 1
    }
    res = requests.get(url, headers=headers, params=params)
    return res.json().get("data", [])


CLIENT_ID = os.environ['FLIGHT_API_KEY']
CLIENT_SECRET = os.environ['FLIGHT_API_SECRET']

token = get_access_token(CLIENT_ID, CLIENT_SECRET)
destinations = get_cheapest_destinations("NYC",  token)
print(destinations)

if destinations:
    first = destinations[0]
    dest_code = first["destination"]
    departure_date = first["departureDate"]
    print(f"Cheapest destination from JFK: {dest_code} on {departure_date} for ${first['price']['total']}")

    offer = get_flight_offer("JFK", dest_code, departure_date, token)
    if offer:
        offer_info = offer[0]
        print("\nFlight Offer:")
        print("Price:", offer_info['price']['total'], offer_info['price']['currency'])
        for seg in offer_info['itineraries'][0]['segments']:
            print(f"{seg['departure']['iataCode']} → {seg['arrival']['iataCode']}")
            print("Airline:", seg['carrierCode'], "| Flight Number:", seg['number'])
else:
    print("No destinations found.")