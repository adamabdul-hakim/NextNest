from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create Flask Blueprint
autocomplete_bp = Blueprint("autocomplete", __name__)
transportation_bp = Blueprint('transportation', __name__)

@autocomplete_bp.route("/api/suggest", methods=["GET"])
def suggest():
    field = request.args.get("field")
    user_input = request.args.get("input", "").strip()

    if not user_input or not field:
        return jsonify({"suggestions": []})

    # Construct GPT prompt based on the field
    if field in ["originCity", "destinationCity"]:
        prompt = f"Suggest 5 U.S. cities that start with '{user_input}'. Give only the suggestions. No other information please."
    elif field == "role":
        prompt = f"Suggest 5 tech job titles that start with '{user_input}'. Give only the suggestions. No other information please."
    else:
        return jsonify({"suggestions": []})

    try:
        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.6,
        )

        # Parse and clean suggestions
        output = response.choices[0].message.content
        suggestions = [
            line.strip().lstrip("1234567890. ").strip()
            for line in output.split("\n") if line.strip()
        ]

        return jsonify({"suggestions": suggestions})
    
    except Exception as e:
        print("OpenAI API error:", e)
        return jsonify({"suggestions": []})
    
@transportation_bp.route("/api/transportation", methods=["GET"])
def transportation():
    user_input = request.args.get("city", "").strip()

    if not user_input:
        return jsonify({"error": "No city provided"})

    prompt = (
        f"For the city of {user_input}, provide transportation scores on a scale from 0 to 100.\n\n"
        "Respond with only the following format:\n\n"
        "Walk Score: <0-100> <short description>\n"
        "Bike Score: <0-100> <short description>\n"
        "Drive Score: <0-100> <short description>\n\n"
        "If the city is unknown or not found, respond with 'Unknown city.'"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.5,
        )

        output = response.choices[0].message.content.strip()

        if "Unknown city" in output:
            return jsonify({"error": "Unknown city"})

        lines = output.splitlines()
        result = {
            "city": user_input,
            "walk": {},
            "bike": {},
            "drive": {}
        }

        for line in lines:
            if line.startswith("Walk Score:"):
                parts = line.replace("Walk Score:", "").strip().split(" ", 1)
                result["walk"] = {"score": int(parts[0]), "description": parts[1]}
            elif line.startswith("Bike Score:"):
                parts = line.replace("Bike Score:", "").strip().split(" ", 1)
                result["bike"] = {"score": int(parts[0]), "description": parts[1]}
            elif line.startswith("Drive Score:"):
                parts = line.replace("Drive Score:", "").strip().split(" ", 1)
                result["drive"] = {"score": int(parts[0]), "description": parts[1]}

        return jsonify(result)

    except Exception as e:
        print("OpenAI API error:", e)
        return jsonify({"error": "Failed to fetch transportation data"})
