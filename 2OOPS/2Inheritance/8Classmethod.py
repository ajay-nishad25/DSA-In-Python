"""
======================== 1. What is a Class Method?

A class method is a method that receives the class itself as its first parameter instead of an object.

That first parameter is conventionally named cls.

Syntax:

class Student:

    @classmethod
    def method_name(cls):
        ...

Notice:

Instance Method → first parameter is self
Class Method → first parameter is cls
Static Method → no self or cls
"""

"""
======================== 2. Why Do We Need Class Methods?

Instance methods work with object data.

class Student:

    def __init__(self, name):
        self.name = name

Here,

self.name

belongs to each object.

Sometimes we want to work with class-level data instead.

Example:

class Student:

    college = "ABC College"

This variable belongs to the class, not individual objects.

A class method is designed for this purpose.
"""

# ======================== Accessing Class Variables using cls

print("Accessing Class Variables using cls example")
class Student:
    college = "ABC college"
    def __init__(self,name):
        self.name = name

    def get_details(self):
        print(self.name)
        print(Student.college) # here when i am calling the class variable i need to call the classname.variable

    @classmethod
    def get_class_detail(cls):
        print(cls.college) # here i dont need to call the classname explicitly instead i can access using cls parameter


s = Student("Ajay")
s.get_details()
s.get_class_detail()

# ======================== Modifying Class Variables

print("Modifying Class Variables example")

class Student:
    college = "ABC college"
    @classmethod
    def get_class_detail(cls):
        return cls.college

    @classmethod
    def change_variable_data(cls,new_name):
        cls.college = new_name


s = Student()
print("old variabale data : ",s.get_class_detail())
s.change_variable_data("IIT college")
print("new variabale data : ",s.get_class_detail())
# The change affects every object, because college is a class variable.


# ======================== Alternative Constructors ⭐⭐⭐
"""
In Python, a class usually has one __init__ method. But what if you want to create objects from different types of input data—like a string, a dictionary, or a timestamp—instead of just individual arguments?

That is where a @classmethod acts as an alternate constructor. It provides an additional, clean way to parse data and instantiate an object.

The Problem (Without Alternate Constructors)
Imagine a Student class that expects a name and an age:

Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
What if your incoming data comes as a single Hyphen-separated string, like "Rahul-25"?

Without an alternate constructor, you have to split the string manually every time before creating a student:

Python
# Raw data
data = "Rahul-25"

# Manual parsing outside the class
name, age = data.split("-")
s1 = Student(name, int(age))
This clutter multiplies every time you receive data in that format.
"""

"""
The Solution: @classmethod as an Alternate Constructor
You can attach a @classmethod directly to the class to handle the parsing and return a brand-new instance using cls(...).
"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,data):
        name,age = data.split("-")
        return cls(name,int(age))

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["age"])

s1 = Student("Ajay",25)
s2 = Student.from_string("Rahul-22")
s3 = Student.from_dict({"name":"Visha","age":26})

print(vars(s1))
print(vars(s2))
print(vars(s3))

"""
Key Things to Remember
1.cls instead of self: The first argument of a @classmethod is cls, which refers to the class itself (Student), not an instance.

2.return cls(...): Calling cls(name, age) inside the method is identical to calling Student(name, age). It creates and returns a new object.

3.Naming Convention: Alternate constructors are conventionally named using from_... (e.g., from_string, from_dict, from_json, from_csv).

4.Built-in Examples: Python uses this pattern internally all the time!
    datetime.fromtimestamp(...) in the datetime module.
    dict.fromkeys(...) in base Python.
"""


"""
======================== Why Use cls Instead of Class Name?

Wrong

class Student:

    @classmethod
    def create():

        return Student()

Correct

class Student:

    @classmethod
    def create(cls):

        return cls()

Why?

Because subclasses inherit correctly.

Example

class GraduateStudent(Student):
    pass

g = GraduateStudent.create()

If Student() were hardcoded, it would always return a Student, not a GraduateStudent.

Using cls() keeps the method polymorphic
"""

"""
======================== Interview Questions
Q1. What is a class method?

A method that receives the class (cls) instead of an object (self).

Q2. Why use @classmethod?
Work with class variables.
Create alternative constructors.
Implement factory methods.
Q3. What is cls?

cls is a reference to the class, similar to how self refers to an object.

Q4. Can a class method access instance variables?

No.

It has no object (self).

Q5. What is the biggest real-world use of @classmethod?

Alternative constructors and factory methods.
"""