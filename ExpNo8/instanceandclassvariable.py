# Class definition
class Student:
    # Class variable
    school = "ABC School"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
s1 = Student("Soham", 18)
s2 = Student("Amit", 19)

# Access variables
print("Class Variable:", Student.school)

print("\nInstance Variables:")
print(s1.name, s1.age)
print(s2.name, s2.age)