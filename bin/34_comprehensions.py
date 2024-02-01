"""
Comprehensions: We can write one line expression inside list/tuple/dict/set
"""
print("List Comprehension")
print("-"*20)
# ---------------

L1 = [1, 2, 3, 4]
print("L1:", L1)

square_L1 = [i*i for i in L1]
square_even_L1 = [i*i for i in L1 if i % 2 == 0]
square_even_odd_L1 = ["greater" if i > 2 else "lesser" for i in L1 if i % 2 == 0]

print("square_L1:", square_L1)
print("square_even_L1:", square_even_L1)
print("square_even_odd_L1:", square_even_odd_L1)

print("#"*40, end="\n\n")
###########################


print("Tuple Comprehension: It is not TUPLE, It will produce generator")
print("-"*20)
# ---------------

L1 = [1, 2, 3, 4]
print("L1:", L1)

square_L1 = (i*i for i in L1)
square_even_L1 = (i*i for i in L1 if i % 2 == 0)
square_even_odd_L1 = ("greater" if i > 2 else "lesser" for i in L1 if i % 2 == 0)

print("square_L1:", square_L1)
print("square_even_L1:", square_even_L1)
print("square_even_odd_L1:", square_even_odd_L1)
print("square_even_odd_L1 in tuple:", tuple(square_even_odd_L1))

print("#"*40, end="\n\n")
###########################


print("Set Comprehension")
print("-"*20)
# ---------------

L1 = [1, 2, 3, 4]
print("L1:", L1)

square_L1 = {i*i for i in L1}
square_even_L1 = {i*i for i in L1 if i % 2 == 0}
square_even_odd_L1 = {"greater" if i > 2 else "lesser" for i in L1 if i % 2 == 0}

print("square_L1:", square_L1)
print("square_even_L1:", square_even_L1)
print("square_even_odd_L1:", square_even_odd_L1)

print("#"*40, end="\n\n")
###########################

print("Dictionary Comprehension")
print("-"*20)
# ---------------

K = ["A", "B"]
V = [100, 200]

D1 = {k:v for k, v in zip(K, V)}
D2 = {k:v for k, v in enumerate(V)}

print("D1:", D1)
print("D2:", D2)

print("#"*40, end="\n\n")
###########################


print("With Lambda function")
print("-"*20)
# ---------------

L = [1, 2, 3, 4]

squared_L = [(lambda a : a * a)(i) for i in L]
print()

print("#"*40, end="\n\n")
###########################

