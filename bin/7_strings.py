"""
Strings
"""

print("Strings PART-1")
print("How to store the values")
print("-"*20)
# ---------------

a = 'PERSON'
# Internally it will create object of predefined/builtin class 'str'
# and store the values

# Using class also we can create
b = str('PERSON')
print(a, b, sep="\n")

print("#"*40, end="\n\n")
###########################


print("Strings PART-2")
print("How to store the values")
print("-"*20)
# ---------------

a = 'PERSON'

b = 'PERSON\'S'
# OR
b = "PERSON'S"

c = '''PERSON'S HEIGHT IS XYZ" (" represents inches)'''

d = """PERSON'S HEIGHT IS XYZ" (" represents inches)"""


print(a, b, c, d, sep="\n")

print("#"*40, end="\n\n")
###########################
# Difference b/n multi line comment and string
# ---------------
# - If we assign to variable it is string
# - If we are not assigning then it is multi line comment
# - Actually it is unassigned string
# - It will execute when we run the program
#   but it will not skipped
# - Only commented line with # will be skipped
# - Since multi line comments using ''' or """
#   are getting executed. We need to avoid using this.
###########################


print("Strings PART-3")
print("How to store the values")
print("-"*20)
# ---------------

data_1 = "C:\newfolder\test.py"
print("data_1:", data_1, sep="\n", end="\n\n")

data_2 = r"C:\newfolder\test.py"
print("raw data data_2 :", data_2, sep="\n", end="\n\n")
# r -> raw data, no special meaning for any character

print("Convert data_1 to raw string:", repr(data_1), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Strings PART-4")
print("How to store the values")
print("-"*20)
# ---------------

x = 10
y = 20
z = x + y

result = f"add of {x} and {y} is {z}"
print("result:", result, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Strings PART-5")
print("Concatination and Repetation")
print("-"*20)
# ---------------

s1 = "Hello"
s2 = "Python"

concat_result = s1 + s2
rept_result = s1*10

print("concat_result:", concat_result)
print("rept_result:", rept_result)

print("#"*40, end="\n\n")
###########################

print("Strings PART-6")
print("Indexes: Access each character using index")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 8_strings.xlsx Section-1
print("0th character using +ve index no:", my_string[0])
print("0th character using -ve index no:", my_string[-8])


# print("100th character using +ve index no:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
###########################


print("Strings PART-7")
print("Slicing: Getting the substring")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 8_strings.xlsx Section-2
print("substring from index-1 to index-6 using +ve index no:", my_string[1:6])
print("substring from index-1 to index-6 using -ve index no:", my_string[-7:-2])
print("substring from index-1 to index-6 using +ve/-ve index no:", my_string[-7:6])
print("substring from index-1 to index-6 using +ve/-ve index no:", my_string[1:-2], end="\n\n")

print("substring from index-1 to END using +ve index no:", my_string[1:], end="\n\n")

print("substring from BEGINNING to index-6 using +ve index no:", my_string[:6], end="\n\n")

print("substring from BEGINNING to END using +ve index no:", my_string[:], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Strings PART-8")
print("Step Value: We can skip characters")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 8_strings.xlsx Section-3

print("substring from index-1 to index-6 using +ve index no step by 1:", my_string[1:6])
print("substring from index-1 to index-6 using -ve index no step by 1:", my_string[-7:-2], end="\n\n")
# by default step value = 1
# which means, from index-1 to 6, give me every character

print("substring from index-1 to index-6 using +ve index no step by 1:", my_string[1:6:1])
print("substring from index-1 to index-6 using -ve index no step by 1:", my_string[-7:-2:1], end="\n\n")
# step value = 1
# which means, from index-1 to 6, give me every character

print("substring from index-1 to index-6 using +ve index no step by 2:", my_string[1:6:2])
print("substring from index-1 to index-6 using -ve index no step by 2:", my_string[-7:-2:2], end="\n\n")
# step value = 2
# which means, from index-1 to 6, give me every 2nd character
# character at start index will always come

print("substring from index-1 to index-6 using +ve index no step by 3:", my_string[1:6:3])
print("substring from index-1 to index-6 using -ve index no step by 3:", my_string[-7:-2:3], end="\n\n")
# step value = 3
# which means, from index-1 to 6, give me every 3rd character
# character at start index will always come

print("#"*40, end="\n\n")
###########################


print("Strings PART-9")
print("-ve Step Value: reverse direction")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 8_strings.xlsx Section-4

print("substring from index-6 to 1 using +ve index no, step by '-1'", my_string[6:1:-1])
print("substring from index-6 to 1 using -ve index no, step by '-1'", my_string[-2:-7:-1], end="\n\n")

print("substring from index-6 to 1 using +ve index no, step by '-2'", my_string[6:1:-2])
print("substring from index-6 to 1 using -ve index no, step by '-2'", my_string[-2:-7:-2], end="\n\n")


print("#"*40, end="\n\n")
###########################


print("Strings PART-10")
print("Methods inside 'str' class")
print("-"*20)
# ---------------

print(dir(my_string))
#
# OR
# we can also pass class name
# print(dir(str))

print("#"*40, end="\n\n")
###########################

print("Strings PART-11")
print("Why __ names?")
print("-"*20)
# ---------------

# -  __ names are system defined names
# - these names are mapped/linked to some operators or some function
# Example

x = "Hello"
y = "Python"
concat_result = x + y
concat_result_2 = x.__add__(y)
print("concat_result:", concat_result)
print("concat_result_2:", concat_result_2, end="\n\n")

rept_result = x * 10
rept_result_2 = x.__mul__(10)
print("rept_result:", rept_result)
print("rept_result_2:", rept_result_2)

length_1 = len(x)
length_2 = x.__len__()
print("length_1:", length_1)
print("length_2:", length_2)

print("#"*40, end="\n\n")
###########################

print("Strings PART-12")
print("Learning 'startswith' method")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string:", my_string, sep="\n", end="\n\n")

result = my_string.startswith("WEL")
print('my_string.startswith("WEL") result is:', result)

print("#"*40, end="\n\n")
###########################


print("Strings PART-13")
print("Learning 'strip' method")
print("-"*20)
# ---------------

my_string = "        WEL       COME        "
print("my_string:", repr(my_string), sep="\n", end="\n\n")

result = my_string.strip()
# It will remove extra-spaces, newline, tabs from BOTH ends
#   not in between space
print("my_string.strip() result :", result)


print("#"*40, end="\n\n")
###########################


print("Strings PART-14")
print("Learning 'strip' method: PART-2")
print("-"*20)
# ---------------

my_string = "XYXYXYXYWEL   XYXY    COMEXYXYXYX"
print("my_string:", repr(my_string), sep="\n", end="\n\n")

result = my_string.strip('XY')
# It will remove extra-spaces, newline, tabs from BOTH ends
#   not in between space
print("my_string.strip('XY') result :", result)


print("#"*40, end="\n\n")
###########################

print("Strings PART-15")
print("Learning 'split' method")
print("-"*20)
# ---------------
my_string = "WEL COME"
print("my_string:", repr(my_string), sep="\n", end="\n\n")

result = my_string.split() # ['WEL', 'COME']
print("my_string.split() result : ", result)

print("#"*40, end="\n\n")
###########################


print("Strings PART-16")
print("Learning 'split' method: PART-2")
print("-"*20)
# ---------------
my_string = "WEL COME"
print("my_string:", repr(my_string), sep="\n", end="\n\n")

result = my_string.split("E") # ["W", "L COM", ""]
print("my_string.split('E') result : ", result)

print("#"*40, end="\n\n")
###########################


print("Strings PART-17")
print("Learning 'index' method")
print("-"*20)
# ---------------
my_string = "WEL COME"
print("my_string:", repr(my_string), sep="\n", end="\n\n")

result = my_string.index('E') # It will return index of 1st occurance
print("my_string.index('E') result:", result)

result = my_string.index('COME') # It will return index of 'C'
print("my_string.index('COME') result:", result)

result = my_string.index('E', 3) # start looking from index-3
print("my_string.index('E', 3) result:", result)

print("#"*40, end="\n\n")
###########################

print("Strings PART-18")
print("Learning 'encode' method")
print("-"*20)
# ---------------
my_string = "WEL COME"
print("my_string:", repr(my_string), sep="\n", end="\n\n")

print("type of my_string:", type(my_string), sep="\n", end="\n\n")

my_string = my_string.encode()
print("type of my_string after encode:", type(my_string), sep="\n", end="\n\n")

print(my_string)
print("#"*40, end="\n\n")
###########################