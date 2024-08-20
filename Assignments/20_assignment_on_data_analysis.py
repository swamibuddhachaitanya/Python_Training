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

"""

import pandas as pd

df = pd.read_csv("../log/FD_bank.csv")


