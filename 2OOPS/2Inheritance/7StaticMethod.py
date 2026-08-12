# Before heading towards the static method code lets first understand types of methods in python 
"""
This topic is short but very important because Python has three types of methods:

✅ Instance Methods (use self) — Already learned
Static Methods (use @staticmethod) ← Today's topic
Class Methods (use @classmethod) — Next topic

If you understand the difference between these three, you'll be comfortable reading and writing production-quality Python code.
"""

# ============= what is @staticmethod
"""
A static method belongs to the class but does not operate on a specific object (self) or the class itself (cls).

It is simply a function placed inside a class because it is logically related to that class.

Unlike instance methods, it:

❌ Doesn't receive self
❌ Doesn't receive cls
✅ Can be called using either the class or an object
"""

# syntax:
# @staticmethod
# def method_name()

# ============ Why Do We Need Static Methods?

# Suppose you have a Math class.
# example
print("Why Do We Need Static Methods?")
class Math:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def multiply(a,b):
        return a*b

print("add : ", Math.add(2,3))
print("multiply : ", Math.multiply(2,3))

"""
NOTE:
We never created an object.
m = Math()   # Not needed
Because the method doesn't depend on object data.
"""
# These parameters are normal function parameters, not self or cls.

# ================== Instance Method vs Static Method

# instance method example
print("instance method example ")
class Student:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print(self.name)

s = Student("Ajay")
s.get_name()
# The method needs self.


# static method example
print("static method example")

class Student:
    @staticmethod
    def get_school_name(): # no self argument required for static method
        print("ABR School")

Student.get_school_name()
# no object required to call the class method 

# ====================== Can We Call a Static Method Using an Object?
print("Can We Call a Static Method Using an Object? ->>>>>>> YES")

class Student:
    @staticmethod
    def greet_student():
        print("Good morning students")

s = Student()
s.greet_student()
# However, calling it through the class name is the recommended style because it makes it clear the method doesn't depend on object state.
# preferred way
Student.greet_student()

# ================= Static Methods Cannot Access Instance Variables [yes we cannot access instance variable in static method]
print("Static Methods Cannot Access Instance Variables Example")

# un-comment below code to see the actual output
# class Studnet:
#     def __init__(self,name):
#         self.name = name
#     @staticmethod
#     def get_name():
#         print(self.name)

# s = Studnet("Ajay")
# s.get_name()

# Why?
# Because there is no self inside a static method.

# ==================== Static Methods Can Be Utility Functions

print("Static Methods Can Be Utility Functions Example")
# one of the most common use

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(37))
# The conversion logic belongs with the Temperature class, but it doesn't require object data.

# Another example:

class StringUtils:

    @staticmethod
    def is_palindrome(text):
        return text == text[::-1]

print(StringUtils.is_palindrome("nitin"))


# ======================== Can Static Methods Access Class Variables?
print("Can Static Methods Access Class Variables? Example")
# Yes, but only by using the class name.

class Student:
    college = "ABC college"
    @staticmethod
    def get_college():
        print(Student.college)

Student.get_college()
"""
NOTE:
We used
Student.college
not
self.college
because self doesn't exist inside a static method.
"""

# ====================== When Should You Use a Static Method?
"""
Use a static method when:

-The function is related to the class.
-It doesn't need object data.
-It doesn't need class data.
-It acts as a helper or utility function.

Examples:

-Math calculations
-String utilities
-Date formatting
-Unit conversions
-Validation helpers
"""

# ================= When Should You NOT Use a Static Method?
"""
Don't use it if the method needs instance variables.

Wrong

class Student:

    def __init__(self, marks):
        self.marks = marks

    @staticmethod
    def print_marks():
        print(self.marks)

self doesn't exist here.

Instead, use an instance method.

class Student:

    def __init__(self, marks):
        self.marks = marks

    def print_marks(self):
        print(self.marks)
"""

# ==================== Real world example

class Employee:
    @staticmethod
    def get_valid_age(age):
        return age>=18 and age <=60

    def __init__(self,name,age):
        if not Employee.get_valid_age(age):
            raise ValueError("Invalid age")
        self.name = name
        self.age = age

emp = Employee("Ajay",13)
print(vars(emp))




