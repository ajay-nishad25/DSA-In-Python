
# Python variable example


# Assigning Values to Variables
# 1. Basic Assignment: Variables are assigned values using the = operator.
age = 10
name = "ajay"
_dev = "software dev"
total_score = 23

print(age)
print(name)
print(_dev)
print(total_score)

# 2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.

hold_value = 10
print("hold_value",hold_value)
hold_value = "ajay"
print("hold_value",hold_value)

# 3. Assigning Same Value: same value can be assigned to multiple variables in a single line.

a = b = c = 100
print(a,b,c)

# 4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.
x, y, z = 1, 2.5, "Python"
print(x, y, z)

temp_value = 139
del temp_value
# print(temp_value)

print(len(_dev))

first_name = input('What is your name: ')
user_age = input('How old are you? ')

print(first_name)
print(user_age)