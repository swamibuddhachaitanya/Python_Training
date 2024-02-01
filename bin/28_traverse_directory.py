"""
os.walk
traverse directories, sub-directories
"""
import os

print("Directory traversal using os.walk")
print("-"*20)
# ---------------

# directory_path = input("Enter Directory Path:")
# print("directory_path:", directory_path)

print(list(os.walk(r"C:\python_training")))

print("#"*40, end="\n\n")
###########################

print("Each Files Path")
print("-"*20)
# ---------------

directory_path = input("Enter Directory Path:")
print("directory_path:", directory_path)

print(list(os.walk(directory_path)))

for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
    for each_file in files_list:
        full_path = main_dir + "\\" + each_file
        print("Each File Path:", full_path)


print("#"*40, end="\n\n")
###########################