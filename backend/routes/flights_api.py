from flask import Blueprint, request, jsonify
from services.amadeus_service import search_flights

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/api/flights', methods=['GET'])
def flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date = request.args.get('date')

    if not origin or not destination or not date:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        results = search_flights(origin, destination, date)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500