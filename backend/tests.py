import unittest
from services.adzuna_service import get_jobs
from services.amadeus_service import search_flights
from services.gemini_service import get_airport_code
from services.gemini_service import get_city_summary
from services.history_service import get_history


class UnitTests(unittest.TestCase):
    @patch('services.adzuna_services.request.get')
    def test_get_jobs(self, mock):
        mock.return_value 
