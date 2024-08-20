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

