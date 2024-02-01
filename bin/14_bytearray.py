"""
MUTABLE TYPES
(Once we store the values, we CAN modify throughout the program)
- bytearray
"""

print("bytearray PART-1")
print("How to store the values")
print("-"*20)
# ---------------

bytearray_data_1 = bytearray(b"WEL COME")

print("bytearray_data_1:", bytearray_data_1)

print("#"*40, end="\n\n")
###########################

print("Bytearray PART-2")
print("Indexes are similar to string")
print("-"*20)
# ---------------

bytes_data = bytearray(b"WEL COME")
print("bytes_data:", bytes_data, end="\n\n")

print("0th character:", bytes_data[0]) # output ascii value=87

print("ascii to character:", chr(bytes_data[0])) # output ascii value=87

print("Slicing: index 1 to 6", bytes_data[1:6])

print("#"*40, end="\n\n")
###########################


print("Bytes PART-4")
print("Methods inside 'bytearray' class")
print("-"*20)
# ---------------

print(dir(bytes_data))

# OR we can use class name
print(dir(bytearray))

print("#"*40, end="\n\n")
###########################

print("Bytes PART-5")
print("'update' using index")
print("-"*20)
# ---------------


bytes_data[0] = 85 # ascii
print("bytearray after update using index:", bytes_data)

print("#"*40, end="\n\n")
###########################