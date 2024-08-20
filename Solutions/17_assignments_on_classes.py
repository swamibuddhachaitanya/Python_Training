"""
Write class with
class MyLogProcessClass:
    pass

m = MyLogProcessClass(r"../log/server_log.txt")

- get_ips Method which returns list of ips
    Example:
        ips_list = m.get_ips()

- get_all method which returns list of tuples
    Example:
        all_data = m.get_all()

- to_txt method which write data to txt file
        m.to_txt("my_out_file.txt")

- support for '+':
        ips_with_port = m + ":8080"
        Expected Output: ['123.123.123.123:8080', '123.123.123.123:8080', ]
"""


# class MyLogProcessClass:
#
#     def __init__(self,log_path):
#         self.location = log_path
#         self.file_content = open(self.location,"r").readlines()
#
#     def get_ips(self):
#         self.ips_list=[]
#         for line in self.file_content:
#             if len(line[0:16].split(".")) == 4:
#                 parts = line.split()
#
#
#                 self.ips_list.append(parts[0])

class MyLogProcessClass:

    def __init__(self, log_path):
        self.location = log_path
        self.file_content = open(self.location, "r").readlines()
        self.ips_list = []  # Initialize ips_list in the constructor

    def get_ips(self):
        for line in self.file_content:
            if len(line[0:16].split(".")) == 4:
                parts = line.split()
                self.ips_list.append(parts[0])
        return self.ips_list  # Return ips_list

    def get_dates(self):
        self.dates_list=[]
        for line in self.file_content:
            if len(line[0:16].split(".")) == 4:
                parts = line.split()


                self.dates_list.append(parts[3][1:12])

    def get_pics(self):
        self.pics_list=[]
        for line in self.file_content:
            if len(line[0:16].split(".")) == 4:
                parts = line.split()
                self.pics_list.append(parts[6].split("/")[2][:-4] if "/pics/" in line else "No Image")

    def get_urls(self):
        self.urls_list=[]
        for line in self.file_content:
            if len(line[0:16].split(".")) == 4:
                parts = line.split()
                for part in parts:
                    if "http://" in part:
                        self.urls_list.append(part)

    def get_all(self):

        return [self.ips_list,self.dates_list,self.pics_list,self.urls_list]

    def to_txt(self,write_location):
        file_to_write = open(write_location,"w")
        # print(str(self.get_all()))
        file_to_write.write(str(self.get_all()))

    def __add__(self, other):
        self.output_list = []

        for ip in self.ips_list:
            self.output_list.append(f"{ip} {other}")

        return self.output_list


obj = MyLogProcessClass(r"C:\Python Training\log\server_log_2.txt")
ips_list = obj.get_ips()
obj.get_dates()
obj.get_pics()
obj.get_urls()
print(f"get all function output: {obj.get_all}")
obj.to_txt(r"assignment_17_report.txt")

answer_list = [(lambda a: a + ":8080")(i) for i in ips_list]

print(f"Expected output is: {answer_list}")
