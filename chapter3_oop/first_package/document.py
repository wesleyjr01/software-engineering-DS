# Import function to perform UPPER STRING
from collections import Counter


class Document:
    def __init__(self, text, token_regex=r"[a-zA-z]+"):
        self.text = text
        self.upper = self._upper()
        self.word_counts = self._counter()

    def _upper(self):  # Non-public method
        return self.text.upper()

    def _counter(self):  # Non-public method
        return Counter(self.text)
