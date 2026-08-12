"""
================ 1. What is an Abstract Class?

An abstract class is a class that cannot be instantiated directly.

Its purpose is to act as a blueprint for other classes.

It can contain:

-Abstract methods (must be implemented by child classes)
-Normal methods
-Constructors
-Instance variables
-Class variables


Real-Life Example

Imagine a company.

Every employee must:

Work
Calculate salary

But how they work or calculate salary depends on the employee type.

So instead of writing a complete Employee class, we create an abstract class.

Employee
   ↑
------------
|          |
Developer  Manager

The child classes decide the implementation.

"""

"""
====================== 2. Why Do We Need Abstract Classes?

Suppose we write:

class Animal:

    def speak(self):
        pass

Then

a = Animal()

a.speak()

This works.

But does an "Animal" really know how to speak?

Not really.

Each animal speaks differently.

Dog → Bark
Cat → Meow
Cow → Moo

So we shouldn't allow anyone to create a generic Animal.

Instead, we make it abstract.
"""


# Implementing Abstraction in Python
"""
Python does not have built-in support for abstract classes in the way some other languages do, but it offers the abc module which stands for Abstract Base Classes. 
This module provides the infrastructure for defining custom abstract classes in Python.
"""

"""
================= 3. The abc Module

Python provides the abc (Abstract Base Classes) module.

Import it:

from abc import ABC, abstractmethod

Where:

ABC → Base class for abstract classes.
@abstractmethod → Marks methods that child classes must implement.
"""

print("Abstract Class Example")
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# a = Animal() # this line will give TypeError that we cannot create an object of abstract class
# print(a.speak())

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

# class Cow(Animal):
#     pass   
# since Cow class didn't implement the speak() @abstractmethod, so creating object of Cow() will lead to an error i,e TypeError: Can't instantiate abstract class Cow with abstract method speak
# cow = Cow()

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()


# ============== Multiple Abstract Methods

print("Multiple Abstract Methods Example")

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def work(self):
        print("Manage team")

    def calculate_salary(self):
        return 70000

class Developer(Employee):
    def work(self):
        print("Write code")

    def calculate_salary(self):
        return 50000

manager = Manager()
manager.work()
print(manager.calculate_salary())

developer = Developer()
developer.work()
print(developer.calculate_salary())


# ===================== Abstract Classes Can Have Normal Methods
print("Abstract Classes Can Have Normal Methods Example")
# Many beginners think abstract classes can contain only abstract methods.
# that's incorrect

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    def speak(self):
        print("Bark", end=" ")

class Cat(Animal):
    def speak(self):
        print("Meow", end=" ")

dog = Dog()
dog.speak()
dog.sleep()
cat = Cat()
cat.speak()
cat.sleep()

# Normal methods are inherited as usual.

# ======================== Abstract Classes Can Have Constructors

print("Abstract Classes Can Have Constructors Example")

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

d = Dog("Max")
print(d.name, end =" ")
d.speak()

c = Cat("Tom")
print(c.name, end =" ")
c.speak()

# Constructors work exactly like normal classes.

# ======================= Abstract Class with Class Variables
print("Abstract Class with Class Variables Example")


class Employee(ABC):

    company = "OpenAI"

    @abstractmethod
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("Work as manager in company : ", self.company)

class Developer(Employee):
    def work(self):
        print("Work as developer in company : ", self.company)

manager = Manager()
manager.work()

developer = Developer()
developer.work()



"""NOTE:
To make a class abstract in Python, we use the abc (Abstract Base Class) module and inherit from ABC. We also use the @abstractmethod decorator to mark methods that child classes must implement.

Here is a deep explanation and a complete code example demonstrating all 5 properties in action.

1. Abstract Methods
An abstract method is a method that has a declaration/signature, but no implementation (body) in the abstract class.

Why? It acts as a strict contract. Any child class must override and define this method, or Python will raise an error when you try to instantiate the child class.

2. Normal (Concrete) Methods
An abstract class is not restricted to abstract methods alone; it can also contain regular methods with complete logic.

Why? To provide shared, reusable code across all subclasses so you don't repeat yourself (DRY principle).

3. Constructors (__init__)
Even though you cannot instantiate an abstract class directly (e.g., a = AbstractClass() raises an error), it can and often does have an __init__ constructor.

Why? To initialize common instance properties when a child object is created via super().__init__().

4. Instance Variables
Variables bound to self (typically set inside __init__).

Why? Every subclass object will inherit these unique per-instance attributes.

5. Class Variables
Variables defined directly inside the class body, shared across all instances.

Why? Useful for defining shared constants or configuration data common to all child classes.


"""


























