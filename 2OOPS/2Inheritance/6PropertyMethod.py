"""
Why Does @property Exist?

In Java, if you want to protect a variable, you usually make it private and expose it through getters and setters.

Java
class Student {

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

Usage

Student s = new Student();

s.setName("Ajay");

System.out.println(s.getName());

Notice:

You must call methods.
"""


# Python Without @property
# lets write the same thing like java 

class Students:
    def __init__(self):
        self.__name = None

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

s1 = Students()
s2 = Students()

s1.set_name("Ajay")
s2.set_name("Rahul")

print(s1.get_name())
print(s2.get_name())

# above code works but this doesnt feel very pythonic
# python prefers
# s1.name = "Ajay"
# s2.name = "Rahul"
# instead of
# s1.set_name("Ajay")
# s2.set_name("Rahul")

# This is exactly why @property exists.

# what is @property?
# @property lets you access a method like an attribute.

# Instead of
# student.get_name()
# you simply write
# student.name
# Even though a method is executed behind the scenes.

#============= Creating a Read-Only Property (Getter)
# example
print("Creating a Read-Only Property (Getter)")
class Student:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

s1 = Student("Ajay")
s2 = Student("Aditya")

print(s1.name)
print(s2.name)

# here instead of calling get_name method for object we simple call it like and atribute i.e s1.name or s2.name
"""
We never wrote

s.name()

We simply wrote

s.name

Python automatically calls

name()

behind the scenes.

* What Happens Internally?

When you write

print(s.name)

Python internally does

print(s.name())

conceptually.

You don't need parentheses.
"""

# Why Is This Better?

"""
Imagine your first version.

student.get_name()

Later,

you decide to calculate the name dynamically.

Without @property

Everywhere in your code

student.name

must become

student.get_name()

Lots of code changes.

With @property

The public interface remains

student.name

Implementation changes.

Usage doesn't.
"""


#============= Creating Setter

print("Creating Setter Example")

"""
Currently,

s.name = "Rahul"

produces

AttributeError

because we only created a getter.

Let's add a setter.
"""
# synatx 
# @attribute_name.setter
# def attribute_name()

class Student:
    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

s1 = Student()
s2 = Student()

s1.name = "Ajay"
s2.name = "Rahul"

print(s1.name)
print(s2.name)

# Notice
# We never called
# set_name()


#============= Deleter
# Python also lets you define what happens when someone deletes an attribute.
print("Deleter Example")
class Student:
    def __init__(self):
        self.__name = None

    # getter method/attribute
    @property
    def name(self):
        return self.__name

    # setter method/attribute
    @name.setter
    def name(self,name):
        self.__name = name

    # deleter method/attribute
    @name.deleter
    def name(self):
        print("Deleting name : ",self.name)
        del self.__name

s1 = Student()
s2 = Student()

s1.name = "Ajay"
s2.name = "Rahul"

print(s1.name)
print(s2.name)

# deleting attributes
del s1.name
del s2.name

# ==================== Read-Only Property
# Simply don't define a setter. then that method/attribute will work as read-only property


# ==================== Computed Properties ⭐
# One of the biggest advantages. we can use this read-only getter methods for computation purpose example
print("Computed Properties Example")

class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    @property
    def area(self):
        return self.__length * self.__width

r1 = Rectangle(10,20)
print("area of rectangle is : ",r1.area)

# ====================== Difference Between Normal Attributes and Properties
"""
Normal

student.name

Simply returns stored data.

Property

student.name

Executes code first.

The syntax looks identical.
"""

# ====================== Order of Property Definitions

"""
Always write

@property

first.

Then

@name.setter

Finally

@name.deleter

Example

@property
def name(self):
    ...

@name.setter
def name(self, value):
    ...

@name.deleter
def name(self):
    ...
"""

# ================= Interview Questions

"""
Q1. What is @property?

A decorator that allows a method to be accessed like an attribute.

Q2. Why use @property?
Validation
Read-only attributes
Computed values
Cleaner API
Q3. Can a property have only a getter?

Yes.

It becomes read-only.

Q4. Can properties have setters?

Yes.

Use

@property_name.setter
Q5. What is a computed property?

A property that calculates its value every time it is accessed instead of storing it.

Example

@property
def area(self):
    return self.length * self.width
"""