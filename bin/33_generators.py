"""
Generators: get-value/create-object whenever we need
instead of creating all objects and storing in some collection like list/tuple etc
"""

print("Without using generators")
print("-"*20)
# ---------------

def my_square(M):
    result = []
    for i in M:
        result.append(i*i)
    return result

L = [1, 2, 3, 4]

squared_result = my_square(L)
# Requirement: print each squared value
for i in squared_result:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
###########################

print("Using generators")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i

L = [1, 2, 3, 4]

squared_result = my_square(L)
# Requirement: print each squared value
for i in squared_result:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
###########################

print("Using generators Example-2")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i

L = [1, 2, 3, 4]

squared_result = my_square(L)
for i in squared_result:
    print("Squared Value:", i)


print("Second Time We can't Regenerate")
print("If we want then call again, so")
squared_result = my_square(L)
for i in squared_result:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
###########################

print("Using generators Example-3")
print("Not only using for-loop we can get values from generators")
print("We can also get values from generators using list/tuple/set/dict")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i

L = [1, 2, 3, 4]

squared_result = my_square(L)
squared_result_in_list = list(squared_result)
print("squared_result_in_list:", squared_result_in_list)

squared_result_in_list = list(squared_result)
print("squared_result_in_list 2nd TIME EMPTY:", squared_result_in_list)

# Call again to get generator object
squared_result = my_square(L)
squared_result_in_tuple = tuple(squared_result)
print("squared_result_in_tuple:", squared_result_in_tuple)


# Call again to get generator object
squared_result = my_square(L)
squared_result_in_dict = dict(enumerate(squared_result))
print("squared_result_in_dict:", squared_result_in_dict)

print("#"*40, end="\n\n")
###########################


print("Using generators Example-4")
print("Without using for-loop")
print("Without using list/tuple etc")
print("We can generate/get values manually")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i

L = [1, 2, 3, 4]

squared_result = my_square(L)

# Step-1: ONE time call iter()
# Step-2: call next() to get the values

i = iter(squared_result)

print("Each Value:", next(i))
print("Each Value:", next(i))
print("Each Value:", next(i))
print("Each Value:", next(i))
# print("Each Value:", next(i)) # StopIteration Error Here

print("Using generators Example-5")
print("OWN Loop using 'while-loop'")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i

L = [1, 2, 3, 4]

squared_result = my_square(L)

# Step-1: ONE time call iter()
# Step-2: call next() to get the values

i = iter(squared_result)
while True:
    try:
        print("Each Value:", next(i))
    except StopIteration:
        print("All the iteration Completed.")
        break

print("It will proceed to execute remaining statements")

print("#"*40, end="\n\n")
###########################

print("#"*40, end="\n\n")
###########################

print("generators Example-6")
print("Using 'yield' and 'return'")
print("-"*20)
# ---------------

def my_square(M):
    for i in M:
        yield i * i
    results = []
    for i in M:
        results.append(i*i)
    return results

L = [1, 2, 3, 4]

squared_result = my_square(L)

# Step-1: ONE time call iter()
# Step-2: call next() to get the values

i = iter(squared_result)
while True:
    try:
        print("Each Value:", next(i))
    except StopIteration:
        print("All the iteration Completed.")
        break

print("It will proceed to execute remaining statements")

print("#"*40, end="\n\n")
###########################