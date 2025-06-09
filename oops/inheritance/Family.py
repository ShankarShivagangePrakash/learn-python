"""
    Parent class Family has an attribute 'familyName'
"""
class Family:
    def __init__(self, familyName):
        self.familyName = familyName

"""
    Child class inherits Family
"""
class Child(Family):
    def __init__(self, name, familyName):
        self.name = name
        """
            Invoking parent constructor using the syntax
                super(ChildClassName, self).__init__(ParentClass constructor parameters...)
        """
        super(Child,self).__init__(familyName)

    def printDetails(self):
        print(f"name: {self.name}, family: {self.familyName}")

vk = Child("VK", "VK")
vk.printDetails()