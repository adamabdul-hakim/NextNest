import unittest
from unittest.mock import patch
from app import app

class TestJobsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch("routes.jobs_api.get_jobs")
    def test_jobs_success(self, mock_jobs):
        mock_jobs.return_value = [
            {
                "title": "Backend Developer",
                "company": "TechCorp",
                "location": "Austin, TX",
                "redirect_url": "http://example.com/job1"
            }
        ]

        res = self.client.get("/api/jobs?field=developer&location=Austin")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[0]["title"], "Backend Developer")

    def test_jobs_missing_params(self):
        res = self.client.get("/api/jobs?field=developer")
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertIn("error", data)
