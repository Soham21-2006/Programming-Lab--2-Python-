# Parent class 1
class Father:
    def show_father(self):
        print("This is Father class")

# Parent class 2
class Mother:
    def show_mother(self):
        print("This is Mother class")

# Child class
class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

# Create object
c = Child()

# Call methods
c.show_father()
c.show_mother()
c.show_child()