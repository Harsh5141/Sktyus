# Create a polymorphic function that works with different shapes.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
def calculate_area(shape):
    print("Area:", shape.area())
c = Circle(5)
r = Rectangle(4, 6)
calculate_area(c)
calculate_area(r)

