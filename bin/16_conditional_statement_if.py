"""
Conditional Statement 'if': Based on the condition if we want to execute block of code

In some languages
if some_condition
{
s1
    s2
        s3
    s4
s5
}
s6

in python, we wont use {} to make a block, instead of {}, we will use INDENTATION

if some_condition
    s1
    s2
    s3
    s4
    s5
    if some_condition
        s1
        s2
        s3
        s4
        s5
s6


"""

print("Only 'if'")
print("-"*20)
# ---------------

x = 10

if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

if x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###########################

print("'if-elif'")
print("-"*20)
# ---------------

x = 10

if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###########################

print("'if-elif-else'")
print("-"*20)
# ---------------

x = 10

if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###########################


print("if-with strings")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string:", my_string, sep="\n", end="\n\n")

if (my_string != "Java") and (my_string !="C++"):
    print("Not Java/C++")

if "th" in my_string:
    print("Substring 'th' found")

if not my_string.startswith("Perl"):
    print("Not Perl")

print("#"*40, end="\n\n")
###########################

print("if-with list/tuple/set any other collections")
print("-"*20)
# ---------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, sep="\n", end="\n\n")

if "Java-1" in my_list:
    print("Value 'java-1' found")

print("#"*40, end="\n\n")
###########################


print("if with dictionary")
print("-"*20)
# ---------------
my_dictionary = {"course": "python", "duration": 20, "mode": "classroom"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['course', 'duration', 'mode'])
if "course" in my_dictionary.keys():
    print("Key 'course' found")

# >>> my_dictionary.values()
# dict_values(['python', 20, 'classroom'])
if "python" in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 20), ('mode', 'classroom')]
if ('mode', 'classroom') in my_dictionary.items():
    print("Item found")

print("#"*40, end="\n\n")
###########################

