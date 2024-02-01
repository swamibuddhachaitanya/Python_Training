"""
How to put the values and get the values

3-way

In this section, we should get 100% clarity on
1) Constructor: __new__
2) Initialization : __init__
"""

print("How to put the values and get the values")
print("-"*20)
# ---------------

class Employee:

    company_name = "comp-1"
    # If we define any varaibles inside class then it will get stored in class object

    def __init__(self, en):
        self.name = en

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def get_employee_name(self):
        return self.name

# create 2 objects
e1 = Employee("emp-1")
e2 = Employee("emp-2")


print("Company Name:", Employee.get_company_name())
print("Employee-1 Name:", e1.get_employee_name())
print("Employee-2 Name:", e2.get_employee_name())

print("#"*40, end="\n\n")
###########################

print("Inside builtin class 'object'")
print("-"*20)
# ---------------

print(dir(object))

print("#"*40, end="\n\n")
###########################


print("When we create object then....")
print("-"*20)
# ---------------

# POINT-1:
# When we create object like
# --------------
# e1 = Employee("emp-1")
# then
# internally
# it calls 2 methods automatically one after the other
# 1) __new__() This will construct the object and steore in 'e1'
# then automatically it will execute
# 2) __init__() to initialize the object
#
# POINT-2:
# - We can always rewrite methods coming from objects
#   with same name(POLYMORPHISM) : Method overriding
#
# POINT-3:
# - we wrote __init__ () , we are overriding __init__
#   to store values
print("#"*40, end="\n\n")
###########################