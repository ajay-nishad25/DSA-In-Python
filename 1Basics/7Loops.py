
# Loops
# Python programming language also provides the following types of two loops:
# while loop
# for loop

# While Loop


count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count) # once the loop gets stop else part will continue to print the 5 

# Break: We use break when we like to get out of or stop the loop.

print("\nBreak statement")
count = 1
while count < 10:
    print(count)
    if count == 5:
        break
    count = count + 1



print("\nContinue statement")
count = 1
while count < 10:
    if count == 5:   
        count+=1
        continue
    print(count)
    count = count + 1

# For Loop
print("\nFor Loop")
"""
A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. 
Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""

# syntax
# for iterator in lst:
#     code goes here


numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    print(i)

print("\n")
language = 'Python'
for letter in language:
    print(letter)

# for loop in tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# Break statement 
print("\nBreak statement")
numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        break
    print(i)


print("\nContinue statement")
numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        continue
    print(i)


# The Range Function

"""
The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. 
By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
"""

lst = list(range(11))
print(lst)


lst = list(range(3,30,3))
print(lst)


for i in range(12):
    print(i)

print("\nFor Else")
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


# Exercises 

# 1 Iterate 0 to 10 using for loop, do the same using while loop.

for i in range(11):
    print(i)

count = 0
while count <= 10:
    print(count)
    count += 1

print("\nreverse loop on range list")
for i in range(10,-1,-1):
    print(i)

print("with end keyword")
count = 10
while count != -1:
    print(count, end="")
    count -=1


print()
outer = 0
while outer < 7:
    inner = 0
    while inner <= outer:
        print("#", end="")
        inner +=1
    print()
    outer +=1

"""
The Super Clean "Pythonic" Way (Only 1 Loop!)
The exercise asks you to make seven calls to print(). In Python, you don't actually need a nested loop (a loop inside a loop) to do this.

Python allows you to multiply a string by a number to repeat it. For example, "#" * 3 results in "###". You can use a single for loop to handle this beautifully:
"""

for i in range(1,8):
    print("#"*i)


"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

print("print  l x b for #")
for i in range (1,8):
    print("#"*7)


"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

"""
print()
for i in range(0,11):
    print("{} x {} = {}".format(i,i,i*1))

print("For even numbers")
for i in range(0,101):
    if i%2==0:
        print(i,end=" ") 

print("\nFor odd numbers")
for i in range(0,101):
    if i%2!=0:
        print(i,end=" ") 

result = 0
for i in range(0,101):
    result += i
print("\nsum of 0 to 100 : ", result)

result_even = 0
result_odd = 0

for i in range(0,101):
    if i%2==0:
        result_even += i
    else:
        result_odd += i

print("Even number sum from 0 to 100 : ", result_even)
print("Odd number sum from 0 to 100 : ", result_odd)
        

# Loop through the countries and extract all the countries containing the word land.
print()

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];


countries_with_land = []

for country in countries:
    if "land" in country.lower():
        countries_with_land.append(country)

print(countries_with_land)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []

for fruit in range(len(fruits)-1,-1,-1):
    reversed_fruits.append(fruits[fruit])

print(reversed_fruits)