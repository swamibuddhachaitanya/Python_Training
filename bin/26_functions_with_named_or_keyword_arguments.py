"""
Here,
2nd way: We can pass values to name and company using key=value format
"""


print("Function with named or keyword arguments")
print("-"*20)
# ---------------


# name, company are called named or keyword arguemnts
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1", company="comp-1")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee(company="comp-1", name="emp-2")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

received_value = employee(name="emp-2", company="comp-2")
# pass in the same order as arguments order specified in function definition
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with named or keyword arguments with default values")
print("-"*20)
# ---------------


# name, company are called named or keyword arguemnts
def employee(*, name, company="comp-1"):
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee(name="emp-1") # company will make use of default value
print("received_value:", received_value)

received_value = employee(name="emp-2", company="comp-1")
print("received_value:", received_value)

received_value = employee(name="emp-2", company="comp-2")
print("received_value:", received_value)

# ----------
# Order of the arguments
############
# 1st put all non-default/default value named or keyword arguments in any order IF ANY
###########################

print("#"*40, end="\n\n")
###########################


print("Function with variable named or keyword arguments")
print("-"*20)
# ---------------


# **prev_companies: Called variable named or keyword arguments
# name, company are called named or keyword arguments
def employee(*, name, company="comp-1", **prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]


received_value = employee(name="emp-1")
# prev_companies={}
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee(name="emp-2", company="comp-1")
# prev_companies={}
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee(name="emp-2", company="comp-2")
# prev_companies={}
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = employee(name="emp-2", company="comp-2", pc1="prev_comp_1")
# prev_companies={pc1: "prev_comp_1"}
print("received_value:", received_value, sep="\n", end="\n\n")


received_value = employee(name="emp-2", company="comp-2", pc1="prev_comp_1", pc2="prev_comp_2")
# prev_companies={pc1: "prev_comp_1", pc2: "prev_comp_2"}
print("received_value:", received_value, sep="\n", end="\n\n")

# ----------
# Order of the arguments in function definition
############
# 1st put all non-default/default value named or keyword arguments IF ANY
# then
# put variable named or keyword arguments IF ANY
###########################

print("#"*40, end="\n\n")
###########################


print("Packing and Unpacking dictionary")
print("-"*20)
# ---------------


def employee(*, name, company="comp-1", **prev_companies):
    print("Name:", name)
    print("Company:", company)
    print("prev_companies:", prev_companies)
    return [name, company, prev_companies]

# Assume this data we are getting from some source say file/db etc
my_dictionary = {  "pc1": "prev_comp_1", "pc2": "prev_comp_2"}

received_value = employee(name="emp-1", company="comp-1", **my_dictionary) # **my_dictionary Unpacking
print("received_value:", received_value, sep="\n", end="\n\n")


# Assume this data we are getting from some source say file/db etc
my_dictionary = {"name": "emp-1", "company": "comp-1", "pc1": "prev_comp_1", "pc2": "prev_comp_2"}

received_value = employee(**my_dictionary) # **my_dictionary Unpacking
print("received_value:", received_value, sep="\n", end="\n\n")


print("#"*40, end="\n\n")
###########################