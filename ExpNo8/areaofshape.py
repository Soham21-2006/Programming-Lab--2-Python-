# Base class
class Shape:
    def area(self):
        pass

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of Rectangle:", self.l * self.b)

# Derived class for Circle
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area of Circle:", 3.14 * self.r * self.r)

# Create objects
r = Rectangle(5, 3)
c = Circle(4)

# Call methods
r.area()
c.area()