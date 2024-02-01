"""
Get data from database

and write to below files

db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
db_dump_6.html
"""

print("Select data from table")
print("-" * 20)
# -------------

import sqlite3

print("Connecting/Creating 'my_data_db.sqlite3'")
my_db_connection = sqlite3.connect('my_data_db.sqlite3')
print("Done\n\n")


print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("Execute select query")
my_query="SELECT * FROM MY_DATA_TABLE"
my_db_cursor.execute(my_query)
print("Done\n\n")

print("DB result:")
my_db_result = my_db_cursor.fetchall()
print(my_db_result)

print("#" * 40, end="\n\n")
##################################

print("Create DataFrame object with db data")
print("-" * 20)
# -------------

import pandas as pd

# OPTION-1
# my_db_df = pd.DataFrame(my_db_cursor) # we can pass cursor as well

my_db_df = pd.DataFrame(my_db_result, columns=["IP", "DATE", "PICS", "URL"])
print(my_db_df)

print("#" * 40, end="\n\n")
##################################

print("Write to files")
print("-" * 20)
# -------------

# db_dump_1.txt
my_db_df.to_csv("db_dump_1.txt", sep="\t") # default sep=","

# db_dump_2.csv
my_db_df.to_csv("db_dump_2.csv")

# db_dump_3.xlsx
my_db_df.to_excel("db_dump_3.xlsx", sheet_name="MyLogData")

# db_dump_4.json
my_db_df.to_json("db_dump_4.json")

# db_dump_5.xml
my_db_df.to_xml("db_dump_5.xml")

# db_dump_6.html
my_db_df.to_html("db_dump_6.html")

print("""
Created Below files

db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
db_dump_6.html

Please check
""")

print("#" * 40, end="\n\n")
##################################