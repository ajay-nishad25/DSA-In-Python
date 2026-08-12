"""
If you remember the previous topic:

map() → Changes every element.
filter() → Keeps only the elements that satisfy a condition.

This is the easiest way to remember the difference.

What is filter()?

Definition:

filter() is a built-in Python function that filters an iterable based on a condition and returns only those elements for which the condition is True.

In simple words:
"Keep only the elements that match a condition."

syntax : filter(function, iterable)

we can implement this on list, tuple, set and dict
"""

numbers = [1,2,3,4,5,6,7,8]

# Traditional Way

even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

print(even)

# filter()

result = list(filter(lambda x: x%2==0, numbers))
print("Even number : ", result)

# Example 1 : Even Numbers
numbers = [1,2,3,4,5,6,56]

result = filter(lambda x: x % 2 == 0, numbers)

print("Even numbers : ",list(result))

# Example 2 : Odd Numbers
numbers = [1,2,3,4,5,56]

result = filter(lambda x: x % 2 != 0, numbers)

print("Odd numbers : ",list(result))

# Example 3 : Numbers Greater Than 50
result = filter(lambda x: x > 50, numbers)
print("Number greater than 50 : ",list(result))

# Example 4 : Positive Numbers
result = filter(lambda x: x > 0, numbers)
print("Postive number : ",list(result))

# Example 5 : Remove Empty Strings
words = ["Python","","Java","","React"]
result = list(filter(lambda word: word != "", words))
print("Remove empty strings : ", result)

# A shorter version:
result = filter(None, words)
print(list(result))

"""
Why does this work?

None tells filter() to remove all falsy values.

Falsy values include:

False
None
0
0.0
''
[]
{}
set()
"""



# List
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))

# Tuple
print(tuple(filter(lambda x: x > 2, (1, 2, 3, 4))))

# Set
print(set(filter(lambda x: x > 2, {1, 2, 3, 4})))

# Dictionary (filter key-value pairs)
d = {"a": 10, "b": 20, "c": 5}
print(dict(filter(lambda item: item[1] > 10, d.items())))