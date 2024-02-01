"""
Process fd_bank.csv
1) "age-column": replace age > 50 & < 0 with avg ***
2) "job-column": Fill missing value with 'admin' *******
3) "job-column": keep only 'admin' and replace other than 'admin' with 'others' ******
4) filter complete data frame where marital != 'divorced' *****
5) 'education': remove education column ********
6) 'default': fill missing value with 'no' ****************
7) 'default': replace 'no' with 0 and 'yes' with 1 *******
8) 'balance':fill missing value with 0 *****************
9)  'housing': remove column housing **********
10) 'loan': remove column housing ***********
11) remove all other columns ***************

write final output to
df_bank_output.csv

write to db also
"""
import sqlite3

import pandas as pd

df = pd.read_csv("../log/FD_bank.csv")
# print(df)

df= df[['age', 'job','marital','default','balance']]
# print(df)
df['balance'].fillna(0,inplace=True)
df['default'].fillna('no',inplace=True)
df['default']= df['default'].map({'no': 0, 'yes': 1})
df= df[df['marital'] != 'divorced']
# df.loc[df['Gender'] == 'Male', 'Gender'] = 'Other'
df['job'].fillna('admin.',inplace=True)
df.loc[df['job'] != 'admin.', 'job'] = 'Others'
df.loc[df['age']>50 ,'age'] = int(df['age'].mean())

print(df)

df.to_csv("df_bank_output.csv")

# Connect to SQLite database (create a new one if it doesn't exist)
conn = sqlite3.connect('Data_analysis.sqlite3')

# Use the to_sql method to write the DataFrame to a table in the database
df.to_sql('PD_TABLE', conn)

# Close the connection
conn.close()

