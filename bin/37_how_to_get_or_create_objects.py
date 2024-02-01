"""
How to get or create objects
- using class

In this section, we should get 100% clarity on
1) CLASS OBJECT
2) INSTANCE OBJECTS
"""

print("How to get or create objects")
print("-"*20)
# ---------------

class Employee:
    pass
# Even though block is empty it is valid class

# create 2 objects
e1 = Employee()
e2 = Employee()

# Total  objects
# CLASS OBJECT: 'Employee' which is automatically getting created
# INSTANCE OBJECTS: 'e1' & 'e2' which we create

print("Class object 'Employee':", Employee)
print("Instance object 'e1':", e1)
print("Instance object 'e2':", e2)

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