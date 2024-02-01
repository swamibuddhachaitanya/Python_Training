"""
In this program, we are using
1) variables
2) function definitions
3) class definitions
defined in mymodule
"""

print("About 'import'")
print("-"*20)
# ---------------

import mymodule
# - import will search for mymodule.py
# - import will create brand new object 'mymodule'
# - import will execute mymodule.py
# - When we execute mymodule.py below objects will get created
#   1) course
#   2) add
#   3) MyClass
# - import will store all 3 objects inside 'mymodule' object

print(dir(mymodule))

print("#"*40, end="\n\n")
###########################

print("1-way 'import'")
print("-"*20)
# ---------------

import mymodule

print("course:", mymodule.course)
print("add:", mymodule.add(10,20))
m = mymodule.MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("2-way 'import'")
print("-"*20)
# ---------------

import mymodule as mm

print("course:", mm.course)
print("add:", mm.add(10,20))
m = mm.MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("3-way 'import'")
print("-"*20)
# ---------------
from mymodule import course, add, MyClass

print("course:", course)
print("add:", add(10,20))
m = MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("4-way 'import'")
print("-"*20)
# ---------------
from mymodule import course as c, add as a, MyClass as MC

print("course:", c)
print("add:", a(10,20))
m = MC()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("5-way 'import'")
print("-"*20)
# ---------------
from mymodule import *

print("course:", course)
print("add:", add(10,20))
m = MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("List of variables in current scope: i.e global scope")
print("-"*20)
# ---------------

print(locals())

print("#"*40, end="\n\n")
###########################

print("List of variables in current scope: i.e local scope")
print("-"*20)
# ---------------

def f():
    x = 100
    print(locals())

f()

print("#"*40, end="\n\n")
###########################




