# int to float and float to int conversion
int_num = 34
print("int number : ", int_num)

float_convert_int = float(int_num)
print("float number : ", float_convert_int)

float_number = 89.39243
print("float number : ", float_number)

int_convert_float = int(float_number)
print("int number : ", int_convert_float)


# string to int/float conversion 
# dont convert decimal string number directely to int instead 1st converted it to float then convert it to int

og_str = "25"
print("string number : ", og_str)

str_convert_int = int(og_str)
print("int number : ", str_convert_int)

og_str2 = "34.55"
print("string number : ",type(og_str2), og_str2)

str2_convert_float = float(og_str2)
print("float number : ", type(str2_convert_float), str2_convert_float)

str3_convert_int = int(str2_convert_float)
print("int number : ", type(str3_convert_int), str3_convert_int)

# boolean to int/float

boolean_value1 = False
print("boolean value : ", boolean_value1)

int_convert_boolean = int(boolean_value1)
print("int number : ", type(int_convert_boolean), int_convert_boolean)

string_convert_boolean = str(boolean_value1)
print("string value : ", type(string_convert_boolean), string_convert_boolean)


print(bool(1))
print(bool(100))
print(bool(-1))
print(bool(0))

print(bool("")) # empty string is considered as False and non-empty string is considered as True
print(bool("ajay"))

print(bool([]), "empty list also considered as False")
print(bool([1,2,3]), "non-empty list is considered as True")

print(bool({}), "empty dictionary also considered as False") 
print(bool(set()), "empty set also considered as False")



# list
print(list("Python")) # converting string to list

print(list((1, 2, 3))) # converting tuple to list


# typle

print(tuple([1, 2, 3])) # converting list to tuple

print(tuple("Python")) # converting string to tuple

# set

print(set([1, 2, 2, 3]))

print(set("Python"))