from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.flights_api import flights_bp
from routes.jobs_api import jobs_bp
from routes.city_summary_api import city_bp
from routes.history_api import history_bp
from routes.openai import autocomplete_bp, transportation_bp


load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(flights_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(city_bp)
app.register_blueprint(history_bp)
app.register_blueprint(autocomplete_bp)
app.register_blueprint(transportation_bp)



@app.route("/")
def index():
    return {"message": "Welcome to NextNest API"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
