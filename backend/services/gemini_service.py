import os
import json
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env")

# Configure the Gemini SDK
configure(api_key=api_key)

# Use a model instance (recommended: "gemini-1.5-flash")
model = GenerativeModel("gemini-1.5-flash")


def get_airport_code(city_name: str) -> str:
    prompt = (
        "You are an assistant that returns only valid IATA airport codes. "
        f"Given the city '{city_name}', return ONLY the closest major airport IATA code. "
        "Return just the 3-letter code, nothing else."
    )
    response = model.generate_content(prompt)
    return response.text.strip()


def get_city_summary(city_name: str) -> dict:
    prompt = (
        "You are an assistant that returns information in JSON. "
        f"Given the city '{city_name}', provide:\n"
        "1. The approximate average yearly temperature in Fahrenheit (integer or rounded).\n"
        "2. A short friendly sentence describing the type of people who would enjoy living or visiting there, "
        "based on climate and general lifestyle.\n"
        "Return the result strictly in JSON format with keys 'average_temp' and 'summary'. "
        "Do not include any Markdown, code blocks, or explanations—ONLY JSON."
    )

    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    # Remove markdown fences if needed
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        lines = raw_text.splitlines()
        json_part = "\n".join(
            line for line in lines if not line.strip().startswith("```") and not line.lower().startswith("json")
        )
    else:
        json_part = raw_text

    try:
        return json.loads(json_part)
    except json.JSONDecodeError:
        return {"average_temp": None, "summary": raw_text}
