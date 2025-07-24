import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")
if not my_api_key:
    raise ValueError("Missing YOUTUBE_API_KEY in .env")

# Create the client
client = genai.Client(api_key=my_api_key)


def get_airport_code(city_name: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an assistant that returns only valid IATA airport codes. "
                "Given a city name, return ONLY the closest major airport IATA code. "
                "Return just the 3-letter code, nothing else."
            )
        ),
        contents=city_name,
    )

    return response.text.strip()

def get_city_summary(city_name: str) -> dict:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an assistant that returns information in JSON. "
                "Given a city name, provide: "
                "1. The approximate average yearly temperature in Fahrenheit (integer or rounded). "
                "2. A short friendly sentence describing the type of people who would enjoy living or visiting there, "
                "based on climate and general lifestyle. "
                "Return the result strictly in JSON format with keys 'average_temp' and 'summary'. "
                "Do not include any Markdown, code blocks, or explanations—ONLY JSON."
            )
        ),
        contents=city_name,
    )

    raw_text = response.text.strip()


    # Remove markdown code fences if present
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")  # remove backticks
        # split by newline and find the JSON part
        lines = raw_text.splitlines()
        json_part = "\n".join(line for line in lines if not line.strip().startswith("```") and not line.strip().lower().startswith("json"))
    else:
        json_part = raw_text

    import json
    try:
        data = json.loads(json_part)
    except json.JSONDecodeError:
        # fallback: return as summary
        data = {"average_temp": None, "summary": raw_text}

    return data

def get_airline_name(iata_code: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are an assistant that returns the full name of an airline given its IATA code. "
                "Respond only with the airline name, with no extra text. "
                "If the code is unknown or invalid, say 'Unknown airline'."
            )
        ),
        contents=iata_code,
    )

    name = response.text.strip()
    return name
