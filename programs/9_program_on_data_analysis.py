"""
Data Analysis using pandas

Get data from 3 different files and produce single report
"""

print("csv_data_df")
print("-" * 20)
# -------------

import pandas as pd

csv_data_df = pd.read_csv("db_dump_2.csv")
print(csv_data_df)

print("#" * 40, end="\n\n")
##################################


print("excel_data_df")
print("-" * 20)
# -------------

import pandas as pd

excel_data_df = pd.read_excel("db_dump_3.xlsx")
print(excel_data_df)

print("#" * 40, end="\n\n")
##################################

print("json_data_df")
print("-" * 20)
# -------------

import pandas as pd

json_data_df = pd.read_json("db_dump_4.json")
print(json_data_df)

print("#" * 40, end="\n\n")
##################################

print("all_in_one_df")
print("-" * 20)
# -------------

all_in_one_df = pd.concat([csv_data_df, excel_data_df, json_data_df], axis=0)
print(all_in_one_df)
# axis=0 : Append one below the other

print("#" * 40, end="\n\n")
##################################


print("all columns")
print("-" * 20)
# -------------

print(all_in_one_df.columns)
# ['Unnamed: 0', 'IP', 'DATE', 'PICS', 'URL']

print("#" * 40, end="\n\n")
##################################


print("Remove column 'Unnamed: 0'")
print("-" * 20)
# -------------

all_in_one_df.drop('Unnamed: 0', axis=1, inplace=True)
# axis=1 : Remove column
# inplace=True : make changes in same object 'all_in_one_df'
print(all_in_one_df.columns)

print("#" * 40, end="\n\n")
##################################

print("drop duplicate rows")
print("-" * 20)
# -------------

all_in_one_df.drop_duplicates(inplace=True)
print(all_in_one_df)

print("#" * 40, end="\n\n")
##################################

print("Add new column IP_WITH_PORT")
print("-" * 20)
# -------------

all_in_one_df["IP_WITH_PORT"] = all_in_one_df["IP"] + ":8080"
# Update if column is present else add new column
print(all_in_one_df)

print("#" * 40, end="\n\n")
##################################


print("PICS Column")
print("-" * 20)
# -------------

print(all_in_one_df["PICS"])
# print(all_in_one_df.iloc[:,2]) # [rows,columns]

print("#" * 40, end="\n\n")
##################################


print("Count PICS Column")
print("-" * 20)
# -------------

print(all_in_one_df["PICS"].count())
# print(all_in_one_df.iloc[:,2]) # [rows,columns]

print("#" * 40, end="\n\n")
##################################


print("Value Count PICS Column")
print("-" * 20)
# -------------

print(all_in_one_df["PICS"].value_counts())

print("#" * 40, end="\n\n")
##################################

print("plot value counts in graph")
print("-" * 20)
# -------------

import matplotlib.pyplot as plt

pics_value_counts = all_in_one_df["PICS"].value_counts()
pics_value_counts.plot()
plt.show()

print("#" * 40, end="\n\n")
##################################


print("plot value counts in graph using matplotlib")
print("-" * 20)
# -------------

import matplotlib.pyplot as plt

pics_value_counts = all_in_one_df["PICS"].value_counts()
plt.plot(pics_value_counts)
plt.show()

print("#" * 40, end="\n\n")
##################################


print("save graph")
print("-" * 20)
# -------------

import matplotlib.pyplot as plt

pics_value_counts = all_in_one_df["PICS"].value_counts()

plt.title("Pics Value Analysis")
plt.xlabel("Image names")
plt.ylabel("Value count")
plt.plot(pics_value_counts)
plt.savefig("mygraph.png")

print("""
Graph saved. Please check
mygraph.png
""")

print("#" * 40, end="\n\n")
##################################


print("Write data to sheet1 and graph to sheet2")
print("-" * 20)
# -------------

# to interact with default sheet we can use to_excel
# Use 'ExcelWriter' class to work with multiple sheets

my_writer = pd.ExcelWriter("final_report.xlsx", engine='xlsxwriter')

# send data to default sheet
all_in_one_df.to_excel(my_writer, sheet_name="Data", index=None)

# Add new sheet
new_sheet = my_writer.book.add_worksheet("MyGraph")

# add image
# new_sheet.insert_image("Which cell?", "path to image file")
new_sheet.insert_image("B2", "mygraph.png")

my_writer.close()

print("""
Final report created with graph,
Please check

final_report.xlsx

""")

print("#" * 40, end="\n\n")
##################################

