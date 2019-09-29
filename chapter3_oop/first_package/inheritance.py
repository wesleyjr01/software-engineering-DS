# Import ParentClass Object
from .document import Document

# Create a child class with inheritance
class ChildClass(Document):
    def __init__(self, text):
        # Call parent's __init__ method
        Document.__init__(self, text)
        self.tokens = self._tokenize()

    def _tokenize(self):
        return self.text.split(" ")
