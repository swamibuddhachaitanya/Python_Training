"""
Static Methods
"""

print("Static Methods")
print("-"*20)
# ---------------

class Employee:
    @staticmethod
    def get_avg_salary(sal1, sal2):
        return (sal1+sal2)/2

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
e1.store_employee_name("emp-1") # e1.store_employee_name(e1, "emp-1")
e2.store_employee_name("emp-2") # e2.store_employee_name(e2, "emp-1")

avg_salary_1 = Employee.get_avg_salary(20000, 40000)
avg_salary_2 = e1.get_avg_salary(20000, 40000)


print("Company Name:", Employee.get_company_name())
print("Employee-1 Name:", e1.get_employee_name())
print("Employee-2 Name:", e2.get_employee_name())
print("avg_salary_1:", avg_salary_1)
print("avg_salary_2:", avg_salary_2)

print("#"*40, end="\n\n")
###########################