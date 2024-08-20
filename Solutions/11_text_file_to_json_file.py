"""
Read data from log_report.txt

PART-1:
prepare below dictionary print on the console
{
IP: ('123.123.123.123','123.123.123.123','123.123.123.123','123.123.123.123','123.123.123.123','123.123.123.123',)
DATE: ()
PICS : ()
URL: ()
}

PART-2:
create json file with above data
"""
import json

# Define the path to log_report.txt
report_txt_path = "log_report.txt"

# PART-1: Read data from log_report.txt and prepare the dictionary
data_dict = {'IP': (), 'DATE': (), 'PICS': (), 'URL': ()}

with open(report_txt_path, 'r') as report_txt:
    # Skip the header line
    next(report_txt)

    # Iterate over each line and extract information
    for line in report_txt:
        parts = line.split()

        # Extract IP, DATE, PICS, and URL
        ip = parts[0]
        date = parts[1]
        pics = parts[2]
        url = ' '.join(parts[3:])

        # Append the information to the dictionary
        data_dict['IP'] += (ip,)
        data_dict['DATE'] += (date,)
        data_dict['PICS'] += (pics,)
        data_dict['URL'] += (url,)

# Print the prepared dictionary on the console
print(data_dict)

# PART-2: Create a JSON file with the above data
json_file_path = "log_data.json"
with open(json_file_path, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f"JSON file '{json_file_path}' created successfully.")
