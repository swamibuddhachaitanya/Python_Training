"""
for-loop: Iterate any collection
"""

print("print each char using for loop")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string:", my_string, sep="\n", end="\n\n")

# Syntax
# for provide_any_variable_name_here in provide_any_collection_here

for each_char in my_string:
    print("Each Char:", each_char)


print("#"*40, end="\n\n")
###########################

print("Iterate list/tuple/set any other collections")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")

for each_value in my_list:
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
###########################

print("for with dictionary keys()")
print("-"*20)
# ---------------
my_dictionary = {"course": "python", "duration": 20, "mode": "classroom"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
for each_key in my_dictionary.keys():
    print("Key:", each_key)
    print("value for the key:", my_dictionary[each_key], end="\n\n")

print("#"*40, end="\n\n")
###########################


print("for with dictionary values()")
print("-"*20)
# ---------------
my_dictionary = {"course": "python", "duration": 20, "mode": "classroom"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")


# >>> my_dictionary.values()
# dict_values(['python', 20, 'classroom'])
for each_value in my_dictionary.values():
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
###########################


print("for with dictionary items()")
print("-"*20)
# ---------------
my_dictionary = {"course": "python", "duration": 20, "mode": "classroom"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 20), ('mode', 'classroom')]
for each_item in my_dictionary.items():
    print("Item:", each_item)
    print("Key:", each_item[0])
    print("Value:", each_item[1], end="\n\n")

print("#"*40, end="\n\n")
###########################

print("for with dictionary items()")
print("-"*20)
# ---------------
my_dictionary = {"course": "python", "duration": 20, "mode": "classroom"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 20), ('mode', 'classroom')]
for k, v in my_dictionary.items():
    print("Key:", k)
    print("Value:", v, end="\n\n")

print("#"*40, end="\n\n")
###########################

# 2 Cases
# ---------------
# Case-1: break: How to end for-loop in between
# Case-2: continue: How to skip current iteration and jump to next iteration
###########################

print("# Case-1: break: How to end for-loop in between")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


# Requirement: Are there any value starting with Java?
#   if one value found then no need to check for other values
for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
        break


print("#"*40, end="\n\n")
###########################

# 2 Cases
# ---------------
# Case-1: break: How to end for-loop in between
# Case-2: continue: How to skip current iteration and jump to next iteration
###########################

print("# Case-1: break: How to end for-loop in between")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


# Requirement: Are there any value starting with Java?
#   if one value found then no need to check for other values
for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
        break


print("#"*40, end="\n\n")
###########################


print("# Case-2: continue: How to skip current iteration and jump to next iteration")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


for each_value in my_list:
    print("Every Value:", each_value, end="\n\n")
    if not  each_value.startswith("Java"):
        continue
    # Below code till end of for-block, is applicable only for 'Java'
    print("This Java course name is:", each_value)
    print("This is one version of Java")
    print("This Java course duration is 20 days", end="\n\n")



print("#"*40, end="\n\n")
###########################


print(" 'for-else' ")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
else:
    print("Inside for-else")

# After completing the for-loop, else will execute

print("#"*40, end="\n\n")
###########################


print(" 'for-else' ")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


for each_value in my_list:
    if each_value.startswith("Java"):
        print("Found")
        break
else:
    print("Not Found")

# if for-loop ended by 'break' then 'else' will not execute

print("#"*40, end="\n\n")
###########################

