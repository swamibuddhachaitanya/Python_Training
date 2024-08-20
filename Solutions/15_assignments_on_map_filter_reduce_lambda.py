"""
1) filter function: Write filter function to filter only server_log files
2) map function: obtain 4 lists a) ips_list b) dates_list c) pics_list d) urls_list
3) zip all 4 lists
4) reduce function: Using reduce function, prepare one string and return
"""
#2 1 after giving the location it should give me the content of the lines which has ipa as the start

import os
from functools import reduce

directory_path = r"C:\Python Training"



#to put file names inside the file list first, first I need to
#use the walk function to find all the list files under the directory C:\Python Training


def finding_the_list_of_files_in_directory():
    file_collection=[]
    for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
        for each_file in files_list:
            full_path = main_dir + "\\" + each_file
            # write code for log file location extraction
            if each_file.endswith(".txt"):
                file_collection.append(full_path)

    return file_collection

# files_list= finding_the_list_of_files_in_directory()

files_list = finding_the_list_of_files_in_directory()
print(files_list)

def filter_server_log_files(file_name):
    if file_name.split("\\")[3].startswith("server_log"):
        return True
    else:
        return False


filtered_values = filter(filter_server_log_files,files_list)
log_locations = list(filtered_values)

#2 1 after giving the location I need to use the filter function
# it should give me the content of the lines which has ipa as the start

lines_list= []

for log_file in log_locations:
    file_content = open(log_file,"r").readlines()
    for line in file_content:
        # print(line)
        lines_list.append(line)

lines_list = list(lines_list)
# print(f"lines list is: {list(lines_list)}")

def filter_lines_function(line):
    if line[0:15] == "123.123.123.123":
        return True
    else:
        return False






filtered_lines = filter(filter_lines_function,lines_list)
# print(f"filtered lines are: {list(filtered_lines)}")
lines_to_extract_data = list(filtered_lines)

ips_list = list (map(lambda line: line[0:15],lines_to_extract_data))
# print(f"ips list is: {list(ips_list)}")
dates_list =list( map(lambda line: line.split()[3][1:12] ,lines_to_extract_data))
# print(f"dates list is: {list(dates_list)}")

pics_list = list(map(lambda line: line.split()[6].split("/")[2][:-4] if "/pics/" in line else "No Image",lines_to_extract_data))
# print(f"pics list is: {list(pics_list)}")
urls_list = list(map(lambda line: line.split('"')[3] ,lines_to_extract_data))
# print(f"urls list is: {list(urls_list)}")


zipped_list = list( zip(ips_list,dates_list,pics_list,urls_list))

# print(f"zipped list is: {zipped_list}")

def my_reduce_func(a,b):
    return f"{a}\n {b}"

reduced_result = reduce(my_reduce_func, zipped_list)

print(reduced_result)






