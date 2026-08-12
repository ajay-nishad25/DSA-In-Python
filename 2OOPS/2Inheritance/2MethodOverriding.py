"""
1. What is Method Overriding?

The definition is exactly the same as Java.

Method Overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

The child method replaces the parent method for objects of the child class.
"""

# Runtime Polymorphism
# Method Overriding enables runtime polymorphism.


class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()

# Python first searches inside the child class.
# If the method exists there, it stops searching.

# =================== Calling the Parent Method (super())

print("Calling the Parent Method (super())")

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Bark")

dog = Dog()
dog.sound()


# ==================== Overriding Constructors
print("Overriding Constructors")

class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        print("Dog Constructor")


Dog()

# using super method to call the parent class constructor

class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")


Dog()
