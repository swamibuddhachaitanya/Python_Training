"""
MUTABLE TYPES
(Once we store the values, we CAN modify throught the program)
- list
    -- to keep list of values
    -- it keeps duplicate values as well
"""

print("list PART-1")
print("How to store the values")
print("-"*20)
# ---------------

my_list_1 = [10, 12.5, "Python", "Java", ("Online", "Offline")]
# Internally it will create object of predefined/builtin class 'list' and store the values

# OR we can create using class name
my_list_2 = list((10, 12.5, "Python", "Java", ("Online", "Offline")))

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
###########################

print("list PART-2")
print("Indexes are similar to strings. Please refer strings example")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", "Java", ("Online", "Offline")]
print("my_list:", my_list, sep="\n", end="\n\n")

print("1st value:", my_list[0], end="\n\n")

print("1st course name:", my_list[2]) # Python
print("2nd character in 1st course name:", my_list[2][1], end="\n\n") # y

print("Inner list:", my_list[4]) # ("Online", "Offline")
print("2nd value in Inner list:", my_list[4][1]) # "Offline"
print("1st character in 2nd value in Inner list:", my_list[4][1][1], end="\n\n") # "f"

print("#"*40, end="\n\n")
###########################

print("list PART-3")
print("Methods inside 'list' class")
print("-"*20)
# ---------------

print(dir(my_list))

# OR we can pass class name
print(dir(list))

print("#"*40, end="\n\n")
###########################


print("list PART-4")
print("Add new element")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", "Java", ("Online", "Offline"), ["Blr", "Hyd"]]
print("my_list:", my_list, sep="\n", end="\n\n")

my_list.append("C++")
my_list[5].append("Pune")

print("my_list after append:", my_list, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("list PART-5")
print("Update element")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", "Java", ("Online", "Offline"), ["Blr", "Hyd"]]
print("my_list:", my_list, sep="\n", end="\n\n")

my_list[2] = "C++"
my_list[4] = ["Online", "Offline"]
my_list[5][0] = "Mumbai"

print("my_list after update:", my_list, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("list PART-6")
print("remove element")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", "Java", ("Online", "Offline"), ["Blr", "Hyd"]]
print("my_list:", my_list, sep="\n", end="\n\n")

removed_element = my_list.pop(2)
print("removed_element:", removed_element)

removed_element = my_list.pop(3)
print("removed_element:", removed_element)

removed_element = my_list[3].pop(0)
print("removed_element:", removed_element)

print("my_list after remove:", my_list, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

