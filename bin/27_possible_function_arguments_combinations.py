"""
Possible function arguments combination:

We can combine both positional and keyword arguments
in single function
"""

# ----------
# Order of the arguments in function definition
############
# 1st put all non-default value positional arguments IF ANY
# then
# put all default value positional arguments IF ANY
# then
# put variable positional arguments IF ANY
# then
# put all non-default/default value named or keyword arguments IF ANY
# then
# put variable named or keyword arguments IF ANY
###########################

print("Combination-1")
print("Function without arguments")
print("-"*20)
# ---------------

def add():
    a = 10
    b = 20
    c =a + b
    return c


received_value = add()
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-2")
print("Function with positional arguments")
print("-"*20)
# ---------------

def add(a, b):
    c =a + b
    return c


received_value = add(10, 20)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-3")
print("Function with default value positional arguments")
print("-"*20)
# ---------------

def add(a, b=10):
    c =a + b
    return c


received_value = add(10)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################
print("Combination-4")
print("Function with variable positional arguments")
print("-"*20)
# ---------------

def add(a, b=10, *c):
    result =a + b + sum(c)
    return result


received_value = add(10)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20, 30, 40, 50)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Combination-5")
print("Function with named or keyword arguments")
print("-"*20)
# ---------------

def add(*, a, b):
    result =a + b
    return result

received_value = add(b=10, a=20)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-6")
print("Function with default value named or keyword arguments")
print("-"*20)
# ---------------

def add(*, a, b=10):
    result = a + b
    return result

received_value = add(a=20)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(a=20, b=30)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-7")
print("Function with variable named or keyword arguments")
print("-"*20)
# ---------------

def add(*, a, b=10, **c):
    result = a + b + sum(c.values())
    return result

received_value = add(a=20)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(a=20, b=30)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(a=20, b=30, x=40, y=50, z=60)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Combination-8")
print("Function with positional and named or keyword arguments")
print("-"*20)
# ---------------

# arguments before the * will be positional
# arguments after the * will be keyword
def add(a, b, *, c, d):
    result = a + b + c + d
    return result

received_value = add(10, 20, c=30, d=40)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-9")
print("Function with variable positional and named or keyword arguments")
print("-"*20)
# ---------------

def add(*a, sep, end, file, flush):
    result = sum(a)
    return [result, sep, end, file, flush]

received_value = add(10, 20, 30, 40, 50, sep="x", end="y", file="z", flush="xyz")
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-10")
print("Function with variable positional arguments")
print("-"*20)
# ---------------

def add(*a):
    result = sum(a)
    return result

received_value = add()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20, 30, 40, 50)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Combination-11")
print("Function with variable keyword or named arguments")
print("-"*20)
# ---------------

def add(**a):
    result = sum(a.values())
    return result

received_value = add()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(x=10)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(x=10,y=20)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(x=10, y=20, z=30)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-12")
print("Function with variable positional and keyword or named arguments")
print("-"*20)
# ---------------

def add(*a, **b):
    result = sum(a) + sum(b.values())
    return result

received_value = add()
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20, 30)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(x=10, y=20, z=30)
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20, 30, x=10, y=20, z=30)
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Combination-13")
print("All in one")
print("-"*20)
# ---------------

def add(a, b=10, *c, d, e=20, **f):
    result = a + b + sum(c) + d + e + sum(f.values())
    return result

received_value = add(10, d=20)
# a=10, b=10, c=(), d=20, e=20, f={}
print("received_value:", received_value, sep="\n", end="\n\n")

received_value = add(10, 20, 30, 40, 50, d=60, e=70, x=80, y=90, z=100)
# a=10, b=20, c=(30, 40, 50), d=60, e=70, f={x:80, y:90, z:100}
print("received_value:", received_value, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################
