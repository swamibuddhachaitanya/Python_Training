"""
Operator Overloading

If we use + b/n 2 int objects then it will add
If we use + b/n 2 str objects then it will concatenate

similarly,
we can also support for any operator in our class

To do that,
In python, for each operator there is special name
Example
+  =  __add__
-  =  __sub__
*  =  __mul__

So, to support any operator
we need to write method using special name given to that operator

"""

print("Supported + operator")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self=e1, other=e2
        result = self.name + " " + other.name
        return result


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # e1.__add__(e2)
print("+ result:", result)

print("#"*40, end="\n\n")
###########################


print("Supported printing name when we print 'e1'")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self=e1, other=e2
        result = self.name + " " + other.name
        return result
    def __str__(self):
        return self.name


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # e1.__add__(e2)
print("+ result:", result, end="\n\n")

print("e1:", e1) # Internally 'print' will execute __str__ then return value will be printed

print("#"*40, end="\n\n")
###########################


print("Supported len()")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self=e1, other=e2
        result = self.name + " " + other.name
        return result
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # e1.__add__(e2)
print("+ result:", result, end="\n\n")

print("e1:", e1) # Internally 'print' will execute __str__ then return value will be printed

print("Length of e1:", len(e1)) # __len__

print("#"*40, end="\n\n")
###########################


print("Supported Iteration")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self=e1, other=e2
        result = self.name + " " + other.name
        return result
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        return iter(self.name)

    def __next__(self):
        return next(self.name)


e1 = Employee("emp-1")
e2 = Employee("emp-2")
result = e1 + e2 # e1.__add__(e2)
print("+ result:", result, end="\n\n")

print("e1:", e1) # Internally 'print' will execute __str__ then return value will be printed

print("Length of e1:", len(e1), end="\n\n") # __len__

for i in e1:
    print("Value of i:", i)

print("#"*40, end="\n\n")
###########################