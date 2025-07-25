from flask import Blueprint, request, jsonify
from services.history_service import save_search, get_history, clear_history
from auth_utils import verify_request  # ✅ import the helper

history_bp = Blueprint('history', __name__)

@history_bp.route('/api/history', methods=['POST'])
def add_history():
    # ✅ verify token
    payload, error_resp, status = verify_request()
    if error_resp:
        return error_resp, status

    data = request.get_json()
    origin_city = data.get('origin_city')
    destination_city = data.get('destination_city')
    role = data.get('role')
    travel_date = data.get('travel_date')

    # ✅ get user_id from token
    user_id = payload['sub']
    save_search(origin_city, destination_city, role, travel_date, user_id)

    return jsonify({"message": "Saved successfully"}), 201


@history_bp.route('/api/history', methods=['GET'])
def fetch_history():
    payload, error_resp, status = verify_request()
    if error_resp:
        return error_resp, status

    user_id = payload['sub']
    history = get_history(user_id)
    return jsonify(history), 200


@history_bp.route('/api/history/clear', methods=['DELETE'])
def clear_all_history():
    payload, error_resp, status = verify_request()
    if error_resp:
        return error_resp, status

    user_id = payload['sub']
    clear_history(user_id)
    return jsonify({"message": "History cleared"}), 200
