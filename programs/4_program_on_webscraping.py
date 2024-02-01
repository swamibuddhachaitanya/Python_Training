
print("# Task-2: get log data using bsoup")
print("-" * 20)
# -------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#" * 40, end="\n\n")
##################################

print("log data")
print("-" * 20)
# -------------

log_data = soup.body.pre.text
print(log_data)

print("#" * 40, end="\n\n")
##################################

print("log data in raw format")
print("-" * 20)
# -------------

print(repr(log_data))

print("#" * 40, end="\n\n")
##################################


print("type of log data ")
print("-" * 20)
# -------------

print(type(log_data))

print("#" * 40, end="\n\n")
##################################

