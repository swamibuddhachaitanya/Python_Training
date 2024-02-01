"""
- bytes
"""

print("Bytes PART-1")
print("How to store the values")
print("-"*20)
# ---------------

bytes_data_1 = b"WEL COME"

# OR we can make use of class name
bytes_data_2 = bytes(b"WEL COME")

print("bytes_data_1:", bytes_data_1)
print("bytes_data_2:", bytes_data_2)

print("#"*40, end="\n\n")
###########################

print("Bytes PART-2")
print("Indexes are similar to string")
print("-"*20)
# ---------------

bytes_data = b"WEL COME"
print("bytes_data:", bytes_data, end="\n\n")

print("0th character:", bytes_data[0]) # output ascii value=87

print("ascii to character:", chr(bytes_data[0])) # output ascii value=87

print("Slicing: index 1 to 6", bytes_data[1:6])

print("#"*40, end="\n\n")
###########################

print("Bytes PART-3")
print("Methods inside 'bytes' class")
print("-"*20)
# ---------------

print(dir(bytes_data))

# OR we can use class name
print(dir(bytes))

print("#"*40, end="\n\n")
###########################

print("Bytes PART-4")
print("Learning 'startswith' method")
print("-"*20)
# ---------------


bytes_data = b"WEL COME"
print("bytes_data:", bytes_data, end="\n\n")

result = bytes_data.startswith(b"WEL")
print('bytes_data.startswith(b"WEL") result:', result)

print("#"*40, end="\n\n")
###########################

