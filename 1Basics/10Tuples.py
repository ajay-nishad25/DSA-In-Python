# Tuples
"""A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). 
Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). 
Unlike list, tuple has few methods. Methods related to tuples:"""



# creating tuples

tpl = ("item1","item2","item3")

fruits = ('banana', 'orange', 'mango', 'lemon')


print(len(tpl))
print(len(fruits))

# accessing a tuple 
# we can access tuple using the index 

print(tpl[2])
print(fruits[3])
print(fruits[-4])

# Slicing tuples
# this returns new tuple 

new_fruits = fruits[1:3]
print(new_fruits)

print(hex(id(fruits)))
print(hex(id(new_fruits)))

# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. 
# Tuple is immutable if we want to modify a tuple we should change it to a list.


item_list = ['item1', 'item2', 'item3', 'item4', 'item5']
item_tpl= ["tpl1", "tpl2", "tpl3"]

new_item_tpl = tuple(item_list)
new_item_list = list(item_tpl)

print(new_item_tpl)
print(new_item_list)


# Checking an Item in a Tuple
# we can check if an item exists or not in tuple using "in" it returns boolean 

print("does item4 present in new_item_tpl : ", "item8" in new_item_tpl)

# Joining Tuples
# We can join two or more tuples using + operator

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

print(tpl3)


# 
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])


# Deleting Tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.

del new_item_tpl
del new_item_list

# below line of code will give us error
print(new_item_tpl)
print(new_item_list)


# NOTE 
"""
When we have list then why we need the tuples concept at this place ?

answer: 
In Django, tuples are useful for fixed configuration data like choices, 
where the available options should not change at runtime. 
A list is used when the collection is expected to be modified by adding, removing, or updating elements.
"""