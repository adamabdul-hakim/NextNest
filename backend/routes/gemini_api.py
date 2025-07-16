import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ['GEMINI_API_KEY']
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
def get_movie_recommendation(feeling):
    prompt = f"""
    I am feeling {feeling}.
    Please recommend ONE SPECIFIC MOVIE that matches this mood.
    :sparkles: IMPORTANT: Only respond with the movie title on the FIRST line. Do not include any explanation, description, or follow-up questions. Return ONLY the movie title.
    Example:
    The Pursuit of Happyness
    """
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(GEMINI_URL, json=body)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return "Error fetching recommendation from Gemini."