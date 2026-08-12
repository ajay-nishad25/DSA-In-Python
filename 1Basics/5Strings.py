"""
Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. 
There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.
"""

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
print(len(sentence))

# Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
print("length of multiline string is", len(multiline_string))

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print("length of multiline string is", len(multiline_string))

first_name = "ajay"
last_name = "nishad"
concat = first_name + " " + last_name
print(concat)
print(len(concat))


# Escape Sequences in Strings
print("\nEscape Sequences in Strings")
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

print("\nString formatting")
# New Style String Formatting (str.format)
# This format was introduced in Python version 3.


first_name = 'ajay'
last_name = 'nishad'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)


# Python Strings as Sequences of Characters

print("\nPython Strings as Sequences of Characters")
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n



# Slicing Python Strings
print("\nSlicing Python Strings"),

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_letter = language[-6]
print(last_letter) # n

first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon


text = "helloworld!"

print(text[3:5])
print(text[::-1], "reverse string") # sequence[start : stop : step] when start and stop is not given it by default consider the start and len for end


# String Methods

print("\nString Methods")

# capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'


# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '@ '.join(web_tech)
print(result) 

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'temp coding')) # 'thirty days of temp coding'

# split(): Splits the string, using given string or space as a separator
temp = challenge.split()
print(temp, type(temp)) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON