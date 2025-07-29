import unittest
from unittest.mock import patch
from app import app

class TestFlightsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch("routes.flights_api.search_flights")
    @patch("routes.flights_api.get_airport_code", side_effect=["JFK", "LAX"])
    def test_flights_success(self, mock_get_code, mock_search):
        mock_search.return_value = {
            "airlineCode": "AA",
            "airline": "American Airlines",
            "price": 123.45,
            "departureTime": "2025-09-01T10:00",
            "arrivalTime": "2025-09-01T14:00"
        }

        res = self.client.get("/api/flights?origin=New+York&destination=Los+Angeles&date=2025-09-01")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["airline"], "American Airlines")
        self.assertEqual(data["airlineCode"], "AA")
        self.assertEqual(data["price"], 123.45)

    def test_flights_missing_param(self):
        res = self.client.get("/api/flights?origin=NYC")
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertIn("error", data)
