# Parent class
class Person:
    def show(self):
        print("This is parent class")

# Child class
class Student(Person):
    def display(self):
        print("This is child class")

# Create object
s = Student()

# Call methods
s.show()      # Inherited method
s.display()   # Own method