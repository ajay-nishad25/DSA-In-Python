
# This is one of the most important topic i.e Magic Methods/Dunder Methods

"""
1. What are Magic (Dunder) Methods?

Magic methods are special methods that start and end with double underscores (__).

Examples:

__init__
__str__
__repr__
__len__
__eq__
__add__
__call__
__iter__
__next__

They are called dunder methods because of the double underscores.

- Why do they exist?

They allow your objects to behave like Python's built-in objects.

Example:

print("Hello")

How does Python know how to print a string?

Internally,

print(obj)

calls

obj.__str__()

Similarly,

len(obj)

calls

obj.__len__()

and

obj1 + obj2

calls

obj1.__add__(obj2)

You usually don't call these methods directly. Python calls them automatically.

"""

# =============================== 1. __str__()
# This is the most commonly used magic method.
# It defines the human-readable string representation of an object.

# without __str__()

print("without __str__()")
class Student:

    def __init__(self, name):
        self.name = name

s = Student("Ajay")

print(s)

# with __str__()
print("with __str__()")

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"Student name is : {self.name}")

s = Student("Ajay")

print(s)

# =============================== 2. __repr__()
# __repr__() is mainly for developers/debugging.
# repr -> stands for representation

print("__repr__() example")

class Student:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Studnet ('{self.name}')"

s = Student("Ajay")
print(repr(s))


# str vs repr see the below code output
"""
We use __repr__ alongside __str__ because they serve two completely different audiences: machines/developers versus human end-users.
Here is the simplest way to understand the difference:
1. __str__ hides the messy details (For Humans)__str__ is for creating clean, user-friendly text. It hides data types and internal formatting to make the output look nice on a screen.
2. __repr__ shows the absolute truth (For Developers)__repr__ is for debugging. It leaves no room for confusion. It explicitly shows you exactly what the data is and what type it belongs to.
"""
x = "7"
y = 7

print(str(x))
print(str(y))

print(repr(x))
print(repr(y))

# NOTE: If __str__() isn't defined, Python falls back to __repr__().

# =============================== 3. __len__()

print("__len__() example")

# without len() below code will give type-error
# class Student:
#     pass

# s = Student()
# print(len(s))

# with len()

class Student:

    def __len__(self):
        return 5

s = Student()
print("__len__() method example : ",len(s))

# 4. =============================== __eq__()
# defines equality (==)
print("__eq__() example")

# without it
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Ajay")
s2 = Student("Ajay")

print(s1 == s2)
# Because Python compares memory addresses by default.

# with it

class Student:
    def __init__(self,name):
        self.name = name
    def __eq__(self, other):
        return self.name == other

s1 = Student("Ajay")
s2 = Student("Ajay")
# now equality is based on data not on memory address

print(s1 == s2)

"""
Commonly Used Magic Methods
Method	                    Purpose
__init__	                Constructor
__str__	                    Human-readable string
__repr__	                Developer representation
__len__	                    len()
__eq__	                    ==
__add__	                    +
__lt__	                    <
__gt__	                    >
__call__	                Callable object
__iter__	                Returns iterator
__next__	                Next item in iteration
"""

# NOTE: i am skipping this after __eq__() method since i didnt find it any usefull for interview purpose i have learned the reuqired things