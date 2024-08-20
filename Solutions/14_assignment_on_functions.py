"""
Write file operations example using
functions

Write below functions
1) function should take directory_path as an argument
and return list of txt file paths. File name should startswith server

2) Function should take list of file paths received from above function
extract all information and return extracted info in list of tuple
[(ip, dt, pics, url),() etc]

3) Function should take 2 arguments
    1) extracted_info got from above function
    2) out_file_path
"""

import os


directory_path = r"C:\Python Training" #input("Enter the directory: ")

# print(list(os.walk(directory_path)))



def text_extraction(directory_path):
    text_list = []
    for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
        for each_file in files_list:
            full_path = main_dir + "\\" + each_file
            if each_file.startswith("server"):
                text_list.append(full_path)
    return text_list

server_location_list = text_extraction(directory_path)

def extract_info_from_server_locations(server_location_list):

    stored_data = []

    for location in server_location_list:
        file_content = open(location, "r").readlines()
        for line in file_content:
            if len(line[0:16].split(".")) == 4:
                parts = line.split()

                # Extract IP, DATE, PICS, and URL
                ip = parts[0]
                date = parts[3][1:12]
                pics = parts[6].split("/")[2][:-4] if "/pics/" in line else "No Image"
                for part in parts:
                    if "http://" in part:
                        url = part

                stored_data.append((ip,date,pics,url))
                # Store the information in the dictionary

    return stored_data

stored_data = extract_info_from_server_locations(server_location_list)

def to_output_in_a_file(directory_path,stored_data):
    file_handle= open(directory_path,"w")
    for element in stored_data:
        file_handle.write(f"{element}\n")




path_to_load_data = r"C:\Python training\Assignments\output_file.txt"
to_output_in_a_file(path_to_load_data, stored_data)