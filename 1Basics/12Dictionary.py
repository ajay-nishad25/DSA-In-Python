# Dictionary
# A dictionary is an ordered, mutable collection of key-value pairs, where each key is unique and is used to access its corresponding value.

# deceleration
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct)
print(type(dct))

# using method
person = dict(first_name='Asabeneh', last_name='Yetayeh', age=25)
print(type(person))
print(person)


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(person)

print(len(person))


print(person['first_name'])
print(person['is_married'])
print(person['address'])
print(person['skills'][3])

# if we put key and that key is not available then it will print error
# print(person['man']) # this will print error

# use .get() method return none if key is not available 

print(person.get("man"))

person['age'] = 34 # update
person['skills'].append('Django')
print(person)

# adding new key to the dict

student = {
    "name": "Ajay"
}

student["age"] = 23

print(student)

# updating a key value

student["age"] = 25
print(student)

# update() Method

student = {
    "name": "Ajay",
    "age": 23
}

student.update({
    "age": 24,
    "city": "Mumbai"
})

print(student)

# remove value using pop() method 
# it basically remove the key-value pair and return the value

student = {
    "name": "Ajay",
    "age": 23
}

age = student.pop("age")

print(age)
print(student)

# remove the last inserted key-value pair by using popitem()

student = {
    "name": "Ajay",
    "age": 23,
    "city": "Mumbai"
}

item = student.popitem()

print(item)
print(student)


# use del keyword to delete a specific key-value or entire dict

student = {
    "name": "Ajay",
    "age": 23
}

del student["age"]

print(student)

del student

# print(student) 

# use clear() to clear all the key-value pair but this will keep the empty dict intact
student = {
    "name": "Ajay",
    "age": 23
}

student.clear()

print(student)


# check if key exists using membership operator ie. "in"

student = {
    "name": "Ajay",
    "age": 23
}

print("name" in student)

# key() method will print all the keys present in dict 
student = {
    "name": "Ajay",
    "age": 23,
    "city": "Mumbai"
}

print(student.keys())

# we can iterate over keys 
for key in student.keys():
    print(key)

# values() method will print all the values present in dict
student = {
    "name": "Ajay",
    "age": 23,
    "city": "Mumbai"
}

print(student.values())

# we can iterate over values 
for value in student.values():
    print(value)

# items() method will print all the key-value pair present in dict
student = {
    "name": "Ajay",
    "age": 23,
    "city": "Mumbai"
}

print(student.items())

# we can iterate over items
for item in student.items():
    print(item)

# above code will print something like this
# ('name', 'Ajay')
# ('age', 23)
# ('city', 'Mumbai')
# where evey item is a tuple so to unpack it we can loop in this way given below

for key, value in student.items():
    print(key, value)