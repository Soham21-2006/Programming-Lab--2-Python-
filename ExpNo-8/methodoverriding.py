# Parent class
class Animal:
    def sound(self):
        print("Animal makes sound")

# Child class
class Dog(Animal):
    def sound(self):   # Overriding method
        print("Dog barks")

# Create object
d = Dog()

# Call method
d.sound()