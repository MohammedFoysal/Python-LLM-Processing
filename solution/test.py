import unittest
from main import split_text
from data import data

class LlmChunkerTest(unittest.TestCase):
    def test_split_text(self):
        text = "This is a test string hello bye bye"

        result = split_text(text, 3)

        self.assertEqual(result, ["This is a", "test string hello", "bye bye"])

    def test_split_text_data(self):
        chunks = split_text(data, 200)

        self.assertEqual(len(chunks), 7)

if __name__ == '__main__':
    unittest.main()
