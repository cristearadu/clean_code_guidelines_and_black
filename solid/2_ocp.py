# base class for shapes.
class Shape:
    def calculate_area(self):
        pass


# NOT OKAY
# # We have a class that calculates the area of shapes
# class AreaCalculator:
#     def calculate_area(self, shape):
#         if isinstance(shape, Square):
#             return shape.length**2
#         elif isinstance(shape, Circle):
#             return 3.14 * shape.radius**2
#         # Adding a new shape requires modifying this class, violating the Open/Closed Principle.


# OKAY
# AreaCalculator class can be extended without modifying its code.
class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()


# Create specific shape classes that inherit from the base class.
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return self.length**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


square = Square(length=5)
circle = Circle(radius=3)

calculator = AreaCalculator()

print("Square area:", calculator.calculate_area(square))
print("Circle area:", calculator.calculate_area(circle))