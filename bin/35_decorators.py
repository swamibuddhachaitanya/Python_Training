"""
Decorators:
If we want to rewrite/copy-paste same code more than one time throught the program
then we can write function
Suppose
Assume we need to write more than one function,
in each function some-code/some-logic is getting repeated
then
how to resuse code present inside each function?

Answer: Write another function which is having common code

How to write that function?
"""

print("Without RESUSING OR without decorator")
print("We are repeating same code in all functions")
print("-"*20)
# ---------------

def add1(a, b):
    print("Result is:")
    print(a + b)
    print("End of the result")


def add2(a, b):
    print("Result is:")
    print(a + b + b)
    print("End of the result")

def sub1(a, b):
    print("Result is:")
    print(a - b)
    print("End of the result")

def sub2(a, b):
    print("Result is:")
    print(a - b - b)
    print("End of the result")

print("#"*40, end="\n\n")
###########################

print("Decorator: Function written using decorator design pattern")
print("-"*20)
# ---------------

print("IMPORTANT: THIS IS PARTIAL IMPLEMENTATION")

def my_decorator(my_func): # my_func=add1
    # def decorated_func(*x, **y)
    def decorated_func(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # add2(x,y)
        print("End of the result", end="\n\n")
    return decorated_func


# 1)
# ---------------
def add1(a, b):
    print(a + b)

inner_func_obj = my_decorator(add1)
# inner_func_obj = decorated_func
inner_func_obj(10, 20)
###########################


# 2)
# ---------------
def add2(a, b):
    print(a + b + b)

inner_func_obj = my_decorator(add2)
# inner_func_obj = decorated_func
inner_func_obj(10, 20)
###########################

print("IMPORTANT: THIS IS PARTIAL IMPLEMENTATION")

print("#"*40, end="\n\n")
###########################

print("FINAL DECORATOR")
print("-"*20)
# ---------------

def my_decorator(my_func): # my_func=add1
    # def decorated_func(*x, **y)
    def decorated_func(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # add2(x,y)
        print("End of the result", end="\n\n")
    return decorated_func


# 1)
# ---------------
@my_decorator
def add1(a, b):
    print(a + b)

add1(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func_obj = my_decorator(add1)
# inner_func_obj(10, 20)
###########################


# 2)
# ---------------
@my_decorator
def add2(a, b):
    print(a + b + b)


add2(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func_obj = my_decorator(add2)
# inner_func_obj(10, 20)
###########################


print("#"*40, end="\n\n")
###########################



