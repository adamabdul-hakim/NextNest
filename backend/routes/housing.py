from flask import Blueprint, request, jsonify
from services.housing_service import get_housing

housing_bp = Blueprint('housing', __name__)

@housing_bp.route('/api/housing', methods=['GET'])
def housing():
    state = request.args.get('state')
    housing_data = get_housing(state)
    return jsonify(housing_data)