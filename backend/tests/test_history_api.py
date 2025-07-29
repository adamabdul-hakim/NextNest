import unittest
from unittest.mock import patch
from app import app

class TestHistoryAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user_id = "11111111-1111-1111-1111-111111111111"

    @patch("routes.history_api.verify_request")
    @patch("routes.history_api.save_search")
    def test_add_history(self, mock_save, mock_verify):
        mock_verify.return_value = ({"sub": self.user_id}, None, None)
        payload = {
            "origin_city": "Boston",
            "destination_city": "Miami",
            "role": "Engineer",
            "travel_date": "2025-10-01"
        }

        res = self.client.post("/api/history", json=payload)
        self.assertEqual(res.status_code, 201)
        self.assertIn("Saved", res.get_json()["message"])

    @patch("routes.history_api.verify_request")
    @patch("routes.history_api.get_history")
    def test_get_history(self, mock_get, mock_verify):
        mock_verify.return_value = ({"sub": self.user_id}, None, None)
        mock_get.return_value = [{"origin_city": "Boston"}]

        res = self.client.get("/api/history")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()[0]["origin_city"], "Boston")

    @patch("routes.history_api.verify_request")
    @patch("routes.history_api.clear_history")
    def test_clear_history(self, mock_clear, mock_verify):
        mock_verify.return_value = ({"sub": self.user_id}, None, None)

        res = self.client.delete("/api/history/clear")
        self.assertEqual(res.status_code, 200)
        self.assertIn("cleared", res.get_json()["message"].lower())
