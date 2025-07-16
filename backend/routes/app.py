from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_api import get_weather_details

app = Flask(__name__)
CORS(app) 

@app.route("/get_weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")
    weather = get_weather_details(city)  
    return jsonify(weather)

if __name__ == "__main__":
    app.run(debug=True)
