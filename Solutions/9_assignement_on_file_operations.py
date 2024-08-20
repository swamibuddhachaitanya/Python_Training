"""

Write to file using 'writelines'

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
123.123.123.123,26/Apr/2000,wpaper.gif,http://www.jafsoft.com/asctortf/
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

# Read data from server_log.txt
with open(log_file_path, 'r') as log_file:
    log_data = log_file.readlines()

# Create lists to store extracted information
ip_list, date_list, pics_list, url_list = [], [], [], []

# Iterate over each line and extract information
for line in log_data:
    if len(line[0:16].split(".")) == 4:
        parts = line.split()

        # Extract IP, DATE, PICS, and URL
        ip = parts[0]
        date = parts[3][1:12]
        pics = parts[6].split("/")[2][:-4] if "/pics/" in line else "No Image"
        for part in parts:
            if "http://" in part:
                url = part

        # Append the information to lists
        ip_list.append(ip)
        date_list.append(date)
        pics_list.append(pics)
        url_list.append(url)

# Write to log_report.txt using writelines
with open(report_txt_path, 'w') as report_txt:
    report_txt.writelines([
        "    IP                  DATE            PICS                URL\n"
    ] + [
        f"{ip:<15} {date:<18} {pics:<15} {url}\n" for ip, date, pics, url in zip(ip_list, date_list, pics_list, url_list)
    ])

# Write to log_report.csv using writelines
with open(report_csv_path, 'w') as report_csv:
    report_csv.writelines([
        "IP,DATE,PICS,URL\n"
    ] + [
        f"{ip},{date},{pics},{url}\n" for ip, date, pics, url in zip(ip_list, date_list, pics_list, url_list)
    ])

# Display success message
print("Extraction and writing to files completed successfully.")
