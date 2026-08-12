"""
What is reduce()?

Definition:

reduce() applies a function repeatedly to an iterable and reduces all the elements into a single final value.

In simple words:

Many values → One value
"""

# syntax : reduce(function, iterable, initial_value[optional])

from functools import reduce

numbers = [1,2,3,4]


# Example 1 : Sum of Numbers
result = reduce(lambda x,y: x+y, numbers, 10)
print(result)


# Example 2 : Product
result = reduce(lambda x,y: x*y, numbers)
print(result)


# Example 3 : Maximum
numbers = [10,50,30,80,20]
result = reduce(lambda x,y: x if x>y else y, numbers)
print(result)

# Example 4 : Mimimum
numbers = [10,50,30,80,20]
result = reduce(lambda x,y: x if x<y else y, numbers)
print(result)

# Example 5 : Longest String
words = [
    "Java",
    "Python",
    "React",
    "JavaScript"
]

result = reduce(lambda x,y: x if len(x)> len(x) else y, words)
print(result)

# traditional way

def get_largest_string(words):
    largest_string = words[0]

    for wrd in words:
        if len(wrd) > len(largest_string):
            largest_string += wrd
    return wrd

print(get_largest_string(words))

# Example 6 : Concatenate Strings

words = [
    "I ",
    "love ",
    "Python"
]

# traditional way

def get_string_cont(words):
    result_str = ""
    for wrd in words:
        result_str += wrd
    return result_str

print(get_string_cont(words))

# using reduce
result = reduce(lambda x,y : x + y, words)
print(result)

