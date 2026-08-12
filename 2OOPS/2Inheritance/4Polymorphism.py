
"""
1. What is Polymorphism?

The definition is the same as Java.

Polymorphism means "one interface, many forms."

The same method, function, or operator behaves differently depending on the object or data it works with.

Java Example
Animal a = new Dog();
a.sound();

Animal b = new Cat();
b.sound();

Output

Bark
Meow

The same method (sound()) behaves differently.

"""

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

dog = Dog()

dog.sound()

cat = Cat()

cat.sound()

# This is polymorphism. 

"""
Types of Polymorphism in Python

We'll cover:

1. Duck Typing ⭐⭐⭐
2. Method Overriding
3. Operator Overloading
4. Function Polymorphism
5. Method Overloading (Python approach)
6. Built-in Polymorphism
"""

# 1. Duck Typing ⭐⭐⭐
"""
What is Duck Typing?

Python follows this principle:

"If it walks like a duck and quacks like a duck, treat it as a duck."

In simple words:

Python doesn't care what class an object belongs to.

It only cares whether the object has the required method or attribute.
"""
print("Duck Typing Example")

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Duck:
    def sound(self):
        print("Quack")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
duck = Duck()

make_sound(dog)
make_sound(cat)
make_sound(duck)


"""
NOTE:

make_sound() never checks

Is it a Dog?
Is it a Cat?
Is it an Duck?

It simply calls

animal.sound()

If the method exists, everything works.
"""

"""
Java Comparison

In Java, you'd usually write:

class Animal {

    void sound(){}

}

Then

void makeSound(Animal a){
    a.sound();
}

The parameter type must be Animal (or an interface).

Python doesn't require a common parent class.
"""

# 2. Method Overriding
print("Method Overriding Example")

class Animal:

    def sound(self):
        print("Animal")


class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()

"""
This is runtime polymorphism through inheritance.
"""

# 3. Operator Overloading
# Python lets operators behave differently depending on the operands.

# Example

# Addition

print(5 + 3)

# Output
# 8

# Strings

print("Hello " + "World")

# Output
# Hello World

# Lists

print([1,2] + [3,4])

# Output
# [1, 2, 3, 4]

"""The same + operator behaves differently.

This is polymorphism.

Later, in Magic Methods, you'll learn how to define this behavior for your own classes using __add__()"""

# 4. Function Polymorphism
# some built-in functions work with many different types
# example len() function/method
print("Below is example of len() which accepts many different data types in single function ")

print("string example : ",len("Python"))
print("list example : ",len([1,2,3,4,5]))
print("tuple example : ",len((1,4,5,6,7,8,8,8,8)))
print("set example : ",len({3,4,5,6,7,8,98}))
print("dict example : ",len({"a":23,"b":59,"c":34,"d":[23,5,6,6,]}))

# Another example:

print(max(1,5,3))
print(max([10,20,15]))
print(max("python"))

# one function many types

# 5. Built-in Polymorphism

# Many Python functions are naturally polymorphic.
# Examples:

# len()
# max()
# min()
# sum()
# sorted()

# Example

print(sorted([3,1,2]))
print(sorted("python"))

# Output
# [1,2,3]
# ['h','n','o','p','t','y']

# Same function. Different behavior.


# 6. Method Overloading (Python Approach)

"""
This is another major Java vs Python difference.

Java
void show(){}

void show(String name){}

void show(int age){}

Valid.
"""

print("Method Overloading Example")

class Student:

    def show(self):
        print("First")

    def show(self, name):
        print(name)

s = Student()
# print(s.show()) # Only the last method exists. this line will produce the TypeError
print(s.show("Ajay"))
"""
NOTE: How Python Replaces Method Overloading?
Python does not natively support traditional method overloading. If you define a method twice in a class, the second definition overwrites the first. 
However, you can achieve the same behavior using default arguments or variable positional/keyword arguments (*args, **kwargs).
"""

# Option 1 example of default arugment
print("example of default arugment")

class Calculator:
    # Simulates overloading by making arguments optional
    def add(self, a,b,c=0):
        return a+b+c

calc = Calculator()
print(calc.add(1,2))
print(calc.add(1,2,3))

print()

class Student:
    def show(self,name=None):
        if name:
            return name
        else :
            return "No name given"

s = Student()
print(s.show())
print(s.show("Ajay"))


# Option 2 example of variable Positional arguments 

"""
How It Works
The *args syntax allows a method to accept any arbitrary number of non-keyword (positional) arguments. 
Inside the method, args becomes a tuple containing all passed values.
Best Used When
- You want to perform the same operation regardless of whether the user passes 2, 5, or 100 items.
- You are operating on homogenous data (e.g., adding a bunch of numbers, concatenating strings).
"""

# example with *args
print("Example with *args")

class MultiAdder:
    def get_sum(self, *args):
        if len(args) == 0:
            return 0
        return sum(args)


add = MultiAdder()
print("numbers given : ",add.get_sum(2,4,5,6))
print("no number given : ",add.get_sum())

# Option 3 example of variable keyword arguments
"""
How It Works
The **kwargs (keyword arguments) syntax allows a method to accept any number of named key-value pairs. Inside the method, kwargs acts as a standard dictionary.

Best Used When
- The parameters carry distinct semantic meanings (e.g., configuring an object or processing complex records).
- You want callers to be explicit about what data they are passing.
"""

print("Example with *kwargs")

class UserProfile:
    def create_user_profile(slef,name,**kwargs):
        profile = {"name":name, "status":"Active"}

        if "email" in kwargs:
            profile["email"] = kwargs["email"]
        if "age" in kwargs:
            profile["age"] = kwargs["age"]
        if "phone" in kwargs:
            profile["phone"] = kwargs["phone"]
        if "role" in kwargs:
            profile["role"] = kwargs["role"]
        else:
            profile["role"] = "Guest-User"

        return profile

user = UserProfile()
print(user.create_user_profile("Ajay"))
print(user.create_user_profile("Rahul",email="rahul@gmail.com",age=23, role="Admin"))
print(user.create_user_profile("Rahul",phone="+9190000300202",age=45, role="Super-Admin"))


# =========================== Runtime vs Compile-time Polymorphism

"""Runtime Polymorphism

Achieved through:

Method overriding
Duck typing

Example"""

class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

"""
Compile-time Polymorphism

Java:

show()
show(String)
show(int)

Python:

Not supported directly.

Instead, use:

Default arguments
*args
**kwargs
"""


# Polymorphism Without Inheritance

# This surprises many Java developers.

class Bird:

    def move(self):
        print("Fly")


class Fish:

    def move(self):
        print("Swim")


def travel(obj):
    obj.move()


travel(Bird())
travel(Fish())

# Output
# Fly
# Swim

# No inheritance.
# Still polymorphism.
# This is possible because of duck typing.