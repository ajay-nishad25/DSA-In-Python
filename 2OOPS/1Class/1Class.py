"""
What is a Class?

The definition is exactly the same as Java.

A class is a blueprint used to create objects
"""

class Student:
    pass
# pass means "empty class".

# =================Creating Objects
s1 = Student()

"""There is
No new
No type declaration
Python automatically creates the object."""

# Example
class Student:
    pass

s1 = Student()
s2 = Student()

print(s1)
print(s2) # each objet has its own memory address


# =================Adding Attributes

# Unlike Java,
# Python allows adding variables even after object creation.
# Example

class Student:
    pass

s1 = Student()

s1.name = "Ajay"
s1.age = 22

s2 = Student()

print(s1.name)
print(s1.age)

print(vars(s1))
print(vars(s2))

"""
In Java this is impossible unless the fields already exist.

Java

Student s = new Student();

s.name = "Ajay";   // Error if name isn't declared

Python is dynamic.
"""

# =================Every Object Has Its Own Attributes

class Student:
    pass

s1 = Student()
s2 = Student()

s1.name = "Ajay"
s2.name = "Rahul"

print(s1.name)
print(s2.name)


"""
What is self?

This is the most important concept in Python OOP.

If you understand self,
Python OOP becomes easy.
"""

"""
Think about Java.

class Student{
    String name;
    void show(){
        System.out.println(this.name);
    }
}

Java automatically provides

this

inside every method.

You never pass it.

Python does the same thing,
but it is explicit.

Instead of

this

Python uses

self

"""

# Why self is needed 
"""
Why is self Needed?

Suppose

class Student:

    def show(self):
        print("Hello")

Create object

s = Student()

Now call

s.show()

Looks like

show()

But internally Python converts it into

Student.show(s)

Meaning

self = s

So

s.show()

actually becomes

Student.show(s)

Exactly like Java's hidden

this

except Python shows it explicitly.
"""

class Student:

    def show(self):
        print("This is self print statement : ",self)

s = Student()

s.show()

# Multiple Objects

class Student:

    def show(self):
        print(self)

s1 = Student()
s2 = Student()

s1.show()
s2.show()

# Different objects, different self.

# using self to store data
class Student:

    def set_name(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student()
s2 = Student()

s1.set_name("Ajay")
s2.set_name("Rahul")

s1.display()
s2.display()

"""
Without self

class Student:

    def set_name(self, name):
        name = name

This only creates a local variable.

After method ends

name disappears.

Nothing is stored inside the object.

Correct
self.name = name
This stores it inside the object.
"""

# Can We Name self Anything? : YES 

"""
This works

class Student:

    def show(me):
        print(me)

But don't do this.

PEP 8 (Python's style guide) recommends always using self. Every Python developer expects it, so using another name makes your code harder to read.
"""


"""
Difference Between Java and Python
Java	                    Python
this keyword	            self parameter
this is implicit	        self is explicit
new Student()	            Student()
Types are required	        Dynamic typing
Fields must be declared	    Attributes can be added dynamically
Curly braces {}	            Indentation + :
"""


# =================Practice Questions
"""
Practice Questions

Try these on your own before moving ahead:

Create a Student class.
Create two student objects.
Add name and age attributes dynamically.
Print both students' details.
Create a Car class with set_brand() and show() methods.
Print self inside a method and observe that each object has a different memory address.
Create a Book class with methods set_title() and display(), using self to store and print the title.
"""

class Students:
    pass

s1 = Students()
s2 = Students()

s1.name = "Ajay"
s1.age = 23

s2.name = "Rahul"
s2.age = 25

print(vars(s1))
print(vars(s2))


class Car:
    def set_brand(self,brand):
        self.brand = brand
    
    def show(self):
        print(self)
        print(self.brand)
    
c1 = Car()
c2 = Car()

c1.set_brand("BMW")
c2.set_brand("Audi")

c1.show()
c2.show()


class Book:
    def set_title(self, title):              
        self.title = title
    
    def didpaly(self):
        print(self.title)


