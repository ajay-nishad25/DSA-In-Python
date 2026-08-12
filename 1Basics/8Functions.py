
def get_full_name():
    first_name = "ajay"
    last_name = "nishad"
    space = " "
    full_name = first_name+space+last_name
    print(full_name)

get_full_name()


def get_sum(a,b):
    return a+b

result = get_sum(29,34)
print(result)

def greetings (name):
    message = name + ', welcome to Python Learning!'
    return message

print(greetings('Ajay'))

def square_number(number):
    return number*number

print(square_number(3))

# Passing Arguments with Key and Value
# If we pass the arguments with key and value, the order of the arguments does not matter.

print()

def print_fullname(first_name, last_name):
    space =" "
    full_name = first_name+space+last_name
    return full_name

result = print_fullname(last_name='nishad',first_name='ajay')
print("Result of fullname : ",result)


print()

def is_even(number):
    if number%2 == 0:
        return True
    return False

print("578 is even", "Yes" if is_even(578) else "No")
print("571 is even", "Yes" if is_even(571) else "No")

# Function with Default Parameters

print()

def greetings (name = 'Aditya'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Ajay'))


# Arbitrary Number of Arguments

print()


def sum_all_nums(*nums):
    print(type(nums))
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10


print()
# Function as a Parameter of Another Function

def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

def total_till_n(n):
    total = 0
    for i in range (n+1):
        total += i
    return total

def do_total(func, x):
    return func(x)

print(do_total(total_till_n,10))
