import unittest
from unittest.mock import patch, MagicMock
from services.adzuna_service import get_jobs
from services.amadeus_service import search_flights
from services.gemini_service import get_airport_code, get_city_summary
from services.history_service import get_history, save_search, clear_history

# 1. Test Adzuna get_jobs
class TestAdzunaService(unittest.TestCase):
    @patch('services.adzuna_service.requests.get')
    def test_get_jobs(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "title": "Backend Developer",
                    "company": {"display_name": "TechCorp"},
                    "location": {"display_name": "Austin, TX"},
                    "redirect_url": "http://example.com/job1"
                }
            ]
        }
        mock_get.return_value = mock_response
        jobs = get_jobs("developer", "Austin")
        self.assertEqual(jobs[0]["title"], "Backend Developer")

# 2. Test Amadeus search_flights
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
            ]
        }
        mock_get.return_value = mock_response
        result = search_flights("NYC", "LAX", "2025-09-01")
        self.assertEqual(result["airline"], "AA")
        self.assertEqual(result["price"], 150.00)

# 3. Test Gemini get_airport_code
class TestGeminiAirportCode(unittest.TestCase):
    @patch('services.gemini_service.client.models.generate_content')
    def test_get_airport_code(self, mock_generate):
        mock_generate.return_value.text = "JFK"
        code = get_airport_code("New York")
        self.assertEqual(code, "JFK")

# 4. Test Gemini get_city_summary
class TestGeminiCitySummary(unittest.TestCase):
    @patch('services.gemini_service.client.models.generate_content')
    def test_get_city_summary(self, mock_generate):
        mock_generate.return_value.text = '{"average_temp": 75, "summary": "A sunny place for outdoor lovers."}'
        summary = get_city_summary("Los Angeles")
        self.assertEqual(summary["average_temp"], 75)
        self.assertIn("sunny", summary["summary"].lower())

# 5. Test HistoryService - save and retrieve
class TestHistorySave(unittest.TestCase):
    def setUp(self):
        # Using actual DB; ideally should mock or use in-memory
        clear_history()

    def test_save_and_get_history(self):
        save_search("Boston", "Miami", "Data Analyst", "2025-10-01")
        history = get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["origin_city"], "Boston")

# 6. Test HistoryService - clear
class TestHistoryClear(unittest.TestCase):
    def test_clear_history(self):
        save_search("Chicago", "Dallas", "Engineer", "2025-12-12")
        clear_history()
        history = get_history()
        self.assertEqual(history, [])

# Add this to run tests directly
if __name__ == "__main__":
    unittest.main()
