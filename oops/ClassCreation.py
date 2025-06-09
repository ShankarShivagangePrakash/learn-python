"""
    Basic syntax of class creation is
    class <ClassName>
"""
class Human:
    """
        constructor can be created as
        def __init__(self, list of variables belonging to your class)
            self.var = var
    """
    def __init__(self, name):
        self.name = name

    """
        instance methods can be created as
        def <methodName>(self):
            your logic
    """
    def walk(self):
        print(self.name + "is walking")

shankar = Human("Shankar")
shankar.walk()