from flask import Blueprint, request, jsonify
from services.adzuna_service import get_jobs

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/api/jobs', methods=['GET'])
def jobs():
    field = request.args.get('field')
    location = request.args.get('location')

    if not field or not location:
        return jsonify({"error": "Missing required parameters: field and location"}), 400

    try:
        jobs_list = get_jobs(field, location)
        return jsonify(jobs_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
