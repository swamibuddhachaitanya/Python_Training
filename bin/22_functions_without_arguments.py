"""
Functions: If we want to rewrite/copy-paste same code
thorught the program, then instead of rewrite/copy-paste
keep that code in a block and use it
"""

print("Without using function")
print("-"*20)
# ---------------

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

a = 10
b = 20
c = a + b
print("c:", c)

print("#"*40, end="\n\n")
###########################

print("Using function")
print("-"*20)
# ---------------

def my_func():
    a = 10
    b = 20
    c = a + b
    print("c:", c)


my_func()
my_func()
my_func()
my_func()

print("#"*40, end="\n\n")
###########################

