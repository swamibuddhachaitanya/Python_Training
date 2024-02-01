"""
Get data from DB
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