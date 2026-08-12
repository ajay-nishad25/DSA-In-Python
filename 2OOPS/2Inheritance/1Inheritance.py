"""
1. What is Inheritance?

The definition is exactly the same as Java.

Inheritance allows one class (child/subclass) to acquire the properties and methods of another class (parent/superclass).

It helps in:

Code Reusability
Extensibility
Maintainability
"""

# example
class Animal:
    pass

class Dog(Animal):
    pass

# Java uses extends, Python uses parentheses.

# ============================= 1. Single Inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(self.name)

class Dog(Animal):
    def sound(self):
        print("Barking sound of dog : ", self.name)


dog = Dog("Max")
dog.info()
dog.sound()

animal = Animal("Cat")
print(vars(animal))
animal.info()

# parent cannot access child methods like java
print("New parent cannot access child methods like java")

# uncomment below code to see the output

# class Animal:
#     pass

# class Dog(Animal):

#     def bark(self):
#         print("Bark")

# a = Animal()

# a.bark()


# ============================= 2. Multilevel Inheritance
"""
A child class inherits from a parent class, which in turn inherits from another parent class. 
This creates a multi-layered genealogical chain (Grandparent → Parent → Child). 
"""
print("Multilevel Inheritance Example")

class GrandParent:
    def __init__(self,grandparent_name):
        self.grandparent_name = grandparent_name

    def info(self):
        print(self.grandparent_name)

    def land_owned_by_grandparent(self):
        print("Land owned by grandparent : ", self.grandparent_name, " 10 bigha")

    def temp_method(self):
        print("Ajay searching for this method but found this in grandparent class")

class Parent(GrandParent):
    def __init__(self,parent_name):
        self.parent_name = parent_name

    def info(self):
        print(self.parent_name)

    def land_owned_by_parent(self):
        print("Land owned by parent : ", self.parent_name, " 5 bigha")

class Child(Parent):
    def __init__(self,child_name):
        self.child_name = child_name

    def info(self):
        print(self.child_name)

    def land_owned_by_child(self):
        print("Land owned by child : ", self.child_name, " 2 bigha")

grand_parent = GrandParent("Sukhu")
grand_parent.info()
grand_parent.land_owned_by_grandparent()

parent = Parent("Bhola")
parent.info()
parent.land_owned_by_parent()

child = Child("Ajay")
child.info()
child.land_owned_by_child()
child.temp_method()


# ============================= 3. Hierarchical Inheritance

"""
Hierarchical Inheritance is a type of inheritance in which a single base class is inherited by multiple derived classes. 
In this scenario, each derived class shares common attributes and methods from the same base class, forming a hierarchy of classes.

Syntax :

class BaseClass:
    # Base class attributes and methods
class DerivedClass1(BaseClass):
    # Additional attributes and methods specific to DerivedClass1
class DerivedClass2(BaseClass):
    # Additional attributes and methods specific to DerivedClass2
"""

# example

print("Hierarchical Inheritance Example")

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

    def info(self):
        print(self.name)

class Cat(Animal):
    def speak(self):
        print("Meow")

    def info(self):
        print(self.name)

dog = Dog("Max")
dog.speak()
dog.info()

cat = Cat("Tom")
cat.speak()
cat.info()

animal = Animal("Animal")
animal.speak()


# ============================= 4. Multiple Inheritance

"""
When a class inherits from more than one base class, it is called multiple inheritance. 
The derived class inherits all features of its base classes.

Syntax:
class Base1:
     # Body of the class
        pass

class Base2:
    # Body of the class
        pass

class Derived(Base1, Base2):
         # Body of the class
         pass 
"""
print("Multiple Inheritance Example")

class Father:
    def skills(self):
        print("programming")

class Mother:
    def hobby(self):
        print("Painting")

class Child(Father,Mother):
    pass

child = Child()
child.skills()
child.hobby()

# Like java python does comes with diamond problem in multiple inheritance too like 
"""
The Diamond Problem
Diamond Problem occurs when two classes inherit from a common superclass, and another class inherits from both. 
If a method is overridden in the intermediate classes, ambiguity arises about which method the derived class should use.

Class1 is the base, Class2 and Class3 inherit from it, Class4 inherits from both.
Calling a method overridden in Class2 and Class3 creates ambiguity.
Python uses MRO to resolve it and ensure a consistent call sequence.
*** Python have a built-in solution to the Diamond Problem, and it's handled through the Method Resolution Order (MRO) using the C3 linearization algorithm.

Method Resolution Order
Method Resolution Order (MRO) in Python determines the order in which base classes are searched when looking for an attribute in multiple inheritance. 
It follows a linearization rule: the current class is checked first, then parent classes are searched from left to right, each class only once. You can view it using:

Class.mro()-> returns a list
Class.__mro__ -> returns a tuple
"""

class Class1:
    def m(self):
        print("In class 1")

class Class2(Class1):
    def m(self):
        print("In class 2")

class Class3(Class1):
    def m(self):
        print("In class 3")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()

print(Class4.mro())
print(Class4.__mro__)


# Example 1: When the method is overridden in both classes
# The code demonstrates multiple inheritance where Class4 inherits from Class2 and Class3; calling obj.m() executes Class2’s method because, according to Python’s MRO, Class2 is checked before Class3.


print("Example 1 : When the method is overridden in both classes")

"""
The code demonstrates multiple inheritance where Class4 inherits from Class2 and Class3; calling obj.m() executes Class2’s method because, 
according to Python’s MRO, Class2 is checked before Class3.
"""

class Class1:
    def m(self):
        print("In Class1") 

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")  

class Class4(Class2, Class3):
    pass   
    
obj = Class4()
obj.m()

# Example 2: When the Method overridden in one class only

"""The code shows multiple inheritance where Class4 inherits from Class2 and Class3; calling obj.m() executes Class3’s method due to Python’s 
method resolution order (MRO).
"""

print("Example 2: When the Method overridden in one class only")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    pass

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()


# Example 3: All classes define the same method

"""
The code demonstrates multiple inheritance, showing that Class4 overrides the m method, but methods from parent classes (Class2, Class3, Class1) 
can still be called explicitly using the class name.
"""

print("Example 3: All classes define the same method")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")

obj = Class4()
obj.m()
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)

# Example 4: Calling methods of parent classes from child class

print("Example 4: Calling methods of parent classes from child class")

"""
The code demonstrates multiple inheritance and explicitly calls parent class methods, showing how Class1.m() is invoked multiple times through
Class2 and Class3.
"""

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)

obj = Class4()
obj.m()


# ========================== Super Function

"""
Super Function in Python is used to call a method from a parent (base) class, especially in multiple inheritance.
It helps avoid explicitly naming the parent class, ensures proper method resolution following the MRO, and prevents duplicate calls of the same method.
"""

print("Super function example")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()

obj = Class4()
obj.m()
print(Class4.mro())
print(Class4.__mro__)

"""
output of above code is :
In Class4
In Class2
In Class3
In Class1

instead of 

In Class4
In Class2
In Class1
In Class3
In Class1

because before executing the super method python check's the MRO list and accoridng to MRO list

[<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>]
(<class '__main__.Class4'>, <class '__main__.Class2'>, <class '__main__.Class3'>, <class '__main__.Class1'>, <class 'object'>)

class 4
class 2
class 3
class 1
is the right sequence
"""

# NOTE: super method can also be used to call the parent constructor

# example 

print("Using super method to call the parent constructor")

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)

        self.roll = roll

s = Student("Ajay",101)

print(s.name)

print(s.roll)


# ========================= object Class

# Every Python class ultimately inherits from object

# Example

class Student:
    pass

# Actually behaves like

class Student(object):
    pass


"""
Common Mistakes
❌ Forgetting super()
class Parent:

    def __init__(self):
        print("Parent")


class Child(Parent):

    def __init__(self):
        print("Child")

Output

Child

Parent constructor is skipped.

❌ Calling Parent Method Incorrectly

Avoid

Parent.__init__(self)

Prefer

super().__init__()

super() respects MRO, which is especially important with multiple inheritance.

❌ Confusing isinstance() and issubclass()
isinstance(obj, Class)

Object check.

issubclass(Child, Parent)

Class check.

Java        vs                                          Python
Java	                                                Python
extends	                                                class Child(Parent)
Single inheritance only	                                Supports multiple inheritance
super() inserted automatically in constructors	        Must call super() explicitly
Interfaces required for multiple-type behavior	        Multiple inheritance can often achieve similar goals
MRO not needed	                                        Uses C3 Linearization (MRO)

Interview Questions
Q1. Does Python support multiple inheritance?

✅ Yes.

Q2. What is MRO?

The order in which Python searches classes for attributes and methods.

Use:

ClassName.mro()

or

ClassName.__mro__

Q3. Why use super()?

To call the parent implementation while respecting the Method Resolution Order.

Q4. Does Python automatically call the parent constructor?

❌ No.

You must call:

super().__init__()
Q5. What is the base class of all Python classes?
object


"""