"""
1. What is a Constructor?

The definition is the same as Java.

A constructor is a special method that is called automatically when an object is created.

Its main purpose is to initialize the object's data.

Java Constructor
class Student {

    String name;

    Student(String name) {
        this.name = name;
    }
}

Student s = new Student("Ajay");

"""

class Students:

    def __init__(self,name):
        self.name = name

s1 = Students("Ajay")
s2 = Students("Rahul")

print(vars(s1))
print(vars(s2))

"""
Notice:

- Constructor name is always __init__
- It is not the class name (unlike Java)
- self is always the first parameter

You never call __init__() yourself.

When you write

Student()

Python internally does something like

obj = Student.__new__(Student)
Student.__init__(obj)

For now, just remember:

__new__() creates the object.
__init__() initializes it.

You will rarely need __new__() in normal Python programming.
"""

# =========================Initializing Instance Variables
print()

class Student:

    # using constructor to initialize the value as soon as we create an objet of this class
    def __init__(self): 
        self.name = "Ajay"
        self.age = 22

    def display(self):
        print(self.name)
        print(self.age)

s = Student()
s.display()



# =========================Parameterized Constructor
print()

class Students:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


s1 = Students("Ajay",23)
s2 = Students("Rahul",25)
s1.display()
s2.display()


# =========================Constructor with Default Values
print()
class Student:

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

s1 = Student()
s2 = Student("Ajay")
s3 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)
print(s3.name, s3.age)

# =========================Constructor Overloading?

"""
This is one of the biggest differences from Java.

Java
class Student {

    Student() {}

    Student(String name) {}

    Student(String name, int age) {}
}

Perfectly valid.
"""

class Student:

    def __init__(self):
        print("First")

    def __init__(self, name):
        print("Second")

    def __init__(self):
        print("Third")


# Only the last method exists.
# The first one is overwritten.

obj = Student()

# because only the second __init__ remains.
"""
Python does not support traditional constructor overloading like Java or C++ because it allows only one __init__ method per class. 
If you define multiple __init__ methods, the last definition will completely overwrite the previous ones. 
"""

# However, you can simulate constructor overloading using three clean, Pythonic workarounds

# 1. Using Default Arguments (Best for varying numbers of arguments)

# example

class User:

    def __init__(self, name="unkown",age=18,email=None):
        self.name = name
        self.age = age
        self.email = email


user1 = User()
user2 = User("Ajay")
user3 = User("Rahul",22)
user4 = User("Visha",22,"vishal@gmail.com")

print(vars(user1))
print(vars(user2))
print(vars(user3))
print(vars(user4))


# 2. Using Class Methods as Factory Methods (Best for varying data types/formats)
"""
When you need to initialize objects from completely different data formats (e.g., a dictionary, a string, or a JSON file), use the @classmethod decorator. 
This keeps your main __init__ clean and provides explicit, readable alternative constructors
"""

print()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, data_string):
        title, author = data_string.split(',')
        return cls(title, author)

    @classmethod
    def from_dict(cls, data_dict):
        title = data_dict['title']
        author = data_dict['author']
        return cls(title, author)

book1 = Book('Java Dev', 'Oracle')
book2 = Book.from_string("Dune, Frank Herbert")
book3 = Book.from_dict({"title":"The Hobbit", "author":"J.R.R Tolkien"})


print(vars(book1))
print(vars(book2))
print(vars(book3))

# 3. Using *args and **kwargs (Best for variable-length inputs)
print()
class Point:
    def __init__(self, *args):
        if len(args) == 0:
            self.x, self.y = 0, 0  # Default origin
        elif len(args) == 2:
            self.x, self.y = args[0], args[1]
        else:
            raise TypeError("Point() takes 0 or 2 positional arguments")

p1 = Point()       # x=0, y=0
p2 = Point(5, 10)  # x=5, y=10

print(vars(p1))
print(vars(p2))

# =========================Can We Call the Constructor Again?
# Yes, but it's almost never a good idea.
class Student:

    def __init__(self, name):
        self.name = name

s = Student("Ajay")

print(s.name)

s.__init__("Rahul")

print(s.name)

# The object isn't recreated—it is simply reinitialized.
# Normally, you should create a new object instead.

# =========================Constructor Can Call Other Methods ?

print("Constructor Can Call Other Methods ?")
class Student:

    def __init__(self, name):
        self.name = name
        self.display()


    def display(self):
        print(self.name)

Student("Ajay")

# This works because self.name has already been initialized. Before calling the dispaly() 


"""
Interview Questions
Q1. Is __init__() the constructor?

Answer:
Not exactly. __new__() creates the object, while __init__() initializes it. In everyday Python development, people commonly refer to __init__() as the constructor because it's where object initialization happens.

Q2. Does Python support constructor overloading?

Answer:
No. Defining multiple __init__ methods will overwrite the previous ones. Use default arguments or variable-length arguments (*args, **kwargs) instead.

Q3. Can __init__() return a value?
class Student:

    def __init__(self):
        return 10

Output

TypeError:
__init__() should return None, not 'int'

__init__() must not return anything other than None.
"""
