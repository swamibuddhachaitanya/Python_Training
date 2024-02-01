"""
- tuple
    -- to keep list of values
    -- it keeps duplicate values as well
"""

print("Tuple PART-1")
print("How to store the values")
print("-"*20)
# ---------------

my_tuple_1 = (10, 12.5, "Python", "Java", ("Online", "Offline"))
# Internally it will create object of predefined/builtin class 'tuple' and store the values

# OR we can create using class name
my_tuple_2 = tuple((10, 12.5, "Python", "Java", ("Online", "Offline")))

print(my_tuple_1, my_tuple_2, sep="\n")

print("#"*40, end="\n\n")
###########################


print("Tuple PART-2")
print("Indexes are similar to strings. Please refer strings example")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "Python", "Java", ("Online", "Offline"))
print("my_tuple:", my_tuple, sep="\n", end="\n\n")

print("1st value:", my_tuple[0], end="\n\n")

print("1st course name:", my_tuple[2]) # Python
print("2nd character in 1st course name:", my_tuple[2][1], end="\n\n") # y

print("Inner tuple:", my_tuple[4]) # ("Online", "Offline")
print("2nd value in Inner tuple:", my_tuple[4][1]) # "Offline"
print("1st character in 2nd value in Inner tuple:", my_tuple[4][1][1], end="\n\n") # "f"

print("#"*40, end="\n\n")
###########################

print("Tuple PART-3")
print("Methods inside 'tuple' class")
print("-"*20)
# ---------------

print(dir(my_tuple))

# OR we can pass class name
print(dir(tuple))

print("#"*40, end="\n\n")
###########################

print("Tuple PART-4")
print("__add__ method")
print("-"*20)
# ---------------

my_tuple_1 = (10, 12.5, "Python", "Java", ("Online", "Offline"))
my_tuple_2 = (10, 12.5, "Python", "Java", ("Online", "Offline"))

print("my_tuple_1:", my_tuple_1, sep="\n", end="\n\n")
print("my_tuple_2:", my_tuple_2, sep="\n", end="\n\n")

my_tuple_3 = my_tuple_1.__add__(my_tuple_2)
print("my_tuple_3 using __add__ :", my_tuple_3, sep="\n", end="\n\n")

my_tuple_4 = my_tuple_1 + my_tuple_2
print("my_tuple_4 using + :", my_tuple_4, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Tuple PART-5")
print("-"*20)
# ---------------

my_tuple_1 = (10, 12.5, "Python", "Java", ("Online", "Offline", "Python", "Python"))
print("my_tuple_1:", my_tuple_1, sep="\n", end="\n\n")

count_of_python = my_tuple_1.count("Python")
count_of_python_inner_tuple = my_tuple_1[4].count("Python")

print("count_of_python:", count_of_python)
print("count_of_python_inner_tuple:", count_of_python_inner_tuple)

print("#"*40, end="\n\n")
###########################

print("Tuple PART-6")
print("Single value in tuple")
print("-"*20)
# ---------------


a = 10
b = 20
c = (a+b) # c = (30) # c = 30

# Since we are are using paranthesis for other tasks
# so to create one value tuple we will write like
T = (10,)
print("c:", c)
print("T:", T)

print("#"*40, end="\n\n")
###########################