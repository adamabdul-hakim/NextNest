from flask import Blueprint, request, jsonify
from services.amadeus_service import search_flights
from services.gemini_service import get_airport_code

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/api/flights', methods=['GET'])
def flights():
    origin_city = request.args.get('origin')
    destination_city = request.args.get('destination')
    date = request.args.get('date')

    if not origin_city or not destination_city or not date:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        origin_code = get_airport_code(origin_city)
        destination_code = get_airport_code(destination_city)

        if not origin_code or not destination_code:
            return jsonify({"error": "Could not resolve airport codes"}), 400

        cheapest = search_flights(origin_code, destination_code, date)

        airline_code = cheapest.get("airlineCode")
        airline_name = cheapest.get("airline")

        result = {
            "airline": airline_name,
            "airlineCode": airline_code,
            "price": cheapest.get("price"),
            "departureTime": cheapest.get("departureTime"),
            "arrivalTime": cheapest.get("arrivalTime"),
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
