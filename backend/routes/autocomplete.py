from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key="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")

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
        prompt = f"Suggest 5 U.S. cities that start with '{user_input}'"
    elif field == "role":
        prompt = f"Suggest 5 tech job titles that start with '{user_input}'"
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
