"""
Write log_file processing program using os.walk to read list of log files
in a directory

Expected Output
----------------
Enter Log Directory: C:\training (this should be the location where your files are present)

- this should read all files ending with .txt
- extract data from all server_log file and .txt files and append to only ONE report.txt
----------------
"""


import os

print(list(os.walk(r"C:\Python Training"))) #enter your location here

