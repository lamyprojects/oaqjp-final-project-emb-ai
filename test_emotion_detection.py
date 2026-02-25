import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_output_keys(self):
        result = emotion_detector("I am happy")

        self.assertIn("anger", result)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)
        self.assertIn("dominant_emotion", result)

    def test_return_type(self):
        result = emotion_detector("I am happy")
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()
