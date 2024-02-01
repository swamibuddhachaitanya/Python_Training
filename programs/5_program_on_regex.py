"""
Extract using regular expression
"""
# Split into smaller tasks
# -----------
# Task-1: Get data from server_log.txt
# Task-2: Extract using regular expression
############################

print("# Task-1: Get data from server_log.txt")
print("-" * 20)
# -------------

with open(r"../log/server_log_2.txt","r") as my_log_file_handle:
    list_of_lines = my_log_file_handle.readlines()

print(list_of_lines)

print("#" * 40, end="\n\n")
##################################



print("check whether it is IP address line or not")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("Match Result:", match_result, end="\n\n")

'''
regular expression

IDENTIFIERS
--------------
\d -> represent digits b/n 0 to 9
\D -> represent non-digits. any character except 0 to 9
. -> represent any one any character
\. -> strictly DOT
[.] -> strictly DOT
[0-9] -> represent digits b/n 0 to 9, here we can mention different range
[0-255] -> it can be any digit b/n 0 to 2 OR it can be 5
[a-z,A-Z] -> it can be ONE lower case OR UPPER case OR it can be one COMMA
[a-z A-Z] -> it can be ONE lower case OR UPPER case OR it can be one SPACE
[a-z9BX-] -> it can be ONE lower case OR it can be 9 OR it can be 'B' OR
                it can be 'X' OR it can be '-'
--------------

QUANTIFIERS
--------------
\d{3} -> internally it will become \d\d\d
\d{1,3} -> internally it will become (\d|\d\d|\d\d\d)
--------------


MODIFIERS
--------------
* -> it makes 0 or more times
+ -> it makes 1 or more times
? -> it makes 0 or one time
--------------

'''

print("#" * 40, end="\n\n")
##################################

# Example: r[ea]d
# -------------
# rd # WONT MATCH
# red # MATCH
# rad # MATCH
# read  # WONT MATCH
##################################

# Example: r[ea]+d
# -------------
# rd # WONT MATCH
# red # MATCH
# rad # MATCH
# read  # MATCH
# reaeeeeaeaeaead  # MATCH
##################################


# Example: r[ea]*d
# -------------
# rd # MATCH
# red # MATCH
# rad # MATCH
# read  # MATCH
# reaeeeeaeaeaead  # MATCH
##################################

# Example: r[ea]?d
# -------------
# rd # MATCH
# red # MATCH
# rad # MATCH
# read  # WONT MATCH
# reaeeeeaeaeaead  # WONT MATCH
##################################


print("Extract IP")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print("Only IP:", ip)
        print("all groups in string:", match_result.group(0))



"""
put () to IP address portion to capture the IP
"""

print("#" * 40, end="\n\n")
##################################


print("Extract IP, DATE")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt, sep="\t")
        # print("all groups in string:", match_result.group(0))
        # print("all groups in tuple:", match_result.group(1,2))


"""
26/Apr/2000

26
--
\d{2} # Strictly 2 digits
\d\d # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # minimum 1 maximum 2
[0-9]{1,2} # minimum 1 maximum 2
\d?\d # minimum 1 maximum 2
[0-9]?[0-9] # minimum 1 maximum 2
[0-9]?\d # minimum 1 maximum 2
\d?[0-9] # minimum 1 maximum 2
--

Apr
--
[a-zA-Z]{3}
[A-Z][a-z]{2}
(Jan|Feb|Mar)
--

"""


"""
MODIFIERS
--------------

GREEDY MODE

* -> it makes 0 or more times
+ -> it makes 1 or more times
? -> it makes 0 or one time

NON GREEDY MODE

*? -> it makes 0 or more times
+? -> it makes 1 or more times
?? -> it makes 0 or one time

--------------

"""

print("#" * 40, end="\n\n")
##################################



print("Extract IP, DATE, PICS: PARTIAL OUTPUT-1")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*?(\w+\.(gif|jpg)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(3)
        print(ip, dt, img, sep="\t")
        # print("all groups in string:", match_result.group(0))
        # print("all groups in tuple:", match_result.group(1,2))


"""
5star2000.gif

5star2000
---
[a-zA-Z0-9_]+
\w ->  [a-zA-Z0-9_] # word character
\W ->  [^a-zA-Z0-9_] # Excluding these characters
[^abc] # Excluding a or b or c
---

"""

print("#" * 40, end="\n\n")
##################################


print("Extract IP, DATE, PICS")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        print(ip, dt, img, sep="\t")
        # print("all groups in string:", match_result.group(0))
        # print("all groups in tuple:", match_result.group(1,2))


"""
5star2000.gif

5star2000
---
[a-zA-Z0-9_]+
\w ->  [a-zA-Z0-9_] # word character
\W ->  [^a-zA-Z0-9_] # Excluding these characters
[^abc] # Excluding a or b or c
---

\s - > One Space
\S -> Except space any character

"""

print("#" * 40, end="\n\n")
##################################


print("Extract IP, DATE, PICS, URL")
print("-" * 20)
# -------------

import re

for each_line in list_of_lines:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST)\s+/(pics/(\w+\.(gif|jpg)))?.*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        print(ip, dt, img, url, sep="\t")
        # print("all groups in string:", match_result.group(0))
        # print("all groups in tuple:", match_result.group(1,2))


"""
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF


http[s]?://[a-z./A-Z_]+
http[s]?://[\w./=?]+

https? -> s is optional
http[s]? -> s is optional
(https)? -> https is optional
[https] -> any one char in this group


"""

print("#" * 40, end="\n\n")
##################################
