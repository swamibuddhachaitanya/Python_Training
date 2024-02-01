"""
How to put the values and get the values

2-way

In this section, we should get 100% clarity on
1) CLASS METHODS
2) INSTANCE METHODS
"""


print("How to put the values and get the values")
print("-"*20)
# ---------------

class Employee:
    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def store_employee_name(self, en):
        self.name = en

    def get_employee_name(self):
        return self.name

# create 2 objects
e1 = Employee()
e2 = Employee()

# Store the value in class object
Employee.store_company_name("comp-1") # Employee.store_company_name(Employee, "comp-1")
#
#     def store_company_name(cls, cn):
#         cls.company_name = cn
#
# Internally
#
#     def store_company_name(Employee, "comp-1"):
#         Employee.company_name = "comp-1"
#
# cls: To keep class object reference
#
e1.store_employee_name("emp-1") # e1.store_employee_name(e1, "emp-1")
#
#     def store_employee_name(self, en):
#         self.name = en
#
# Internally
#
#     def store_employee_name(e1, "emp-1"):
#         e1.name = "emp-1"
#
# self: to hold instance object reference
#
e2.store_employee_name("emp-2") # e2.store_employee_name(e2, "emp-1")


print("Company Name:", Employee.get_company_name())
print("Employee-1 Name:", e1.get_employee_name())
print("Employee-2 Name:", e2.get_employee_name())

print("#"*40, end="\n\n")
###########################

print("Why @classmethod")
print("-"*20)
# ---------------

print("Company Name:", Employee.get_company_name())
# @classmethod will make sure to pass Class object 'Employee' as 1st argument

print("Employee-1 Name:", e1.get_employee_name())
# @classmethod will make sure to pass Class object 'Employee' as 1st argument

print("Employee-2 Name:", e2.get_employee_name())
# @classmethod will make sure to pass Class object 'Employee' as 1st argument

print("#"*40, end="\n\n")
###########################


print("Access instance method using class object")
print("-"*20)
# ---------------

print("Employee-1 Name:", Employee.get_employee_name(e1))

print("#"*40, end="\n\n")
###########################