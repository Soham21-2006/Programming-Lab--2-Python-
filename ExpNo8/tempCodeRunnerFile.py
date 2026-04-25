# Polymorphism using method overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
a = Animal()
d = Dog()
c = Cat()

# Same method, different behavior
for obj in (a, d, c):
    obj.sound()