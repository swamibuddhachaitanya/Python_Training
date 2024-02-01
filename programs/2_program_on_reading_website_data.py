"""
Read and print website data
"""

# about 'with' statement
# -------------
# Example: file operations
# - here we can use 'try' block to keep all open/read/write operations
# - then we can use 'finally' to keep closing the file handle
#
# OR
# we have another option using CONTEXT MANAGER 'with' statement
##################################


print("Read and print website data using 'try' and 'finally' block")
print("-"*20)
# -------------

import urllib.request as u

# 1. connect
# -------------
my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

# 2. read
# -------------
web_content = my_web_file_handle.read()

# 3. close
# -------------
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
##################################

print("type of web content")
print("-"*20)
# -------------

print(type(web_content))

print("#"*40, end="\n\n")
##################################

print("type of web content after decode")
print("-"*20)
# -------------

web_content = web_content.decode()

# print(web_content,end="\n\n")
print(type(web_content))

print("#"*40, end="\n\n")
##################################


print("Read and print website data using 'try' and 'finally' block")
print("-" * 20)
# -------------

import urllib.request as u

try:
    # 1. connect
    # -------------
    my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")

    # 2. read
    # -------------
    web_content = my_web_file_handle.read()

finally:
    # 3. close
    # -------------
    my_web_file_handle.close()

print(web_content)

print("#" * 40, end="\n\n")
##################################

print("Using CONTEXT MANAGER 'with'")
print("-" * 20)
# -------------

import urllib.request as u

with u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html") as my_web_file_handle:
    web_content = my_web_file_handle.read()
    # my_web_file_handle.close() # NOT REQUIRED, 'with' will take care

web_content = web_content.decode()
print(web_content)

print("#" * 40, end="\n\n")
##################################

