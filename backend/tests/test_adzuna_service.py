import unittest
from unittest.mock import patch, MagicMock
from services.adzuna_service import get_jobs

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
