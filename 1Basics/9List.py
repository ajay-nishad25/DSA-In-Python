
# Python List
"""
A list is the most commonly used data structure in Python.

It is:

- Ordered ✅
- Mutable (can be modified) ✅
- Allows duplicate values ✅
- Can store different data types together ✅
- Dynamically resizable ✅
"""

numbers = [10, 20, 30, 4, 22, 59]
print(numbers)


# Creating Lists


# 1 can be created using the [] brackets example given below
shopping = ["Milk", "Bread", "Eggs", "Butter"]

# 2 can be created using the list() in built function 
shopping_cart = list(("Milk", "Bread", "Eggs", "Butter"))

print("create using the [] brackets : ",shopping)
print("create using the list() in built function : ",shopping_cart)


# List can store different datatypes example given below
different_datatypes = [23,"34",3.44,True, [245,45]]
print(different_datatypes)


print()
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix)


# Accessing the list element directly example given below

print(shopping[3])

# Accessing based on negative indexs example given below

print(shopping[-3])

# check length of a list using len method (inbuilt)
print(len(shopping))

# Updating Elements

shopping[3] = "Maggie"
print(shopping)

# Adding new elements in list
# using append method this add element to the last of the list
numbers_array = [1,2,3,5,6]

numbers_array.append(9)
numbers_array.append(7)
print(numbers_array)

# Insert method 
# this help to add element in last, start or mid using the index given by the user

numbers_array.insert(3,4)
print(numbers_array)

# extend() method 
# this helps to extend a method i.e adds 2 list together example given below

numbers_array.extend(numbers)

print("numbers_array list", numbers_array)


# unpacking list items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# Slicing Items from a List

"""
Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. 
(default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
print("all_fruits",all_fruits)
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']

# checking items in list

is_banana = "banana" in fruits
print("is_banana",is_banana)

is_jackfruit = "jackfruit" in fruits
print("is_jackfruit", is_jackfruit)

# adding items in a list
fruits.append("Lichi")
fruits.append("Apple")

print("appended fruits : ", fruits)

# inserting new elements in list
fruits.insert(3, "watermelon")
print("Insert new item in list : ", fruits)


# Remove item form list
# this method remove specified element form list by matching the element name 

fruits.remove("watermelon")
print("removed watermelon", fruits)

# Remove item based using pop method
# The pop() method removes the specified index, (or the last item if index is not specified):

fruits.pop() # remove the last item if i dont specify the last index
print("remove last item", fruits)

fruits.pop(2)
print("remove the element which is on 2nd index : ", fruits)

# Clearing List Items
# The clear() method empties the list

# fruits.clear()
# print(fruits)
# commenting above code so that i can reuse the fruits list

# copying a list 
new_fruits = fruits

print("original fruits list : ", fruits)
print("copy fruits list : ", new_fruits)

fruits.append("watermelon")

print("original fruits list : ", fruits)
print("copy fruits list : ", new_fruits)

# since is am doing a reference here i,e new_fruits variable is just point to the original fruits array list so
# when i append watermelon in original fruits array it also shown in the new_fruits array list 

# so to copy same array list but both behave as seperate list instead of refering to the same list for both variable we use the copy() method
# id(variable_name) gives the memory address of vairbale in decimal format and hex(id(variable_name)) give address in hex-decimal format

new_copy_fruits = fruits.copy()

print("original fruits list address : ", hex(id(fruits)))
print("new copy fruits list address : ", hex(id(new_copy_fruits)))

print("original fruits list : ", fruits)
print("new copy fruits list : ", new_copy_fruits)

fruits.append("jackfruit")

print("original fruits list : ", fruits)
print("new copy fruits list : ", new_copy_fruits)



# Joining Lists


# option 1: use + operator to join multiple list using + operator we can join multiple list and store it into new variable
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + positive_numbers + zero 
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# option 2: use extend() method which add new list in the current list 
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
print(list1)


# Count method
# The count() method returns the number of times an item appears in a list:

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))   

# Finding Index of an Item
# The index() method returns the index of an item in the list:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

# Reversing a List
# The reverse() method reverses the order of a list.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)


# Sorting List Items

# option 1: using sort() method this method sort the current list in ascending or descending order if reverse=True is passed as argument

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

# option 2: using sorted() method this method returns the ordered list without modifying the original list 


# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = sorted(fruits,reverse=True)

print("original fruits list : ", fruits)     # ['banana', 'orange', 'mango', 'lemon']
print("new fruits list : ", new_fruits)     # ['orange', 'mango', 'lemon', 'banana']

print("original fruits list address : ", hex(id(fruits)))
print("new copy fruits list address : ", hex(id(new_fruits)))