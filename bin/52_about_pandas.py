"""
About pandas
- pandas is one library like mymodule/mypackage
- Inside pandas library,
    -- we have many functions like read_csv, read_excel etc
    -- we have many classes like Series, DataFrame, ExcelWriter etc
- Main class is 'DataFrame'
- 'DataFrame' class has methods related to tabular data processing
"""

print("Inside 'pandas' library")
print("-"*20)
# ---------------

import pandas as pd

print(dir(pd))

print("#"*40, end="\n\n")
###########################

print("Inside 'DataFrame' class")
print("-"*20)
# ---------------

import pandas as pd

print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
###########################

print("'DataFrame' class Example-1")
print("-"*20)
# ---------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
###########################


print("'DataFrame' class Example-2")
print("-"*20)
# ---------------

my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
###########################