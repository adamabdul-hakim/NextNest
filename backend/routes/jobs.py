# Defines the Flask routes for the Jobs API, 
# handling requests and returning job data as JSON

from flask import Blueprint, request, jsonify
from services.adzuna_service import get_jobs

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/api/jobs', methods=['GET'])
def jobs():
    field = request.args.get('field')
    state = request.args.get('state')
    count = get_jobs(field, state)
    return jsonify({"field": field, "state": state, "job_count": count})
