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
