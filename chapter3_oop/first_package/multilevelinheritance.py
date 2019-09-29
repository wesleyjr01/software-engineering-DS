class Parent:
    def __init__(self):
        print("I'm a parent!")


class SuperChild(Parent):
    def __init__(self):
        super().__init__()
        print("I'm a super child!")


class GrandChild(SuperChild):
    def __init__(self):
        super().__init__()
        print("I'm a grandchild!")
