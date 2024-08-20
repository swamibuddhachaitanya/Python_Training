"""
Parse complete head tag using beautifulsoup

# Output-1: title
A Web server log file explained

# output-2: all link tags
<LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
<LINK REL="SHORTCUT ICON" HREF="favicon.ico">

# output-3:
<LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
REL = "StyleSheet"
HREF = "../style.css"
TYPE = "text/css"
<LINK REL="SHORTCUT ICON" HREF="favicon.ico">
REL="SHORTCUT ICON"
HREF="favicon.ico"

output-4: META tag and its attributes

output-5: print all urls in complete website
"""

import urllib.request as u

with u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html") as web_file_handle:
    web_content = web_file_handle.read()

# print("the Web content is:",web_content,end="\n\n")

from bs4 import BeautifulSoup
html_doc = web_content
soup = BeautifulSoup(html_doc,'html.parser')

print("The soup is:",soup,end="\n\n")


print("Output-1: Title")
print("--"*20)
print(soup.title.string,end="\n\n")
print("--"*20)

print("Output-2:all link tags")
print("--"*20)
for link in soup.head.find_all('link'):
    print(link,end="\n")
print("--"*20)


print("Output-3:")
print("--"*20)
# REL = "StyleSheet"
# HREF = "../style.css"
# TYPE = "text/css"
print("The all link tags are: ",end="\n\n")
for link in soup.head.find_all('link'):
    print(link)
    for item in link.attrs:
        print(item,":",link.attrs[item])
print("--"*20)

print("Output-4:")
print("--"*20)
print("The META tag and its attributes: ",end="\n\n")
for meta in soup.head.find_all('meta'):
    print(meta)
    for item in meta.attrs:
        print(item,":",meta.attrs[item])
print("--"*20)

print("Output-5:")
print("--"*20)
print("all urls in complete website: ",end="\n\n")
for url in soup.find_all('a'):
    if url.get('href') is not None:
        print(url.get('href'))
print("--"*20)

