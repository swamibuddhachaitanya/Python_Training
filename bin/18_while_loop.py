"""
While loop: Execute the loop based on the condition
"""

print("While loop example")
print("-"*20)
# ---------------

x = 0
while x < 5:
    print("Value of x is:", x)
    x = x + 1 # x += 1


print("#"*40, end="\n\n")
###########################


print("print each char using while loop")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string:", my_string, sep="\n", end="\n\n")

index_no = 0

while index_no < len(my_string):
    print("Each Char:", my_string[index_no])
    index_no += 1


# for each_char in my_string:
#     print("Each Char:", each_char)


print("#"*40, end="\n\n")
###########################

# 2 Cases
# ---------------
# Case-1: break: How to end while-loop in between
# Case-2: continue: How to skip current iteration and jump to next iteration
###########################

print("# Case-1: break: How to end while-loop in between")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")


index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Found")
        break
    index_no += 1
else:
    print("Not Found")

# Requirement: Are there any value starting with Java?
#   if one value found then no need to check for other values
# for each_value in my_list:
#     if each_value.startswith("Java"):
#         print("Found")
#         break


print("#"*40, end="\n\n")
###########################


print("# Case-2: continue: How to skip current iteration and jump to next iteration")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")

index_no = 0
while index_no < len(my_list):
    print("Every Value:", my_list[index_no], end="\n\n")
    if not  my_list[index_no].startswith("Java"):
        index_no += 1
        continue
    # Below code till end of for-block, is applicable only for 'Java'
    print("This Java course name is:", my_list[index_no])
    print("This is one version of Java")
    print("This Java course duration is 20 days", end="\n\n")
    index_no += 1


# for each_value in my_list:
#     print("Every Value:", each_value, end="\n\n")
#     if not  each_value.startswith("Java"):
#         continue
#     # Below code till end of for-block, is applicable only for 'Java'
#     print("This Java course name is:", each_value)
#     print("This is one version of Java")
#     print("This Java course duration is 20 days", end="\n\n")



print("#"*40, end="\n\n")
###########################

