"""
From the given string below, extract
DATE

Expected Output
---------------
26/Apr/2000
---------------
"""

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

# 1-way
extr1= input_data.split(' ')
extr2= extr1[3]
extr3= extr2[1:12]
print(extr3)

# 2-way
extr1= input_data.split('-')
extr2= extr1[2]
# print(extr2)
extr3= extr2[2:13]
print(extr3)
