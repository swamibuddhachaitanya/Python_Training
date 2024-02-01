"""
Currently: mymodule.py, mypackage, program-47 & 48
all are in the same directory so import will be able to find mymodule & mypackage

If we keep mymodule & mypackage in some other directory/drive/mount-point etc
then
2 ways
1-way: we can add directory path(ex:D:\\mylib) in sys.path

2-way: we can add below entry in ENVIRONMENT VARAIBLE
    VARAIBLE NAME: PYTHONPATH
    VARIABLE VALUE: D:\\mylib

"""

print("List of directories where import will search")
print("-"*20)
# ---------------

import sys
print(sys.path)

print("#"*40, end="\n\n")
###########################

print("Add new directory path")
print("-"*20)
# ---------------

import sys
sys.path.append(r"D:\mylib")
# After this line, we need to import

print("sys.path after adding new directory path")

print(sys.path)


print("#"*40, end="\n\n")
###########################

