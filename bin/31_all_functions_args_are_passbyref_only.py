"""
Function arguments are pass by reference only
"""

print("Function arguments are pass by reference only")
print("-"*20)
# ---------------

def my_func(a, b, c, d):
    print("id of a inside function:", id(a))
    print("id of b inside function:", id(b))
    print("id of c inside function:", id(c))
    print("id of d inside function:", id(d))


a = 100
b = [100]
c = "Python"
d = {"A":10}
print("id of a outside function:", id(a))
print("id of b outside function:", id(b))
print("id of c outside function:", id(c))
print("id of d outside function:", id(d), end="\n\n")

my_func(a, b, c, d)

print("#"*40, end="\n\n")
###########################