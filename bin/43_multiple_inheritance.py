"""
Multiple Inheritance
"""

print("Multiple Inheritance")
print("-"*20)
# ---------------

# Assume this is existing class-1
class Salary:
    def store_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

# Assume this is existing class-2
class Tax:
    def store_tax(self, t):
        self.tax = t
    def get_tax(self):
        return self.tax


# Requirement:
# Create class which is having
# 1) add/view tax
# 2) add/view salary
# 3) add/view name

class Employee(Salary, Tax):
    def store_employee_name(self, n):
        self.name = n

    def get_employee_name(self):
        return self.name

e = Employee()
e.store_employee_name("emp-1")
e.store_salary(20000)
e.store_tax(2000)
# 1st check for method 'store_tax' in 'Employee'
# then
# check for method 'store_tax' in 'Salary'
# then
# check for method 'store_tax' in 'Tax'

print("Name:", e.get_employee_name())
print("Salary:", e.get_salary())
print("Tax:", e.get_tax())

print("#"*40, end="\n\n")
###########################


print("Multiple Inheritance: Example-2")
print("-"*20)
# ---------------

# Assume this is existing class-1
class OldTax:
    def store_tax(self, t):
        self.tax = t
    def get_tax(self):
        return self.tax

# Assume this is existing class-2
class NewTax:
    def store_tax(self, t):
        self.tax = t + 100
    def get_tax(self):
        return self.tax + 100


class Employee(NewTax):
    def __init__(self):
        self.oldtax_obj = OldTax()
    def store_employee_name(self, n):
        self.name = n

    def get_employee_name(self):
        return self.name


e = Employee()
e.store_tax(2000)
e.oldtax_obj.store_tax(200)

print("New Tax:", e.get_tax())
print("Old Tax:", e.oldtax_obj.get_tax())


print("#"*40, end="\n\n")
###########################