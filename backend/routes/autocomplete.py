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
