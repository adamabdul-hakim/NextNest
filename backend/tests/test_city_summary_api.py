import unittest
from unittest.mock import patch
from app import app

class TestCitySummaryAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch("routes.city_summary_api.get_city_summary")
    def test_city_summary_success(self, mock_summary):
        mock_summary.return_value = {
            "average_temp": 75,
            "summary": "Great for sun lovers."
        }

        res = self.client.get("/api/city-summary?city=Los+Angeles")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["average_temp"], 75)
        self.assertIn("sun", data["summary"].lower())

    def test_city_summary_missing_param(self):
        res = self.client.get("/api/city-summary")
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertIn("error", data)
