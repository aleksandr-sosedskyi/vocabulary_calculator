import os
from unittest import TestCase

from ..text_processor import TextProcessor

# Get current path
TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestTextProcessor(TestCase):
    def test_extract_text_from_file(self):
        text = TextProcessor.extract_text_from_file(
            os.path.join(TEST_DIR, "test_helpers", "text.txt")
        )
        self.assertEqual(text.strip(), "Some test text for tests.")

    def test_extract_text_from_pdf(self):
        text = TextProcessor.extract_text_from_pdf(
            os.path.join(TEST_DIR, "test_helpers", "test.pdf")
        )
        self.assertEqual(
            text.strip(),
            "This is a test PDF document. \nIf you can read this, you have Adobe Acrobat Reader installed on your computer.",
        )

    def test_lemmatize_words(self):
        words = TextProcessor.lemmatize_words("This is a test sentence.")
        self.assertEqual(words, ["this", "be", "a", "test", "sentence"])

    def test_count_words(self):
        words = TextProcessor.get_words_counter(
            ["this", "be", "a", "test", "sentence", "this"]
        )
        self.assertEqual(words["this"], 2)
        self.assertEqual(words["be"], 1)
        self.assertEqual(words["a"], 1)
        self.assertEqual(words["test"], 1)
        self.assertEqual(words["sentence"], 1)
