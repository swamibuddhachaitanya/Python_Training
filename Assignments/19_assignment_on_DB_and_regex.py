
import sqlite3
import csv

print("Connecting/Creating 'ASSIGNMENT_TABLE.sqlite3'")
my_db_connection = sqlite3.connect('ASSIGNMENT_TABLE.sqlite3')
print("Done!")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done!")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS ASSIGNMENT_TABLE(
    AGE INT(100),
    EDUCATION VARCHAR(100),
    LOAN INT(100),
    DURATION INT(100)
)
"""
my_db_cursor.execute(my_query)
print("Done!")

file_path = "../log/FD_bank.csv"

with open(file_path, 'r') as file_handler:
    csv_reader = csv.reader(file_handler)
    header = next(csv_reader)  # Skip the header line
    for row in csv_reader:
        age = row[0]
        education = row[3]
        loan = row[7]
        duration = row[11]

        if not age:
            age = "not available"

        if education not in ['primary', 'secondary', 'tertiary']:
            education = "not available"
        if loan not in ['yes', 'no']:
            loan = "not available"
        if not duration:
            duration = "not available"

        my_query = f"INSERT INTO ASSIGNMENT_TABLE VALUES ('{age}', '{education}', '{loan}', '{duration}')"
        my_db_cursor.execute(my_query)

my_db_connection.commit()
print("All records inserted.", end="\n\n")

my_db_connection.close()
print("DB connection closed")
