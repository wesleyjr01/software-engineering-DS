# Import ParentClass Object
from .document import Document

# Create a child class with inheritance
class ChildClass(Document):
    def __init__(self, text):
        # Call parent's __init__ method
        self.text = text
        Document.__init__(self, text)
        self.tokens = self._tokenize()

    def _tokenize(self):
        self.tokens = self.text.split(" ")
        return self.tokens

