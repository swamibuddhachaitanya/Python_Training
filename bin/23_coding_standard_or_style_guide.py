"""
Coding Standard
OR

1)
PEP 8 – Style Guide for Python Code
PEP: Python Enhancement Proposals
LinK: https://peps.python.org/pep-0008/

2)
And also use below library
pip install pylint

and execute
pylint filename.py
"""

print("Employee Function: NOT IN CODING STANDARD")
print("-"*20)
# ---------------
name = "xyz"
def Employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)


print("#"*40, end="\n\n")
###########################

print("Employee Function: USING CODING STANDARD")
print("-"*20)
# ---------------
outer_name = "xyz"


def employee():
    inner_name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)


print("#"*40, end="\n\n")
###########################

# Also execute below command to verify the coding without executing
# pylint filename.py

