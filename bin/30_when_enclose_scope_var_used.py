"""
Enclosed scope variable usage
"""

print("Enclosed scope variable usage")
print("-"*20)
# ---------------

# Track Total number of log file processed

def log_file_process_func():
    files_count = 0
    def csv_log_process_func():
        nonlocal files_count
        files_count += 1
    def txt_log_process_func():
        nonlocal files_count
        files_count += 1

    def get_total_log_files_processed():
        return files_count

    return csv_log_process_func, txt_log_process_func, get_total_log_files_processed


received_value = log_file_process_func()
# received_value = (csv_log_process_func, txt_log_process_func, get_total_log_files_processed)
received_value[0]()
received_value[1]()
count = received_value[2]()
print("Total log processed:", count)

print("#"*40, end="\n\n")
###########################

