import unittest
from unittest.mock import patch, MagicMock
from services.amadeus_service import search_flights

class TestAmadeusService(unittest.TestCase):
    @patch('services.amadeus_service.get_amadeus_token', return_value='fake-token')
    @patch('services.amadeus_service.requests.get')
    def test_search_flights(self, mock_get, _):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "price": {"total": "150.00"},
                    "itineraries": [{"segments": [{"carrierCode": "AA"}]}]
                }
            ],
            "dictionaries": {
                "carriers": {
                    "AA": "American Airlines"
                }
            }
        }
        mock_get.return_value = mock_response
        result = search_flights("NYC", "LAX", "2025-09-01")
        self.assertEqual(result["airline"], "American Airlines")
        self.assertEqual(result["price"], 150.00)
