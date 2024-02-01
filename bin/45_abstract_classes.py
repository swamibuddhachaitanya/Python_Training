"""
Abstract Class:
How to make use of portion of the class where
we have complete implementations for few methods
and for few methods we need to provide implementation


"""

print("Abstract Class")
print("-"*20)
# ---------------

# To Provide restriction to the class not to instantiate
# we need to follow 2 steps
# step-1: make sub-class of ABC
# step-2: use abstractmethod decorator for abstract method

from abc import ABC, abstractmethod

# step-1: make sub-class of ABC
class Employee(ABC):
    def add_name(self,n):
        self.name = n

    # step-2: use abstractmethod decorator for abstract method
    @abstractmethod
    def view_name(self):
        pass

# e = Employee()


print(" Extending Abstract Class")
print("-"*20)
# ---------------


class Employee(ABC):
    def add_name(self,n):
        self.name = n
    @abstractmethod
    def view_name(self):
        pass

# Steps to extend
# Step-1: create subclass of Employee
# Step-2: provide implementation to all abstract methods

class MyClass(Employee):
    def view_name(self):
        return "Hello " + self.name


e = MyClass()
e.add_name("emp-1")
print("Name:", e.view_name())


print("#"*40, end="\n\n")
###########################
print("#"*40, end="\n\n")
###########################

