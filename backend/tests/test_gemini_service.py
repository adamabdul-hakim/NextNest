import unittest
from unittest.mock import patch
from services.gemini_service import get_airport_code, get_city_summary

class TestGeminiAirportCode(unittest.TestCase):
    @patch("services.gemini_service.model.generate_content")
    def test_get_airport_code(self, mock_generate):
        mock_generate.return_value.text = "JFK"
        code = get_airport_code("New York")
        self.assertEqual(code, "JFK")

class TestGeminiCitySummary(unittest.TestCase):
    @patch("services.gemini_service.model.generate_content")
    def test_get_city_summary(self, mock_generate):
        mock_generate.return_value.text = '{"average_temp": 75, "summary": "Great for sun lovers."}'
        result = get_city_summary("Los Angeles")
        self.assertEqual(result["average_temp"], 75)
        self.assertIn("sun", result["summary"].lower())
