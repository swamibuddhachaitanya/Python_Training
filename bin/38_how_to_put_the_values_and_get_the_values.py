"""
How to put the values and get the values

1-way

In this section, we should get 100% clarity on
1) CLASS VARIABLES
2) INSTANCE VARIABLES
"""

print("How to put the values and get the values")
print("-"*20)
# ---------------

class Employee:
    pass
# Even though block is empty it is valid class

# create 2 objects
e1 = Employee()
e2 = Employee()

# Put values
Employee.company_name = "comp-1"
e1.name = "emp-1"
e2.name = "emp-2"

# Get the values
print("Company Name:", Employee.company_name)
print("Employee 1 name:", e1.name)
print("Employee 2 name:", e2.name)

print("#"*40, end="\n\n")
###########################

print("Inside each object")
print("-"*20)
# ---------------

print("Inside Class object 'Employee':", dir(Employee))
print("Inside Instance object 'e1':", dir(e1))
print("Inside Instance object 'e2':", dir(e2))

print("#"*40, end="\n\n")
###########################

# CLASS OBJECT: is common space for all instance objects. data
# which is common for all instance objects, those data we can keep it
# inside CLASS OBJECT. We can access using either instance or class object


print("Access Company Name Using instance and class objects")
print("-"*20)
# ---------------

print("Access company_name using class object 'Employee':", Employee.company_name)
print("Access company_name using instance object 'e1':", e1.company_name)
print("Access company_name using instance object 'e2':", e2.company_name)

print("#"*40, end="\n\n")
###########################