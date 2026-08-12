# What is map()?
# Definition:
# map() is a built-in Python function that applies a function to every element of an iterable and returns a map object (iterator).
# map works with list, set, tuple and dict

# Why do we need map()?
# Suppose you have

numbers = [1, 2, 3, 4, 5]

# You want the square of every number.

# traditional 
square = []

for num in numbers:
    square.append(num*num)

print(square)

# syntax : map(function, iterable)

# using map along with lambda

# Wrap map() inside list()
result = list(map(lambda x: x*x, numbers))
print(result)

# why wrapping read below text
"""
Why does Python do this? (Lazy Evaluation)
This behavior is called lazy evaluation, and it’s actually a huge memory optimization feature!

Imagine you had a list of 10 million numbers:

Without lazy evaluation (list): Python would instantly compute all 10 million squares and load them all into your computer's RAM at once, which could crash your script.

With lazy evaluation (map object): Python stores zero results in RAM initially. It calculates 1*1 when you ask for the 1st item, 2*2 when you ask for the 2nd, and drops them from memory as soon as you're done processing them.
"""

# Normally we convert it into
# list()
# tuple()
# set()

# why
# Why list()?

# Look carefully.

# numbers = [1,2,3]

# result = map(lambda x:x*x, numbers)

# print(result)

# Output

# <map object at 0x...>

# Because map() returns an iterator, not a list.

# Convert it.

# print(list(result))

# Output

# [1,4,9]


numbers = [1,2,3,4,5]


# Example 1 : Square Numbers
result = list(map(lambda x: x*x, numbers))
print("square result : ", result)

# Example 2 : Cube Numbers
result = list(map(lambda x: x**3, numbers))
print("cube result : ", result) 

# Example 3 : Double Numbers
result = list(map(lambda x: x+x, numbers))
print("double result : ", result) 

# Example 4 : Convert String to Uppercase
names = ["ajay","rahul","amit"]

result_string = list(map(lambda str: str.upper(), names))
print("uppercase result : ", result_string)

# Example 5 : String Length
names = ["Ajay","Rahul","Python"]

result_string = list(map(lambda str: len(str),names))
print("string length result : ", result_string)

# Example 6 : Convert to Integer
numbers = ["1","2","3"]
result_int = list(map(lambda i : int(i), numbers))
print("integer result : ", result_int)

# Example 7 : Convert Integer to String
numbers = [1, 2, 3]
result_str = list(map(lambda x: str(x), numbers))
print("int to str : ",result_str)

# Mapping Multiple Iterables
list1 = [1,2,3]

list2 = [10,20,30]

result = map(lambda x,y:x+y, list1, list2)

print(list(result))
