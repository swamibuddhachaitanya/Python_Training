"""
Read json file created by 11th assignment
using json library
and
produce json_to_text_report.txt

Expected Output in json_to_text_report.txt
---------------
    IP                  DATE            PICS                URL
123.123.123.123     26/Apr/2000     wpaper.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image        http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif   http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.gif     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image        http://www.jafsoft.com/asctortf/
---------------

"""

import json

# Define the path to the JSON file
json_file_path = "log_data.json"

# Define the path to json_to_text_report.txt
json_to_text_report_path = "json_to_text_report.txt"

# Read data from the JSON file
with open(json_file_path, 'r') as json_file:
    data_dict = json.load(json_file)

# Write the data to json_to_text_report.txt
with open(json_to_text_report_path, 'w') as json_to_text_report:
    json_to_text_report.write("    IP                  DATE            PICS                URL\n")
    for ip, date, pics, url in zip(data_dict['IP'], data_dict['DATE'], data_dict['PICS'], data_dict['URL']):
        json_to_text_report.write(f"{ip:<15} {date:<18} {pics:<15} {url}\n")

print(f"Data written to '{json_to_text_report_path}' successfully.")
