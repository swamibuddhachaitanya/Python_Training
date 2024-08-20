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

