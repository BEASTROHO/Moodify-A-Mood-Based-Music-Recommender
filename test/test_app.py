import unittest
from app import app

class MoodifyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_mood_input(self):
        response = self.client.post('/analyze', json={'text': 'I feel joyful'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('mood', response.get_json())

    def test_empty_input(self):
        response = self.client.post('/analyze', json={'text': ''})
        self.assertEqual(response.status_code, 400)

    def test_missing_text_key(self):
        response = self.client.post('/analyze', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
