"""
Why Object ?
OR
Why Object Oriented Programming ?
OR
What is the idea behind making OOP


In this section, we should get 100% clarity on
1) Encapsulation: keeping data and related methods together
2) Abstraction: If we want to use any method then no need to know
    how it is implemented, instead we need to know how to use it
"""

print("Data inside the object")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
###########################

print("Methods inside 'str' class object")
print("-"*20)
# ---------------

print(dir(input_data))

print("#"*40, end="\n\n")
###########################