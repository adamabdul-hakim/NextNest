import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestOpenAIApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch("routes.openai.client.chat.completions.create")
    def test_suggest_success(self, mock_chat):
        mock_chat.return_value.choices = [MagicMock(message=MagicMock(content="1. Seattle\n2. San Jose"))]

        res = self.client.get("/api/suggest?field=originCity&input=S")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertIn("Seattle", data["suggestions"])

    @patch("routes.openai.client.chat.completions.create")
    def test_transportation_success(self, mock_chat):
        mock_chat.return_value.choices = [
            MagicMock(message=MagicMock(content=(
                "Walk Score: 85 Very walkable\n"
                "Bike Score: 72 Good for biking\n"
                "Drive Score: 60 Some traffic congestion"
            )))
        ]

        res = self.client.get("/api/transportation?city=Austin")
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["city"], "Austin")
        self.assertEqual(data["walk"]["score"], 85)

    def test_suggest_missing_params(self):
        res = self.client.get("/api/suggest")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"suggestions": []})

    def test_transportation_missing_params(self):
        res = self.client.get("/api/transportation")
        self.assertEqual(res.status_code, 200)
        self.assertIn("error", res.get_json())
