# If Condition

# syntax
# if condition:
#     this part of code runs for truthy conditions
# else:
#     this part of code runs for false conditions




a = 3
b = 10

if b>=10:
    print("b is greater or equal to 10")

if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')


# if elif else

if a>0:
    print("a is positive number")
elif a<0:
    print("a is negative number")
else:
    print("a is zero")


# If Condition and Logical Operators

a = 34
b = 55

if a>0 and b>0:
    print("a and b are positive numberes")
elif a<0 and b<0:
    print("a and b both are negative number")
else:
    print("a and b both are zero")



user = "ajay"
access_level = 3

if user =="admin" or access_level >= 4:
    print("Access Granted")
else:
    print("Access Denied")


user_age = int(input("Enter your age : "))

if user_age >= 18:
    print("Your are eligible for driving")
else:
    temp = 18-user_age
    print("You need {} more years to learn to drive.".format(temp))


marks = int(input("Enter your marks : "))

if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79:
    print("Grade C")
elif marks>=60 and marks<=69:
    print("Grade D")
else:
    print("Grade E")

    
# Excercise
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person and len(person["skills"]) >0:
    person_skills = person["skills"]
    print(person_skills)

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person and len(person["skills"]) >0:
    if "Python" in person["skills"]:
        print("Person has Python skill")
    else:
        print("Person does not have Python skill")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if "skills" in person and len(person["skills"]) >0:
    person_skills = person["skills"]
    if("JavaScript" in person_skills and "React" in person_skills):
        print("He is a front end developer")
    elif("Node" in person_skills and "Python" in person_skills and "MongoDB" in person_skills):
        print("He is a backend developer")
    elif("React" in person_skills and "Node" in person_skills and "MongoDB" in person_skills):
        print("He is a fullstack developer")
    else:
        print("unknown title")

#  * If the person is married and if he lives in Finland, print the information in the following format:

if "is_married" in person and "country" in person:
    if person["is_married"] and person["country"] == "Finland":
        print(f"{person['first_name']} {person['last_name']} is married and lives in Finland")
    else:
        print("Person is not married or does not live in Finland")



# Switch case example
"""
syntax:
match term:
    case pattern-1:
        action-1
    case pattern-2:
        action-2
    case pattern-3:
        action-3
    case _:
        action-default
"""

print("Switch Case Example : ")


lang = input("What's the programming language you want to learn? ")



match lang.lower():
    case "python":
        print("You can become a Data Scientist")
    case "javaScript":
        print("You can become a web developer.")
    case "java":
        print("You can become a mobile app developer.")
    case "c++":
        print("You can become a game developer.")
    case _:
        print("The language doesn't matter, what matters is solving problems.")