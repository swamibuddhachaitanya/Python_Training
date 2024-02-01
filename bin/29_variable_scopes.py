"""
Scopes:
1. Local
2. Enclosed
3. Global
4. Builtin

"""

print("Local Scope")
print("-" * 20)


# ---------------

def my_outer_func():
    def my_inner_func():
        x = 10  # Local Variable
        print("Value of x:", x)

    my_inner_func()


my_outer_func()

print("#" * 40, end="\n\n")
###########################


print("Enclosed Scope: Example-1")
print("-"*20)
# ---------------

def my_outer_func():
    x = 10
    # This is called ENCLOSED Scope where current
    # and inner function will be able to access
    def my_inner_func():
        print("Value of x:", x) # Using Enclosed Scope X
    my_inner_func()
    print("Value of x:", x) # Using Enclosed Scope X

my_outer_func()

print("#"*40, end="\n\n")
###########################


print("Enclosed Scope: Example-2")
print("Change value of enclosed scope variable inside inner function")
print("-"*20)
# ---------------

def my_outer_func():
    x = 10
    # This is called ENCLOSED Scope where current
    # and inner function will be able to access
    def my_inner_func():
        # x = 100 # This will create local variable
        nonlocal x
        x = 1000
        print("Value of x:", x) # Using Enclosed Scope X
    my_inner_func()
    print("Value of x:", x) # Using Enclosed Scope X

my_outer_func()

print("#"*40, end="\n\n")
###########################



print("Global Scope: Example-1")
print("-"*20)
# ---------------
x = 2000 # Global Scope: which can be accessed anywhere
def my_outer_func():
    def my_inner_func():
        print("Value of x:", x) # Using Global Scope X
    my_inner_func()
    print("Value of x:", x) # Using Global Scope X

my_outer_func()
print("Global x:", x)

print("#"*40, end="\n\n")
###########################

print("Global Scope: Example-2")
print("-"*20)
# ---------------
x = 2000 # Global Scope: which can be accessed anywhere
def my_outer_func():
    def my_inner_func():
        # x  = 100 # It will create local variable
        global x
        x = 3000
        print("Value of x:", x) # Using Global Scope X
    my_inner_func()
    print("Value of x:", x) # Using Global Scope X

my_outer_func()
print("Global x:", x)

print("#"*40, end="\n\n")
###########################


# Flow
#-----------------
# 1st check in local scope if variable not present
# then
# check in enclosed scope  if variable not present
# then
# check in global scope  if variable not present
# then
# check in builtins if variable not present
# then
# throw ERROR
######################

