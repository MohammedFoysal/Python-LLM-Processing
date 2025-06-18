import unittest
from main import split_text

class LlmChunkerTest(unittest.TestCase):
    def test_split_text(self):
        text = "This is a test string hello bye bye"

        result = split_text(text, 3)

        self.assertEqual(result, ["This is a", "test string hello", "bye bye"])

if __name__ == '__main__':
    unittest.main()
