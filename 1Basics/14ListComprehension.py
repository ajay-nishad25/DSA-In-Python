"""
What is List Comprehension?

Definition:

List Comprehension is a concise way of creating a new list from an existing iterable using a single line of code.
"""

# Instead of writing a loop and calling .append() repeatedly, Python lets you do it in one expression.

number = [1,2,3,4,5,6,7]

square = []

for num in number:
    square.append(num**2)

print(square)

# instead of writing the lengthy code using loop we can write short syntax using List Comprehension example given below
# synatx : [new_value for item in iterable]

square_lst_cmp = []

square_lst_cmp = [num**2 for num in number]

print(square_lst_cmp)

names = ["ajay", "rahul", "rohit"]

result = [name.upper() for name in names]

print(result)

# List Comprehension with if statement
# syntax : [new_value for item in iterable if condition]

numbers = [1,2,3,4,5,6]

even = []

even = [num for num in numbers if num%2==0]

odd = []

odd = [num for num in numbers if num%2!=0]

print(even)
print(odd)

# List Comprehension with if...else
# syntax : [value_if_true if condition else value_if_false for item in iterable]

numbers = [1,2,3,4,5,6]
result = []

result = ["Even" if num%2==0 else "Odd" for num in numbers]
print(result)

numbers_list = [-1,-4,6,5,-4,2,-5,9,5,-88]
result = ["Postive" if num>0 else "Negative" for num in numbers_list]
print(result)

# Nested List Comprehension
# Equivalent to nested loops.

# Traditional
pairs = []

for i in [1,2]:
    for j in ['A','B']:
        pairs.append((i,j))

print(pairs)

# List Comprehension

numbers=[1,2]
char_list = ['A','B']

pairs = [(i,j) for i in numbers for j in char_list]
print(pairs)



# Split Sentence
sentence = "I love python"

result = [word.upper() for word in sentence.split()]

print(result)

# Flatten a 2D List ⭐⭐⭐⭐⭐
# Very common in interviews.

matrix = [
    [1,2],
    [3,4],
    [5,6,7,8,9]
]

result = []

# traditional solution
for row in matrix:
    for col in row:
        print("col index ",row.index(col))
        print("row index ",matrix.index(row))
        result.append(col)

print(result)

# List comprehension solution
resutl = [num for row in matrix for num in row]
print(result)

# Create a List of Squares
numbers = [1,2,3,4,5,6]
result = [i**2 for i in numbers if i%2==0] # only print even number square
print("Even number square : ", result)

# Create a List of Cubes
result = [i**3 for i in range(1,10)]
print(result)


# Real-Life Example
# Suppose you have employee names.

employees = [
    "ajay",
    "rahul",
    "rohit"
]

result = [emp.title() for emp in employees]
print(result)

# revers each word in a string
words = "I love python"

result = [word[::-1] for word in words.split()]
print(" ".join(result))