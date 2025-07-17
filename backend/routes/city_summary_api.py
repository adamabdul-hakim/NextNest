from flask import Blueprint, request, jsonify
from services.gemini_service import get_city_summary

city_bp = Blueprint('city_summary', __name__)

@city_bp.route('/api/city-summary', methods=['GET'])
def city_summary():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing city parameter"}), 400

    try:
        data = get_city_summary(city)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
