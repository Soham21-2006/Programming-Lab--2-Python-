# Grandparent class
class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")

# Parent class
class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class")

# Child class
class Child(Parent):
    def show_child(self):
        print("This is Child class")

# Create object
c = Child()

# Call methods
c.show_grandparent()
c.show_parent()
c.show_child()