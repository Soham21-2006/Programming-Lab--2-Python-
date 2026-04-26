# Class with encapsulation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private variable

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks

# Create object
s = Student("Soham", 85)

# Access using methods
print("Marks:", s.get_marks())

# Update value
s.set_marks(90)
print("Updated Marks:", s.get_marks())