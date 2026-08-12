# Sets
"""
A set is an unordered, mutable collection of unique elements. like hashset in java
"""

# how to declare sets in python

# using {}
numbers = {10,20,30,40}
print(numbers)
print(type(numbers))
# using set() method
new1_numbers = set([23,34,435,5,6,4])
print(new1_numbers)
print(type(new1_numbers))
# we can pass iterabls to set() method
new2_char_set = set("Python")
print(new2_char_set)
print(type(new2_char_set))
# Remember: sets are unordered, so don't depend on display order.


# Empty set 
# when we try to create empty set using {} it creates dictionary so to create empty set
# use set() method check given example below

empty_set1 = {}
print(empty_set1)
print(type(empty_set1))

empty_set2 = set()
print(empty_set2)
print(type(empty_set2))

# set stores unique values
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

# Accessing Set Elements
# print(numbers[2]) this line will give error TypeError: 'set' object is not subscriptable
# since set is unordered so there is no concept of index
# we can interate over set using for loop check below example
for number in numbers:
    print(number, end=" ")
print()


# adding new element into set
numbers = {10, 20, 20, 30, 30, 30}
numbers.add(90)
print(numbers)

# add multiple iteranle elements in one go use update() method todo so
numbers.update([2,5,6,24,66])
print(numbers)

# remove element form set using remove method
numbers.remove(90)
print(numbers)

# since i already removed the 90 form set but in below code i am retrying the same thing
# so below line will give me error "KeyError: 90"
# numbers.remove(90)
# print(numbers)

# in order to remove element in such a way if element is present then remove it and if it is not present simply ignore it 
# this can be done using discard() method
numbers.discard(90)
print(numbers)


# we can also delete an element form set using pop() but it doesnt gurantee which element will get removed from set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# to remove all element form set we use clear() method
fruits.clear()
print(fruits)


# Checking if an Element Exists check this using membership operator usin "in"
numbers = {10, 20, 20, 30, 30, 30, 50, 60, 70}
print(20 in numbers)


# if you want to delete the set variable itself use del keyword

del numbers
del fruits