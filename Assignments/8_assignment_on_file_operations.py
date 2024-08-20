"""

Write to file using 'write'

Read data from server_log.txt
extract
IP
DATE
PICS
URL
and
write extracted information to log_report.txt and log_report.csv

Expected Output in log_report.txt
---------------
    IP                  DATE            PICS                URL
123.123.123.123     26/Apr/2000     wpaper.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image        http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif   http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.gif     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image        http://www.jafsoft.com/asctortf/
---------------


Expected Output in log_report.csv
---------------
IP,DATE,PICS,URL
123.123.123.123,     26/Apr/2000,     wpaper.gif,      http://www.jafsoft.com/asctortf/
123.123.123.123,     26/Apr/2000,     No Image,        http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123,     26/Apr/2000,     5star2000.gif,   http://www.jafsoft.com/asctortf/
123.123.123.123,     26/Apr/2000,     5star.gif,       http://www.jafsoft.com/asctortf/
123.123.123.123,     26/Apr/2000,     a2hlogo.gif,     http://www.jafsoft.com/asctortf/
123.123.123.123,     26/Apr/2000,     No Image,        http://www.jafsoft.com/asctortf/
---------------

"""
# Define the paths
log_file_path = "../log/server_log.txt"
report_txt_path = "log_report.txt"
report_csv_path = "log_report.csv"

