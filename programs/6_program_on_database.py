"""
Send extracted data to database
"""

# Split into smaller tasks
# -----------
# Task-1: Get data from server_log.txt
# Task-2: Extract using regular expression and send to database
############################

print("# Task-1: Get data from server_log.txt")
print("-" * 20)
# -------------

with open(r"../log/server_log_2.txt", "r") as my_log_file_handle:
    list_of_lines = my_log_file_handle.readlines()

print(list_of_lines)

print("#" * 40, end="\n\n")
##################################


'''
How to communicate with databases in python?

python-program  <-- Communicate using library -->  Any databases

Example:
python-program  <-- Communicate using library(cx-oracle) -->  Oracle databases
python-program  <-- Communicate using library(mysql-connector-python) -->  MySQL databases
python-program  <-- Communicate using library(sqlite3) -->  SQLite databases

'''


'''
We need one database
- We can use SQLite database

How to create/communicate with SQLite databses?
OPTION-1: Using SQLite database software
OPTION-2: Using python library sqlite3 we can create/communicate with SQLite databses
        without installing SQLIte database software
'''

import sqlite3

print("Connecting/Creating 'my_data_db.sqlite3'")
my_db_connection = sqlite3.connect('my_data_db.sqlite3')
print("Done!")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done!")


print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_DATA_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done!")

print("Extract IP, DATE, PICS, URL")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST)\s+/(pics/(\w+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        my_query = f"INSERT INTO MY_DATA_TABLE VALUES('{ip}', '{dt}', '{img}', '{url}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted", end="\n\n")

my_db_connection.commit()
print("All records inserted.", end="\n\n")

my_db_connection.close()
print("DB connection closed")

