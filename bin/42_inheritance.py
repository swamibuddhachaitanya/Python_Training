"""
Inheritance

In this section
1) multilevel inheritance
2) multiple inheritance
"""

print("1) multilevel inheritance: Example-1")
print("-"*20)
# ---------------

# Assume this is existing class
class Salary:
    def store_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

# New Requirement:
# 1) add/view tax methods
# 2) modify get_salary method to return (salary-tax)

class Employee(Salary):
    # 1) add/view tax methods
    def store_tax(self, t):
        self.tax = t

    def get_tax(self):
        return self.tax

    # 2) modify get_salary method to return (salary-tax)
    # Polymorphism: We can rewrite method using same name as super class method
    # Polymorphism: Super class method also available
    def get_salary(self):
        # 1-way
        # return self.salary - self.tax
        # 2-way, call super class method to get salary
        salary_from_super = super().get_salary()
        return salary_from_super - self.tax


e = Employee()
e.store_salary(20000)
e.store_tax(2000)
print("Salary:", e.get_salary())
print("Tax:", e.get_tax())

print("Salary:", Salary.get_salary(e))

print("#"*40, end="\n\n")
###########################