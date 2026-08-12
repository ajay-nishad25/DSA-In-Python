# what is lambda
# A Lambda Function is an anonymous (nameless) function that can have any number of arguments but only one expression.


# traditional way of writing function
def square(x):
    return x * x

print(square(5))

# lambda synatx : lambda parameters : expression
# Notice there is no return keyword.
# The expression is automatically returned.

# square example

square = lambda x : x**2
print(square(5))

# addition example

addition = lambda a,b,c : a+b+c
print(addition(1,2,3))

# multiplication example

multiply = lambda a, b: a * b
print(multiply(5, 6))

# check even and odd
check_even_odd = lambda x : "Even" if x%2==0 else "Odd"
print(check_even_odd(2))

# lambda with sorted()

# suppose we have
students = [
    ("Ajay", 70),
    ("Rahul", 95),
    ("Amit", 85)
]
# sort by marks 

def get_marks(student):
    return student[1]

result_sorted = sorted(students, key=get_marks)
print(result_sorted)

# using lambda function

result_sorted_lambda = sorted(students, key= lambda student:student[1])
print(result_sorted_lambda)


# Limitations of Lambda
# ❌ Cannot contain multiple statements
"""lambda x:
    print(x)
    return x*x"""

# ❌ Cannot use loops
"""lambda x:
    for i in range(x):
        ..."""

