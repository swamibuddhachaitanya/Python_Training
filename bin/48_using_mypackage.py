"""
PACKAGES
- if we have more modules
    then
we can keep/organize in folders and sub-folders
these folders are called PACKAGES
- we can directly import from package
"""

print("1-way 'import'")
print("-"*20)
# ---------------

import mypackage.db.mymodule

print("course:", mypackage.db.mymodule.course)
print("add:", mypackage.db.mymodule.add(10,20))
m = mypackage.db.mymodule.MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################


print("2-way 'import'")
print("-"*20)
# ---------------

import mypackage.db.mymodule as mm

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
from mypackage.db.mymodule import course, add, MyClass

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
from mypackage.db.mymodule import course as c, add as a, MyClass as MC

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
from mypackage.db.mymodule import *

print("course:", course)
print("add:", add(10,20))
m = MyClass()
m.add_name("emp-1")
print("Emp Name:", m.view_name())

print("#"*40, end="\n\n")
###########################