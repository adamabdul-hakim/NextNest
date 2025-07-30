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
jobs_comparison_bp = Blueprint("salary_comparison", __name__)

@autocomplete_bp.route("/api/suggest", methods=["GET"])
def suggest():
    field = request.args.get("field")
    user_input = request.args.get("input", "").strip()

    print("👉 /api/suggest hit:", {"field": field, "input": user_input})

    if not user_input or not field:
        return jsonify({"suggestions": []})

    if field in ["originCity", "destinationCity"]:
        prompt = f"Suggest 5 U.S. cities that start with '{user_input}'. Only list the cities."
    elif field in ["role", "current_role"]:
        prompt = f"Suggest 5 tech job titles that start with '{user_input}'. Only list the titles."
    else:
        return jsonify({"suggestions": []})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
            temperature=0.6,
        )

        output = response.choices[0].message.content
        print("✅ GPT raw output:", output)

        suggestions = [
            line.strip().lstrip("1234567890. ").strip()
            for line in output.split("\n") if line.strip()
        ]

        return jsonify({"suggestions": suggestions})

    except Exception as e:
        print("❌ OpenAI API error:", e)
        return jsonify({"suggestions": [], "error": str(e)}), 500
 
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


@jobs_comparison_bp.route("/api/salary-comparison", methods=["GET"])
def salary_comparison():
    origin = request.args.get("originCity", "").strip()
    destination = request.args.get("destinationCity", "").strip()
    current_role = request.args.get("current_role", "").strip()
    desired_role = request.args.get("role", "").strip()

    if not origin or not destination or not current_role or not desired_role:
        return jsonify({"error": "Missing one or more required fields"}), 400

    # Role alias map
    role_aliases = {
        "software engineer": ["software developer", "full stack developer", "backend engineer", "frontend developer"],
        "data scientist": ["ml engineer", "machine learning engineer"],
        # Extend this list as needed
    }

    def roles_are_equivalent(r1, r2):
        r1, r2 = r1.lower(), r2.lower()
        if r1 == r2:
            return True
        for key, aliases in role_aliases.items():
            if (r1 == key and r2 in aliases) or (r2 == key and r1 in aliases):
                return True
        return False

    is_similar = "no"

    # First check manual equivalents
    if roles_are_equivalent(current_role, desired_role):
        is_similar = "yes"
    else:
        # Use GPT to determine similarity if no manual match
        similarity_prompt = (
            f"Are the job titles '{current_role}' and '{desired_role}' considered similar or equivalent in most companies in terms of duties, required skills, or industry context?\n"
            "Answer only with 'Yes' or 'No'. If they are commonly used interchangeably or overlap greatly, respond with 'Yes'."
        )

        try:
            similarity_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": similarity_prompt}],
                max_tokens=5,
                temperature=0.2,
            )

            is_similar = similarity_response.choices[0].message.content.strip().lower()
        except Exception as e:
            print("Similarity check failed:", e)

    # Continue regardless of similarity result (just include a note)
    comparison_prompt = (
        f"Compare the average salary for a {desired_role} in {origin} vs {destination}.\n\n"
        "Respond only in the following format:\n\n"
        "Origin City: <salary> <short description>\n"
        "Destination City: <salary> <short description>\n"
        "Overall Comparison: <short summary of differences>\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": comparison_prompt}],
            max_tokens=250,
            temperature=0.5,
        )

        output = response.choices[0].message.content.strip()
        lines = output.splitlines()

        result = {
            "origin": origin,
            "destination": destination,
            "current_role": current_role,
            "desired_role": desired_role,
            "origin_salary": {},
            "destination_salary": {},
            "summary": "",
            "match": is_similar == "yes"
        }

        for line in lines:
            if line.startswith("Origin City:"):
                parts = line.replace("Origin City:", "").strip().split(" ", 1)
                result["origin_salary"] = {
                    "amount": parts[0],
                    "description": parts[1] if len(parts) > 1 else ""
                }
            elif line.startswith("Destination City:"):
                parts = line.replace("Destination City:", "").strip().split(" ", 1)
                result["destination_salary"] = {
                    "amount": parts[0],
                    "description": parts[1] if len(parts) > 1 else ""
                }
            elif line.startswith("Overall Comparison:"):
                result["summary"] = line.replace("Overall Comparison:", "").strip()

        # If GPT said no, include a soft warning message
        if is_similar != "yes":
            result["note"] = f"Roles '{current_role}' and '{desired_role}' may not be identical, but salary comparison is still provided."

        return jsonify(result)

    except Exception as e:
        print("OpenAI API error:", e)
        return jsonify({"error": "Failed to fetch salary comparison"}), 500
