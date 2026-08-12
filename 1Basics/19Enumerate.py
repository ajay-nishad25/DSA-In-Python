"""
What is enumerate()?

Definition:

enumerate() is a built-in Python function that adds an index (counter) to every element of an iterable.

In simple words:

It gives you both the index and the value while iterating.

SYNTAX:
    enumerate(iterable, start=0)
    Parameters
    iterable → List, Tuple, String, Set, Dictionary, etc.
    start → Starting index (default is 0)

"""

# Example 1 : 

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# to achive simple implementation we need this below traditional way i.e

index = 0
for element in fruits:
    print(index,element)
    index+=1

# Example 2: for start parameter
print("Enumerate with start parameter : ")
for index, fruit in enumerate(fruits,start=1):
    print(index, fruit)



# Example 3 : Tuple

print("Tuple Example : ")
numbers = (10,20,30)

for index, value in enumerate(numbers):
    print(index, value)

# Example 4 : String
print("String Example : ")
word = "Python"
for index, char in enumerate(word):
    print(index, char)


# Example 5 : Set
print("Set Example : ")
colors = {"Red", "Blue", "Green"}

for index, color in enumerate(colors):
    print(index, color)
# Remember: Sets are unordered, so the order may differ each time.

# Example 6 : Dictionary

print("Dictionary Example : ")
student = {
    "name":"Ajay",
    "age":23,
    "city":"Mumbai"
}

for index, (key,values) in enumerate(student.items()):
    print(index, (key,values))



# Why Not Use range(len())?
# Many beginners write:

fruits = ["Apple", "Banana", "Mango"]

for i in range(len(fruits)):
    print(i, fruits[i])

# This works.
# But Python developers prefer:

for index, fruit in enumerate(fruits):
    print(index, fruit)

# because it is
# Cleaner
# More readable
# More Pythonic