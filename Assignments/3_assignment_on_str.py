"""
From the given string below, extract
URL

Expected Output
---------------
http://www.jafsoft.com/asctortf/
---------------
"""


input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

#1-way

e1= input_data.split(' ')
e2= e1[10]
print(e2[1:-1])

#2-way

e1= input_data.split('"')
e2= e1[3]
print(e2)
