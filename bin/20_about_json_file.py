"""
About json file
"""

"""
- JSON file one of the file type like .txt, .csv, .xlsx etc
- In JSON file, we are keeping data in the form key=value pair
- Content of entire the Json file is one string
    it is like keeping dictionary inside string
    example: "{'A':10}"  

- We can use below types
    -- Numbers
    -- strings
    -- list
    -- dictionary
    -- booleans

- So, It can be like
{
    {'a': 10},
    {'b': 20}
}

OR

[
    {'a': 10},
    {'b': 20}
]

- Convert to json means we are converting python object  to string
- Once we read from json, we need to convert this
    string to python object
"""

"""
Serialization:
    converting python-object to byte/byte-stream
DeSerialization:
    converting byte/byte-stream to python-object 
"""


"""
For Serialization and DeSerialization WE have below libraries
- struct
    WE can serialize python objects
    and
    we can  DeSerialization using any other language as well
- pickle
    WE can serialize python objects
    and
    we can  DeSerialization python-object
    Any python object including user defined class objects
- marshal
    WE can serialize python objects
    and
    we can  DeSerialization python-object
    WE CAN'T use with user defined class objects
- json
    WE can serialize python objects which json serializable
    and
    we can  DeSerialization json-object
"""

print("Create json file")
print("-"*20)
# ---------------

my_data = {"course": "python", "mode": "online"}
print("my_data:", my_data)

import json

my_json_file_handle = open("my_data.json", "w")
json.dump(my_data, my_json_file_handle)
my_json_file_handle.close()

print("""
Json file
my_data.json
created. Please check
""")

print("#"*40, end="\n\n")
###########################

print("Reading json file")
print("-"*20)
# ---------------


import json

my_json_file_handle = open("my_data.json", "r")

data_from_json_file = json.load(my_json_file_handle)

my_json_file_handle.close()

print("data_from_json_file:", data_from_json_file)
print("type of data_from_json_file:", type(data_from_json_file))

print("#"*40, end="\n\n")
###########################

print("Serialized data stored in variable")
print("-"*20)
# ---------------

my_data = {"course": "python", "mode": "online"}
print("my_data before serialization:", my_data)

my_data_serialized = json.dumps(my_data)

print("my_data after serialization:", my_data_serialized)
print("type of my_data after serialization:", type(my_data_serialized))


print("#"*40, end="\n\n")
###########################

print("DeSerialized data ")
print("-"*20)
# ---------------

my_data_Deserialized = json.loads(my_data_serialized)


print("my_data after Deserialization:", my_data_Deserialized)
print("type of my_data after Deserialization:", type(my_data_Deserialized))

print("#"*40, end="\n\n")
###########################





