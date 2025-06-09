class DefaultConstructor:
    """
        You can create default constructor like Java in Python as below
        self is the first parameter in both constructor and instance methods
            it gives access for these methods to access instance variables
        for parameters, if you are not expecting values
        provide default value of their data type
        for the majority of the data types None works
        for numerical data types 0 works
    """
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"name = {self.name}, age = {self.age}")

shankar_without_any_value = DefaultConstructor()
shankar_without_any_value.print_info()

shankar_with_name = DefaultConstructor("Shankar")
shankar_with_name.print_info()

shankar_with_all_values = DefaultConstructor("Shankar", 24)
shankar_with_all_values.print_info()
