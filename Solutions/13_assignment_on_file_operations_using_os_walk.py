"""
Write log_file processing program using os.walk to read list of log files
in a directory

Expected Output
----------------
Enter Log Directory: C:\training

- this should read all files ending with .txt
- extract data from all server_log file and .txt files and append to only ONE report.txt
----------------
"""


import os


# directory_path = input("Enter the directory: ")

# print(list(os.walk(directory_path)))

print(list(os.walk(r"C:\Python Training")))

# text_list = []

# for main_dir, sub_dirs_list, files_list in os.walk(r"C:\Python Training"):
#     for each_file in files_list:
#         full_path = main_dir + "\\" + each_file
#         print("Each File Path:", full_path)
#         if full_path.split("\\")[-1].endswith(".txt"):
#             text_list.append(full_path.split("\\")[-1])
#
# print(text_list)

# def text_extraction(directory_path):
#     text_list=[]
#     for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
#         for each_file in files_list:
#             full_path = main_dir + "\\" + each_file
#             print("Each File Path:", full_path)
#             if full_path.split("\\")[-1].endswith(".txt"):#for text file location extraction
#                 text_list.append(full_path)
#
#     return text_list

#find location of the log files
def log_file_extraction(directory_path):
    log_files_list=[]
    for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
        for each_file in files_list:
            full_path = main_dir + "\\" + each_file
            #write code for log file location extraction
            if each_file.startswith("server") and each_file.endswith(".txt"):
                log_files_list.append(full_path)

    return log_files_list

#find location of the report files
def report_files_extraction(directory_path):
    report_files_list=[]
    for main_dir, sub_dirs_list, files_list in os.walk(directory_path):
        for each_file in files_list:
            full_path = main_dir + "\\" + each_file
            #write code for log file location extraction
            if each_file.endswith(".txt") and each_file.startswith("log_report"):
                report_files_list.append(full_path)

    return report_files_list

# text_list = text_extraction(r"C:\Python Training")
log_files_list = log_file_extraction(r"C:\Python Training")
report_files_list = report_files_extraction(r"C:\Python Training")




# print(f"Text files locations are: + {text_list}") #files extracted
print(f"log files locations are: + {log_files_list}") #log files extracted
print(f"report files locations are: + {report_files_list}") #report files extracted

# now i just need to give the log and text files locations as an arguments to a function
# and then this function will extract all the data from these files and then append it to one report file

#loop through and extract data from each of these files and then append it to the report file

def putting_extracted_data(log_files_list):

    file_to_write = open(r"C:/Python Training/Assignments/report.txt", "a")

    for location in log_files_list:
        print(location)
        file_handle = open(location,"r")
        file_content= file_handle.readlines()
        for line in file_content:
            # print(line)
            if len(line[0:16].split(".")) == 4:
                parts = line.split()

                # Extract IP, DATE, PICS, and URL
                ip = parts[0]
                date = parts[3][1:12]
                pics = parts[6].split("/")[2][:-4] if "/pics/" in line else "No Image"
                for part in parts:
                    if "http://" in part:
                        url = part


                # Store the information in the dictionary
                file_to_write.write(f"{ip}" +"   "+ f"{date}" +"   "+ f"{pics}" +"   "+  f"{url} \n")






putting_extracted_data(log_files_list)
print("file successfully written",end="\n")





