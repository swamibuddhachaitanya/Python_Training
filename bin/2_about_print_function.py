"""
about print function
"""

print("print function PART-1")
print("-"*20)
# ---------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d) # Default sep=SPACE
print(a, b, c, d, sep=",")
print(a, b, c, d, sep="|")
print(a, b, c, d, sep="ABC")
print(a, b, c, d, sep="XYZ")
print(a, b, c, d, sep="\n")


print("#"*40, end="\n\n")
###########################

print("print function PART-2")
print("-"*20)
# ---------------

a = 100
b = 200
c = 300
d = 400

print(a, b, c, d)
print(a, b, c, d)
print(a, b, c, d) # By default end="\n": after printing all the values put '\n'
print(a, b, c, d, end=".") # after printing all the values put '.'
print(a, b, c, d, end="|") # after printing all the values put '|'
print(a, b, c, d, end="ABC") # after printing all the values put 'ABC'
print(a, b, c, d, end="XYZ\n") # after printing all the values put 'XYZ\n'

# Total 4 arguments we can pass
# 1) sep 2) end 3) file 4) flush
# We will discuss 3) file 4) flush during file operations

print("#"*40, end="\n\n")
###########################
