"""
From the given string below, extract
PICS

Expected Output
---------------
wpaper.gif
---------------
"""

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

#1-way
e1= input_data.split("/")
e2= e1[4]
e3= e2[:6]
print(e3)

#2-way
e1= input_data.split("GET")
e2= e1[1]
e3= e2[7:13]
print(e3)