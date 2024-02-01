"""
File operations:
Communicate(Read/Write) with text files
with any extension like .txt, .csv, .log, .mylog, .yourlog etc
Finally files which can be opened in notepad
"""

"""
We need follow 3 steps
Step-1: connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: connect to file
    - open() function
Step-2: Read/Write
    - For writing: 1) write 2) writelines 3) print function
    - For reading: 1) read 2) readline 3) for-loop to read line by line
        4) readlines 5) list/tuple/dict/set classes for reading
Step-3: Disconnect
    - close() # 
"""

print("All write operations")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
# my_file_handle = open(r"provide file name or file path here", "which mode?")
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only
# mode 'w': It will create new file
# mode 'w': IMPORTANT- It will erase existing content

# Step-2: Write
# ---------------

# Our data
x = 10
y = "Python\n"

# Convert other type of data to strings. Because 1) write 2) writelines
# are expecting data in string
x = str(x) + "\n"

# 1) write: It will take single string of any size
# If we have data in string which we want to write to file
# then we can make use of this option
my_file_handle.write(x)
my_file_handle.write(y)

# 2) writelines: It will take any collection of values
# If we have data in any collection like list/tuple etc then
# make use of this option
my_data_in_list = [x, y]
my_file_handle.writelines(my_data_in_list)


# 3) print function
# - no need of converting to string
# - no need of adding \n

# remove \n
x = x.strip()
y = y.strip()

print(x, y, 20, "Java", sep="\n", end="", file=my_file_handle)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("""
created
my_out_file.txt
Please check
""")

print("#"*40, end="\n\n")
###########################


print("Read Operations: 1) read")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
file_content = my_file_handle.read()
# It will read complete file content and return in single string
print("file_content:", file_content, sep="\n", end="\n\n")
print("file_content in raw format:", repr(file_content), sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

print("Read Operations: 2) readline")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
file_content = my_file_handle.readline()# It will read one line
print("1st line:", file_content, sep="\n", end="\n\n")

file_content = my_file_handle.readline()# It will read one line
print("2nd line:", file_content, sep="\n", end="\n\n")

file_content = my_file_handle.readline()# It will read one line
print("3rd line:", file_content, sep="\n", end="\n\n")

# seek pointer
# - internally there is a pointer to keep track
# - by default, in 'r' or 'w' mode seek will be pointing to beginning of
#   the file
# - by default, in 'a' mode seek will be pointing to end of
#   the file
# - It is character based seek, means we can set to any character
# - Example: seek(0) means 0th character, i.e beginning of the file

# Set to beginning of the file
my_file_handle.seek(0)
file_content = my_file_handle.readline()# It will read one line
print("1st line:", file_content, sep="\n", end="\n\n")

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

print("Read Operations: 3) for loop to read line by line")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################


print("Read Operations: 4) readlines()")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
file_content = my_file_handle.readlines()
print_param = {'sep': "\n", 'end' : "\n\n"}
print("file_content:", file_content, **print_param)

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################


print("Read Operations: 5) list/tuple/set")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
file_content = list(my_file_handle)
print_param = {'sep': "\n", 'end' : "\n\n"}
print("file_content in list:", file_content, **print_param)
# seek reached EOF

# set seek to beginnning of the file
my_file_handle.seek(0)
file_content = tuple(my_file_handle)
print_param = {'sep': "\n", 'end' : "\n\n"}
print("file_content in tuple:", file_content, **print_param)
# seek reached EOF

# set seek to beginnning of the file
my_file_handle.seek(0)
file_content = set(my_file_handle)
print_param = {'sep': "\n", 'end' : "\n\n"}
print("file_content in set:", file_content, **print_param)
# seek reached EOF

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################


print("Read Operations: 6) dictionary")
print("-"*20)
# ---------------

# Step-1: connect to file
# ---------------
my_file_handle = open("my_out_file.txt", "r")
# mode "r": Read Only
# mode "r": It will not create new file

# Step-2: Read
# ---------------
file_content = dict(enumerate(my_file_handle))
print_param = {'sep': "\n", 'end' : "\n\n"}
print("file_content in dictionary:", file_content, **print_param)
# seek reached EOF

# Step-3: Disconnect
# ---------------
my_file_handle.close()

print("#"*40, end="\n\n")
###########################

# Dictionary creation examples
# ---------------
# >>> # Example-1
# >>> D = {"A": 10, "B":20}
#
# >>> # Example-2
# >>> K = ["A", "B"]
# >>> V = [10, 20]
# >>> z = zip(K, V)
# >>> list(z)
# [('A', 10), ('B', 20)]
# >>> dict(list(z))
# {}
# >>> dict(zip(K,V))
# {'A': 10, 'B': 20}
# >>>
#
# >>> # Example-3
# >>> L = [100, 200, 300]
# >>> dict(L)
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     dict(L)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
# >>>
# >>> # 1st Make pair with some key then pass to dict()
# >>> M = [(0, 100), (1, 200), (2, 300)]
# >>> dict(M)
# {0: 100, 1: 200, 2: 300}
#
# >>> # Example-4
# >>> L = [100, 200, 300]
# >>> # To make index/value pair, we can make use of enumerate
# >>> e = enumerate(L)
# >>> list(e)
# [(0, 100), (1, 200), (2, 300)]
# >>>
# >>> e = enumerate(L, start=10)
# >>> list(e)
# [(10, 100), (11, 200), (12, 300)]
# >>>
# >>> dict(enumerate(L))
# {0: 100, 1: 200, 2: 300}
# >>>
###########################


# Different Modes
# ---------------
# mode 'w': Write only, It will create new file, It will erase existing content
# mode 'r': Read only, It will not create new file
# mode 'a': Append only, It will create file only if file not present
# mode 'w+': RW, It will create new file, It will erase existing content
# mode 'r+': RW, It will not create new file
# mode 'a+': RW, It will create file only if file not present
#
# NOTE: RW- Read/Write: Which means using same file handle
#       we can call read and write methods
###########################
