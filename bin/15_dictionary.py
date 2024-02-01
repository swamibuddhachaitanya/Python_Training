"""
MUTABLE TYPES

- dictionary
    -- to keep list of values
    -- it keeps duplicate values as well
    -- we are storing in key/value format
"""

print("Dictionary PART-1")
print("How to store the values")
print("-"*20)
# ---------------

my_dictionary_1 = {0: "Python", 1: 20, 2: "Blr"}
# - Internally it will create object of predefined/builtin class 'dict' and store the values
# - if we keep only values inside {} then it will become set

# OR we can also create
my_dictionary_2 = dict({0: "Python", 1: 20, 2: "Blr"})

print(my_dictionary_1, my_dictionary_2, sep="\n")

print("#"*40, end="\n\n")
###########################


print("Dictionary PART-2")
print("How to store the values")
print("-"*20)
# ---------------

# For Key: We can use any IMMUTABLE values for key
# Fo Value: WE can store any value

my_dictionary_1 = {0: "Python", 1: 20, 2: "Blr"}
my_dictionary_2 = {"course": "Python", "duration": 20, "location": "Blr"}

my_dictionary_3 = {
    "duration": 20,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1, sep="\n", end="\n\n")
print("my_dictionary_2:", my_dictionary_2, sep="\n", end="\n\n")
print("my_dictionary_3:", my_dictionary_3, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Dictionary PART-3")
print("Access each value using 'key'")
print("-"*20)
# ---------------
my_dictionary = {
    "duration": 20,
    "course": "Python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("Duration:", my_dictionary["duration"], sep="\n", end="\n\n")

print("Course:", my_dictionary["course"]) # "Python"
print("2nd char in Course:", my_dictionary["course"][1], sep="\n", end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("2nd value in Mode:", my_dictionary["mode"][1]) # "offline"
print("2nd character in 2nd value in Mode:", my_dictionary["mode"][1][1],sep="\n", end="\n\n") # "f"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("lname of Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("lname of Trainer:", my_dictionary["trainer"]["lname"][1],sep="\n", end="\n\n") # "y"

print("#"*40, end="\n\n")
###########################


print("Dictionary PART-4")
print("Methods inside 'dict' class")
print("-"*20)
# ---------------

print(dir(my_dictionary))

# OR
# print(dir(dict))

print("#"*40, end="\n\n")
###########################


print("Dictionary PART-5")
print("Add OR Update")
print("-"*20)
# ---------------

my_dictionary = {"course": "Python", "duration": 20, "location": "Blr"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

my_dictionary["mode"] = ["online", "offline"]
# If key present update else add new record
print("my_dictionary after add/update:", my_dictionary, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################


print("Dictionary PART-6")
print("Add OR Update using 'update' method")
print("-"*20)
# ---------------

my_dictionary = {"course": "Python", "duration": 20, "location": "Blr"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

new_data = {"mode" : ["online", "offline"]}
# If key present update else add new record

my_dictionary.update(new_data)

print("my_dictionary after add/update:", my_dictionary, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Dictionary PART-7")
print("Remove element")
print("-"*20)
# ---------------

my_dictionary = {"course": "Python", "duration": 20, "location": "Blr"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

removed_element_value = my_dictionary.pop("course")
removed_element_item = my_dictionary.popitem()

print("removed_element_value:", removed_element_value)
print("removed_element_item:", removed_element_item)
print("my_dictionary after remove:", my_dictionary, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###########################

print("Dictionary PART-8")
print("get value using get() method")
print("-"*20)
# ---------------

my_dictionary = {"course": "Python", "duration": 20, "location": "Blr"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("course name:", my_dictionary["course"], sep="\n", end="\n\n")
print("course name:", my_dictionary.get("course"), sep="\n", end="\n\n")

# my_dictionary["course"] # This will return error if key not found
# my_dictionary.get("course") # This will return None if key not found

print("#"*40, end="\n\n")
###########################