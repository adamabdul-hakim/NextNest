from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_api import get_lat_lon, get_weather_forecast
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/get_weather/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)



@app.route("/get_weather/<city>", methods=["POST"])
def get_weather(city):
    data = request.get_json()

    if not city:
        return jsonify({"error": "City is required"}), 400

    lat, lon = get_lat_lon(city)
    if not lat or not lon:
        return jsonify({"error": "Invalid city or not found"}), 404

    forecast = get_weather_forecast(lat, lon)
    if not forecast:
        return jsonify({"error": "Weather data unavailable"}), 500

    return jsonify({
        "city": city,
        "lat": lat,
        "lon": lon,
        "forecast": forecast
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

