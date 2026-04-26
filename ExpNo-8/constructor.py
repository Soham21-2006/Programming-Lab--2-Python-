# Class with constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create object
s1 = Student("Soham", 18)

# Call method
s1.display()