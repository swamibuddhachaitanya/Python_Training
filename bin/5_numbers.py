"""
Numbers
"""

print("Numbers PART-1")
print("How to store the values?")
print("-"*20)
# ---------------

a = 100
# Internally it will create object of predefined/builtin class 'int' and store the value

# OR
# we can use class name
b = int(200) # same as b=200

print(a, b, sep="\n")

# 1. NO primitive data types in python
# 2. All data types are objects
# 3. using class we can create object


print("#"*40, end="\n\n")
###########################


print("Numbers PART-2")
print("How it is immutable?")
print("-"*20)
# ---------------

# Refer 6_stack_and_heap.xlsx

a = 100
print("Value of a:", a)
print("Reference ID of a:", id(a), end="\n\n")

a = 200
print("Value of a:", a)
print("Reference ID of a:", id(a), end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Immutable values will be reused internally by interpreter")
print("-"*20)
# ---------------

# Refer 6_stack_and_heap.xlsx

a = 100
b = 100
c = 100
print("Reference ID of a:", id(a), end="\n\n")
print("Reference ID of b:", id(b), end="\n\n")
print("Reference ID of c:", id(c), end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Reference count")
print("-"*20)
# ---------------

a = 1000000000000
b = 1000000000000
c = 1000000000000

import sys
print("Total references refering to value/object 1000000000000 is:", sys.getrefcount(1000000000000))

print("#"*40, end="\n\n")
###########################


print("garbage Collection")
print("-"*20)
# ---------------

# Refer 6_stack_and_heap.xlsx
print("Refer 6_stack_and_heap.xlsx")

print("#"*40, end="\n\n")
###########################