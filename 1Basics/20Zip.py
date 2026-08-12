"""
What is zip()?

Definition:

zip() is a built-in Python function that combines multiple iterables element by element.

In simple words:

It joins corresponding elements from multiple iterables into tuples.

SYNTAX : zip(iterable1, iterable2, ...)
"""

names = ["Ajay", "Rahul", "Amit", "Aditya"]

marks = [90, 80, 95, 34]

result = list(zip(names, marks))

print(result)

# Example 2 : Looping with zip()

names = ["Ajay", "Rahul", "Amit"]

marks = [90, 80, 95]

for name, mark in zip(names, marks):
    print(name, mark)


# Example 3 : Three Lits

names = ["Ajay", "Rahul", "Amit"]

marks = [90, 80, 95]

city = ["Mumbai", "Delhi", "Pune"]

for name, mark, place in zip(names, marks, city):
    print(name, mark, place)

# Example 4 : Different Lengths

names = ["Ajay", "Rahul", "Amit"]

marks = [90, 80]

print(list(zip(names, marks)))

# Example 5 : Dictionary Creation

names = ["Ajay", "Rahul", "Amit"]

marks = [90, 80, 95]

student = dict(zip(names, marks))

print(student)