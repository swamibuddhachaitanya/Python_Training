"""
Pickle
Refer 20th example to know about pickle
"""


print("Create pickle file")
print("-"*20)
# ---------------

import pickle

my_data = "Python"
print("my_data:", my_data)

my_file_handle = open("my_data.pkl", 'wb')
pickle.dump(my_data, my_file_handle)
my_file_handle.close()

print("Created my_data.pkl. Please check")

print("#"*40, end="\n\n")
###########################

print("Reading pickle file")
print("-"*20)
# ---------------

import pickle


my_file_handle = open("my_data.pkl", 'rb')

de_serialized_data = pickle.load(my_file_handle)

my_file_handle.close()

print("de_serialized_data:", de_serialized_data)
print("type of de_serialized_data:", type(de_serialized_data))

print("#"*40, end="\n\n")
###########################

print("Serialize and store in variable")
print("-"*20)
# ---------------

import pickle

my_data = "Python"
print("my_data before serialize:", my_data)
print("type of my_data before serialize:", type(my_data))

my_data_serialized = pickle.dumps(my_data)

print("my_data after serialize:", my_data_serialized)
print("type of my_data after serialize:", type(my_data_serialized))

print("#"*40, end="\n\n")
###########################

print("DeSerialize data stored in variable")
print("-"*20)
# ---------------

my_data_Deserialized = pickle.loads(my_data_serialized)

print("my_data after Deserialize:", my_data_Deserialized)
print("type of my_data after Deserialize:", type(my_data_Deserialized))

print("#"*40, end="\n\n")
###########################