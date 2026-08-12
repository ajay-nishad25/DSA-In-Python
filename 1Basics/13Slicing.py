# What is slicing
# Slicing is the process of extracting a portion (or subset) of a sequence such as a string, list, or tuple.

# Which data types support slicing?
# string, list and tuple this are supported by slicing
# these are not supported by slicing set and dict


# e.g
name = "Ajay Bhola Nishad"

numbers = [10,20,30,40,50,60,70,80,90,100]

marks = (95,90,85,343,5,56,6)

# syntax : sequence[start : stop : step]
# If you don't provide start, Python assumes it is 0.
# If you don't provide stop, Python goes until the end.
# Omitting both : This creates a shallow copy of the sequence (for immutable types like strings, it simply returns an equivalent string).

print(name[0:9:2])
print(numbers[4:8])
print(marks[:3])

# omitting both 
temp_str = name[:]
print(temp_str)

# now lets compare the both string with its id

print(hex(id(name)))
print(hex(id(temp_str)))

# since temp_str is shallow copy of name string they both share same memory address


# reverse a string 

temp_string = "This is temp string"

print(temp_string[::-1])

