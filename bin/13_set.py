"""
MUTABLE TYPES
(Once we store the values, we CAN modify throught the program)
- set
    -- to keep list of values
    -- it keeps UNIQUE values only
    -- It will not maintain the order
    -- We can store only immutable values
    -- No index to each value
"""

print("set PART-1")
print("How to store the values")
print("-"*20)
# ---------------


my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
print("my_set_1:", my_set_1)

my_set_2 = set({10, 10, 10, "Python", "Python", "Java", "Java"})
print("my_set_2:", my_set_2)

print("#"*40, end="\n\n")
###########################

# About indexes
# ---------------
# - Since We don't have indexes to each values
#   we will not be able to access each value
#   instead we can also convert this to other type
#   like list/tuple etc to get index if we want
# - OR we can iterate using loops
###########################


print("set PART-2")
print("Methods inside set class")
print("-"*20)
# ---------------

print(dir(my_set_1))

# OR we can also pass class name
print(dir(set))

print("#"*40, end="\n\n")
###########################


print("set PART-3")
print("Add new element")
print("-"*20)
# ---------------

my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
print("my_set_1:", my_set_1)

my_set_1.add("C++")
my_set_1.add("C++")
my_set_1.add("C++")
my_set_1.add("C++")
print("my_set_1 after add:", my_set_1)

print("#"*40, end="\n\n")
###########################

print("set PART-4")
print("Update new element")
print("-"*20)
# ---------------

my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
print("my_set_1:", my_set_1)

# Update 'Python' to 'C++'
my_set_1.remove("Python")
my_set_1.add("C++")
print("my_set_1 after update:", my_set_1)

print("#"*40, end="\n\n")
###########################

print("set PART-4")
print("Update new element")
print("-"*20)
# ---------------

my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
print("my_set_1:", my_set_1)

my_set_2 = {"C++", 20, 20}
print("my_set_2:", my_set_2)


my_set_1.update(my_set_2)
print("my_set_1 after update my_set_2:", my_set_1)

print("#"*40, end="\n\n")
###########################

print("set PART-5")
print("Remove element")
print("-"*20)
# ---------------

my_set_1 = {10, 10, 10, "Python", "Python", "Java", "Java"}
print("my_set_1:", my_set_1)

my_set_1.remove("Python")
removed_value = my_set_1.pop()

print("my_set_1 after remove & pop:", my_set_1)
print("removed_value:", removed_value)

print("#"*40, end="\n\n")
###########################