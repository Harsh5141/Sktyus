class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Object creation
rec = Rectangle(50, 25)

print("Area:", rec.area())
print("Perimeter:", rec.perimeter())
