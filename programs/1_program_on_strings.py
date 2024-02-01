"""
From the given string below, extract
IP

Expected Output
---------------
123.123.123.123
---------------
"""

print("How input data looks like?")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
###########################

print("How input data looks like in raw format?")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(input_data))

print("#"*40, end="\n\n")
###########################

print("type of input data")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
###########################


print("Methods inside 'str' class which we can use to get output")
print("-"*20)
# ---------------

print(dir(input_data))

print("#"*40, end="\n\n")
###########################


print("Extract IP: 1-way")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
###########################


print("Extract IP: 2-way")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

# 1-way: WRONG
# end_index = input_data.index("3") # WRONG

# 2-way
end_index = input_data.index("-")
end_index = end_index - 1

# 3-way
end_index = input_data.index(" ")

ip = input_data[0:end_index]
print(ip)

print("#"*40, end="\n\n")
###########################

print("Extract IP: 3-way")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("splitted Values:", sp, sep="\n", end="\n\n")

ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
###########################