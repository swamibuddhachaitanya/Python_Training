"""
Lambda functions
- it is one line function
- no name to this function
- we can write lambda function inside function arguments
- we can write comprehensions
- We can also assign lambda function to variable
    and that variable will be function object
"""

print("Without using lambda")
print("-" * 20)


# ---------------

def add_port(ip):
    return ip + ":8080"


ips_list = ['123.123.123.123', '123.123.123.123', '123.123.123.123']

new_list = []
for i in ips_list:
    result = add_port(i)
    new_list.append(result)

print(new_list)

print("#" * 40, end="\n\n")
###########################


print("Without using lambda but using map")
print("-" * 20)


# ---------------

def add_port(ip):
    return ip + ":8080"


ips_list = ['123.123.123.123', '123.123.123.123', '123.123.123.123']

new_list = map(add_port, ips_list)
# How map works?
# - take one value
# - call add_port
# - store return value in new_list
print(list(new_list))

print("#" * 40, end="\n\n")
###########################


print("Using lambda but using map")
print("-"*20)
# ---------------

# def add_port(ip):
#     return ip + ":8080"
# Equivalent lambda function is
# lambda ip: ip + ":8080"

ips_list = ['123.123.123.123', '123.123.123.123', '123.123.123.123']

new_list = map(lambda ip: ip + ":8080", ips_list)
# How map works?
# - take one value
# - call add_port
# - store return value in new_list
print(list(new_list))

print("#"*40, end="\n\n")
###########################

print("We can assign lambda function")
print("-"*20)
# ---------------

f = lambda ip: ip + ":8080"

result = f("123.123.123.123")
print(result)

print("#"*40, end="\n\n")
###########################

print("Using filter")
print("-"*20)
# ---------------

def filter_jpg_file_func(file_name):
    if file_name.endswith(".jpg"):
        return True
    else:
        return False

pics_list = ['wpaper.gif', 'No Image', '5star2000.gif', '5star.gif', 'a2hlogo.jpg', 'No Image']

filtered_values = filter(filter_jpg_file_func, pics_list)
print(list(filtered_values))

print("#"*40, end="\n\n")
###########################



print("Using filter with lambda")
print("-"*20)
# ---------------
#
# def filter_jpg_file_func(file_name):
#     if file_name.endswith(".jpg"):
#         return True
#     else:
#         return False

# Lambda for the above function
# lambda file_name: file_name.endswith(".jpg")

pics_list = ['wpaper.gif', 'No Image', '5star2000.gif', '5star.gif', 'a2hlogo.jpg', 'No Image']

filtered_values = filter(lambda file_name: file_name.endswith(".jpg"), pics_list)
print(list(filtered_values))

print("#"*40, end="\n\n")
###########################


print("reduce result to single value")
print("-"*20)
# ---------------

def my_reduce_func(a, b):
    return a + b


all_results = [10, 20, 30, 40]

from functools import reduce
reduced_result = reduce(my_reduce_func, all_results)
# all_results = [10, 20, 30, 40]
# 1st call my_reduce_func(10,20) # 30
# 2nd call my_reduce_func(30,30) # 60
# 3rd call my_reduce_func(60,40) # 100
print("reduced_result:", reduced_result)

print("using lambda reduce result to single value")
print("-"*20)
# ---------------

# def my_reduce_func(a, b):
#     return a + b
#
# lambda a, b : a + b

all_results = [10, 20, 30, 40]

from functools import reduce
reduced_result = reduce(lambda a, b : a + b, all_results)
print("reduced_result:", reduced_result)

print("#"*40, end="\n\n")
###########################

print("#"*40, end="\n\n")
###########################