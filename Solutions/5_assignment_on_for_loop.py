"""
From the given string below, extract
IP
DATE
PICS
URL
from each IP address lines

Expected Output
---------------
[
('123.123.123.123', '26/Apr/2000',  'wpaper.gif',      'http://www.jafsoft.com/asctortf/')
('123.123.123.123', '26/Apr/2000',  'No Image',        'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF')
('123.123.123.123', '26/Apr/2000',  '5star2000.gif',   'http://www.jafsoft.com/asctortf/')
('123.123.123.123', '26/Apr/2000',  '5star.gif',       'http://www.jafsoft.com/asctortf/')
('123.123.123.123',  '26/Apr/2000', 'a2hlogo.gif',     'http://www.jafsoft.com/asctortf/')
('123.123.123.123',  '26/Apr/2000', 'No Image',        'http://www.jafsoft.com/asctortf/')
]
---------------
"""

print("How input data looks like?")
print("-"*20)
# ---------------

input_data="""
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
###########################

stored_data=[]

for line in input_data.splitlines():
    if len(line[0:16].split(".")) == 4:
        parts = line.split()

        # Extract IP, DATE, PICS, and URL
        ip = parts[0]
        date = parts[3][1:12]
        pics = parts[6].split("/")[2][:-4] if "/pics/" in line else "No Image"
        for part in parts:
            if "http://" in part:
                url = part

        stored_data.append((ip, date, pics, url))

print(stored_data,sep="\n")