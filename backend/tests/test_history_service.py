import unittest
from services.history_service import get_history, save_search, clear_history

class TestHistoryService(unittest.TestCase):
    def setUp(self):
        user_id = "11111111-1111-1111-1111-111111111111"
        clear_history(user_id)

    def test_save_and_get_history(self):
        user_id = "11111111-1111-1111-1111-111111111111"
        save_search("Boston", "Miami", "Data Analyst", "2025-10-01", user_id)
        history = get_history(user_id)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["origin_city"], "Boston")

    def test_clear_history(self):
        user_id = "11111111-1111-1111-1111-111111111111"
        save_search("Chicago", "Dallas", "Engineer", "2025-12-12", user_id)
        clear_history(user_id)
        history = get_history(user_id)
        self.assertEqual(history, [])
