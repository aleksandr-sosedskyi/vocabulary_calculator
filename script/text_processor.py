from collections import Counter

import spacy
import textract

# Load english language model
nlp = spacy.load("en_core_web_sm")


class TextProcessor:
    @classmethod
    def _extract_text_from_pdf(cls, file_path: str) -> str:
        """Extract text from pdf file"""
        text_encoded = textract.process(file_path, method="pdfminer")
        file_text = text_encoded.decode("utf-8")

        return file_text.lower()

    @classmethod
    def _extract_text_from_txt(cls, file_path: str) -> str:
        """Extract text from txt file"""
        with open(file_path, "r") as file:
            file_text = file.read()

        return file_text

    @classmethod
    def extract_text_from_file(cls, file_path: str) -> str:
        if file_path.endswith(".pdf"):
            file_text = cls._extract_text_from_pdf(file_path)
        elif file_path.endswith(".txt"):
            file_text = cls._extract_text_from_txt(file_path)

        return file_text

    @classmethod
    def lemmatize_words(cls, text: str) -> list[str]:
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
