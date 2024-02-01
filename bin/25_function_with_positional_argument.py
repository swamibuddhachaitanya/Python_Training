"""
Here
case-2: How to pass values to variables present inside the function
    - in this case, how to pass values to name and company

2 ways to pass values to name and company
1st way: We can pass only values to name and company
2nd way: We can pass values to name and company using key=value format

Here
1st way: We can pass only values to name and company
"""

print("Function with positional arguments")
print("-"*20)
# ---------------


# name, company are called positional arguemnts
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1", "comp-1")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee("emp-2", "comp-1")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee("emp-2", "comp-2")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with positional arguments with default values")
print("-"*20)
# ---------------


# name, company are called positional arguemnts
def employee(name, company="comp-1"):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee("emp-1") # company will make use of default value
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee("emp-2", "comp-1")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee("emp-2", "comp-2")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

# ----------
# Order of the arguments
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################


print("Function with variable positional arguments")
print("-"*20)
# ---------------


# *prev_companies: Called variable positional arguments
# name, company are called positional arguemnts
def employee(name, company="comp-1", *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-1")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-2")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-2", "prev_comp_1")
# prev_companies=("prev_comp_1",)
print("received_value:", received_value, sep="\n", end="\n\n")


received_value = employee("emp-2", "comp-2", "prev_comp_1", "prev_comp_2")
# prev_companies=("prev_comp_1", "prev_comp_2")
print("received_value:", received_value, sep="\n", end="\n\n")

# ----------
# Order of the arguments
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
# then
# put variable positional arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################


print("Function with variable positional arguments")
print("-"*20)
# ---------------


# *prev_companies: Called variable positional arguments
# name, company are called positional arguemnts
def employee(name, company="comp-1", *prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee("emp-1")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-1")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-2")
# prev_companies=()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee("emp-2", "comp-2", "prev_comp_1")
# prev_companies=("prev_comp_1",)
print("received_value:", received_value, sep="\n", end="\n\n")


received_value = employee("emp-2", "comp-2", "prev_comp_1", "prev_comp_2")
# prev_companies=("prev_comp_1", "prev_comp_2")
print("received_value:", received_value, sep="\n", end="\n\n")

# ----------
# Order of the arguments
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
# then
# put variable positional arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################

print("Packing and Unpacking")
print("-"*20)
# ---------------


def employee(name, company="comp-1", *prev_companies): # *prev_companies called PACKING
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]

# Assumen this data we are getting from some source say file/db etc
my_list = ["emp-2", "comp-2", "prev_comp_1", "prev_comp_2"]

# received_value = employee(my_list) # WRONG: mylist will be passed to name

# 1-way
received_value = employee(my_list[0], my_list[1], my_list[2], my_list[3])
print("received_value:", received_value, sep="\n", end="\n\n")


# 2-way: Shortcut- UNPACKING
# *my_list will take care of passing individual values like mentioned in 1-way
received_value = employee(*my_list)
print("received_value:", received_value, sep="\n", end="\n\n")

# ----------
# Order of the arguments
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
# then
# put variable positional arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################


print("Packing and Unpacking dictionary")
print("-"*20)
# ---------------


def employee(name, company="comp-1", *prev_companies): # *prev_companies called PACKING
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]

# Assume this data we are getting from some source say file/db etc
my_dictionary = {0: "emp-2", 1: "comp-2", 2: "prev_comp_1", 3: "prev_comp_2"}

received_value = employee(*my_dictionary.keys())
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee(*my_dictionary.values())
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee(*my_dictionary.items())
print("received_value:", received_value, sep="\n", end="\n\n")

# ----------
# Order of the arguments
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
# then
# put variable positional arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################

