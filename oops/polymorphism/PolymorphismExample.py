# Parent class Shape
class Shape:
    """
        I can't write any logic for draw() without shape.
        so I just define the method and don't write any logic
        using `pass` keyword
    """
    def draw(self):
        pass

# Inherit Shape class
class Rectangle(Shape):
    # overriding parent class draw()
    def draw(self):
        print("Rectangle")

# Inherit Shape class
class Circle(Shape):
    # overriding parent class draw()
    def draw(self):
        print("Circle")

"""
    Achieving dynamic binding
    In each iteration, different class object is given to shape object
    and corresponding class draw() is invoked
"""
shapes = [Rectangle(), Circle(), Shape()]
for shape in shapes:
    shape.draw()