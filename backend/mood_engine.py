import unittest
from backend.mood_engine import analyze_mood

class TestMoodEngine(unittest.TestCase):
    def test_happy_mood(self):
        self.assertEqual(analyze_mood("I feel amazing and joyful!"), "Happy")

    def test_content_mood(self):
        self.assertEqual(analyze_mood("I'm doing okay today."), "Content")

    def test_neutral_mood(self):
        self.assertEqual(analyze_mood("It is a regular day."), "Neutral")

    def test_melancholy_mood(self):
        self.assertEqual(analyze_mood("I'm a bit down and tired."), "Melancholy")

    def test_sad_mood(self):
        self.assertEqual(analyze_mood("I feel terrible and hopeless."), "Sad")

if __name__ == '__main__':
    unittest.main()
