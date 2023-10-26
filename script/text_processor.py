from collections import Counter

import pypdf
import spacy

# Load english language model
nlp = spacy.load("en_core_web_sm")


class TextProcessor:
    @staticmethod
    def extract_text_from_file(file_path: str) -> str:
        """Extract text from file"""
        with open(file_path, "r") as file:
            return file.read()

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extract text from pdf file"""
        reader = pypdf.PdfReader(file_path)
        file_text: str = ""

        for page in reader.pages:
            file_text += page.extract_text()

        return file_text

    @staticmethod
    def lemmatize_words(text: str) -> list[str]:
        """Extracting Unique Words from Text

        Currently, we need to process all words twice due to an issue with inflected words.
        The problem arises because some words are not inflected as expected,
        some gerundings or other words are not inflected according to Spacy logic.
        We will attempt to find a solution for this at a later time.
        """
        tokenized_text = nlp(text)
        inflected_words: list[str] = [
            token.lemma_ for token in tokenized_text if token.is_alpha
        ]

        return inflected_words

    @staticmethod
    def get_words_counter(words: list[str]):
        counter: Counter = Counter(words)

        return counter
