# Define a minimal class with an attribute
class MyClass:
    """A minimal example class

    :param value: value to set as the ``attribute`` attribute
    :ivar attribute: contains the contest of ``value`` passed in init
    """

    # Method to create a new instane of MyClass
    def __init__(self, value):
        # Define attribute with the contents of the value param
        self.attribute = value
