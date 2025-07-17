from flask import Blueprint, request, jsonify
from services.history_service import save_search, get_history

history_bp = Blueprint('history', __name__)

@history_bp.route('/api/history', methods=['GET'])
def fetch_history():
    data = get_history()
    return jsonify(data)

@history_bp.route('/api/history', methods=['POST'])
def add_history():
    data = request.get_json()
    origin_city = data.get('origin_city')
    destination_city = data.get('destination_city')
    role = data.get('role')
    travel_date = data.get('travel_date')
    save_search(origin_city, destination_city, role, travel_date)
    return jsonify({"message": "Saved successfully"}), 201

@history_bp.route('/api/history/clear', methods=['DELETE'])
def clear_all_history():
    from services.history_service import clear_history
    clear_history()
    return jsonify({"message": "History cleared successfully"})
